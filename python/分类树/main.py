from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler

x, y = make_classification(n_samples=100
                           , n_features=2
                           , n_redundant=0
                           , n_informative=2
                           , random_state=1
                           , n_clusters_per_class=1
                           )
rng = np.random.RandomState(2)
x += 2 * rng.uniform(size=x.shape)
linearly_separable = (x, y)
datasets = [make_moons(noise=0.3, random_state=0),
            make_circles(noise=0.2, factor=0.5, random_state=1),
            linearly_separable]

figure = plt.figure(figsize=(6, 9))
i = 1
for ds_index, ds in enumerate(datasets):
    x, y = ds
    x = StandardScaler().fit_transform(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.4,
                                                        random_state=42)
    x1_min, x1_max = x[:, 0].min() - .5, x[:, 0].max() + .5
    x2_min, x2_max = x[:, 1].min() - .5, x[:, 1].max() + .5

    array1, array2 = np.meshgrid(np.arange(x1_min, x1_max, 0.2),
                                 np.arange(x2_min, x2_max, 0.2))

    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    ax = plt.subplot(len(datasets), 2, i)
    if ds_index == 0:
        ax.set_title("Input data")

    ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train,
               cmap=cm_bright, edgecolors='k')
    ax.scatter(x_test[:, 0], x_test[:, 1], c=y_test,
               cmap=cm_bright, alpha=0.6, edgecolors='k')

    ax.set_xlim(array1.min(), array1.max())
    ax.set_ylim(array2.min(), array2.max())
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1

    ax = plt.subplot(len(datasets), 2, i)

    clf = DecisionTreeClassifier(max_depth=5)
    clf.fit(x_train, y_train)
    score = clf.score(x_test, y_test)

    z = clf.predict_proba(np.c_[array1.ravel(), array2.ravel()])[:, 1]

    z = z.reshape(array1.shape)

    ax.contourf(array1, array2, z, cmap=cm, alpha=.8)
    ax.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap=cm_bright,
               edgecolors='k')

    ax.scatter(x_test[:, 0], x_test[:, 1], c=y_test, cmap=cm_bright,
               edgecolors='k', alpha=0.6)

    ax.set_xlim(array1.min(), array1.max())
    ax.set_ylim(array1.min(), array1.max())
    ax.set_xticks(())
    ax.set_yticks(())

    if ds_index == 0:
        ax.set_title("Decision Tree")

    ax.text(array1.max() - .3, array2.min() + .3, ('{:.1f}%'.format(score * 100)),
            size=15, horizontalalignment='right')

    i += 1

plt.tight_layout()
plt.show()
