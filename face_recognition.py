from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np
from time import strftime
from datetime import datetime
import time 
class face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=10,  pady=10 )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #bg image
        img3 = Image.open(r"Images\backgimage.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=45, width = 1530, height = 650)

        #image
        # img_top= Image.open(r"Images\detector.jpg")
        # img_top = img_top.resize((650,700), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg = ImageTk.PhotoImage(img_top)


        # f_lbl = Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0, y=45, width=650, height=600)

        img_left= Image.open(r"Images\scanning.jpg")
        img_left = img_left.resize((500,595), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg1 = ImageTk.PhotoImage(img_left)


        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400, y=45, width=500, height=595)

        #button
        b1_1 = Button(self.root, text="Scan", cursor="hand2",font=("times new roman", 16, "bold"), bg="dark blue", fg="white",command=self.face_recognition)  
        b1_1.place(x=550, y=560, width=200, height=40)

        #==========ATTENDACE===============
    def mark_attendance(self,s,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList= f.readlines()
            name_List=[]
            for line in myDataList:
                entry = line.split((","))
                name_List.append(entry[0])
            if((s not in name_List)and (r not in name_List)and (n not in name_List) and (d not in name_List)):
                now  = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{d},{dtString},{d1},Present")






        #=======FACE RECOGNITION============

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor,minNeighbors , color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3)
                #predict image
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                #predict confidence
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password = "root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n ="+".join(n)

                my_cursor.execute("select rolll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d ="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                s = my_cursor.fetchone()
                s ="+".join(s)
 

                if confidence>77:
                    cv2.putText(img, f"ID:{s}",(x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255), 3)

                    cv2.putText(img, f"Roll:{r}",(x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255), 3)

                    cv2.putText(img, f"Name:{n}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255), 3)

                    cv2.putText(img, f"Dep:{d}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255), 3)
                    self.mark_attendance(s,r,n,d)

                else:
                     cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),3)
                     cv2.putText(img, f"Unknown face",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255), 3)
                
                coord=[x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255), "Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("welcome",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


# Main block to run the application
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()
