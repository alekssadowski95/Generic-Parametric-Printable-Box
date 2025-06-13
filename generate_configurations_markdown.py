import pandas as pd
import os

# Load the spreadsheet
file_name = "box_configurations.xlsx"
df = pd.read_excel(os.path.join(os.path.dirname(__file__), file_name))

# Add a new column with the constructed URL for each row
base_url = "https://github.com/alekssadowski95/Generic-Parametric-Printable-Box/releases/latest"
def create_url(row):
    return f"({base_url}/{row['Partnumber']}_{row['inside_length (mm)']}_{row['inside_width (mm)']}_{row['box_inside_height (mm)']})"

df['Download_Link'] = df.apply(create_url, axis=1)

# Convert to Markdown format and print
markdown_table = df.to_markdown(index=False)
print(markdown_table)

# Write Markdown to a file
with open(os.path.join(os.path.dirname(__file__), "box_configurations.md"), "w") as md_file:
    md_file.write(markdown_table)
