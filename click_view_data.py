import pandas as pd
import numpy as np
from data_pipeline_methods import *

output_folder='csv_files/'
folder=performance_folder
# click_record=pd.read_excel(folder+'7b5a59828993482b9705e5272016a609.xlsx')
# click_record.to_csv(folder+'7b5a59828993482b9705e5272016a609.csv')
click_record=pd.read_csv(folder+'7b5a59828993482b9705e5272016a609.csv')

module_ID='M0107' 
new_df=filter_value_bb_activity('Module ID',module_ID,click_record) 
new_df.to_csv(output_folder+module_ID+'_click_view.csv') 
df=pd.read_csv(output_folder+'ISDT_bb_dataset.csv')
df['Username']=df['Username'].str.upper() 
cols_to_use = new_df.columns.difference(df.columns)
df['Student ID']=df['Student ID'].astype(int)
# df['Student ID']=df['Student ID'].astype(str)
print(cols_to_use)
# exit()

merged_df = pd.merge(df, new_df[cols_to_use], left_on='Username',right_on= 'Network ID', how='inner')
merged_df.to_csv(output_folder+'ISDT_dataset.csv')
print(merged_df)




