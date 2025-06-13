import sys
import os

import pandas as pd


# Load the spreadsheet
file_name = "box_configurations.xlsx"
df = pd.read_excel(os.path.join(os.path.dirname(__file__), file_name))

print(df)

# Add path to FreeCAD Python interface
# path to your FreeCAD.so or FreeCAD.dll file
FREECAD_ABS_PATH = 'C:/Users/Work/Downloads/FreeCAD-0.21.2-Windows-x86_64\FreeCAD_0.21.2-2023-12-17-conda-Windows-x86_64-py310/bin'
sys.path.append(FREECAD_ABS_PATH)

# import the FreeCAD Python interface
try:
    import FreeCAD
    print('The FreeCAD Python interface has been loaded. ')
except:
    print('FreeCAD API not found. Check that your installed external Python interpreter has the same version as the FreeCAD internal interpreter.')

doc_path = os.path.join(os.path.dirname(__file__), 'generic_parametric_printable_box.FCStd')
print(doc_path)
doc = FreeCAD.openDocument(doc_path)

print(doc)