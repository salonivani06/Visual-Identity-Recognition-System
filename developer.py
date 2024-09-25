from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face_Recognition_System")


        title_lbl = Label(self.root, text="DEVELOPER", font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=15,  pady=10 )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top= Image.open(r"D:\projects\Attendance Management System\Images\bgImage.jpg")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg = ImageTk.PhotoImage(img_top)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=50, width=1530, height=720)

        #Framw
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=780, y=10, width=500, height=200)

        img_top1= Image.open(r"D:\projects\Attendance Management System\Images\developerFace.jpg")
        img_top1 = img_top1.resize((200,200), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg1 = ImageTk.PhotoImage(img_top1)


        f_lbl = Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        #developer info
        dev_label = Label(main_frame,text="Hello Visitor!!",font=("Helvetica", 20, "bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame,text="I'm Saloni Vani",font=("Helvetica", 20, "bold"),bg="white")
        dev_label.place(x=0,y=40)

        devo_label = Label(main_frame,text="Transforming ideas into reality ",font=("Helvetica", 15, "italic bold"),bg="white")
        devo_label.place(x=0,y=100)

        
        devoo_label = Label(main_frame,text="through code and creativity.",font=("Helvetica", 15, "italic bold"),bg="white")
        devoo_label.place(x=0,y=130)

        # img_dev= Image.open(r"Images\dface.jpg")
        # img_dev = img_dev.resize((500,300), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimgdev = ImageTk.PhotoImage(img_dev)


        # f_lbl = Label(main_frame,image=self.photoimgdev)
        # f_lbl.place(x=0, y=210, width=500, height=300)
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()