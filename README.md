# JOB_STATS
Python ETL outline to outline outlooks of Data Analyst Jobs for late 2022 early 2023

NOTE: Previledged data is hidded to maintain data integrity.


# Extract.py
This file holds code meant to pull data from our Amazon RDS data source regarding job titles and the affiliated values including salaries, turn it into a csv format we can clean and utilise later.

An initial connection to Amazon RDS and the data is read into the file from the created variable "engine".
Then an automapper to turn the table into objects which can be called later using the variable "Base". 
After the object is created, using another variable "Session" I created another yet temporary connection and disposed of "Base", so as to dismiss interferance when building queries.

Using a query assigned to variable "Jobs_result", all Amazon data is pulled, saved, and merged as new data in order to avoid duplicates.
####Multiple coding options provided in code.###

NOTE: Nulls will still be present and the new final joined data will be writing in as a new csv file to the "Data" folder as a file titled "Joined_data.csv" but not yet cleaned.


# Transform.ipynb
This file holds code used to develop and clean the acummulation of the merged data file "Joined_data.csv, soucred from Amazon RDS and stored in the Data folder created buy the code in the Extract.py file.

To do this the data will be imported using the pandas module, missing values are identified and dropped to produce clean data.
The new data is written into the file by using a binary encoder while token key is transformed.
The cleaned data will be found as a new file rewriten as a new csv file titled "New_Joined_Data.csv" in the "Joined_Data" Folder.


# Predict.ipynb

This file holds code that is meant to predict future salary outcomes. When creating the code to predict future outcomes the new data is loaded in, a model is created and assigned to a variable "L_R", a predictor variables, target variable, & X,Y  arrays are selected and assign.

The data will the be split into training and testing sets. A linear regression model will be created and fit to the training data. 
Print the R-squared value of the model on the test set to produce the predicted values.

