# Feature-Selection-Toolkit-for-Nearest-Neighbor-Classification
A Python toolkit for optimized feature selection in Nearest Neighbor classification using greedy search algorithms (Forward Selection &amp; Backward Elimination), combined with Euclidean distance and leave-one-out validation.

## Overview

This project provides a comprehensive toolkit for optimizing feature selection in machine learning models using Nearest Neighbor classification. Through the implementation of greedy search algorithms, Forward Selection and Backward Elimination, it aims to enhance classification accuracy. The toolkit leverages Euclidean distance metric and the leave-one-out validation technique for the optimization process.


## Datasets

Two datasets have been provided for demonstration:

- [Small Dataset](CS170_Spring_2022_Small_data__93.txt)
- [Large Dataset](CS170_Spring_2022_Large_data__93.txt)

## Algorithms

### 1. Forward Selection

This greedy search algorithm begins with an empty set of features and iteratively adds the most significant feature until no further improvement is observed.

### 2. Backward Elimination

Starting with all features, this greedy search algorithm iteratively removes the least significant feature until no further improvement is observed.

## Results

### Forward Selection (Small Dataset):

- **Single Feature**: The highest classification accuracy achieved with a single feature was 90% using feature #7.
- **Two Features**: Combining features #7 and #6 yielded an improved accuracy of 95%.

| Feature Combination      | Accuracy (%) |
|--------------------------|--------------|
| 7                        | 90           |
| 7, 6                     | 95           |
| 7, 6, 3                  | 94           |


### Backward Elimination (Small Dataset):

- **All Features**: Using all features, the classification accuracy was 78%.
- **Nine Features**: Removing feature #1 improved the accuracy to 80%.
- **Eight Features**: The highest classification accuracy achieved was 87% removing features 1# and #10.

| Feature Combination        | Accuracy (%) |
|----------------------------|--------------|
| 1, 2, 3, 4, 5, 6, 7, 9, 10 | 78        |
| 2, 3, 4, 5, 6, 7, 9, 10    | 80          |
| 2, 3, 4, 5, 6, 7, 9        | 85          |
| 2, 3, 4, 6, 7, 9           | 83          |

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.
