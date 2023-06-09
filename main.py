# pip3 install pandas_profiling
# pip3 install pandas     
import pandas as pd 
from pandas_profiling import ProfileReport

df = pd.read_csv("housing.csv")
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="housing.html")