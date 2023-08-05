import math

def evaluate_accuracy(dataset, selected_features):
    correct_predictions = 0
    for current_data in dataset:
        shortest_distance = float('inf')
        most_similar_data = None
        for comparison_data in dataset:
            if current_data != comparison_data:
                distance = sum((current_data[index] - comparison_data[index])**2 for index in selected_features)
                distance = math.sqrt(distance)
                if distance < shortest_distance:
                    shortest_distance = distance
                    most_similar_data = comparison_data
        if current_data[0] == most_similar_data[0]:
            correct_predictions += 1
    return correct_predictions / len(dataset) * 100

def perform_forward_selection(dataset, total_features):
    chosen_features = []
    best_accuracy = 0
    print("Beginning search.\n")
    for _ in range(1, total_features + 1): 
        feature_to_add = None
        local_best_feature = None
        accuracy_decreased = True
        local_best_accuracy = 0
        for feature_index in range(1, total_features + 1):
            if feature_index not in chosen_features:
                current_features = chosen_features[:]
                current_features.append(feature_index)
                accuracy = evaluate_accuracy(dataset, current_features)
                print(f"Using Feature(s) {current_features} accuracy is {accuracy}%")
                if accuracy > local_best_accuracy:
                    local_best_accuracy = accuracy
                    local_best_feature = feature_index
                    feature_to_add = feature_index
        print()
        if local_best_accuracy > best_accuracy:
            best_accuracy = local_best_accuracy
            chosen_features.append(feature_to_add)
            accuracy_decreased = False
            print(f"Feature set {chosen_features} was best, accuracy is {local_best_accuracy}%")        
        else:
            current_features = chosen_features[:]
            current_features.append(local_best_feature)
            print(f"Feature set {current_features} was best, accuracy is {local_best_accuracy}%")         
        print() 
        if accuracy_decreased:
            print("\n(Warning, Accuracy has decreased!)")
            print(f"Finished search!!! The best feature set is {chosen_features}, which has an accuracy of {best_accuracy}%")
            break

def perform_backward_elimination(dataset, total_features):
    chosen_features = [i for i in range(1, total_features + 1)]
    initialize = [i for i in range(1, total_features + 1)]
    best_accuracy = evaluate_accuracy(dataset, initialize)
    print("Beginning search.\n")
    for _ in range(total_features, 1, -1): 
        feature_to_remove = None
        local_best_feature = None
        accuracy_decreased = True
        local_best_accuracy = 0
        for feature_index in range(1, total_features + 1):
            if feature_index in chosen_features:
                current_features = chosen_features[:]
                current_features.remove(feature_index)
                accuracy = evaluate_accuracy(dataset, current_features)
                print(f"Using Feature(s) {current_features} accuracy is {accuracy}%")
                if accuracy > local_best_accuracy:
                    local_best_accuracy = accuracy
                    local_best_feature = feature_index
                    feature_to_remove = feature_index
        print()
        if local_best_accuracy > best_accuracy:
            best_accuracy = local_best_accuracy
            chosen_features.remove(feature_to_remove)
            accuracy_decreased = False
            print(f"Feature set {chosen_features} was best, accuracy is {local_best_accuracy}%")        
        else:
            current_features = chosen_features[:]
            current_features.remove(local_best_feature)
            print(f"Feature set {current_features} was best, accuracy is {local_best_accuracy}%")         
        print() 
        if accuracy_decreased or len(chosen_features) == 1:
            print("\n(Warning, Accuracy has decreased!)")
            print(f"Finished search!!! The best feature set is {chosen_features}, which has an accuracy of {best_accuracy}%")
            break

def load_dataset(file_name):
    dataset = []
    with open(file_name, 'r') as file:
        for line in file:
            data_point = [float(number) for number in line.split()]
            dataset.append(data_point)
    return dataset

def get_algorithm_choice():
    return int(input("Enter algorithm choice: 1)Forward Selection 2) Backwards Elimination "))

def main():
    file_name = input("Type in the name of the file to test: ")
    dataset = load_dataset(file_name)
    total_features = len(dataset[0]) - 1
    algorithm_choice = get_algorithm_choice()

    if algorithm_choice == 1:
        perform_forward_selection(dataset, total_features)
    elif algorithm_choice == 2:
        perform_backward_elimination(dataset, total_features)
    else:
        print("Invalid choice. Please select either 1 for Forward Selection or 2 for Backwards Elimination.")

if __name__ == "__main__":
    main()
