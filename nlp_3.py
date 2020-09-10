import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
from numpy.lib.shape_base import tile
myfont = fm.FontProperties(fname='C:\Windows\Fonts\STXINWEI.TTF')


def create_dataset():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5], [9, 9, 3],
                      [1, 3, 4]])
    labels = ['非常热', '非常热', '一般热', '一般热', '非常热', '一般热']
    return datasets, labels


def analyze_data_plot(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    plt.title('游客冷热感知点散点图', fontsize=25, fontname='新魏', fontproperties=myfont)
    plt.xlabel('天热吃冰激淋数目', fontsize=15, fontname='新魏', fontproperties=myfont)
    plt.ylabel('天热喝水数目', fontsize=15, fontname='新魏', fontproperties=myfont)
    plt.show()


def getDistance(v, dataset):
    rowsize, columnsize = dataset.shape
    diffMat = tile(v, (rowsize, 1)) - dataset
    sqDiffMat = diffMat**2
    sqrtDiffMat = sqDiffMat.sum(axis=1)**0.5
    return sqrtDiffMat


def knn_classifier(v, dataset, labels, k):
    import operator
    dist = getDistance(v, dataset)
    sorted_index = dist.argsort(axis=0)
    # print(sorted_index)
    class_count = {}
    for i in range(k):
        label_name = labels[sorted_index[i]]
        class_count[label_name] = class_count.get(label_name, 0) + 1
    print(class_count)
    sorted_class_count = sorted(class_count.items(),
                                key=operator.itemgetter(1),
                                reverse=True)
    print(sorted_class_count)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    datasets, labels = create_dataset()
    print('数据集:\n', datasets, '\n类标签:\n', labels)
    # analyze_data_plot(datasets[:, 0], datasets[:, 1])
    print('预测结果是: ', knn_classifier([2, 4, 4], datasets, labels, 3))
