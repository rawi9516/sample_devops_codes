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

 **Inputs**

        |   **Name**                |      **Description**                                      |   **sample Vaules**   |
        |---------------------------|-----------------------------------------------------------|-----------------------|
        | `subscription ID`         |`subscription value`                                       | `5c09efad-987e-4392-b86b-e27fddefe153`|
        | `Environment`             |`Environment prefix for different environments`            | `dev` |
        | `Resource Group Location` | `Azure data centers where the resource has to be created` | `west europe` |

## Tech Details

        1. Terraform : Terraform modules are created to provision resource in Azure (Infrastructure As Code)
        2. YAML : Dynamic input parameters with YAML Templates are created for pipeline execution
        3. Az modules for Non-terraform modules

## Demo Piplines

        1. Manual trigger pipeline
        2. Auto schedule pipeline
        3. VM- start and stop pipeline