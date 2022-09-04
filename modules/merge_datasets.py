import os
import numpy as np
import pandas as pd

# old_data_dir = "../data/emnist_balanced/"
# old_train_filename = "emnist-balanced-train.csv"
# old_test_filename = "emnist-balanced-test.csv"

new_data_dir = "../data/new_datasets/"
new_filename = ""
for root, dirs, files in os.walk(new_data_dir):
    new_filename = files[-1]

# old_train_df = pd.read_csv(old_data_dir + old_train_filename)
# old_test_df = pd.read_csv(old_data_dir + old_test_filename)

new_df = pd.read_csv(new_data_dir + new_filename).sample(frac = 1)
n_split = int(0.8 * len(new_df))
new_train_df, new_test_df = new_df[:n_split], new_df[n_split:]

# merged_train_arr = np.concatenate([old_train_df.values, new_train_df.values], axis = 0)
# merged_train_df = pd.DataFrame(merged_train_arr).sample(frac = 1)
merged_train_df = new_train_df
# merged_test_arr = np.concatenate([old_test_df.values, new_test_df.values], axis = 0)
# merged_test_df = pd.DataFrame(merged_test_arr).sample(frac = 1)
merged_test_df = new_test_df

merged_train_df.to_csv("../data/merged_datasets/merged-train.csv", header = False, index = False)
merged_test_df.to_csv("../data/merged_datasets/merged-test.csv", header = False, index = False)
