# The Epstein Files List

## Purpose

This is meant to be a compilation of metadata about every file in [The Epstein Files](https://en.wikipedia.org/wiki/Epstein_files). "Metadata" means that this repo is not meant to store the files themselves but instead store information about the files for those wishing to do mass analysis.

## How to View

The core dataset is `files.csv`, which is meant to be a list of every record in The Epstein Files and information about that record.

## How to Contribute

Please start an issue if you know of a dataset that should be included. Great information would the topic of each record, a list of records that were later deleted from `justice.gov`, or a list of records that are related to each other.

## Data Sources

[`yung-megafone/Epstein-Files`](https://github.com/yung-megafone/Epstein-Files) - Torrent files where you can download The Epstein Files for yourself
* From this, we get dataset file boundaries. In other words, we get the minimum and maximum record numbers for each dataset and consider anything between those values to be part of that dataset. What we got:
    ```
    Dataset 1 is from 1 to 3158
    Dataset 2 is from 3159 to 3857
    Dataset 3 is from 3858 to 5586
    Dataset 4 is from 5705 to 8320
    Dataset 5 is from 8409 to 8528
    Dataset 6 is from 8529 to 8998
    Dataset 7 is from 9016 to 9664
    Dataset 8 is from 9676 to 39023
    Dataset 9 is from 39025 to 1262729
    Dataset 10 is from 1262782 to 2212882
    Dataset 11 is from 2212883 to 2730262
    Dataset 12 is from 2730265 to 2731783
    ```
* Data current as of commit `43263b145ceb9863ad01143339c2bf2d2200e121`