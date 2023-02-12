# Hand-Written-Digit-Recognition-using-DeepLearning(VGG16)
This is a machine learning project that uses a deep learning model (VGG16) to predict handwritten digits, a jupyter notebook contains the code to build and train the model. This repository also contains a demo that allows the user to draw digits to be recognized, you will find two python files and a pt file for the demo.
  
# Getting Started
## To run the demo, walk with the following steps:
    1- Install the required packages, you can use the following command in CMD or Terminal:     `pip install requirements.txt`
    2- Run the python file (main.py), you can use the following command in CMD or Terminal:    `python main.py`

## To run the code of VGG16 training:
  - You can download the notebook, and open it using Visual Studio Code, Anaconda jupyter, or any editor you want. Or you can upload it on Google Colab, or kaggle. 

# Project Structure
## The project has the following file structure:
. <br>
├── Training <br> 
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; └── VGG16_training.ipynb <br>
├── assets <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── model_parameters <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── model.pt <br>
├── main.py <br>
├── model.py <br>
└── requirements.txt
 
  note that if you want only to run the demo then you don't need (VGG16_training.ipynb) file, you will only need (assets folder, main.py file, model.py file, requirements.txt file)

## Describtion:
### The repository contains:
    1- A Jupyter Notebook (VGG16_training.ipynb) that contains the code of the machine learning process starting by reading the data, building the model, training it, until finally saving its parameters as pt files to be used later.
    2- A demo that is a desktop application which consists of two python files, and pt file. The first one is (main.py) which contains the code that builds the GUI using Tkinter. The second Python script is (model.py) that loads the weights of the pre-trained model using (model.pt) file and provides a predict function to make predictions on new data. This script also includes the definition of the VGG16 model and the necessary preprocessing steps to prepare the data for the model.
    3- An assets folder that contains the trained model parameters saved as a pt file, which is going to be used in the demo.
    4- A (requirements.txt) file which contains all libraries and packages used in the project.
  
#  Contributions
This project is open-source, and contributions are welcome. If you find any bugs or have any suggestions for improvements, please open an issue or submit a pull request.

# Conclusion
This repository demonstrates how a VGG16 deep learning model can be used for handwritten digit recognition. The demo application provides an interactive interface for users to write or draw a digit, and the model will recognize it. The repository also includes the code for training the model, so you can use it as a starting point for your own projects.
