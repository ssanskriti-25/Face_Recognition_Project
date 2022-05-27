# Face_Recognition_Project
This project can detect the live faces of the students and mark their attendance in the csv file.
This project will detect the live faces through the webcam by searching the face in the 'ImageAttendance' folder and after detecting the face it will create the new csv file for that day in case if not present and write the name , current time and the current date of the detected person in the file.

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

5.Run the code file- AttendanceProject.py in your visual stdio.

## Note
To recognize new faces through the webcam add clear front facing images of the new faces in the 'ImageAttendance' folder with the name of the image renamed to the name of the Person.
