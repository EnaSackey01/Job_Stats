import pandas as pd

#Importing Data

job_df = pd.read_csv("Data/joined_data.csv")
job_df.head

job_df["work_from_home"].isna()
print (job_df["work_from_home"].isna())

job_df["work_from_home"].isna().count()
print (job_df["work_from_home"].isna().count())

job_df["work_from_home"].isna().sum()
print (job_df["work_from_home"].isna().sum())

job_df["work_from_home"] = job_df["work_from_home"].fillna(value = False)
print(job_df["work_from_home"])

job_df["work_from_home"].isna()
print (job_df["work_from_home"].isna())

job_df["work_from_home"].isna().count()
print (job_df["work_from_home"].isna().count())

job_df["work_from_home"].isna().sum()
print (job_df["work_from_home"].isna().sum())

job_df["work_from_home"].isna().sum()

droped_df = job_df.dropna(subset = ["salary_standardized"])
droped_df.isna().sum()
droped_df

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MultiLabelBinarizer
from ast import literal_eval

mlb = MultiLabelBinarizer()
def convert_to_list(s):
    try:
        return eval(s)
    except:
        return []
job_df['description_tokens'] = job_df['description_tokens'].apply(convert_to_list)

mlb = MultiLabelBinarizer()
mlb.fit(job_df['description_tokens'])

FTokens = pd.DataFrame(mlb.transform(job_df['description_tokens']), columns=mlb.classes_)
job_df = pd.concat([job_df, FTokens], axis=1)

job_df.to_csv("Joined_Data/New_Joined_Data.csv", index=False)

job_df = job_df.dropna(subset=["salary_standardized"])
print(job_df)

job_df["salary_standardized"].isna().sum()
print(job_df['salary_standardized'].isna().sum())

job_df.to_csv("Joined_Data/Cleaned_New_Joined_Data.csv", index=False)
job_df['work_from_home'].isna().sum()

