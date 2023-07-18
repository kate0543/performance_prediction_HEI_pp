import calendar
import pandas as pd
from datetime import datetime
from data_pipeline_methods import *

output_folder='csv_files/'
folder = '../../../Downloads/New Folder/'
appendix = '.csv'
ISDT_bb_record_file = 'gc_BN-N100-M0107-T1-M-22_fullgc_2023-05-22-18-29-31'
filename = 'BN-N100-M0107-T1-M-22_laf854_20230522_a'

df = pd.read_csv(folder + 'ISDT/' + filename + appendix)
ISDT_bb_record = pd.read_csv(folder + ISDT_bb_record_file + appendix)
ISDT_bb_record_dict = ISDT_bb_record.to_dict()

my_dict = {month: index for index, month in enumerate(calendar.month_abbr) if month}

start_date = datetime(2021, 11, 8)
end_date = datetime(2021, 12, 19)

df['Date'] = pd.to_datetime(df['Date'], format="%d %b %Y, %H:%M:%S")



new_df = filter_time_range_bb_activity(start_date, end_date, df)
weeks = new_df['Date'].dt.strftime('%Y-%m-%d').tolist()

for week in weeks:
    if week not in ISDT_bb_record.columns:
        ISDT_bb_record[week] = ""

ISDT_bb_record.to_csv(output_folder+'ISDT_bb_performance.csv')

def find_csv_files_with_value(directory, value_list):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                for value in value_list:
                    if value in file:
                        csv_files.append(os.path.join(root, file))
                        break  # Stop searching for other values in this file
    return csv_files
print(ISDT_bb_record.columns)