# Data preprocessing: (a) import, (b) parse (e.g., convert strings to ints), (c)
# organize (e.g., set up a database or a pandas DataFrame).

import pandas as pd

# sleep_mobile_stress_dataset_15000.csv
df = pd.read_csv("dataset.csv")

print(df.head)