HOW TO SETUP THE INSECT DETECTION SYSTEM (I.D.S)

SETUP ENVIREMOENT

#First you will need to install Python version 3.7.6 or newer
#Make sure during installation you check the PIP option ("this installs the pip command in the command line")

#Here is the link for Windows:
https://www.python.org/downloads/windows/

#Here is the link for Mac:
https://www.python.org/downloads/mac-osx/ 

#Once the python installer is finished, it is time to access the "Command prompt"
#How to access the command prompt:
#Windows: Press the windows key and type "command prompt" and select the "Command Prompt" application
#Mac: In the top right of your desktop window there is a magnifying glass icon, click that icon and type
      in the search "terminal" your top result should be the "Terminal" application, click on the "Terminal"
      application to open your command prompt.

#Open the command prompt and type the following commands to install the necessary packages:

#Protobuf
pip install protobuf

#Pillow
pip install pillow

#lxml
pip install lxml

#Cython
pip install Cython

#Jupyter
pip install jupyter

#Matplotlib
pip install matplotlib

#Pandas
pip install pandas

#OpenCV (Must be Version 4.2.0)
pip install opencv-python==4.2.0

#TensorFlow (Must Be Version 1.14.0)
pip install tensorflow==1.14.0

#Once these packages are installed then we are ready to run the I.D.S



RUNNING THE I.D.S

#From the command prompt
1. Change the directory to the location of the downloaded file with the command "cd"
      For example, if you store it on the desktop (using windows):
      "cd C:\Users\<username>\Desktop\T5_Insect_Detection_System"

2. Change the directory to the InsectDetectionSystem folder
   "cd InsectDetectionSystem" 

3. Change the directory to the object_detection folder
   "cd object_detection" 

   #At this point you should be in the right location for the I.D.S to run
   #Here is an example of what the final directory location should look like
   #Assuming the file was saved on the desktop (using Windows)  
   "C:\Users\<username>\Desktop\T5_Insect_Detection_System\InsectDetectionSystem\object_detection"

7. run the command "python ids_gui.py" this will launch the I.D.S


#Directly from file
1. Go to wherever you stored the downloaded file ("T5_Insect_Detection_System") and open the folder.

2. Inside the "T5_Insect_Detection_System" there is a folder called "InsectDetectionSystem", open it.

3. Inside the "InsectDetectionSystem" folder there is a folder called "object_detection", open it.

4. Locate the .py file "ids_gui.py" inside the "object_detection" folder, right click on it and select "Edit with IDLE". This opens the IDLE python editor.

5. In the navigation bar (top of the editor window) select "Run" and then click "Run Module"
