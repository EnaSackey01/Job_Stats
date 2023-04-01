from config import connection

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd

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

#Building queries to pull all Amazon Data using the "Jobs_result" query)"
jobs_result = session.query(jobs)
skills_result = session.query(skills)
salaries_result = session.query(salaries)

#Saving query into Dataframes
jobs_df = pd.read_sql(jobs_result.statement, engine)
skills_df = pd.read_sql(skills_result.statement, engine)
salaries_df = pd.read_sql(salaries_result.statement, engine)
