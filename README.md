# Perceptron Classifier for Iris Dataset

## Overview

This project implements a perceptron-based binary classifier that can distinguish between two classes of flowers from the Iris dataset. It uses the **delta rule** for training, and provides functionalities to:
- Train the perceptron on a given training dataset.
- Evaluate the perceptron's accuracy on a test dataset.
- Allow real-time classification of input vectors provided by the user.

The program is designed to demonstrate fundamental concepts in machine learning, including supervised learning, gradient-based updates, and the perceptron algorithm.

---

## Features

1. **Training on CSV Dataset:**
   - Accepts a training dataset (`train-set`) in CSV format.
   - Uses a specified learning rate (`a`) to train the perceptron.

2. **Evaluation:**
   - Computes overall classification accuracy on a test dataset (`test-set`).
   - Reports accuracy for each individual class.

3. **Interactive Classification:**
   - Allows the user to classify individual feature vectors through a simple text-based interface.

---

