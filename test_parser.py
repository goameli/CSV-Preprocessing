import pandas as pd
import numpy as np
import os, glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--path", "-p")
parser.add_argument("--output", "-o")

parsed = parser.parse_args()

path = parsed.path
output = parsed.output

def read_datasets(path,year,output):
    
    filename = str(year) + "_*.csv"
    all_files = glob.glob(os.path.join(path, filename))
    df = (pd.read_csv(f, sep=",") for f in all_files)
    df_merged = pd.concat(df, ignore_index=True)
    df_merged.to_csv(output)
    return df_merged

def main():
    read_datasets(path, 2017, output)

if __name__ == "__main__":
    main()
