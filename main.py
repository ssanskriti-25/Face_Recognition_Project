import cv2                                   #Importing all the necessary libraries
import numpy as np
import face_recognition
import os
from datetime import datetime

video_capture= cv2.VideoCapture(0)
path ='Images'                   #Folder which contains images of people to detect is given in the path.To detect more faces , add 
                                 #the images of those people in this folder and save their images as the name of the people.
images=[]
studentNames=[]
cnt=0

myList=os.listdir(path)
print(myList)

for i in myList:
    curImg=cv2.imread(f'{path}/{i}')
    images.append(curImg)
    studentNames.append(os.path.splitext(i)[0])     # To only determine the name present at the zero index in the myList.
print(studentNames)                                  # print the name of all the people who are present in the Images 

def findEncodings(images):                           #Function to find Encodings
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)         # face_recognition library works on RGB images whereas the computer works on 
                                                           # BGR images                                       
        encode=face_recognition.face_encodings(img)[0]     #finding image encodings
        encodeList.append(encode)
    return encodeList

def markAttendance(name,date1):                   #Function to mark Attendance and store it in a csv or Excel File.
    current_date = datetime.now()
    today = current_date.strftime('%Y-%m-%d')
    try:
        with open('Attendance-'+today+'.csv','r+') as f:    # If already the cvs file present for that particular day then open in the 
                                                            # read and append mode
            myDataList1=f.readlines()                      
            nameList1=[]
            for line in myDataList1:
                entry1=line.split(',')
                nameList1.append(entry1[0])

            if(len(nameList1) == 0):
                pass
            if(name not in nameList1):            #To prevent marking Attendance twice and mark for the entering time 
                print ("Welcome")                            
                now=datetime.now()
                dtString=now.strftime('%H:%M:%S')
                ttString = now.strftime('%Y-%m-%d')
                f.writelines(f'\n{name},{dtString},{ttString},Present')    #storing the name, current time, and the date in the Attendance File.
           

    except:
        with open('Attendance-'+today+'.csv','w+') as f:  #If the csv file not present for that day then open it with write append mode.
            f.writelines('Name,Time,Date,Description')

encodeListKnown=findEncodings(images)           #Function to find encodings of images called.
cap=cv2.VideoCapture(0)                         #allows working with video by capturing via live webcam.

while True:
    success, img = cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)           #resizing the input of webcam to fasten the processing

    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame=face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace , faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)      #comparing the faces in webcam from images (bool value)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)      #Comparing the encodings to recognize faces.
        matchIndex=np.argmin(faceDis)                                           #Minimum face distance image is the most similar image 
                                                                                #found.
        if matches[matchIndex]:
            name=studentNames[matchIndex].upper()
            y1,x2,y2,x1=faceLoc
            y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4                                 #Changing coordinates with respect to original webcam 
                                                                               #image
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,122),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,54,122),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(244,0,23),2)        #Writing the name of the recognized face
            date1=""
            markAttendance(name,date1)    #Function to mark Attendance called.
    

    cv2.imshow("Webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):    #Close the webcam on pressing q.
       break

video_capture.release()                     
cv2.destroyAllWindows()