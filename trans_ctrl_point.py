import math

import numpy as np
from surf_gen import BasicSurfaceGenerator
from math import cos, sin
import vis


def translation(org_ctrl_points, trans_vector):
    """
    Apply a translation
    :param org_ctrl_points: original control points
    :param trans_vector: translation vector to be applied
    :return: new control points
    """
    org_ctrl_points = np.array(org_ctrl_points)
    return (org_ctrl_points + trans_vector).tolist()


def rotation_cardan(org_ctrl_points, angles):
    """
    Apply a rotation with Cardan representation (ref https://fr.wikipedia.org/wiki/Matrice_de_rotation#Matrices_de_rotation_dans_le_cas_g%C3%A9n%C3%A9ral)
    :param: org_ctrl_points : original control points
    :param: angles : [alpha, beta, gamma] lacet entre 0 et 2*pi, tangage, roulis
    :return: new control points
    """
    alpha, beta, gamma = angles
    assert 0 <= alpha < 2 * math.pi, "Alpha should be between 0 and 2Pi"
    assert -math.pi / 2 < beta <= 0, "Beta should be between -pi/2 and 0"
    assert -math.pi / 2 < gamma <= 0, "Gamma should be between -pi/2 and 0"
    rot_X = np.array([[1, 0, 0],
                      [0, cos(gamma), -sin(gamma)],
                      [0, sin(gamma), cos(gamma)]])
    rot_Y = np.array([[cos(beta), 0, sin(beta)],
                      [0, 1, 0],
                      [-sin(beta), 0, cos(beta)]])
    rot_Z = np.array([[cos(alpha), -sin(alpha), 0],
                      [sin(alpha), cos(alpha), 0],
                      [0, 0, 1]])
    rot = rot_Z @ rot_Y @ rot_X
    org_ctrl_points = np.array(org_ctrl_points)
    return (org_ctrl_points @ rot).tolist()


def noise_injection(org_ctrl_points, snr=10):
    """
    Add a white noise to the control points
    :param org_ctrl_points: original control points
    :param snr: signal to noise ration defining variance of white noise
    :return: new control points
    """
    org_ctrl_points = np.array(org_ctrl_points)
    mean = np.mean(org_ctrl_points)
    std_noise = np.sqrt(mean / snr)
    noise = np.random.normal(0, std_noise, size=org_ctrl_points.shape)
    return (org_ctrl_points + noise).tolist()


def scaling(org_ctrl_points, scale):
    """
    Apply scaling to the control points
    :param org_ctrl_points: original control points
    :param scale: scaling on x, y, z axis, where scale on z need to be positive and neither of three should be 0
    :return: new control points
    """
    org_ctrl_points = np.array(org_ctrl_points)
    assert scale[-1] > 0, "Scaling on z-axis needs to be positive"
    assert scale[0] != 0, "Scaling on x-axis cannot be zero"
    assert scale[1] != 0, "Scaling on y-axis cannot be zero"
    return np.multiply(org_ctrl_points, scale).tolist()


