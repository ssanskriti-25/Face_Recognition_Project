# Face_Recognition_Project
This project can detect the live faces of the students and mark their attendance in the csv file.
This project will detect the live faces through the webcam by searching the face in the 'Images' folder and after detecting the face it will create the new csv file for that day in case if not present and write the name , current time and the current date of the detected person in the file.

# Steps to Run the Project
1.Install python-3.10.4 (64 bit) or above from 'https://www.python.org/downloads/' and add the PATH to your user and System Variables under Environment variables.

2.Install VISUAL STUDIO Community Edition from 'https://visualstudio.microsoft.com/downloads/' and install plugins for PYTHON development and C++ Desktop Development(important).

3.Packages to install to run the code

  -> opencv-python
  
  -> numpy
  
  -> cmake
  
  -> dlib
  
  -> face-recognition
  
  -> datetime
  
4.Clone my git repository to a directory in your device using : git clone command.

![Screenshot (4)](https://user-images.githubusercontent.com/87524185/170824495-3fed93a5-b6e3-4051-8cbb-6b98787212b3.png)
 
copy the link and open the git bash in the new directory created for this project and write git clone (paste the url copied above).

5.Run the code file- main.py in your visual stdio.When we will run the code firstly the mylist will print and them the name of all the all the students present in the Images folder and then after that webcam start detecting the face of the students and when the face get detected 'Welcome' will be printed in the terminal.
![Screenshot (5)](https://user-images.githubusercontent.com/87524185/170824984-1836a1aa-91c4-4deb-85b5-e67c1b4537ea.png)

6.Now to check whether the attendance got marked or not we will open the csv file of that particular day to check the name of students present on that day.

## Note
To recognize new faces through the webcam add clear front facing images of the new faces in the 'Images' folder with the name of the image renamed to the name of the Person.

The attendance of one students will be marked only once in the day indead of detecting them whenever they come infront of the webcam. 
