## load packages ----
import pandas as pd
import numpy as np
import pyreadr

## load data ----
file = "../data/input/aggregated_2000-2016_medicare_mortality_pm25_zip/aggregate_data.csv"
df = pd.read_csv(file, nrows=1e6)

## load args ----
nrows = sum(1 for line in open(file))
sample_frac = 0.01

## prepare dataset ----
df.zip = df.zip.astype('str')
df.dual = df.dual.astype('int')
df.followup_year = df.followup_year.apply(lambda x: int(x))

categorical_cols = [
    'zip', 'year', 'sex', 
    'race', 'dual', 'entry_age_break', 
    'followup_year', 'dead', 'region']

numerical_cols = [
    'time_count', 'pm25_ensemble', 'mean_bmi', 'smoke_rate',
    'hispanic', 'pct_blk', 'medhouseholdincome', 'medianhousevalue',
    'poverty', 'education', 'popdensity', 'pct_owner_occ', 
    'summer_tmmx', 'winter_tmmx', 'summer_rmax', 'winter_rmax']

df_fake = pd.DataFrame()

for col_ in categorical_cols:
    x = df[col_]
    df_fake[col_] = np.random.choice(x.unique(), size=round(nrows * sample_frac), replace=True)

for col_ in numerical_cols:
    x = df[col_]
    df_fake[col_] = np.random.default_rng().uniform(low=min(x), high=max(x), size=round(nrows * sample_frac))

pyreadr.write_rds("../data/output/fake_aggregate_data.rds", df_fake)
