# Data Dictionary

## `files.csv`

| Column | Data Type | Description | Format | Source |
| ------ | --------- | ----------- | ------ | ------ |
| `record_number` | Whole number | The number of the record as assigned by 'justice.gov', used to uniquely identify a record across all datasets | Numeric (e.g. `123`) | Assigned by `justice.gov`. If this value is not between the minimum and maximum records found in any dataset in the `yung-megafone/Epstein-Files` torrents, it's excluded from this dataset |
| `record_number_padded` | Text | A string representation of `record_number` | Padded with leading `0`'s to 7 characters (e.g. `0000123`) | Calculated |
| `file_stem` | Text | The `record_number_padded` value with a prefix of "EFTA", meant to match the file names (excluding the  file extension) provided by `justice.gov` | Padded with leading `0`'s to 7 characters and prefixed with "EFTA" (e.g. `EFTA0000123`) | Calculated |
| `dataset_number` | Whole number | The number of the dataset that this record would be expected to be in. This is "expected" because the record may not have been released, it may simply be that this record falls between the first and last record in a released dataset | Numeric (e.g. `2`) | `yung-megafone/Epstein-Files` |
| `dataset_name` | Text | A friendly name of the dataset | The number of the dataset prefixed with "Dataset" (e.g. `Dataset 2`) | Calculated |
| `file_extension` | Text | The extension of the file provided by `justice.gov` | Text without a leading period (e.g. `pdf`) | Assumed to be PDF unless otherwise discovered (such as in the `ThotuB/ep-videos` database) |
| `file_name` | Text | The filename of the record provided by `justice.gov` | A file name without directory (e.g. `EFTA0000123.pdf`) | Calculated