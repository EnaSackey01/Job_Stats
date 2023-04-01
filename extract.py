from config import connection

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import functools as ft

#Establishing initial connection to Amazon RDS
engine = create_engine(connection)

#Creating an automapper: Turn our tables into objects
Base = automap_base()
Base.prepare(engine, reflect=True)
jobs = Base.classes.jobs
salaries = Base.classes.salaries
skills = Base.classes.skills

#Creating a Session: Temporary connection to the database
session = Session(engine)
engine.dispose()

#Building queries to pull all Amazon data using the "Jobs_result" query)"
jobs_result = session.query(jobs)
skills_result = session.query(skills)
salaries_result = session.query(salaries)

#Saving query into data frames
jobs_df = pd.read_sql(sql = jobs_result.statement, con = engine.connect())
skills_df = pd.read_sql(sql = skills_result.statement, con = engine.connect())
salaries_df = pd.read_sql(sql = salaries_result.statement, con = engine.connect())

# OP1 - Creating code to join all 3 tables together on their primary key
#dfs = [jobs_df, skills_df, salaries_df]
#df_final = ft.reduce(lambda left: pd.merge(left, right, on= 'ID'), dfs) or df_merged = ft.reduce (lambda left, right: pd.merge(left, right, on =['id'], how ='outer'),dfs)

#OP2 - Make two merges
m1 = pd.merge(salaries_df, jobs_df, how = "inner", on = ["id"])
tot_merge = pd.merge(m1, skills_df, how = "inner", on = ["id"])

#Writing this join dataframe to the "Data" folder
tot_merge.to_csv("Data/Joined_data.csv", index = False)
