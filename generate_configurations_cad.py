import sys
import os

import pandas as pd

import FreeCAD


# Load the spreadsheet
file_name = "box_configurations.xlsx"
df = pd.read_excel(os.path.join(os.path.dirname(__file__), file_name))

print(df)