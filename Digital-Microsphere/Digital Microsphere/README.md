# Digital Microsphere

### Contents:
- [Project Summary](#summary)
- [Stages of the project](#stages)
  - [Image Cropping and Processing](#image)
  - [Generating the point cloud and 3d mesh](#mesh)
  - [Projecting the embryo images onto the generated mesh](#projecting)
- [Installing Instructions](#instructions)
- [User Guide](#user)
### <h3 id="summary">1. Project Summary:</h3>
In some organisms like axolotl, the surface of the embryo is transparent and thus allowing us to see the embryogenetic events taking place before the neural tube closure. Therefore, acquiring images of the outside of early stage developing embryos could give us many insights. Hence, aim of this project is to build a computational tool that allows us to visualize 4D data derived from the surface of an Axolotl embryo using a special microscope called Digital Microsphere. That is, a computational tool which will display a sphere on which the images of the embryo from different angles will be mapped creating a 3D model.
### <h3 id="stages">2. Stages of the Project:</h3>
  - #### <h4 id="image">Stage #1: Image Cropping and Processing</h4>
    In this stage, the main focus is to crop the images to get the required portion and do some image processing on it. The python file retrieves the outline of the embryo and then uses it to find out the radius of the embryo in the x,y and z directions respectively.
  - #### <h4 id="mesh">Stage #2: Generating the Point Cloud and the 3D mesh</h4>
    The python script takes three values of the radius of the embryo and using them it calculates all the 3d coordinates and then stores it in a **_.ply_** file to get the point cloud.
    Then, it takes the **_embryo.ply_** file and creates its mesh using the **_open3d_** library of python.

    ![image](https://user-images.githubusercontent.com/91690484/182136823-4bd264e7-66b7-4176-976a-531f63d6c2da.png)
  
  - #### <h4 id="projecting">Stage #3: Projecting the embryo images onto the generated mesh</h4>
    The mesh generated from the python code is then imported into blender to UV unwrap it in the required manner. Then the model is exported and then any image can be     chosen to map onto it according to its UV coordinates.
    These are the expected outputs that I showed in the proposal but I am still working on this part to improve it.
    ![image](https://user-images.githubusercontent.com/91690484/189043051-bfc45a66-f9d5-4e65-bd10-e516122481d5.png)
    
    ![image](https://user-images.githubusercontent.com/91690484/182139982-bdb7d14b-00ed-4298-b5a3-079a6b28eabc.png)
    
    This is what the projected image looks like on a ellipsoid.
    
    
### <h3 id="instructions">3. Installing Instructions</h3>
- Clone the repositry into your computer<br> 
```
git clone <repo_link>
```
- <h4>Type the following commands into the terminal to install the necessary things: </h4>
  <br>
  
  To install electron modules into the project folder 
  ```
  npm install electron
  ```
  To create a virtual env type(You must have virtualenv installed first):
  ```
  virtualenv env
  ```
  To activate the virtual env
  ```
  source env/bin/activate
  ```
  To install the required python packages in our environment
  ```
  pip install -r requirements.txt
  ```
  To start the application in elctron
  ```
  npm start
  ```
- The application will open after this command. You can see the embryo model in it. Now follow the user guide to use it.
![image](https://user-images.githubusercontent.com/91690484/188815554-f432c965-3092-4775-86ed-a2345d03e9dd.png)

### <h3 id="user">4. User Guide</h3>
<hr>

![img1](https://user-images.githubusercontent.com/91690484/188880937-5bbbed57-ef1c-44e1-9c1e-8dca285fec1d.png)
<br>
<h3>Click the import button to import images from your pc.</h3>
<br>

![image](https://user-images.githubusercontent.com/91690484/188862650-a7e96be5-2242-4240-9145-926a88fb94b4.png)
<br>
<h3>Select two images of the embryo which represent its two opposite sides</h3>
<br>

![img1](https://user-images.githubusercontent.com/91690484/188885611-adf56d48-34f7-4c09-889f-10642f35d97a.png)
<br>

<h3>Click the load the model button to load the new images that were selected in the previous step.</h3>
