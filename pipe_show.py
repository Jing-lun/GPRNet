import numpy as np
import open3d as o3d
import os
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

def getFile(path):
    ''' get all the suffix files in one directory '''

    f_list = os.listdir(path)
    ret_list = []
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[-1] == '.png':
            ret_list.append(i)
    return ret_list

if __name__ == "__main__":
    pcd = o3d.geometry.PointCloud()
    file_path = "/home/jinglun/Data/gprMax/gt/"
    os.chdir(file_path)
    ret_list = getFile(file_path)
    single_slice_point_cloud = []

    for img_name in ret_list:
        img = cv2.imread(img_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        prefix = os.path.splitext(img_name)[0]
        if int(prefix) < 20:
            height, width = img.shape[:2]
            for m in range(height):
                for n in range(width):
                    if img[m,n] == 255:
                        Y = n * 0.001
                        Z = m * 0.001
                        X = (int(prefix)-9) * 0.025
                        single_point_XYZ = [X, Y, Z]
                        single_slice_point_cloud.append(single_point_XYZ)
        else:
            height, width = img.shape[:2]
            for m in range(height):
                for n in range(width):
                    if img[m,n] == 255:
                        Y = (int(prefix)-21) * 0.025 + 0.05;
                        Z = m * 0.001
                        X = n * 0.001;
                        single_point_XYZ = [X, Y, Z]
                        # print(single_point_XYZ)
                        single_slice_point_cloud.append(single_point_XYZ)

    single_slice_point_cloud = np.asarray(single_slice_point_cloud, dtype=np.float32)

    ''' below are two ways to color the points '''
    # first way
    pcd.colors = o3d.utility.Vector3dVector(np.tile(np.asarray([0.1, 0.3, 0.5]),((single_slice_point_cloud.shape)[0], 1)))
    # second way
    pcd.paint_uniform_color([0.5, 0.5, 0.5])

    pcd.points = o3d.utility.Vector3dVector(single_slice_point_cloud)
    o3d.visualization.draw_geometries([pcd])
