# Face_Recognition_Project
This project can detect the live faces of the students and mark their attendance in the csv file.
This project will detect the live faces through the webcam by searching the face in the 'Images' folder and after detecting the face it will create the new csv file for that day in case if not present and write the name , current time and the current date of the detected person in the file.

#Project Description
This is face recognition project which is used to mark the attendance of the students in schools and colleges. The entire code is written in python and to detect the face firstly i have store the data of some students in the 'Images' folder and named their images with their actual name. The images saved get encoded and then during the detection process the webcam opens and then based on the encodings determine the name of the student and show the name in the rectangular box at the bottom of the face of the student. After the detection process the data get stored in the attendence.csv file of that particular day.

# Steps to Run the Project
1.Install python-3.10.4 (64 bit) or above from 'https://www.python.org/downloads/' and add the PATH to your user and System Variables under Environment variables.

2.Install VISUAL STUDIO Community Edition from 'https://visualstudio.microsoft.com/downloads/' and install plugins for PYTHON development and C++ Desktop Development(important).

3.Packages to install to run the code

  -> opencv-python  (pip install opencv-python)
  
  -> numpy  (pip install numpy)
  
  -> cmake  (pip install cmake)
  
  -> dlib   (pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl)
  
  -> face-recognition  (pip install face_recognition)
  
  -> datetime   (pip install datetime)
  
to install all the above packages open the command prompt and type the command written in the bracket in front of each.
  
4.Clone my git repository to a directory in your device using : git clone command.


![Screenshot (4)](https://user-images.githubusercontent.com/87524185/170824495-3fed93a5-b6e3-4051-8cbb-6b98787212b3.png)
 
copy the link and open the git bash in the new directory created for this project and write git clone (paste the url copied above).


5.Run the code file- main.py in your visual stdio.When we will run the code firstly the mylist will be printed and them the name of all the all the students present in the Images folder and then after that webcam opens and start detecting the face of the students and when the face got detected 'Welcome' will be printed in the terminal.


![Screenshot (7)](https://user-images.githubusercontent.com/87524185/170825385-db5f5b00-0751-424d-a27c-969600b33052.png)


6.Now to check whether the attendance got marked or not we will open the csv file of that particular day to check the name of students present on that day.
![Screenshot (6)](https://user-images.githubusercontent.com/87524185/170825291-2d2b668b-6e89-44c1-9238-13e8ec416836.png)


## Note
To recognize new faces through the webcam add clear front facing images of the new faces in the 'Images' folder with the name of the image renamed to the name of the Person.

The attendance of one students will be marked only once in the day indead of detecting them whenever they come infront of the webcam. 
