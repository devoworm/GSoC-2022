from cmath import sqrt
import math
from sys import argv
from PIL import Image
import open3d as o3d
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv
from pyvista import examples
# import mpl_toolkits.mplot3d.axes3d as axes3d
import plotly.graph_objects as go
# # import open3d as o3d
# # from pyntcloud import PyntCloud
def run(thetha_divisions,phi_divisions,Rx,Ry,Rz):
    # thetha_divisions = 50
    # phi_divisions = 50
    theta, phi = np.linspace(0, 2 * np.pi, thetha_divisions), np.linspace(0, np.pi, phi_divisions)
    # THETA, PHI = np.meshgrid(theta, phi)
    # Rx = 1
    # Ry=0.9
    # Rz=0.87
    x = Rx * np.outer(np.cos(theta),np.sin(phi))
    y = Ry * np.outer(np.sin(theta), np.sin(phi))
    z = Rz * np.outer(np.ones(np.size(theta)), np.cos(phi))
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])


    _3d_points = []
    for i in range(len(fig['data'][0]['x'])):
        for j in range(len(fig['data'][0]['x'][0])):
            _3d_points.append([fig['data'][0]['x'][i][j],fig['data'][0]['y'][i][j],fig['data'][0]['z'][i][j]])
        

    cloud = pv.PolyData(_3d_points)
    # cloud.plot(show_edges=True)
    volume = cloud.delaunay_3d(alpha=2)
    shell = volume.extract_geometry()
    shell.active_t_coords = np.zeros((shell.points.shape[0],2))

    R = sqrt(shell.points[i, 0]*shell.points[i,0] + shell.points[i,1]*shell.points[i,1] + shell.points[i,2]*shell.points[i,2]).real
    for i in range(shell.points.shape[0]):
        shell.active_t_coords[i] = [
        0.5 + ((sqrt(shell.points[i, 0]**2 + shell.points[i,1]**2).real)/R)*(np.cos(np.arctan(shell.points[i, 1]/shell.points[i, 0]))),
        0.5 + ((sqrt(shell.points[i, 0]**2 + shell.points[i,1]**2).real)/R)*(np.sin(np.arctan(shell.points[i, 1]/shell.points[i, 0]))),
        ]

    text = pv.read_texture("./resources/emb_alpha.png")
    text.InterpolateOn()
    text.MipmapOn()
    print(shell.volume)
  
    p = pv.Plotter()
    p.add_mesh(shell, texture=text)
    p.export_obj("./resources/embryo_final.obj")
    p.close()


run(argv[1],argv[2],argv[3],argv[4],argv[5])