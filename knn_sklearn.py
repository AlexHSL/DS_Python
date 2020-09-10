from sklearn import neighbors
import nlp_3


def knn_sklearn_predict():
    knn = neighbors.KNeighborsClassifier()
    dataset, label = nlp_3.create_dataset()
    knn.fit(dataset, label)
    return knn.predict([[2, 4, 0], [1, 1, 1]])


if __name__ == "__main__":
    print(knn_sklearn_predict())