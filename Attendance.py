from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import csv
import os
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x710+0+0")
        self.root.title("Face_Recognition_System")

        #variables
        self.var_atten_id = StringVar()
        self.var_atten_roll= StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


         #bg image
        img3 = Image.open(r"D:\projects\Attendance Management System\Images\backgimage.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS) #high leve image -> low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root , image = self.photoimg3)
        bg_img.place(x=0, y=0, width = 1530, height = 710)

        title_lbl = Label(bg_img,text="Attendance Sheet",font=("Helvetica", 28, "bold"),  bg="#1e3a8a",  fg="#ffffff",  bd=4,relief="flat",padx=15,  pady=10  )
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10, y=50, width=1225, height=550)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman",12,"bold"),bg="white")
        Left_frame.place(x=10, y=10 ,width=600, height= 520)

        # img = Image.open(r"D:\projects\Attendance Management System\Images\atendance.jpg")
        # img = img.resize((450,130), Image.Resampling.LANCZOS) #high leve image -> low level image
        # self.photoimg = ImageTk.PhotoImage(img)

        # f_lbl = Label(self.root , image = self.photoimg)
        # f_lbl.place(x=20, y=50, width = 550, height = 150)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=10,width=720,height=370)

       

        #Label and Entries
        # attendanceId_label = Label(class_student, text="Attendance ID:",font=("times new roman",12,"bold")) 
        # attendanceId_label.grid(row=0, column=0, padx=10, sticky = W)

        # #attendance id
        # attendanceId_entry = Entry(left_inside_frame,textvariable=self.var_id, width=12, font=("times new roman",12,"bold") )
        # attendanceId_entry.grid(row=0, column=1, padx=10, sticky=W)\

        #attendance id
        attendance_Id_label = Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        attendance_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_Id_Entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_atten_id,font=("times new roman",12,"bold") )
        attendance_Id_Entry.grid(row=0, column=1, padx=10, pady=5,sticky=W)

        #roll
        roll_label = Label(left_inside_frame,text="Roll Number:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_roll,font=("times new roman",12,"bold") )
        atten_roll.grid(row=0, column=3,pady=5)

        #name
        name_label = Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_name,font=("times new roman",12,"bold") )
        atten_name.grid(row=1, column=1, padx=10, pady=5,sticky=W)

        #Dept
        dept_label = Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dept_label.grid(row=1,column=2,padx=4,pady=8,sticky=W)

        atten_dep = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_dep,font=("times new roman",12,"bold") )
        atten_dep.grid(row=1, column=3, padx=10, pady=5,sticky=W)

        #time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10, pady=5,sticky=W)

        atten_time = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_time,font=("times new roman",12,"bold") )
        atten_time.grid(row=2, column=1,padx=10, pady=5)

        #date
        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        atten_date = ttk.Entry(left_inside_frame, width=15,textvariable=self.var_atten_date,font=("times new roman",12,"bold") )
        atten_date.grid(row=2, column=3, pady=8)

        #attendance\
        attendance_label = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame,width=15,textvariable=self.var_atten_attendance,font=("times new roman",13,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

         
        #button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=210, width=715,height=50)

        #Save button
        save_btn = Button(btn_frame, text="Import CSV",command=self.importCSV,width=14, font=("Helvetica", 13, "bold"),bg="#1e3a8a",  fg="#ffffff")
        save_btn.grid(row=0, column=0)
        #update button
        update_btn = Button(btn_frame, text="Export CSV",command=self.ExportCSV, width=14, font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff")
        update_btn.grid(row=0, column=1)
        #delete button
        delete_btn= Button(btn_frame, text="Update",  width=14,font=("Helvetica", 13, "bold"),bg="#1e3a8a",  fg="#ffffff" )
        delete_btn.grid(row=0, column=2)
        #reset button
        reset_btn= Button(btn_frame, text="Reset", width=14,command=self.reset_data,font=("Helvetica", 13, "bold"), bg="#1e3a8a",  fg="#ffffff")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(left_inside_frame, bd=2, bg="white")
        btn_frame1.place(x=0, y=240, width=715, height=35)

        



        
         #Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman",12,"bold"),bg="white")
        Right_frame.place(x=620, y=10 ,width=600, height= 520)
        #table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5, width=585,height=445)

        #scroll bar table
        #scoll bar
        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.AttendanceReoprtTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command =self.AttendanceReoprtTable.xview)
        scroll_y.config(command =self.AttendanceReoprtTable.yview)

        self.AttendanceReoprtTable.heading("id",text="Attendance Id")
        self.AttendanceReoprtTable.heading("roll",text="Roll No.")
        self.AttendanceReoprtTable.heading("name",text=" Name")
        self.AttendanceReoprtTable.heading("department",text=" Department")
        self.AttendanceReoprtTable.heading("time",text="Time")
        self.AttendanceReoprtTable.heading("date",text="Date")
        self.AttendanceReoprtTable.heading("attendance",text="Attendance")

        self.AttendanceReoprtTable["show"]="headings"
        self.AttendanceReoprtTable.column("id",width=100)
        self.AttendanceReoprtTable.column("roll",width=100)
        self.AttendanceReoprtTable.column("name",width=100)
        self.AttendanceReoprtTable.column("department",width=100)
        self.AttendanceReoprtTable.column("time",width=100)
        self.AttendanceReoprtTable.column("date",width=100)
        self.AttendanceReoprtTable.column("attendance",width=100)

        self.AttendanceReoprtTable.pack(fill=BOTH,expand=1)

        self.AttendanceReoprtTable.bind("<ButtonRelease>", self.get_cursor)

#====FETCH DATA ==========
    def fetchdata(self,rows):
        self.AttendanceReoprtTable.delete(*self.AttendanceReoprtTable.get_children())
        for i in rows:
            self.AttendanceReoprtTable.insert("",END,values=i)
    
    def importCSV(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*csv"),("All File","*.*")],parent=self.root)
        with open(fin) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    def ExportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No DATA:","No data found in the file", parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*csv"),("All File","*.*")],parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i  in mydata:
                   exp_write.writerow(i)
            messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fin)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReoprtTable.focus()
        content = self.AttendanceReoprtTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
















if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()