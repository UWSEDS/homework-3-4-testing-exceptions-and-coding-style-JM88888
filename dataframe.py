"""This module gets a dataframe of seattle building permits checks column names"""
import pandas as pd
import collections


def get_permits(data_frame=pd.read_csv("https://data.seattle.gov/api/views/76t5-zqzr/rows.csv?accessType=DOWNLOAD",
                                       usecols=["PermitClass", "PermitTypeDesc", "EstProjectCost"],
                                       dtype={"PermitClass": object, "PermitTypeDesc": object, "EstProjectCost":float})):
    """
Gets the building permits
    """
    permits = data_frame
    permits = permits.dropna()
    check_col_names(permits)
    return permits


def check_col_names(data_frame):
    """
Checks the dataframe column names
    """
    df_cols_read = data_frame.columns
    df_cols_expect = ["PermitClass", "PermitTypeDesc", "EstProjectCost"]
    if len(df_cols_read) != len(df_cols_read):
        raise ValueError("Different numbers of columns!")
    for col in df_cols_read:
        if col not in df_cols_expect:
            raise ValueError("Column names not the same")
