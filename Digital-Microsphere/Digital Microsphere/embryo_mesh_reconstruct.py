import open3d as o3d
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import plotly.graph_objects as go
# import open3d as o3d
# from pyntcloud import PyntCloud
thetha_divisions = 150
phi_divisions = 150
theta, phi = np.linspace(0, 2 * np.pi, thetha_divisions), np.linspace(0, np.pi, phi_divisions)
# THETA, PHI = np.meshgrid(theta, phi)
r = 1
x = 1.2 * np.outer(np.cos(theta),np.sin(phi))
y = 1.1 * np.outer(np.sin(theta), np.sin(phi))
z = 1.3 * np.outer(np.ones(np.size(theta)), np.cos(phi))
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

file = open("embryo1.ply","w")
point_file = open("embryo.xyz","w")
file.write("ply\nformat ascii 1.0\nelement vertex "+ str(thetha_divisions * phi_divisions) + "\nproperty float x\nproperty float y\nproperty float z\nend_header\n")

_3d_points = []
for i in range(len(fig['data'][0]['x'])):
  for j in range(len(fig['data'][0]['x'][0])):
    file.write(str(fig['data'][0]['x'][i][j]) +" "+ str(fig['data'][0]['y'][i][j]) +" "+ str(fig['data'][0]['z'][i][j]) + "\n")

for i in range(len(fig['data'][0]['x'])):
  for j in range(len(fig['data'][0]['x'][0])):
    point_file.write(str(fig['data'][0]['x'][i][j]) +" "+ str(fig['data'][0]['y'][i][j]) +" "+ str(fig['data'][0]['z'][i][j]) + "\n")
fig.update_layout(title='Embryo Viewport', autosize=True,
                  width=1000, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))
# fig.show()
file.close()
point_file.close()
pcd = o3d.io.read_point_cloud("embryo1.ply")


alpha = 1.5
print(f"alpha={alpha:.3f}")
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)