import re
from .spec import ExpectedColumnItem, Type, BaseSpec
from typing import Dict, List


class RNAseqSpec(BaseSpec):
    @property
    def version(self) -> str:
        return "2022051201"

    @property
    def description(self) -> str:
        return """"The template includes two worksheets: metadata and quality_control (Please don't rename these worksheets). If you have any questions, please feel free to contact us at quartet@fudan.edu.cn.\nNOTE: This template table may change in the future as the specification is upgraded. You need to rename the excel file to metadata.xlsx before you uploading to Quartet Data Portal.
        """

    @property
    def specs(self) -> Dict[str, List[ExpectedColumnItem]]:
        return {
            "metadata": [
                ExpectedColumnItem(
                    name="file_name",
                    required=True,
                    type=Type.TEXT,
                    procedure="Basic Info",
                    description="The name of the file, including the file extension. The file name should be unique within the project.",
                    example="FDU_ILM_D5_20200808_001_R1.fastq.gz",
                ),
                ExpectedColumnItem(
                    name="file_size",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=100000000000,
                    procedure="Basic Info",
                    description="The size of the file in bytes.",
                    example=3500000,
                ),
                ExpectedColumnItem(
                    name="md5sum",
                    required=True,
                    type=Type.TEXT,
                    regex=re.compile(r"^[a-f0-9]{32}$"),
                    procedure="Basic Info",
                    description="The MD5 checksum of the file.",
                    example="d41d8cd98f00b204e9800998ecf8427e",
                ),
                ExpectedColumnItem(
                    name="library_id",
                    required=True,
                    type=Type.TEXT,
                    procedure="Basic Info",
                    description="The unique identifier for the library. The library ID should be unique within the project.",
                    example="FDU_ILM_D5_20200808_001",
                ),
                ExpectedColumnItem(
                    name="sample_id",
                    required=True,
                    type=Type.CATEGORY,
                    options=["D5", "D6", "F7", "M8"],
                    procedure="Basic Info",
                    description="Sample ID",
                    example="D5",
                ),
                ExpectedColumnItem(
                    name="data_format",
                    required=True,
                    type=Type.CATEGORY,
                    options=["FASTQ", "CSV"],
                    procedure="Basic Info",
                    description="The format of the data file.",
                    example="FASTQ",
                ),
                ExpectedColumnItem(
                    name="input_ng",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="RNA Enrichments",
                    description="The amount of input RNA in ng.",
                    example=100,
                ),
                ExpectedColumnItem(
                    name="enrichment_method",
                    required=True,
                    type=Type.CATEGORY,
                    options=["PolyA", "RiboZero"],
                    procedure="RNA Enrichments",
                    description="The method used to enrich the RNA.",
                    example="PolyA",
                ),
                ExpectedColumnItem(
                    name="enrichment_kit_manufacturer",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The manufacturer of the enrichment kit.",
                    example="Vazeme",
                ),
                ExpectedColumnItem(
                    name="enrichment_kit_name",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The name of the enrichment kit.",
                    example="VAHTS mRNA Capture Beads",
                ),
                ExpectedColumnItem(
                    name="enrichment_kit_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The catalog number of the enrichment kit.",
                    example="N401",
                ),
                ExpectedColumnItem(
                    name="enrichment_kit_lot_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The lot number of the enrichment kit.",
                    example="",
                ),
                ExpectedColumnItem(
                    name="clean_beads",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The name of the clean beads.",
                    example="VAHTS RNA Clean Beads",
                ),
                ExpectedColumnItem(
                    name="clean_beads_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA Enrichments",
                    description="The catalog number of the clean beads.",
                    example="N412",
                ),
                ExpectedColumnItem(
                    name="fragment_temperature",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=500,
                    procedure="RNA Enrichments",
                    description="The temperature of the fragmentation.",
                    example=85,
                ),
                ExpectedColumnItem(
                    name="fragment_time",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=500,
                    procedure="RNA Enrichments",
                    description="The time of the fragmentation (minutes).",
                    example=5,
                ),
                ExpectedColumnItem(
                    name="enrichment_date",
                    required=True,
                    type=Type.NUMBER,
                    min=20150101,
                    max=20361231,
                    procedure="RNA Enrichments",
                    description="The date of the enrichment.",
                    example=20200808,
                ),
                ExpectedColumnItem(
                    name="is_automated",
                    required=True,
                    type=Type.CATEGORY,
                    options=["Manual", "Automated"],
                    procedure="RNA Enrichments",
                    description="Whether the enrichment is automated.",
                    example="Manual",
                ),
                ExpectedColumnItem(
                    name="is_strand_specific",
                    required=True,
                    type=Type.CATEGORY,
                    options=["TRUE", "FALSE"],
                    procedure="Library Preparation",
                    description="Whether the enrichment is strand specific.",
                    example="TRUE",
                ),
                ExpectedColumnItem(
                    name="preparation_kit_manufacturer",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The manufacturer of the library preparation kit.",
                    example="Vazeme",
                ),
                ExpectedColumnItem(
                    name="preparation_kit_name",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The name of the library preparation kit.",
                    example="VAHTS Universal V8 RNA-seq Library Prep Kit for Illumina",
                ),
                ExpectedColumnItem(
                    name="preparation_kit_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The catalog number of the library preparation kit.",
                    example="NR605",
                ),
                ExpectedColumnItem(
                    name="preparation_kit_lot_no",
                    required=False,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The lot number of the library preparation kit.",
                    example="",
                ),
                ExpectedColumnItem(
                    name="adapter_manufacturer",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The manufacturer of the adapter.",
                    example="Vazeme",
                ),
                ExpectedColumnItem(
                    name="adapter_name",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The name of the adapter.",
                    example="VAHTS RNA Multiplex Oligos Set1- Set2 for Illumina",
                ),
                ExpectedColumnItem(
                    name="adapter_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The catalog number of the adapter.",
                    example="N323",
                ),
                ExpectedColumnItem(
                    name="adapter_volume",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library Preparation",
                    description="Volume for RNA adapter (uL)",
                    example=1,
                ),
                ExpectedColumnItem(
                    name="barcode_manufacturer",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The manufacturer of the barcode (index).",
                    example="Vazeme",
                ),
                ExpectedColumnItem(
                    name="barcode_name",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The name of the barcode (index).",
                    example="VAHTS RNA Multiplex Oligos Set1- Set2 for Illumina",
                ),
                ExpectedColumnItem(
                    name="barcode_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The catalog number of the barcode (index).",
                    example="N323",
                ),
                ExpectedColumnItem(
                    name="barcode_volume",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library Preparation",
                    description="Volume for RNA barcode (index) (uL)",
                    example=5,
                ),
                ExpectedColumnItem(
                    name="library_clean_beads",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The name of the library clean beads.",
                    example="VAHTS DNA Clean Beads",
                ),
                ExpectedColumnItem(
                    name="library_clean_beads_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Preparation",
                    description="The catalog number of the library clean beads.",
                    example="N411",
                ),
                ExpectedColumnItem(
                    name="beads_f_volume",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library Preparation",
                    description="First volume of beads for size selection (uL)",
                    example=13,
                ),
                ExpectedColumnItem(
                    name="beads_s_volume",
                    required=True,
                    type=Type.FLOAT,
                    min=0.0,
                    max=100.0,
                    procedure="Library Preparation",
                    description="Second volume of beads for size selection (uL)",
                    example=7.5,
                ),
                ExpectedColumnItem(
                    name="pcr_cycles",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=100,
                    procedure="Library Preparation",
                    description="The number of PCR cycles.",
                    example=15,
                ),
                ExpectedColumnItem(
                    name="preparation_date",
                    required=True,
                    type=Type.NUMBER,
                    min=20150101,
                    max=20361231,
                    procedure="Library Preparation",
                    description="The date of the library preparation.",
                    example=20200808,
                ),
                ExpectedColumnItem(
                    name="library_is_automated",
                    required=True,
                    type=Type.CATEGORY,
                    options=["Manual", "Automated"],
                    procedure="Library Preparation",
                    description="Whether the library preparation is automated.",
                    example="Manual",
                ),
                ExpectedColumnItem(
                    name="sequence_tech",
                    required=True,
                    type=Type.CATEGORY,
                    options=["Illumina", "MGI", "Other"],
                    procedure="Library Sequencing",
                    description="The sequencing technology.",
                    example="Illumina",
                ),
                ExpectedColumnItem(
                    name="sequence_machine",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The sequencing machine.",
                    example="NovaSeq 6000",
                ),
                ExpectedColumnItem(
                    name="sequence_method",
                    required=True,
                    type=Type.CATEGORY,
                    options=["PE150"],
                    procedure="Library Sequencing",
                    description="The sequencing method.",
                    example="PE150",
                ),
                ExpectedColumnItem(
                    name="seq_kit",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The sequencing kit.",
                    example="NovaSeq 6000 S4 Reagent Kit v1.5 (300 cycles) ",
                ),
                ExpectedColumnItem(
                    name="seq_kit_cat_no",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The catalog number of the sequencing kit.",
                    example="20028312",
                ),
                ExpectedColumnItem(
                    name="seq_kit_lot_no",
                    required=False,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The lot number of the sequencing kit.",
                    example="",
                ),
                ExpectedColumnItem(
                    name="is_paired_end",
                    required=True,
                    type=Type.CATEGORY,
                    options=["TRUE", "FALSE"],
                    procedure="Library Sequencing",
                    description="Whether the sequencing is paired-end.",
                    example="TRUE",
                ),
                ExpectedColumnItem(
                    name="read_length",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library Sequencing",
                    description="The read length.",
                    example=150,
                ),
                ExpectedColumnItem(
                    name="flowcell_id",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The flowcell ID.",
                    example="H5LJYDSXY",
                ),
                ExpectedColumnItem(
                    name="lane_id",
                    required=True,
                    type=Type.TEXT,
                    procedure="Library Sequencing",
                    description="The lane ID.",
                    example="1",
                ),
                ExpectedColumnItem(
                    name="run_date",
                    required=True,
                    type=Type.NUMBER,
                    min=20150101,
                    max=20361231,
                    procedure="Library Sequencing",
                    description="The date of the sequencing run.",
                    example=20200808,
                ),
            ],
            "quality_control": [
                ExpectedColumnItem(
                    name="library_id",
                    required=True,
                    type=Type.TEXT,
                    procedure="RNA QC",
                    description="The unique identifier for the library. The library ID should be unique within the project.",
                    example="FDU_ILM_D5_20200808_001",
                ),
                ExpectedColumnItem(
                    name="rin",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=100,
                    procedure="RNA QC",
                    description="The RNA integrity number (RIN).",
                    example=8.5,
                ),
                ExpectedColumnItem(
                    name="rna_conc",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="RNA QC",
                    description="RNA conc. (ng/uL)",
                    example=480,
                ),
                ExpectedColumnItem(
                    name="rna_volume",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="RNA QC",
                    description="RNA volume (uL)",
                    example=10,
                ),
                ExpectedColumnItem(
                    name="cdna_fragments",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library QC",
                    description="cDNA fragments (bp)",
                    example=340,
                ),
                ExpectedColumnItem(
                    name="cdna_conc",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library QC",
                    description="cDNA conc. (ng/uL)",
                    example=20,
                ),
                ExpectedColumnItem(
                    name="cdna_volume",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library QC",
                    description="cDNA volume (uL)",
                    example=22,
                ),
                ExpectedColumnItem(
                    name="cdna_yield",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Library QC",
                    description="cDNA yield (ng)",
                    example=440,
                ),
                ExpectedColumnItem(
                    name="q30",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=100,
                    procedure="Sequencing QC",
                    description="Q30",
                    example=95,
                ),
                ExpectedColumnItem(
                    name="total_reads",
                    required=True,
                    type=Type.NUMBER,
                    min=0,
                    max=1000,
                    procedure="Sequencing QC",
                    description="Total reads (M)",
                    example=100,
                ),
            ],
        }