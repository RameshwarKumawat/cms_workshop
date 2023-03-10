import numpy
import os
file_location = os.path.join('ram', 'phth.xyz')
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2,  dtype='unicode')
symbols = xyz_file[:,0]
coordinates = (xyz_file[:,1:])
coordinates = coordinates.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
             x_distance = coordinates[num1,0] - coordinates[num2,0]
             y_distance = coordinates[num1,1] - coordinates[num2,1]
             z_distance = coordinates[num1,2] - coordinates[num2,2]
             bond_length_12 = numpy.sqrt(x_distance**2+y_distance**2+z_distance**2)
             print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')  
