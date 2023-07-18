import os
import shutil
import pandas as pd

from data_pipeline_methods import *

appendix = '.csv'
ISDT_bb_record_file = 'gc_BN-N100-M0107-T1-M-22_fullgc_2023-05-22-18-29-31'

ISDT_bb_record = pd.read_csv(os.path.join(folder, ISDT_bb_record_file + appendix))
ISDT_students = ISDT_bb_record['Username']

source_dir = '../../../Downloads/'   
destination_dir = activity_folder  

matching_files = find_csv_files_with_value(source_dir, ISDT_students)

move_files(source_dir, destination_dir, matching_files)
