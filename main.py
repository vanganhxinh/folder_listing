import os
import pandas as pd

# Function to retrieve list of sub folders inside a folder and export the list to csv file
# Input parameter: path to the parent folder - string (e.g.: 'D:\\my_folder')


def get_folder_list(folder_path):
    data = []

    for root, dirs, files in os.walk(folder_path, topdown=False):
        data.append(root)

    df = pd.DataFrame(data)
    df = df.rename(columns={0: 'FOLDER'})
    df.to_csv('folder.csv', sep='\t', encoding='utf-8', index=False, compression=None)


if __name__ == '__main__':
    get_folder_list('D:\\my_folder')