# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4440 (Data Mining) - Assignment #3
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#IMPORTANT NOTE: YOU ARE ALLOWED TO USE ANY PYTHON LIBRARY TO COMPLETE THIS PROGRAM

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score


#  'cheat_training_2.csv', 'cheat_training_3.csv'
dataSets = ['cheat_training_1.csv']

for ds in dataSets:

    X = []
    Y = []



    df = pd.read_csv(ds, sep=',', header=0)   #reading a dataset eliminating the header (Pandas library)
    
    
    data_training = np.array(df.values)[:,1:] #creating a training matrix without the id (NumPy library)

    #transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
    refund_encoded = np.where(data_training[:, 0] == 'Yes', 1, 0)
    marital_status = data_training[:, 1]
    single = (marital_status == 'Single').astype(int)
    divorced = (marital_status == 'Divorced').astype(int)
    married = (marital_status == 'Married').astype(int)
    income_clean = np.char.replace(data_training[:, 2].astype(str), 'k', '')
    income_floats = income_clean.astype(float)
    labels_encoded = np.where(data_training[:, 3] == 'Yes', 1, 2)

    X = np.column_stack((refund_encoded, single, divorced, married, income_floats)).tolist()
    Y = labels_encoded.tolist()



   
    

    
    #Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
    #be converted to a float.
    # X =
    X = np.array(X)
    #transform the original training classes to numbers and add them to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    Y = np.array(Y)
    accuracy = []
    #loop your training and test tasks 10 times here
    for i in range (10):

    #    #fitting the decision tree to the data by using Gini index and no max_depth
        clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=None)
        clf = clf.fit(X, Y)

    #    #plotting the decision tree
        tree.plot_tree(clf, feature_names=['Refund', 'Single', 'Divorced', 'Married', 'Taxable Income'],     class_names=['Yes','No'], filled=True, rounded=True)
        plt.show()

    #    #read the test data and add this data to data_test NumPy
    #    #--> add your Python code here
        df_test = pd.read_csv('cheat_test.csv', sep=',', header=0)
        data_test = np.array(df_test.values)[:,1:]



        for data in data_test:
    #        #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
    #        #class_predicted = clf.predict([[1, 0, 1, 0, 115]])[0], where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
    #        #--> add your Python code here
            refund_encoded = np.where(data_test[:, 0] == 'Yes', 1, 2)
            marital_status = data_test[:, 1]
            single = (marital_status == 'Single').astype(int)
            divorced = (marital_status == 'Divorced').astype(int)
            married = (marital_status == 'Married').astype(int)
            income_clean = np.char.replace(data_test[:, 2].astype(str), 'k', '')
            income_floats = income_clean.astype(float)
            true_labels = np.where(data_test[:, 3] == 'Yes', 1, 2)


            X_test = np.column_stack((refund_encoded, single, divorced, married, income_floats))



            predicted_labels = clf.predict(X_test)



        correct = np.sum(predicted_labels == true_labels)
        total = len(true_labels)
        acc = correct / total
        accuracy.append(acc)




    final_accuracy = sum(accuracy) / len(accuracy)
    print(f"final accuracy when training on {ds}: {final_accuracy:.2f}")





