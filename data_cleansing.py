# Importing the required libraries here
import numpy as np
import pandas as pd

#function to cleanse dataset
def cleanse():

    # loading data into a dataframe
    factors_df = pd.read_excel('Factors contributing to the success and the failures of TUT students.xlsx')

    # removing duplicate rows
    factors_df.drop_duplicates(keep='first')

    # creating a list of the columns to remove
    columns = ['ID','Start time','Completion time','Email','Name','Last modified time']

    factors_df = factors_df.drop(columns, axis = 1) #dropping colums

    # proposed new column names list
    new_columns = [
        'Faculty','Registration Year','Funding','NSFAS Application Process',
        'Recommendations On NSFAS Process',
        'NSFAS Process Rating',
        'Residence','Reason for Off Campus Stay','Graduation Status','Completion Period',
        'Reason for No Graduation',
        'Major Challenges','Support','Challenges With Lecturers',
        'Lecture Ratings','Reason For Rating',
        'Employment Status','Employed In Field Of Study',
        'Period Spent Looking For Work','Was It Easy Applying Undergrad Knowledge',
        'Career Aspirations','TUT Rating','Recommendations'
    ]

    # renaming the columns in the dataframe
    factors_df = factors_df.set_axis(new_columns, axis = 1)

    #imputation on the columns with missing values
    columns = ['NSFAS Application Process','Recommendations On NSFAS Process']

    factors_df[columns] = factors_df[columns].fillna('Not Applicable')

    factors_df['NSFAS Process Rating'] = factors_df['NSFAS Process Rating'].fillna(0)

    columns = ['Reason for No Graduation', 'Employed In Field Of Study']

    factors_df[columns] = factors_df[columns].fillna('No Answer')

    factors_df['Reason for Off Campus Stay'] = factors_df['Reason for Off Campus Stay'].fillna('Not Applicable')

    # returning the cleansed dataframe
    return factors_df