from geomdl.visualization import VisMPL
from matplotlib import cm
from geomdl import BSpline, utilities
import vis
import numpy as np


# create standard surfaces (Rubio and Choi)
class BasicSurfaceGenerator:
    def __init__(self, contrl_points=None, basic_surf_name=None, dim_ctrl_points=None, delta=1 / 81):
        surf = {"Rubio": [[0, 0, 0], [0, 20, 10], [0, 40, 0],
                          [40, 0, 5], [40, 20, 15], [40, 40, 5],
                          [80, 0, 20], [80, 20, 35], [80, 40, 20]],
                "Choi": [[0, 0, 38.1], [0, 25.4, 30.48], [0, 50.8, 30.48], [0, 76.2, 38.1],
                         [17.78, 0, 30.48], [17.78, 25.4, 22.86], [17.78, 50.8, 22.86], [17.78, 76.2, 30.84],
                         [35.56, 0, 38.1], [35.56, 25.4, 30.48], [35.56, 50.8, 30.48], [35.56, 76.2, 38.1],
                         [50.8, 0, 30.48], [50.8, 25.4, 22.86], [50.8, 50.8, 22.86], [50.8, 76.2, 30.48]],
                "Bosse": [[0, 0, 0], [0, 40, 0], [0, 80, 0],
                          [40, 0, 0], [40, 40, 80], [40, 80, 0],
                          [80, 0, 0], [80, 40, 0], [80, 80, 0]],
                "Creux": [[0, 0, 0], [0, 40, 0], [0, 80, 0],
                          [40, 0, 0], [40, 40, -80], [40, 80, 0],
                          [80, 0, 0], [80, 40, 0], [80, 80, 0]],
                "Tuile": [[0, 0, -40], [0, 40, -40], [0, 80, -40],
                          [40, 0, 0], [40, 40, 0], [40, 80, 0],
                          [80, 0, -40], [80, 40, -40], [80, 80, -40]],
                "Gorge": [[0, 0, 40], [0, 40, 40], [0, 80, 40],
                          [40, 0, 0], [40, 40, 0], [40, 80, 0],
                          [80, 0, 40], [80, 40, 40], [80, 80, 40]],
                "Selle": [[0, 0, 0], [0, 40, -40], [0, 80, 0],
                          [40, 0, 40], [40, 40, 0], [40, 80, 40],
                          [80, 0, 0], [80, 40, -40], [80, 80, 0]],
                "Marche": [[0, 0, 0], [0, 35, -15], [0, 30, 40], [0, 50, 40], [0, 45, 95], [0, 80, 80],
                           [40, 0, 0], [40, 35, -15], [40, 30, 40], [40, 50, 40], [40, 45, 95], [40, 80, 80],
                           [80, 0, 0], [80, 35, -15], [80, 30, 40], [80, 50, 40], [80, 45, 95], [80, 80, 80]],
                "Meplat": [[0, 0, 40], [0, 40, 40], [0, 80, 0],
                           [40, 0, 40], [40, 40, 0], [40, 80, -40],
                           [80, 0, 0], [80, 40, -40], [80, 80, -40]],
                "Plat": [[0, 0, 40], [0, 40, 0], [0, 80, 0],
                         [40, 0, 0], [40, 40, 0], [40, 80, 0],
                         [80, 0, 0], [80, 40, 0], [80, 80, 0]]
                }
        if contrl_points is None:
            self.ctrl_points = surf[basic_surf_name]
        if dim_ctrl_points is None:
            dim_ctrl_points = [3, 3]
        if basic_surf_name == "Marche":
            dim_ctrl_points = [3, 6]
        if basic_surf_name is None:
            self.ctrl_points = contrl_points
        self.dim_ctrl_points = dim_ctrl_points
        self.surf = BSpline.Surface()
        self.surf.degree_u = dim_ctrl_points[0] - 1
        self.surf.degree_v = dim_ctrl_points[1] - 1
        print(self.ctrl_points, dim_ctrl_points)
        self.surf.set_ctrlpts(self.ctrl_points, dim_ctrl_points[0], dim_ctrl_points[1])
        self.surf.knotvector_u = utilities.generate_knot_vector(self.surf.degree_u, self.surf.ctrlpts_size_u)
        self.surf.knotvector_v = utilities.generate_knot_vector(self.surf.degree_v, self.surf.ctrlpts_size_v)
        self.surf.delta = delta
        self.surf.evaluate()

    def surf_visu(self, resolution=1 / 10):
        self.surf.delta = resolution
        self.surf.evaluate()
        self.surf.vis = VisMPL.VisSurface()
        self.surf.render(colormap=cm.cool)
        return 0

    def get_nodes(self):
        return self.surf.evalpts


# sg = BasicSurfaceGenerator(basic_surf_name="Bosse", delta=1/10)
# DATA=np.array(sg.get_nodes())
# print(DATA)
# vis.viz_evalpts_3d(DATA)
# sg.surf_visu()