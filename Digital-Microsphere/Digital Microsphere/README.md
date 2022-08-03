# Digital Microsphere
### 1. Project Summary:
In some organisms like axolotl, the surface of the embryo is transparent and thus allowing us to see the embryogenetic events taking place before the neural tube closure. Therefore, acquiring images of the outside of early stage developing embryos could give us many insights. Hence, aim of this project is to build a computational tool that allows us to visualize 4D data derived from the surface of an Axolotl embryo using a special microscope called Digital Microsphere. That is, a computational tool which will display a sphere on which the images of the embryo from different angles will be mapped creating a 3D model.
### 2. Stages of the Project:
  - #### Stage #1: Image Cropping and Processing
    In this stage, the main focus is to crop the images to get the required portion and do some image processing on it. The python file retreives the outline of the embryo and then uses it to find out the radius of the embryo in the x,y and z directions respecitvely.
  - #### Stage #2: Generating the Point Cloud and the 3D mesh
    The python script take the three values of the radius of the embryo and using them it calculates all the 3d coordinates and then store it in a **_.ply_** file to get the point cloud.
    Then, it takes the **_ebryo.ply_** file and creates it's mesh using the **_open3d_** librabry of python.

    ![image](https://user-images.githubusercontent.com/91690484/182136823-4bd264e7-66b7-4176-976a-531f63d6c2da.png)
  
  - #### Stage #3: Projecting the embryo images onto the generated mesh
    This are the expected outputs that I showed in the proposal but I am still working on this part to improve it.
    ![image](https://user-images.githubusercontent.com/91690484/182139982-bdb7d14b-00ed-4298-b5a3-079a6b28eabc.png)
    
    ![image](https://user-images.githubusercontent.com/91690484/182140178-2cbc32f7-ba69-40f7-af67-e6dc4c6f8cae.png)
    
