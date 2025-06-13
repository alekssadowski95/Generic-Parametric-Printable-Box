import pandas as pd
import os

# Load the spreadsheet
file_name = "box_configurations.xlsx"
df = pd.read_excel(os.path.join(os.path.dirname(__file__), file_name))

# Convert to Markdown format and print
markdown_table = df.to_markdown(index=False)
print(markdown_table)

# Write Markdown to a file
with open(os.path.join(os.path.dirname(__file__), "box_configurations.md"), "w") as md_file:
    md_file.write(markdown_table)
