import pandas as pd
from pymongo import MongoClient
import json


uri = "mongodb+srv://crypto2581:RfPsgeeO0vReT817@cluster0.g3mhs31.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

DATABASE_NAME = "Wafer_Database"
COLLECTION_NAME = "Wafer_Collection"
df = pd.read_csv('/content/sample_data/wafer_23012020_041211.csv')
df = df.drop('Unnamed: 0' , axis=1 ) 
json_record = list(json.loads(df.T.to_json()).values())
client[DATABASE_NAME][COLLECTION_NAME].insert_many(list(json_record))