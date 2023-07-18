import datetime
from datetime import datetime
import glob 
import pandas as pd
import os
from data_pipeline_methods import *


output_folder='csv_files/'
folder =activity_folder
files = find_csv_files(folder)
usernames = [file.split('_')[-3] for file in files] 

df = pd.DataFrame({'Username': usernames})

start_date = datetime(2021, 11, 8)
end_date = datetime(2021, 12, 19)
weeks_list = ['2021-11-08', '2021-11-15', '2021-11-22', '2021-11-29', '2021-12-06', '2021-12-13']

csv_files_path = folder 
column_name = 'activity per week (hours in course)' 

csv_files = glob.glob(csv_files_path) 
dataframe = convert_columns_to_rows(folder, files, weeks_list, column_name)
dataframe.to_csv(output_folder+'ISDT_bb_'+column_name+'.csv', index=False)
print(dataframe)
df1 = pd.read_csv(performance_folder+'gc_BN-N100-M0107-T1-M-22_fullgc_2023-05-22-18-29-31.csv')
merged_df = pd.merge(df1, dataframe, on='Username', how='inner')
merged_df.to_csv(output_folder+'ISDT_bb_dataset.csv')
print(merged_df)
