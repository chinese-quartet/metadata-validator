"""Console script for metadata_validator."""
import os
import sys
import click

from metadata_validator.validator import DNAseqMetadataValidator
from metadata_validator.specs import spec_dict

validator_dict = {
    "DNAseq": DNAseqMetadataValidator,
    "RNAseq": None,
    "Proteomics": None,
    "Metabolomics": None,
}


@click.group()
def cli():
    pass


@cli.command(help="Metadata Validator")
@click.option(
    "--input",
    "-i",
    required=True,
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    help="Input file path, only support xlsx file.",
)
@click.option(
    "--output", "-o", required=True, help="Output error and warning messages as a file."
)
@click.option(
    "--template-type",
    "-t",
    required=True,
    help="It support the following metadata tables: 'DNAseq', 'RNAseq', 'Proteomics, 'Metabolomics'",
    type=click.Choice(["DNAseq", "RNAseq", "Proteomics", "Metabolomics"]),
)
def validate(input, output, template_type):
    """Console script for metadata_validator."""
    if template_type in validator_dict.keys():
        validator = validator_dict[template_type](input)
        validator.validate()

        error_msg = validator.errors
        warning_msg = validator.warnings

        if output:
            if os.path.exists(output):
                raise FileExistsError("The output file already exists.")
            else:
                with open(output, "w") as f:
                    f.write(error_msg)
                    f.write("\n")
                    f.write(warning_msg)
        else:
            print(error_msg)
            print("\n")
            print(warning_msg)
    else:
        click.echo("The template type is not supported.")

    return 0


@cli.command(help="Generate metadata template as a xlsx file.")
@click.option(
    "--output", "-o", required=True, help="Output metadata template as a file."
)
@click.option(
    "--template-type",
    "-t",
    required=True,
    help="It support the following metadata tables: 'DNAseq', 'RNAseq', 'Proteomics, 'Metabolomics'",
    type=click.Choice(["DNAseq", "RNAseq", "Proteomics", "Metabolomics"]),
)
def generate_template(output, template_type):
    if template_type in spec_dict.keys():
        template = spec_dict[template_type]()
        template.generate_template(output)
    else:
        click.echo("The template type is not supported.")

    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
