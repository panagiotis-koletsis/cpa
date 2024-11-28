import pandas as pd
import glob
import os


#---------------------this function only runs the first time
# def read_gt(task): 
#     file_path = '/home/kpanag/Desktop/semtab/round1_23/cpa_gt.csv'
#     #print(file_path)
#     gt = pd.read_csv(file_path)
#     #print(gt)
#     return(gt)



def read_datasets():

    # Path to the folder containing CSV files
    folder_path = '/home/kpanag/Desktop/semtab/round1_23/random_datasets'
    #folder_path = '/home/kpanag/Desktop/semtab/all_datasets'

    # Get a list of all CSV files in the folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    #print(csv_files)

    file_names = [os.path.basename(path) for path in csv_files]
    file_names =  [filename.replace(".csv", "") for filename in file_names]
    file_names =  [filename.replace("'", "") for filename in file_names]

    #print(file_names)
    # List to hold DataFrames
    dataframes = []

    # Loop through the list of CSV files and read each file
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    return dataframes, file_names    

def read_gt():
    file_path = 'data/gt_22.csv'
    gt = pd.read_csv(file_path)
    return gt 
