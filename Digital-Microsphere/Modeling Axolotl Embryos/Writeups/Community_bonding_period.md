# Writeup for community bonding period

## Project Introduction

The key objective of my project is to generate a 3d model based on a set of 2d images of an axolotl embryo at a particular stage. We can approach this by dividing our problem into 3 sub problems :-
* Extracting embryo images from given 2D images
* Generating a 3D model based on given 2D images
* Projecting embryo images on the generated 3D model

### Extracting embryo images
Extracting embryo images accurately is very critical in generating a model as we’ll be deriving all the necessary spatial information from the features present in the extracted embryo image.

### Generating a 3D model
The 3D model that we are going to generate would resemble an irregular ellipsoid. To generate an accurate approximation of the 3D model we have to solve 3 sub problems : -

* Getting accurate outlines/contours
* Finding the approximate axis of rotation
* Finding the angle of rotation for each contour by measuring the displacement of corresponding points wrt the axis
* Generating a 3D mesh based on the point cloud

### Projecting embryo images
There are various projection methods that outline how to go about projecting an image to a 3D model in the Open3D, Scikit and PyOpenGL libraries. Image projection requires transforming the perspective image to a projection texture that can be applied to the model.
Out of the existing projection methods cylindrical projection methods would suit this model the best as we are dealing with an irregular ellipsoid. We can generate an approximate equirectangular image and then apply it to our generated model

## Community Period Insights

The community period was really insightful in the process of developing OSS, ranging from licensing issues to community sop and roles that exist for aspiring developers. It was interesting to see all the work that is being done in the community.


