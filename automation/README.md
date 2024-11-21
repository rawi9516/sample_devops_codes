## Introduction

        This Demo project is all about Identify outliers of timeseries data

## Prerequisites

        1.  Azure DevOps (dev.azure.com) project
        2.  Microsoft hosted agents or self-hosted agents with python version 3.11

## Project structure
        
        |-- price_data                           -(folder to stroe the data files)
        |--------- LSE                           -(folder contains the data file .csv from LSE)
        |--------- NASDAQ                        -(folder contains the data file .csv from NASDAQ)
        |--------- NSE                           -(folder contains the data file .csv with different test scanerios like wrong.csv file etc)
        |--------- NYSE                          -(folder contains the data file .csv from NYSE)
        |-- script                               -(folder to stroe the script files)
        |--------- data_outliers.py              -(python script with functionality)
        |-- data_outliers_pipeline.yml           -(Azure DevOps YAML pipeline to execute the Python script)
        |-- README.md                            --(Read file instructions to execute these scripts)

 **Execution Steps **

        1. create a Azure devops project 
        2. upload the contents of "automation" folder or add the cotents of "automation" folder to the devops repository
        3. create a pipleine using "data_outliers_pipeline.yml"
        4. fill the details and Run the pipeline 
        6. results will be generated as .CSV file and readability purpose the details are displayed in the pipeline logs.

## Tech Details

        1. the main script is wtitten in python
        2. Azure devops YAML approach is used to run the scripts as pipelines
        3. sample data files are available at "price_data" fodler to refer
        4. "NSE" folder under "price_data" folder cntains files to validate some of the below cases. 
                        a. pipeline handling empty.csv file
                        b. pipeline validating .csv file 
                        c. pipeline handling wrong data type for price (decimal) and date(datetime)
                        d. pipeline handing wrong file names and empty fileds
                        e. skiping script exeution if both file names are empty

        Note: as per ask the pipeline or scripts are written to handle the cases (not to terminate or break execution).
        
