#-------------------------------------------------------------------------
# AUTHOR: edgar
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4440- Assignment #4
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv 
import numpy as np 
#11 classes after discretization


classes = [i for i in range(-22, 40, 6)]

s_values = [0.1, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001]

#reading the training data
X_train = []
Y_train = []

with open('weather_training.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        try:
            attributes = [float(row[i]) for i in range(1, 6)]
            temp = float(row[6])
        except Exception:
            continue
        X_train.append(attributes)
        Y_train.append(temp)



# make them numpy 
X_train = np.array(X_train)
Y_train = np.array(Y_train)
#update the training class values according to the discretization (11 values only)
#--> add your Python code here

disc = []


for v in Y_train:
    close = min(classes, key = lambda c:abs(v-c))
    disc.append(close)

Y_train = np.array(disc)



X_test = []
Y_test = []
with open('weather_test.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        try:
            features = [float(row[i]) for i in range(1, 6)]
            temp = float(row[6])
        except Exception:
            continue
        X_test.append(features)

        Y_test.append(temp)
#make it numpy 
X_test = np.array(X_test)
Y_test = np.array(Y_test)


disc2 =[]
#update the test class values according to the discretization (11 values only)
#--> add your Python code here
for v in Y_test:
    close = min(classes, key = lambda c: abs(v-c))
    disc2.append(close)

Y_test = np.array(disc2)
#loop over the hyperparameter value (s)
#--> add your Python code here
high_acc = 0.0

best_s = None







for s in s_values:

    #fitting the naive_bayes to the data
    clf = GaussianNB(var_smoothing=s)
    clf = clf.fit(X_train, Y_train)

    #make the naive_bayes prediction for each test sample and start computing its accuracy

    predict = clf.predict(X_test)
    correct = 0
    #the prediction should be considered correct if the output value is [-15%,+15%] distant from the real output values
    #to calculate the % difference between the prediction and the real output values use: 100*(|predicted_value - real_value|)/real_value))
    for p, real_val in zip(predict,Y_test):

        if abs(real_val) > 1e-8:
            percent = 100 *abs(p-real_val)/abs(real_val)
        else:
            percent = 100 * abs(p-real_val)

        if percent <= 15.0:
            correct += 1


    # check if the calculated accuracy is higher than the previously one calculated. If so, update the highest accuracy and print it together
    # with the KNN hyperparameters. Example: "Highest Naive Bayes accuracy so far: 0.32, Parameters: s=0.1
    acc = correct/len(Y_test) if len(Y_test) > 0 else 0.0



    if acc > high_acc:
        high_acc = acc
        best_s = s

        print(f"Highest accuracy: {high_acc}")
        print(f"Parameters s is {best_s}")



