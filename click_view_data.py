import pandas as pd
import numpy as np
from data_pipeline_methods import *


folder=performance_folder
# click_record=pd.read_excel(folder+'7b5a59828993482b9705e5272016a609.xlsx')
# click_record.to_csv(folder+'7b5a59828993482b9705e5272016a609.csv')
click_record=pd.read_csv(folder+'7b5a59828993482b9705e5272016a609.csv')

module_ID='M0107' 
new_df=filter_value_bb_activity('Module ID',module_ID,click_record) 
new_df.to_csv(module_ID+'_click_view.csv') 
df=pd.read_csv('ISDT_bb_dataset.csv')
df['Username']=df['Username'].str.upper() 

merged_df = pd.merge(df, new_df, left_on='Username',right_on= 'Network ID', how='inner')
merged_df.to_csv('ISDT_dataset.csv')
print(merged_df.columns)
