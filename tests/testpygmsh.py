import pygmsh
import numpy as np

import pygimli as pg
from pygimli.meshtools import readGmsh
from urllib.request import urlretrieve

import matplotlib.pyplot as plt


print(pg.__version__)
geom = pygmsh.opencascade.Geometry(
  characteristic_length_min=0.1,
  characteristic_length_max=0.1,
  )


rectangle = geom.add_rectangle([-1.0, -1.0, 0.0], 2.0, 2.0)
#disk1 = geom.add_disk([-1.2, 0.0, 0.0], 0.5)
#disk2 = geom.add_disk([+1.2, 0.0, 0.0], 0.5)
#union = geom.boolean_union([rectangle, disk1, disk2])

#disk3 = geom.add_disk([0.0, -0.9, 0.0], 0.5)
#disk4 = geom.add_disk([0.0, +0.9, 0.0], 0.5)
#flat = geom.boolean_difference([union], [disk3, disk4])
#geom.extrude(flat, [0, 0, 0.3])

#gmsh_path = "C:\\Users\\Yuan\\gmsh-4.1.2-Windows64\\gmsh-4.1.2-Windows64\\gmash.exe"
points, cells, point_data, cell_data, field_data = pygmsh.generate_mesh(geom)
#print(points)

fig, ax = plt.subplots()
#mesh = readGmsh("C:\\Users\\Yuan\\AppData\\Local\\Temp\\tmpsw2rtctb.msh", verbose=True)
#pg.show(mesh, ax=ax, markers=True, hold=True)

#np.savetxt("nodes.gmsh", point_data, fmt='%5.2f', delimiter=' ')
#np.savetxt("ele.gmsh", cell_data, fmt='%d', delimiter=' ')