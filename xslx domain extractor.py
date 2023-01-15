import pandas as pd

# Read in the excel file
df = pd.read_excel("abcd.xlsx")

# Select only the rows where the column you specify is not "404" and is "Cannot Resolve Host"
df = df.loc[(df["HTTP Code"] != "404") & (df["HTTP Code"] == "Cannot resolve host")]

# Write the modified DataFrame to a new excel file
df.to_excel("modified_file.xlsx", index=False)
