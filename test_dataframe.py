# coding: utf-8
"""This module contains two tests for the seattle building permits dataset"""
import unittest
import numpy as np
import pandas as pd


DF = pd.read_csv("https://data.seattle.gov/api/views/76t5-zqzr/rows.csv?accessType=DOWNLOAD",
                 usecols=["PermitClass", "PermitTypeDesc", "EstProjectCost"],
                 dtype={"PermitClass": object, "PermitTypeDesc": object, "EstProjectCost":float})

class TestPermits(unittest.TestCase):
    """
    This class contains tests for na values and at least one row in the dataframe
    """

    def test_for_any_null_values(self):
        """
        test for any null values
        """
        assert pd.notnull(DF.values).any()

    def test_for_at_least_one_row(self):
        """
        test for at least one row
        """
        assert np.size(DF, 0) > 0

SUITE = unittest.TestLoader().loadTestsFromTestCase(TestPermits)
_ = unittest.TextTestRunner().run(SUITE)
