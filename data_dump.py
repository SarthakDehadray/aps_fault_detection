
import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(df.shape)

#convert dataframe to json to dump the records into mongo db
df.reset_index(drop = True,inplace =True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])
#insert converted record to mongodb
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


