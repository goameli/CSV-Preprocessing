import pandas as pd
import numpy as np
import os, glob

path = "data_source/"

def read_datasets(path,year):
    
    filename = str(year) + "_*.csv"
    all_files = glob.glob(os.path.join(path, filename))
    df = (pd.read_csv(f, sep=",") for f in all_files)
    df_merged = pd.concat(df, ignore_index=True)
    df_merged.to_csv("output/merged2018.csv")
    return df_merged

def main():
    read_datasets(path, 2018)

if __name__ == "__main__":
    main()