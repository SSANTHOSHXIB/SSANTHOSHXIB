
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import *

mydb=mysql.connector.connect(host="localhost", user="root", password='SMDS',port='3136', database='student', autocommit=True)
cursor = mydb.cursor()

def login():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("create table if not exists student(Name varchar(20),Reg_No Varchar(10),Year_of_Study Varchar(10),Department_Name Varchar(10),CGPA float,Contact_No Bigint(20),Password Varchar(10));")
    cursor.execute(f"SELECT Name, Reg_no, Year_of_Study, Department_Name, CGPA, Contact_No FROM student WHERE Reg_no = '{username}' AND Password = '{password}'")
    result = cursor.fetchall()

    if result:
        student_info = result[0]
        show_student_details(student_info)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def show_student_details(student_info):
    student_window = tk.Toplevel(root)
    student_window.title("Student Login")
    student_window.geometry("1920x1080")
    student_window.configure(bg="black")
    
    student2_label = tk.Label(student_window, text="                                STUDENT LOGIN PORTAL                             ", font=("ROG FONTS", 30),bg="black",fg="white")
    student2_label.pack()

    labels = ["Name", "Registration Number", "Year of Study", "Department Name", "CGPA", "Contact Number"]
    for i, label in enumerate(labels):
        #tk.Label(student_window, text=label + ":",anchor='center').pack()
        #label_text = label + ": " + student_info[i]
        #tk.Label(student_window, text=label_text, anchor='center').pack()
        
        tk.Label(student_window, text=label + ":",bg="black",fg="white",font=("TIMES NEW ROMAN", 30)).pack()
        tk.Label(student_window, text=student_info[i],bg="black",fg="white",font=("TIMES NEW ROMAN", 30)).pack()

root = tk.Tk()
root.title("Student Login")
root.geometry("1920x1080")
root.configure(bg="black")


frame = tk.Frame(root)
frame.configure(bg="black")
frame.pack()
student_label = tk.Label(frame, text="                                STUDENT LOGIN PORTAL                             ", font=("ROG FONTS", 30),bg="black",fg="white")
student_label.pack()
bg = PhotoImage(file = "D:/sample.png")

student1_label = tk.Label(root, text="", image=bg)
student1_label.pack()

user_label = tk.Label(frame, text="",bg="black",fg="white",font=("TIMES NEW ROMAN", 30))
user_label.pack(pady=20)

username_label = tk.Label(frame, text="Username:",bg="black",fg="white",font=("TIMES NEW ROMAN", 30))
username_label.pack(pady=20)

#username_label.grid(row=0, column=0, sticky='e')
username_entry = tk.Entry(frame,font=("TIMES NEW ROMAN", 12))
#username_entry.grid(row=0, column=1)
username_entry.pack()
password_label = tk.Label(frame, text="Password:",bg="black",fg="white",font=("TIMES NEW ROMAN", 30))
password_label.pack()
#password_label.grid(row=1, column=0, sticky='e')
password_entry = tk.Entry(frame, show="*",font=("TIMES NEW ROMAN", 12))
#password_entry.grid(row=1, column=1)
password_entry.pack()
login_button = tk.Button(frame, text="Login", command=login,bg="black",fg="white",font=("TIMES NEW ROMAN", 20))
login_button.pack(pady=20)
#login_button.grid(row=2, columnspan=2)


root.mainloop()

cursor.close()
mydb.close()
