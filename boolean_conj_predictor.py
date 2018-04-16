import os
import sys
import numpy as np


def calculatePrediction(hypothesis):
    prediction = 1
    d = len(hypothesis)/2
    for i in range(len(hypothesis)):
        if i >= d:
            if hypothesis[i] == 1:
                prediction = prediction*(hypothesis[i]-1)
        else:
            if hypothesis[i] == 1:
                prediction = prediction*hypothesis[i]

    return prediction


def main():
    # This Program accepts a file path as an input parameter
    # e.g. python boolean_conj_predictor.py trainingData\example1.txt
    file_path = sys.argv[1]

    # loading the data from file.
    training_examples = np.loadtxt(file_path)

    # our d equals the size of the bits without the classification.
    d = training_examples[0].size - 1

    # the amount of data we are working with.
    num_examples = training_examples.size/(d+1)

    # separating the data into two containers.
    # matrix that its columns correspond to the examples of the training data.
    matrix_X = training_examples[:, :-1]
    # vector such that its values correspond to the classification.
    vector_Y = training_examples[:, d:]

    # representing the hypothesis in an array.
    hypothesis = [1] * (2*d)

    for i in range(num_examples):
        our_Prediction = calculatePrediction(hypothesis)
        real_Prediction = vector_Y[i]
        if real_Prediction == 1 and our_Prediction == 0:
            for x in range(d):
                if matrix_X[i][x] == 1:
                    hypothesis[x+d] = 0
                if matrix_X[i][x] == 0:
                    hypothesis[x] = 0

    #algorithm's final redicated boolean conjunction written to a file.
    file = open("output.txt", "w")
    for i in range(d):
        if hypothesis[i] == 1:
            file.write("x" + str(i+1) + ",")
        elif hypothesis[i+d] == 1:
            file.write("not(x" + str(i+1) + "),")
    file.seek(-1, os.SEEK_END)
    file.truncate()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Missing Input Training File "
        sys.exit(1)
    main()