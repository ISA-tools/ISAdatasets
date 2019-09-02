# ISAdatasets

## Master branch

In the `master` branch, we provide ISA datasets exemplars, available either in `tab delimited` or `JSON` formats, hence the repository organization.

Many more ISA datasets are available from production repositories such as:

1. [EMBL-EBI Metabolights metabolomics data archive](https://www.ebi.ac.uk/metabolights/): 
ftp://ftp.ebi.ac.uk/pub/databases/metabolights/studies/public/

1. [Nature Springer Scientific Data](http://www.nature.com/sdata/):
https://github.com/ScientificDataLabs/ISA-tab

1. [Stem Cell Commons](https://hsci.stemcellcommons.org/dashboard):
e.g.: https://hsci.stemcellcommons.org/data_sets/ff1cb512-ad8c-4810-83f1-69e929a4ae81/#/about/

## Tests branch

The `tests` branch contains more datasets in ISA `tab` and `json` format as well as ISA datasets converted to other formats (i.e. `Short Read Archive` format (used by INSDC databses ( the US NCBI SRA archive, the EU EMBL-EBI, the Japanese DDBJ and China's CNG), `MAGE-Tab` formats (EMBL-EBI ArrayExpress), `Sample-Tab` format (EMBL-EBI Biosamples), used for testing in the ISA-API (https://github.com/ISA-tools/isa-api). The branch also contains test datasets for the conversion from 3rd party formats to ISA format (e.g. mzml for mass spectrometry data).



