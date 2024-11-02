import numpy as np

from CalculateDistance import CalcOfDistancesCartesian2D, CalcOfDistancesCartesian3D, \
    CalcOfDistancesPolar2D, CalcOfDistancesSphericalThroughTheSphereVolume, \
    CalcOfDistancesSphericalOnTheSphereSurface

from ConvertationSystem import matrix2D, matrix2_2D, matrix3D, matrix2_3D, print_2d_array, print_3d_array\
    , PolarToCartesian, CartesianToPolar, SphericalToCartesian, CartesianToSpherical

from Generator import GeneratorCartesian2D, GeneratorCartesian3D, GeneratorPolar\
    , GeneratorSphericalThroughTheSphereVolume, GeneratorSphericalOnTheSphereSurface


print('\n______________________________________________________________________________________')
print('\nCoordinates in the polar coordinate system:')
print_2d_array(matrix2D)

print('\nCoordinates in the Cartesian coordinate system:')
PolarToCartesian(matrix2D[0][0], matrix2D[0][1], 0)
PolarToCartesian(matrix2D[1][0], matrix2D[1][1], 1)

print('\nCoordinates after inverse transformation in the polar coordinate system:')
CartesianToPolar(matrix2_2D[0][0], matrix2_2D[0][1], 0)
CartesianToPolar(matrix2_2D[1][0], matrix2_2D[1][1], 1)

print('\n______________________________________________________________________________________')
print('\nCoordinates in the spherical coordinate system:')
print_3d_array(matrix3D)

print('\nCoordinates in the Cartesian coordinate system:')
SphericalToCartesian(matrix3D[0][0], (matrix3D[0][1]), (matrix3D[0][2]), 0)
SphericalToCartesian(matrix3D[1][0], (matrix3D[1][1]), (matrix3D[1][2]), 1)

print('\nCoordinates after the inverse transformation in the spherical coordinate system:')
CartesianToSpherical(matrix2_3D[0][0], (matrix2_3D[0][1]), (matrix2_3D[0][2]), 0)
CartesianToSpherical(matrix2_3D[1][0], (matrix2_3D[1][1]), (matrix2_3D[1][2]), 1)

print('\n______________________________________________________________________________________')
print('\nCalculating the distance between points in two-dimensional space in the Cartesian coordinate system:')

x1, y1, x2, y2 = GeneratorCartesian2D()

CalcOfDistancesCartesian2D(x1, x2, y1, y2)

print('\nCalculating the distance between points in three-dimensional space in the Cartesian coordinate system:')

x1, y1, z1, x2, y2, z2 = GeneratorCartesian3D()

CalcOfDistancesCartesian3D(x1, x2, y1, y2, z1, z2)

print('\n______________________________________________________________________________________')
print('\nCalculating the distance between points in two-dimensional space in the polar coordinate system:')

r1, theta1, r2, theta2 = GeneratorPolar()

CalcOfDistancesPolar2D(r1, theta1, r2, theta2)

print('\n______________________________________________________________________________________')
print("\nCalculating the distance between points in a spherical coordinate system using the volume of a sphere:")

r1, theta1, phi1, r2, theta2, phi2 = GeneratorSphericalThroughTheSphereVolume()

CalcOfDistancesSphericalThroughTheSphereVolume(r1, theta1, phi1, r2, theta2, phi2)

print('\n______________________________________________________________________________________')
print("\nCalculate the distance between points in a spherical coordinate system on the surface of a sphere:")

r, theta1, phi1, theta2, phi2 = GeneratorSphericalOnTheSphereSurface()

CalcOfDistancesSphericalOnTheSphereSurface(r, theta1, phi1, theta2, phi2)
print('\n______________________________________________________________________________________')
