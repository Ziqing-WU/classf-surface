import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from scipy import array, newaxis


def viz_evalpts_3d(evalpts):
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

def viz_evalpts_2d(evalpts):
    return 0;
