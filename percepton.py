
import csv
import numpy as np
import sys


def read_csv(filename):
    data = []
    labels = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append([float(x) for x in row[:-1]])
            labels.append(row[-1])

    data = np.array(data)
    labels = np.array(labels)

    # Shuffle the data and labels
    indices = np.random.permutation(len(data))
    data = data[indices]
    labels = labels[indices]

    return data, labels
def train_perceptron(train_data, train_labels, learning_rate, max_iterations=1):
    num_features = train_data.shape[1]
    weights = np.random.uniform(-5, 5, num_features)
    print(weights)
    bias = 1

    for _ in range(max_iterations):
        for i in range(len(train_data)):
            x, label = train_data[i], train_labels[i]
            prediction = int(np.dot(x, weights) + bias > 0)
            error = label - prediction
            weights += learning_rate * error * x
            bias += learning_rate * error

    return weights, bias

def predict_perceptron(x, weights, bias):
    return int(np.dot(x, weights) + bias > 0)

def main(a, train_set_file, test_set_file):
    train_data, train_labels = read_csv(train_set_file)
    test_data, test_labels = read_csv(test_set_file)
    list_of_train_labels = set(train_labels)

    train_labels[train_labels == list(list_of_train_labels)[1]] = 0
    train_labels[train_labels == list(list_of_train_labels)[0]] = 1
    train_labels = train_labels.astype(int)
    list_of_test_labels = set(test_labels)
    test_labels[test_labels == list(list_of_test_labels)[1]] = 0
    test_labels[test_labels == list(list_of_test_labels)[0]] = 1
    test_labels = test_labels.astype(int)

    weights, bias = train_perceptron(train_data, train_labels, a)

    correct_predictions = 0
    class_correct_predictions = [0, 0]
    class_count = [0, 0]

    for i in range(len(test_data)):
        x, true_label = test_data[i], test_labels[i]
        predicted_label = predict_perceptron(x, weights, bias)

        if predicted_label == true_label:
            correct_predictions += 1
            class_correct_predictions[true_label] += 1

        class_count[true_label] += 1

    overall_accuracy = correct_predictions / len(test_data)
    class_accuracies = [class_correct_predictions[i] / class_count[i] for i in range(2)]

    print(f"Overall accuracy: {overall_accuracy * 100:.2f}%")
    print(f"1st flower accuracy: {class_accuracies[0] * 100:.2f}%")
    print(f"2nd flower accuracy: {class_accuracies[1] * 100:.2f}%")
    print(class_correct_predictions)
    print(class_accuracies)

    while True:
        user_input = input("Enter a vector to classify (separated by commas) or 'q' to quit: ")
        if user_input == 'q':
            break

        try:
            user_vector = np.array([float(x) for x in user_input.split(',')])
            prediction = predict_perceptron(user_vector, weights, bias)

            if prediction == 0:
                print("flower 1")
            else:
                print("flower 2")
        except:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python perceptron.py a train_set_file test_set_file")
        sys.exit(1)
    main(0.5 ,'train-setcik.csv ','iris.csv')

