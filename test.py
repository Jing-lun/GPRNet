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

x1 = 0.04 + rho * np.cos(phi)
x2 = 0.13 + rho * np.cos(phi)
x3 = 0.22 + rho * np.cos(phi)
x4 = 0.32 + rho * np.cos(phi)

y1 = 0.11 + rho * np.sin(phi)
y2 = 0.16 + rho * np.sin(phi)
y3 = 0.20 + rho * np.sin(phi)
y4 = 0.21 + rho * np.sin(phi)
y5 = 0.22 + rho * np.sin(phi)
# plt.scatter(x, y)
# plt.axis('equal')
# plt.show()
points = []

''' draw the straight lines'''
# for z in range(0,250,2):
#     z = z/1000
#     for i in range(len(y1)):
#         # points.append([x1[i],y1[i],z])
#         points.append([x2[i],y2[i],z])
#         points.append([x3[i],y1[i],z])
#         # points.append([x4[i],y1[i],z])
#         # points.append([x2[i],y1[i],z])

''' draw the inclined lines -- type 1 '''
for i in range(40,320,2):
    z = 25/28 * i - 250/7
    for j in range(len(y1)):
        points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

for i in range(40,320,2):
    z = -25/28 * i + 2000/7
    for j in range(len(y1)):
        points.append([i/1000 + rho[j] * np.cos(phi[j]), y1[j], z/1000])

''' draw the inclined lines -- type 2 '''
# for i in range(40,182,2):
#     z = 25/14 * i - 500/7
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])
#
# for i in range(180,322,2):
#     z = -25/14 * i + 4000/7
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y1[j], z/1000])

''' draw the inclined lines -- type 3 '''
# for i in range(40,182,2):
#     z = -25/14 * i + 2250/7
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y1[j], z/1000])
#
# for i in range(180,322,2):
#     z = 25/14 * i - 2250/7
#     for j in range(len(y1)):
#         points.append([i/1000 + rho[j] * np.cos(phi[j]), y2[j], z/1000])

points = np.asarray(points, dtype=np.float32)
pcd=o3d.geometry.PointCloud()
pcd.points=o3d.utility.Vector3dVector(points)
pcd.paint_uniform_color([0.1, 0.3, 0.5])
vis = o3d.Visualizer()
vis.add_geometry(axis_pcd)
o3d.visualization.draw_geometries([pcd] + [axis_pcd])

#Saving data to mat file
mat_path='/home/jinglun/Code/gprMax/model_output/model_gt/51.mat'
io.savemat(mat_path, {'scandata': points})
# # 绘制open3d坐标系
# axis_pcd = o3d.create_mesh_coordinate_frame(size=0.5, origin=[0, 0, 0])
# # 在3D坐标上绘制点：坐标点[x,y,z]对应R，G，B颜色
# points = np.array([[0.1, 0.1, 0.1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
# colors = [[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
#
# test_pcd = o3d.geometry.PointCloud()  # 定义点云
#
# # 方法1（非阻塞显示）
# vis = o3d.Visualizer()
# vis.create_window(window_name="Open3D1")
# vis.get_render_option().point_size = 3
# first_loop = True
# # 先把点云对象添加给Visualizer
# vis.add_geometry(axis_pcd)
# vis.add_geometry(test_pcd)
# # while True:
# #     # 给点云添加显示的数据
# #     # points -= 0.001
# #     test_pcd.points = o3d.utility.Vector3dVector(points)  # 定义点云坐标位置
# #     test_pcd.colors = o3d.utility.Vector3dVector(colors)  # 定义点云的颜色
# #     # update_renderer显示当前的数据
# #     vis.update_geometry()
# #     vis.poll_events()
# #     vis.update_renderer()
# #     cv2.waitKey(100)
#
# # 方法2（阻塞显示）：调用draw_geometries直接把需要显示点云数据
# test_pcd.points = o3d.utility.Vector3dVector(points)  # 定义点云坐标位置
# test_pcd.colors = o3d.utility.Vector3dVector(colors)  # 定义点云的颜色
# o3d.visualization.draw_geometries([test_pcd] + [axis_pcd], window_name="Open3D2")
