"""This module gets a dataframe of seattle building permits checks column names"""
import pandas as pd


def get_permits(data_frame=pd.read_csv("https://data.seattle.gov/api/views/76t5-zqzr/rows.csv?accessType=DOWNLOAD",
                                       usecols=["PermitClass", "PermitTypeDesc", "EstProjectCost"],
                                       dtype={"PermitClass": object, "PermitTypeDesc": object, "EstProjectCost":float})):
    """
Gets the building permits
    """
    permits = data_frame
    permits = permits.dropna()
    check_cols(permits)
    return permits


def check_cols(data_frame):
    """
Checks the dataframe column names
    """
    df_cols = ["PermitClass", "PermitTypeDesc", "EstProjectCost"]
    check = data_frame.columns == df_cols
    if not all(check):
        raise ValueError("Column names not the same")
