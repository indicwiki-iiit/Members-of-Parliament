# -*- coding: utf-8 -*-
"""Sweetviz_MPs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IIkCCaTdwHRFmkxK-Q9rXyMZSkOEftv7
"""

!pip install sweetviz

import sweetviz as sv
import pandas as pd

DF = pd.read_csv('/content/MPS-Finalised data1.0.xlsx - Data with attributes.csv')

report = sv.analyze(DF)
report.show_html()