import re
import pandas as pd
from typing import List, Dict, Tuple
from pathlib import Path
from .specs import (
    ExpectedColumnItem,
    RNAseqSpec,
    DNAseqSpec,
    MetabolomicsSpec,
)


class MetadataValidator:
    def __init__(
        self,
        filepath: Path,
        specs: Dict[str, List[ExpectedColumnItem]],
        sheet_names: List[str] = ["metadata", "quality_control"],
    ) -> None:
        self.file_path: Path = filepath
        self.raw_sheet_names: List[str] = sheet_names
        self._errors: Dict[str, List[str]] = {}
        self._warnings: Dict[str, List[str]] = {}
        self._specs = specs

        if specs:
            for sheet_name in self.raw_sheet_names:
                if sheet_name not in self._specs.keys():
                    self._add_warning(
                        sheet_name,
                        f"Sheet name {sheet_name} not found in specs, skipping validation for this sheet.",
                    )

        # Maybe the sheet don't exist in the excel file, so we need to reset the sheet_names
        self._metadata, self.sheet_names = self._read_excel()

    @property
    def errors(self):
        msgs = []
        for sheet_name in self.raw_sheet_names:
            msg = f"Check Sheet {sheet_name} with errors:\n"
            error_msg = "\n".join(
                [f"Error: {e}" for e in self._errors.get(sheet_name, [])]
            )

            if error_msg:
                msg = msg + error_msg + "\n"
            else:
                msg = msg + "No errors found." + "\n"

            msgs.append(msg)

        return "\n".join(msgs)

    @property
    def warnings(self):
        msgs = []
        for sheet_name in self.raw_sheet_names:
            msg = f"Check Sheet {sheet_name} with warnings:\n"
            warn_msg = "\n".join(
                [f"Warning: {e}" for e in self._warnings.get(sheet_name, [])]
            )

            if warn_msg:
                msg = msg + warn_msg + "\n"
            else:
                msg = msg + "No warnings found." + "\n"

            msgs.append(msg)

        return "\n".join(msgs)

    @property
    def metadata(self) -> Dict[str, pd.DataFrame]:
        return self._metadata

    def _read_excel(self) -> Tuple[Dict[str, pd.DataFrame], List[str]]:
        metadata: Dict[str, pd.DataFrame] = {}
        sheet_names: List[str] = []
        for sheet_name in self.raw_sheet_names:
            try:
                metadata[sheet_name] = pd.read_excel(
                    self.file_path, sheet_name=sheet_name
                )
                sheet_names.append(sheet_name)
            except Exception as e:
                msg = f"Reading excel file {sheet_name}, but {e}, please check the file format."
                self._add_error(sheet_name, msg)
        return metadata, sheet_names

    def validate(self):
        raise NotImplementedError

    def _add_error(self, sheet_name, error) -> None:
        if sheet_name not in self._errors.keys():
            self._errors[sheet_name] = [error]
        else:
            self._errors[sheet_name].append(error)

    def _add_warning(self, sheet_name, warning) -> None:
        if sheet_name not in self._warnings.keys():
            self._warnings[sheet_name] = [warning]
        else:
            self._warnings[sheet_name].append(warning)

    def _validate_columns(self) -> None:
        if not self._specs:
            return

        for sheet_name in self.sheet_names:
            missing_columns: List[str] = []
            wrong_type_columns: List[Dict[str, str]] = []

            metadata = self._metadata[sheet_name]
            for column_spec in self._specs.get(sheet_name, []):
                column = []
                if column_spec.name not in metadata.columns:
                    if column_spec.required:
                        missing_columns.append(column_spec.name)

                    # If the column doesn't exist, we don't need to validate the type
                    continue
                else:
                    column = metadata[column_spec.name]

                if column.isnull().all():
                    if column_spec.required:
                        self._add_error(
                            sheet_name, f"Column {column_spec.name} is empty."
                        )
                    else:
                        self._add_warning(
                            sheet_name, f"Column {column_spec.name} is empty."
                        )

                    continue
                elif column.isnull().any():
                    self._add_warning(
                        sheet_name, f"Column {column_spec.name} has null values."
                    )
                    # Remove null values, they may cause problems when validating the type
                    column = column.dropna()

                if column_spec.type == "text":
                    if column_spec.regex:
                        r = column.apply(
                            lambda x: re.match(column_spec.regex, x) is not None  # type: ignore
                        )
                        if not r.all():
                            wrong_type_columns.append(
                                {
                                    column_spec.name: f"{column_spec.name} has values that do not match {column_spec.regex}"
                                }
                            )
                            continue

                elif column_spec.type == "number" or column_spec.type == "float":
                    if column_spec.min:
                        r = column.apply(lambda x: x >= column_spec.min)
                        if not r.all():
                            wrong_type_columns.append(
                                {
                                    column_spec.name: f"{column_spec.name} has values less than {column_spec.min}"
                                }
                            )
                            continue

                    if column_spec.max:
                        r = column.apply(lambda x: x <= column_spec.max)
                        if not r.all():
                            wrong_type_columns.append(
                                {
                                    column_spec.name: f"{column_spec.name} has values greater than {column_spec.max}"
                                }
                            )
                            continue

                elif column_spec.type == "category":
                    if column_spec.options:
                        r = column.apply(lambda x: x in column_spec.options)
                        if not r.all():
                            wrong_type_columns.append(
                                {
                                    column_spec.name: f"{column_spec.name} has values not in {column_spec.options}"
                                }
                            )
                            continue

            if missing_columns:
                self._add_error(sheet_name, f"Missing columns: {missing_columns}")

            if wrong_type_columns:
                wrong_type_columns_str = "\n".join(
                    [f"{k}: {v}" for d in wrong_type_columns for k, v in d.items()]
                )
                self._add_error(
                    sheet_name, f"Wrong type columns: {wrong_type_columns_str}"
                )

    def _validate_rows(self) -> None:
        pass


class DNAseqMetadataValidator(MetadataValidator):
    def __init__(self, filepath: Path) -> None:
        specs = DNAseqSpec().specs
        sheet_names = list(specs.keys())
        super().__init__(filepath, specs, sheet_names)

    def validate(self):
        self._validate_columns()
        self._validate_rows()


class RNAseqMetadataValidator(MetadataValidator):
    def __init__(self, filepath: Path) -> None:
        specs = RNAseqSpec().specs
        sheet_names = list(specs.keys())
        super().__init__(filepath, specs, sheet_names)

    def validate(self):
        self._validate_columns()
        self._validate_rows()


class MetabolomicsMetadataValidator(MetadataValidator):
    def __init__(self, filepath: Path) -> None:
        specs = MetabolomicsSpec().specs
        sheet_names = list(specs.keys())
        super().__init__(filepath, specs, sheet_names)

    def validate(self):
        self._validate_columns()
        self._validate_rows()


if __name__ == "__main__":
    filepath = Path(
        "/Users/codespace/Downloads/metadata_validator/20221128_genomics-metadata-template_english.xlsx"
    )
    validator = DNAseqMetadataValidator(filepath)
    validator.validate()
    print(validator.errors)
    print(validator.warnings)
