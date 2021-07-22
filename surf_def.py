import numpy as np
from surf_gen import BasicSurfaceGenerator


def plat_1(norm_vect, coord_E):
    nx, ny, nz = norm_vect
    ex, ey, ez = coord_E
    xys = np.random.uniform(-100, 100, (8, 2))
    zs = np.zeros(8)
    for i in range(8):
        x, y = xys[i]
        zs[i] = ez - (nx * (x - ex) + ny * (y - ey)) / nz
    ctrl_pts = np.zeros((9, 3))
    ctrl_pts[:8, :2] = xys
    ctrl_pts[:8, 2] = zs
    ctrl_pts[8] = coord_E
    ctrl_pts = ctrl_pts.tolist()
    ctrl_pts = sorted(ctrl_pts, key=lambda l: l[0])
    ctrl_pts[:3] = sorted(ctrl_pts[:3], key=lambda l: l[1])
    ctrl_pts[3:6] = sorted(ctrl_pts[3:6], key=lambda l: l[1])
    ctrl_pts[6:] = sorted(ctrl_pts[6:], key=lambda l: l[1])
    return ctrl_pts


def plat_2(norm_vect, coord_E):
    """

    :param norm_vect: format list
    :param coord_E: format list
    :return: control points with format list
    """
    nx, ny, nz = norm_vect
    ex, ey, ez = coord_E
    bd = np.random.uniform(-100, 100, (2, 2))
    [bx, by], [dx, dy] = bd
    bdz = np.zeros(2)
    for i in range(2):
        x, y = bd[i]
        bdz[i] = ez - (nx * (x - ex) + ny * (y - ey)) / nz
    bz, dz = bdz
    while True:
        hx = np.random.uniform(-100, 100)
        hy = (by - ey) * (hx - ex) / (bx - ex) + ey
        hz = (bz - ez) * (hx - ex) / (bx - ex) + ez
        b = np.array([bx, by, bz])
        h = np.array([hx, hy, hz])
        if np.dot(b - coord_E, h - coord_E) < 0:
            break
    while True:
        fx = np.random.uniform(-100, 100)
        fy = (dy - ey) * (fx - ex) / (dx - ex) + ey
        fz = (dz - ez) * (fx - ex) / (dx - ex) + ez
        d = np.array([dx, dy, dz])
        f = np.array([fx, fy, fz])
        if np.dot(d - coord_E, f - coord_E) < 0:
            break
    a = (b + d) / 2
    c = (b + f) / 2
    g = (d + h) / 2
    i = (h + f) / 2
    list = np.array([b, a, d, c, coord_E, g, f, i, h]).tolist()
    return list


def bosse(norm_vect, coord_E, scaling=50):
    """

    :param norm_vect: nz > 0
    :param coord_E:
    :param scaling:
    :return:
    """
    assert norm_vect[-1] > 0, "The z coordinate of normal vector should be strictly positive"
    ctrlpts = np.array(plat_2(norm_vect, coord_E))
    ctrlpts[4] = np.array(coord_E) + scaling * np.array(norm_vect)
    return ctrlpts.tolist()

def creux(norm_vect, coord_E, scaling=50):
    """

    :param norm_vect:
    :param coord_E:
    :param scaling:
    :return:
    """
    assert norm_vect[-1] < 0, "The z coordinate of normal vector should be strictly negative"
    ctrlpts = np.array(plat_2(norm_vect, coord_E))
    ctrlpts[4] = np.array(coord_E) + scaling * np.array(norm_vect)
    return ctrlpts.tolist()


def tuile(coord_B, axis_prolg, axis_desc1, axis_desc2):
    """

    :param coord_B: format list
    :param axis_prolg: format list
    :param axis_desc1: format list
    :param axis_desc2: format list
    :return:
    """
    assert axis_desc1[-1] < 0 and axis_desc2[-1] < 0
    bD, eD, hD = np.random.uniform(0, 5, 3)
    r1 = 5
    r2 = 10
    # r1, r2 = np.random.uniform(0, 5, 2)
    if r1 >= r2:
        r = r2
        r2 = r1
        r1 = r
    coord_B = np.array(coord_B)
    axis_prolg = np.array(axis_prolg)
    axis_desc1 = np.array(axis_desc1)
    axis_desc2 = np.array(axis_desc2)
    a = coord_B + axis_desc1 * bD
    c = coord_B + axis_desc2 * bD
    e = coord_B + r1 * axis_prolg
    f = e + axis_desc2 * eD
    d = e + axis_desc1 * eD
    h = coord_B + r2 * axis_prolg
    i = h + axis_desc2 * hD
    g = h + axis_desc1 * hD
    return np.array([a, coord_B, c, d, e, f, g, h, i]).tolist()




#
nv = [1, 2, 3]
cE = [5, 4, 8]
# ctrl_pts = [[0, 0, 0], [20, 0, 20], [40, 0, 0], [0, 20, 40], [20, 20, 20], [40, 20, 40], [0, 40, 0], [20, 40, 20], [40, 40, 0]]
# ctrl_pts = plat_2(nv, cE)
# ctrl_pts = bosse(nv, cE, scaling=50)
coord_B = [2, 5, 9]
axis_prolg = [5, 2, 1]
axis_desc1 = [-1, 0, -1]
axis_desc2 = [1, 0, -3]
ctrl_pts=tuile(coord_B, axis_prolg, axis_desc1, axis_desc2)
sg = BasicSurfaceGenerator(contrl_points=ctrl_pts)

# sg = BasicSurfaceGenerator(basic_surf_name="Selle")
sg.surf_visu()
