import os
import shutil
import pandas as pd
import datetime
from datetime import datetime

performance_folder=folder = '../../../Downloads/New Folder/'
activity_folder = '../../../Downloads/New Folder/ISDT/'

def move_files(source_directory, destination_directory, files):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for filepath in files:
        filename = os.path.basename(filepath)
        destination_path = os.path.join(destination_directory, filename)
        shutil.move(filepath, destination_path)
        print(f"Moved {filename} to {destination_directory}")

def find_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
               csv_files.append(file)
    return csv_files

def find_csv_files_with_value(directory, value_list):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                for value in value_list:
                    if value in file:
                        csv_files.append(os.path.join(root, file))
                        break   
    return csv_files

def filter_time_range_bb_activity(start_date, end_date, df): 
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df = df.reset_index(drop=True)
    hours = df[df.columns[0:2]].reset_index(drop=True)
    return df 

def filter_value_bb_activity(column_name,value, df): 
    df = df[df[column_name].str.contains(value) ]
    df = df.reset_index(drop=True)
    hours = df[df.columns[0:2]].reset_index(drop=True)
    return df 

def convert_columns_to_rows(folder, csv_files, weeks_list, column_name):
    data = []
    start_date = datetime(2021, 11, 8)
    end_date = datetime(2021, 12, 19)
    for file in csv_files:
        df = pd.read_csv(os.path.join(folder, file))
        df['Date'] = pd.to_datetime(df['Date'], format="%d %b %Y, %H:%M:%S")
        df = filter_time_range_bb_activity(start_date, end_date, df)
        col_name = df.columns[-1]
        
        column_data = df[col_name].replace('-',0).tolist()
        username = file.split('_')[1]
        row_data = [username] + column_data
        data.append(row_data)

    weeks_list.insert(0, 'Username')
    dataframe = pd.DataFrame(data, columns=weeks_list)
    return dataframe
