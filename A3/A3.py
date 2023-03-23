#*********************************************************************
#File name:     A3.ipynb
#Author:        Roman Stein      
#Date:  	    03/5/23
#Class: 	    DSCI 440W
#Assignment:    IA3
#Purpose:       Decision Stump & the Tree    
#**********************************************************************

#imports
import sympy as sp
import numpy as np
import pylab as pp
import math
import csv
import matplotlib.pyplot as plt
from sympy import *
from numpy.linalg import inv, norm
sp.init_printing(use_unicode=True, use_latex='mathjax')

TEST_FILE = '/Users/nadesocko/Desktop/MachineLearning/A3/SPECT-test.csv'
TRAIN_FILE = '/Users/nadesocko/Desktop/MachineLearning/A3/SPECT-train.csv'
LABEL_INDEX = 22
BIAS = 1
TWO = 2

#Read Data
def readCSVData(fileName):
    """    
    Function:   readData
    Descripion: Opens and reads text file
    Input:      fileName - name of file to read from
    Output:     dataList - numpy array of data from file being read
    """
    dataList = []
    # with open(fileName, "r") as f:
    #     raw = f.read()
    #     for line in raw.split("\n"):
    #         subLine = line.split()
    #         dataList.append(subLine)

    with open(fileName, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            dataList.append(row)
    return dataList

def getNumRows(matX):
    """
    Function:       getNumRows
    Description:    Returns number of rows of passed in matrix
    Input:          matx -  Matrix in question
    Output:         numRows - number of rows in matrix X
    """
    num = shape(matX)

    numRows = num[0]
    return numRows

def calcBenOfSplit(root, output):
    """
    Function:       calcBenOfSplit
    Description:    Calculates the amount of information gain for a specific split of a feater into two leafs.
    Input:          root - array of stratig features
                    leaf1 - array 1 of restuling split from root
                    leaf2 - array 2 of resutling split from root
    Output:         
    """
    leaf0 = []
    leaf1 = []
    rootEntropy = calcFeatureEntropy(output)
    # print(f"rootEntropy: {rootEntropy}")
    rootLen = len(root)
    for i in range(rootLen):
        if(root[i] == 0):
            leaf0.append(output[i])
        elif(root[i] == 1):
            leaf1.append(output[i])
        else:
            print("Bad data")
            return
    leaf0Entropy = calcFeatureEntropy(leaf0)
    # print(f"leaf 0 entropy: {leaf0Entropy}")
    leaf1Entropy = calcFeatureEntropy(leaf1)
    # print(f"leaf 1 entropy: {leaf1Entropy}")
    leaf0Len = len(leaf0)
    leaf1Len = len(leaf1)
    flow0 = leaf0Len / rootLen
    flow1 = leaf1Len / rootLen

    benOfSplit = rootEntropy - ((leaf0Entropy * flow0) + (leaf1Entropy * flow1))

    return benOfSplit


def calcFeatureEntropy(feature):
    prob0 = 0
    prob1 = 0
    num0 = 0
    num1 = 0
    numFeatures = len(feature)
    if not (numFeatures == 0):
        for i in range(numFeatures):
            if (feature[i] == 0):
                num0 += 1
            elif (feature[i] == 1):
                num1 += 1
            else:
                print ("bad entropy data")
                return(1)
        if not (num0 == 0):
            prob0 = num0 / numFeatures
        if not (num1 ==0):
            prob1 = num1 / numFeatures
        if not (prob1 == 0 or prob0 == 0):
            entropy = (-(prob0 * math.log2(prob0)) - (prob1 * math.log2(prob1)))
        elif (prob0 == 0):
            entropy = -(prob1 * math.log2(prob1))
        elif (prob1 == 0):
            entropy = -(prob0 * math.log2(prob0))
        else:
            entropy = 0
    else:
        entropy = 0

    return(entropy)






def driver():


    testData = []
    trainData = []
    trainOutput = []
    testOutput = []

    testData = readCSVData(TEST_FILE)
    trainData = readCSVData(TRAIN_FILE)
    testLabel_Index = 0
    trainLabel_Index = 0



    #Apply outpts to its own array
    for i in range(len(trainData)):
        trainOutput.append(trainData[i][trainLabel_Index])

    for i in range(len(testData)):
        testOutput.append(testData[i][testLabel_Index])

    #Convert outputs to numpy array
    trainOutput = np.array(trainOutput, dtype=float)
    testOutput = np.array(testOutput, dtype=float)

    #Create input array
    trainFeatures = np.array(trainData, dtype=float)
    testFeatures = np.array(testData,dtype=float)

    numTrainFeatures = len(trainOutput)

    #Delte label from feature array
    trainFeatures = np.delete(trainFeatures,0, axis=1)
    testFeatures = np.delete(testFeatures,0, axis=1)

    #reshape arary
    trainOutput = trainOutput.reshape(numTrainFeatures,1)
    numTestFeatures =  getNumRows(testFeatures)
    testOutput = testOutput.reshape(numTestFeatures,1)
    numTrainFeatures = len(trainFeatures)


    # print(trainInputs[0])
    # tamir = trainInputs.T
    # print(tamir[0])
    # Determine Root Node
    maxGain = -1
    index = -1
    featuresTranspose = trainFeatures.T
    num = len(featuresTranspose)
    for i in range(num):
        gain = calcBenOfSplit(featuresTranspose[i], trainOutput)
        print(f"Feature: {i} Information gain: {gain}")
        if (gain > maxGain):
            maxGain = gain
            index = i

    for i in range (len(featuresTranspose[i])):
        gain = calcBenOfSplit(featuresTranspose[i],featuresTranspose[index])
    print()
    print(f"The fature located at index: {index} has most information gain of: {maxGain}")

    print()
    print("Test Data")
    numCorrect = 0
    numWrong = 0
    print("Im not sure how to usehte test data with my tee since it doenst perfectly divide it")

    print()
    print("DT with Early Stopping")
    outPut
    for i in range(num):
        if (i == index):
            return
        else:
            gain



    # print(trainInputs)

## Using entorpy nad benefit of split we dhuld cycle through all possble slits to find the one tha maximizes benefit

#Testin Area
# if(len(root) == len(result)):
#     print('Len Good')
# print(calcBenOfSplit(root,output))
# feature = [[1],[1],[1],[0],[0],[0],[0],[0],[0],[1],[1],[1],[1],[0]]
# output =  [1,1,1,1,1,1,1,1,1,0,0,0,0,0]
# # print(calcBenOfSplit(feature,output))
# feature = np.array(feature)
# print(feature.T)
# print(calcFeatureEntropy(feature, output))
# root = [1,1,1,1,1,0,0,0,0]
# print(calcFeatureEntropy(root))

driver()
