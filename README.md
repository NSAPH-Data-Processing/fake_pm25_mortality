# fake_pm25_mortality

Generator of a fake dataset (noise) that replicates the columns structure of the dataset in X. Wu et al (DOI: 10.1126/sciadv.aba5692)

## Description

    * Size 1/100 of original dataset
    * Independent column samples

## Pipeline

```
export HOME_DIR=$(pwd)

cd $HOME_DIR/data/input
ln -s /n/dominici_nsaph_l3/Lab/projects/analytic/aggregated_2000-2016_medicare_mortality_pm25_zip .

cd $HOME_DIR/src
python prep_sample.py
```

Output in `./data/output/`
