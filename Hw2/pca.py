# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4440 (Data Mining) - Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#importing some Python libraries
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#Load the data
    #LOADING THE CSV FILE with 10 COLUMNS
df = pd.read_csv("heart_disease_dataset.csv")
    
# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

#Get the number of features 
    #USED FOR THE LENGTH OF THE ENTIRE CSV USE TO ITERATE THROUGH ALL COLUMNS
        #KEY IN EXTRACTING SPECIFIC COLUMNS AND ITS DATA 
num_features = len(df.columns)
pca_variance = []
pca_var = {}
# Run PCA using 9 features, removing one feature at each iteration
for i in range(num_features):
#     # Create a new dataset by dropping the i-th feature
    reduced_data = df.drop(columns=[df.columns[i]])
    
#     # Run PCA on the reduced dataset
#         # WE USE LEN SINCE REDUCED DATA HAS ONE COLUMN LESS THAN THE ORIGINAL DATA 
# subtract one from num of features since every iteration has one col less to test 
    pca = PCA(n_components= num_features-1)

    X = pca.fit_transform(reduced_data)
#     #Store PC1 variance and the feature removed
      
    
#     print(pca.explained_variance_ratio_)
#     # pca_variance.append()

    pca_var[df.columns[i]] = np.max(pca.explained_variance_ratio_)
#     #Use pca.explained_variance_ratio_[0] and df_features.columns[i] for that
    # pca_variance.append([df.columns[i], pca.explained_variance_ratio_[0]])






max_pca = pca_var[df.columns[0]] #use the first item to start Max comaprison
feature ='' # attach the name 
    
# Find the maximum PC1 variance
for i in range(len(pca_var)):

    if pca_var[df.columns[i]] > max_pca:

        max_pca = pca_var[df.columns[i]]
        feature = df.columns[i]

print(f"The highest pc1 is: {max_pca} and its when column: {feature} is removed.")
#Print results
#Use the format: Highest PC1 variance found: ? when removing ?





