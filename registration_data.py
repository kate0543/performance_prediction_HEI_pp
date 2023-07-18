import pandas as pd
import numpy as np
from data_pipeline_methods import *


output_folder='csv_files/'
folder=performance_folder 
# registration_record=pd.read_excel(folder+'MST DB and MIT Registrations 21-22.xlsx')
# registration_record.to_csv(folder+'MST DB and MIT Registrations 21-22.csv')

registration_record=pd.read_csv(folder+'MST DB and MIT Registrations 21-22.csv')

df=pd.read_csv(output_folder+'ISDT_bb_dataset.csv')
df['Student ID']=df['Student ID'].astype(int)
# new_df['Student ID']=new_df['Student ID'].astype(str)
df['Banner ID'] = df['Student ID'].apply(lambda x: '@00' + str(x)) 
print(df)

new_df=registration_record
print(new_df.columns)
cols_to_use = new_df.columns.difference(df.columns)
merged_df= pd.merge(df, new_df[cols_to_use], left_on='Banner ID',right_on= 'BannerID', how='inner')
merged_df.to_csv(output_folder+'ISDT_dataset_new.csv')
print(merged_df.columns)
 
