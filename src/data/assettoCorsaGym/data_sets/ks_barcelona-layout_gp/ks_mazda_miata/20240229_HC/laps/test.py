import pandas as pd
from pprint import pprint

file_path = r"C:\Users\kosto\Desktop\Thesis\Repo\src\data\assettoCorsaGym\data_sets\ks_barcelona-layout_gp\ks_mazda_miata\20240229_HC\laps\ks_barcelona_&_ks_mazda_miata_&_adrianremonda_&_stint_1.pkl"
data = pd.read_pickle(file_path)

""" print(type(data))
print(data.keys())

print("\nType of states:", type(data["states"]))
print("Number of states:", len(data["states"]))

print("\nType of first state:", type(data["states"][0]))
print("\nFirst state:")
pprint(data["states"][0])

print("\nStatic info:")
print(data["static_info"])
"""


df = pd.DataFrame(data["states"])

print(df.shape)
print(df.columns)
