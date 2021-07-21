import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from scipy import array, newaxis
import numpy as np
import math


def viz_evalpts_3d(evalpts):
    """
    3D visualisation of evaluated points
    :param evalpts: evaluated points from the class BasicSurfaceGenerator
    :return: 0
    """
    evalpts = array(evalpts)
    Xs = evalpts[:, 0]
    Ys = evalpts[:, 1]
    Zs = evalpts[:, 2]

    # ======
    ## plot:

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.cool, linewidth=0)
    fig.colorbar(surf)

    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(6))
    ax.zaxis.set_major_locator(MaxNLocator(5))

    fig.tight_layout()

    plt.show()  # or:
    # fig.savefig('3D.png')


def viz_evalpts_2d_heatmap(X, Y, Z, show=True, save=False, filename=None):
    """
    2D visualisation of evaluated points with color indicating the coordinates of Z
    :param X: Meshgrid of X, obtained from get_nodes_grid
    :param Y: Meshgrid of Y, obtained from get_nodes_grid
    :param Z: Values of Z, rearranged on a XY grid
    :return: 0
    """

    fig, ax = plt.subplots(figsize=(10, 10))
    ps = ax.pcolormesh(X, Y, Z, cmap="YlOrBr", edgecolors='face', norm=None, vmin=-20, vmax=20)
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    plt.axis('off')

    # plt.colorbar(ps)
    if show:
        plt.show()
    if save:
        plt.savefig(filename)
    return 0


def viz_evalpts_2d_rgb(evalpts, figname=None):
    evalpts = np.array(evalpts)
    l = int(math.sqrt(len(evalpts)))
    R = evalpts[:, 0]
    G = evalpts[:, 1]
    B = evalpts[:, 2]

    def normalize(a):
        range = a.max() - a.min()
        return (1/range)*a - a.min()/range
    # normalization
    evalpts[:, 0] = normalize(R)
    evalpts[:, 1] = normalize(G)
    evalpts[:, 2] = normalize(B)

    fig, ax = plt.subplots(figsize=(10, 10))
    print(evalpts)
    plt.imshow(evalpts.reshape((l,l,3)))
    ax.set_title(figname)
    plt.show()

    return 0
