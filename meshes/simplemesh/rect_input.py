"""
Generate input files from a Gmsh mesh file for a ring with inner pressure
 with symmetry with respect to the horizontal and vertical axws.

It imposes roller constraints for the left side (x==0), and bottom (y==0).
The loading is 1 in the radial direction.
"""
from __future__ import division
import meshio
import numpy as np 
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'C:\\Users\\Yuan\\AppData\\Local\\Temp\\tmpf84y2pii.mesh')#tmpnygiwi5t.mesh
mesh =meshio.read(my_file)


# Elements data
elements = mesh.cells["triangle"]
els_array = np.zeros([elements.shape[0], 6], dtype=int)
els_array[:, 0] = range(elements.shape[0])
els_array[:, 1] = 3
els_array[:, 3::] = elements
# Nodes data
nodes_array = np.zeros([mesh.points.shape[0], 5])
nodes_array[:, 0] = range(mesh.points.shape[0])
nodes_array[:, 1:3] = mesh.points[:, :2]
nodes_array[nodes_array[:, 1]==0, 3] = -1
nodes_array[nodes_array[:, 2]==0, 4] = -1
# Loads data
radius = np.sqrt(mesh.points[:, 0]**2 + mesh.points[:, 1]**2)
nloads = mesh.points[np.abs(radius - 1.5) <= 1e-6, 0].shape[0]
loads_array = np.zeros((nloads, 3))
loads_array[:, 0] = nodes_array[np.abs(radius - 1.5) <= 1e-6, 0]
loads_array[:, 1] = 2.0*(mesh.points[np.abs(radius - 1.5) <= 1e-6, 0]/radius[np.abs(radius - 1.5) <= 1e-6])
loads_array[:, 2] = 2.0*(mesh.points[np.abs(radius - 1.5) <= 1e-6, 1]/radius[np.abs(radius - 1.5) <= 1e-6])
## Material data
mater_array = np.array([[1e3, 1/3]])

ele_file = os.path.join(THIS_FOLDER, 'eles.txt')
nodes_file = os.path.join(THIS_FOLDER, 'nodes.txt')
loads_file = os.path.join(THIS_FOLDER, 'loads.txt')
mater_file = os.path.join(THIS_FOLDER, 'mater.txt')
np.savetxt(ele_file, els_array, fmt="%d")
np.savetxt(nodes_file, nodes_array, fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
np.savetxt(loads_file, loads_array, fmt=("%d", "%.6f", "%.6f"))
np.savetxt(mater_file, mater_array, fmt="%.6f")