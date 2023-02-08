import numpy as np

def read_mesh(points_filename, faces_filename, cells_filename, boundary_filename):

    # call read_file function for each mesh characteristic and return arrays
    points = np.asarray(read_file(points_filename))
    faces = np.asarray(read_file(faces_filename), dtype=int)
    cells = np.asarray(read_file(cells_filename), dtype=int)
    boundary = np.asarray(read_file(boundary_filename), dtype=object)

    return points, faces, cells, boundary

def read_file(filename):

    array = []

    # read each file for the mesh, appropriately format and return array of mesh characteristic
    with open("MeshFiles/" + filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            ls = line.strip('()').replace(" ", "").split(",")
            if filename != "boundary_test.txt":
                ls = [float(i) for i in ls]
            
            array.append(ls)

    return array