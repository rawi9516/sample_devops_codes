#!/usr/bin/env python
import pandas as pd
import os
import random
import argparse
import csv
from datetime import datetime

# Collecting the Arguments values
parser = argparse.ArgumentParser()
parser.add_argument("exchange", type=str, help="Global Exchange Parameter")
parser.add_argument("number_of_files", type=int, help="Number Of Sampled Files Parameter")
parser.add_argument("first_sample_file", type=str, help="First Sample File Name parameter")
parser.add_argument("second_sample_file", type=str, help="Second Sample File Name")
args = parser.parse_args()

#Print the Argument values
print(f"exchange: {args.exchange}")
print(f"number_of_files: {args.number_of_files}")
print(f"first_sample_file: {args.first_sample_file}")
print(f"second_sample_file: {args.second_sample_file}")

# steps to find the path of the files 
file_dir = os.path.dirname(os.path.realpath('__file__'))
first_file_name = os.path.join(file_dir, f'price_data/{args.exchange}/{args.first_sample_file}.csv')
second_file_name = os.path.join(file_dir, f'price_data/{args.exchange}/{args.second_sample_file}.csv')

#Defined a function to validate the file with multiple validations
def file_validation(file_name):
    if os.path.exists(file_name):
        print("The File Found.")
        if os.path.getsize(file_name) == 0:
            print("The File is empty.")
        else:
            with open(file_name, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                #below block is to check if particular fileds in .csv file are vlid like price colum need to be floating value & timelines with Datatime type. 
                for line_num, row in enumerate(csv_reader, start=1):
                    if not row:
                        continue
                    last_column_value = row[-1]
                    middle_column_value = row[1]
                    try:
                        float(last_column_value)
                        datetime.strptime(middle_column_value, "%d-%m-%Y")
                    except ValueError:
                        print("file has an invalid value in the datapoints.")
                        return False
                print("CSV file is readable.")
            #this block to validate if the .CSV file contains minimum 30 rows 
            df = pd.read_csv(file_name)
            if len(df) > 30:
                print("The File is usable.")
                return True
            else:
                print("The File need minimum 30 rows.")
    else:
        print("The File not found.")

#calling the file validation function to validate the .csv files
file_valid1 = file_validation(first_file_name)
file_valid2 = file_validation(second_file_name)

#function returns exactly 30 consecutive data points starting from a random timestamp within the file.
def get_consecutive_data(file_path):
    df = pd.read_csv(file_path)
    start_idx = random.randint(0, len(df) - 30)
    consecutive_data = df.iloc[start_idx:start_idx + 30]
    return consecutive_data

#function to returns the list of outliers with detailed fields as per requirements.
def detect_outliers(data_frame):
    price_list = data_frame.iloc[:,2]
    mean_value = price_list.mean()
    std_dev_value = price_list.std()
    threshold_upper = mean_value + 2 * std_dev_value
    threshold_lower = mean_value - 2 * std_dev_value 
    data_frame[3] =  mean_value
    data_frame[4] =  price_list - mean_value
    data_frame[5] = (abs(data_frame[4]) / data_frame[3]) * 100
    outliers = data_frame[(price_list > threshold_upper) | (price_list < threshold_lower)]
    outliers.columns = ['Stock_ID', 'Timestamp', 'actual_stock_price', 'mean', 'diff', '% deviation']
    return outliers

#function to display the outliers data
def outliers_results(outliers, filenumber):
    if not outliers.empty:
        output_filename = f"{filenumber}-outliers.csv"
        outliers.to_csv(output_filename, index=False)
        print("Outliers detected:")
        print(outliers)
    else:
        print("No outliers detected.")

#Utilizing the functions and calling it as per conditions of number of input files,only assumption that if selected file is 1 then it first validates
# the first file and process, if the first file invalid then it goes for second file and also meets the condition define in the requirements.
#If there aren’t enough files present for a given exchange, process whatever number of files are present even if it is lower. 
#E.g., input is 2 but only 1 file is present, so you process 1 file.

if args.number_of_files == 2:
    if file_valid1 :
        result = get_consecutive_data(first_file_name)
        outliers = detect_outliers(result)
        outliers_results(outliers, {args.first_sample_file})
    if file_valid2 :
        result = get_consecutive_data(second_file_name)
        outliers = detect_outliers(result)
        outliers_results(outliers, {args.second_sample_file})
else:
    if file_valid1 :
        result = get_consecutive_data(first_file_name)
        outliers = detect_outliers(result)
        outliers_results(outliers, {args.first_sample_file})
    elif file_valid2 :
        result = get_consecutive_data(second_file_name)
        outliers = detect_outliers(result)
        outliers_results(outliers, {args.second_sample_file})
    else:
        print("No valid file to process")