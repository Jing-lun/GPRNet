import open3d as o3d
import numpy as np
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import random
import math
pi = math.pi
from matplotlib import pyplot as plt
import scipy.io as io

axis_pcd = o3d.create_mesh_coordinate_frame(size=0.1, origin=[0, 0, 0])

rho = 0.015 * np.sqrt(np.random.uniform(0, 1, 1000))
phi = np.random.uniform(0, 2*np.pi, 1000)

x1 = 0.175 + rho * np.cos(phi)
# x2 = 0.13 + rho * np.cos(phi)
# x3 = 0.22 + rho * np.cos(phi)
# x4 = 0.32 + rho * np.cos(phi)

y1 = 0.21 + rho * np.sin(phi)
y2 = 0.17 + rho * np.sin(phi)
y3 = 0.13 + rho * np.sin(phi)
y4 = 0.10 + rho * np.sin(phi)
y5 = 0.11 + rho * np.sin(phi)
# plt.scatter(x, y)
# plt.axis('equal')
# plt.show()
points = []

''' draw the straight lines'''
for z in range(0,250,2):
    z = z/1000
    for i in range(len(y1)):
        points.append([x1[i],y1[i],z])

''' draw the inclined lines -- type 1 '''
for i in range(50,177,2):
    z = -1 * i + 175
    for j in range(len(y1)):
        points.append([i/1000 + rho[j] * np.cos(phi[j]), y4[j], z/1000])

for i in range(50,302,2):
    z = -1 * i + 300
    for j in range(len(y1)):
        points.append([i/1000 + rho[j] * np.cos(phi[j]), y3[j], z/1000])

for i in range(175,302,2):
    z = -1 * i + 425
    for j in range(len(y1)):
        points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

''' draw the inclined lines -- type 2 '''
# for i in range(50,177,2):
#     z = 1 * i + 75
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y4[j], z/1000])
#
# for i in range(50,302,2):
#     z = 1 * i - 50
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y3[j], z/1000])
#
# for i in range(175,302,2):
#     z = 1 * i - 175
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

''' draw the inclined lines -- type 3 '''
# for i in range(50,302,2):
#     z = -1/2 * i + 150
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y5[j], z/1000])
#
# for i in range(50,302,2):
#     z = 1/2 * i + 100
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

''' draw the inclined lines -- type 4 '''
# for i in range(50,302,2):
#     z = 1/2 * i - 25
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y3[j], z/1000])
#
# for i in range(50,302,2):
#     z = -1/2 * i + 275
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

points = np.asarray(points, dtype=np.float32)
print(points)
pcd=o3d.geometry.PointCloud()
pcd.points=o3d.utility.Vector3dVector(points)
pcd.paint_uniform_color([0.1, 0.3, 0.5])
vis = o3d.Visualizer()
vis.add_geometry(axis_pcd)
o3d.visualization.draw_geometries([pcd] + [axis_pcd])

#Saving data to mat file
# mat_path='/home/jinglun/Code/gprMax/model_output/new_model/29.mat'
# io.savemat(mat_path, {'scandata': points})
