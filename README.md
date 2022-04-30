# GSoC-2022

### Project #1: GNNs as Developmental Networks   
Biological development features many different types of networks: neural connectomes, gene regulatory networks, interactome networks, and anatomical networks. Using cell tracking and high-resolution microscopy, we can reconstruct the origins of these networks in the early embryo. Building on our group's past work in  deep learning and pre-trained models, we look to apply graph neural networks (GNNs) to developmental biological analysis. We seek to create graph embeddings that resemble actual biological networks found throughout development. Potential activities includes growing graph embeddings using biological rules, differentiation of nodes in the network, and GNNs that generate different types of movement output based on movement seen in microscopy movies. The goal is to create a library of GNNs that can simulate developmental processes by analyzing time-series microscopy data. The project duration is 175 hours or 20 hours for 10 coding weeks.

DevoWorm is an interdisciplinary group engaged in both computational and biological data analysis. We have weekly meetings on Jit.si, and are a part of the OpenWorm Foundation. You may also have the chance to work with our DevoLearn (open-source pretrained deep learning) software, in addition to adding your contributions to the DevoWorm AI library.

__What can I do before GSoC to prepare?__   
You can ask one of the mentors to direct you to the data source and you can start working on it. Please feel free to join the OpenWorm Slack or attend our meetings to raise questions/discussions regarding your approach to the problem. 

DevoWorm website: https://devoworm.weebly.com/

DevoLearn (preprint): https://github.com/DevoLearn/devolearn/blob/master/paper.md

DevoWorm AI: https://devoworm.github.io/DevoWormAi/

__Skills/requirements__   
PyTorch/Tensorflow (PyTorch will be preferred because all our other models are on that framework already) Wrangling with video data Building a simple GUI on top of the model to run it on local systems (on Linux/windows/macOS). Basic knowledge of biology and complex networks theory would be helpful.

DevoLearn D-GNNs repository: [link](https://github.com/DevoLearn/D-GNNs)

### Project #2: Digital Microsphere   
This project will build upon the specialized microscopy techniques to develop a shell composed of projected microscopy images, arranged to represent the full external surface of a sphere. This will allow us to create an atlas of the embryo’s outer surface, which in some species (e.g. Axolotl) enables us to have a novel perspective on neural development. You will build a computational tool to visualize these 4D data. The project duration is 175 hours or 20 hours for 10 coding weeks.

__What can I do before GSoC to prepare?__    
Build basic prototypes for this project and discuss about them with the mentors, then read these papers:

Gordon, R. (2009). Google Embryo for Building Quantitative Understanding of an Embryo As It Builds Itself. II. Progress Toward an Embryo Surface Microscope. Biological Theory, 4, 396–412.

Crawford-Young, S., Dittapongpitch, S., Gordon, R., and Harrington, K. (2018). Acquisition and reconstruction of 4D surfaces of axolotl embryos with the flipping stage robotic microscope. Biosystems, 173, 214-220.

__Skills/requirements__   
Handling higher dimensional microscopy data (preferably also creating an API to load them as tensors for computation on the GPU). Building an intuitive GUI (or a web interface). Feature extraction (canny edges/thresholding/denoising)

__Mentor__   
Bradly Alicea [balicea@openworm.org](balicea@openworm.org)
