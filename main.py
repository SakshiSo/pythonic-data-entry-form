import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl



def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        # Course info
        registration_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemesters = numsemesters_spinbox.get()

        print("Name:", title , firstname, lastname)
        print("Age:", age, "Nationality:", nationality)
        print("# Courses:", numcourses, "# Semesters:", numsemesters)
        print("Registration status:", registration_status)
        print("--------------------------------------------")
    
        filepath = "C:/Users/Sakshi/OneDrive/Desktop/Mini Project Sem 4/DATA ENTRY FORM/data.xlsx"
        
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = (["First name", "Last name", "Title", "Age", "Nationality",
                       "# Courses", "# Semesters", "Registration status"])
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active   
        sheet.append([firstname, lastname, title, age, nationality, numcourses,
                      numsemesters, registration_status]) 
        workbook.save(filepath)
    
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "You have not Accepted Terms & Conditons")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack() 

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text = "age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["African", "Antarctican", "Asian", "Europian", "Indian", "North American", "South American"])
nationality_label.grid(row=2,  column=1)
nationality_combobox.grid(row=3, column=1)
  
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text = "Registration Status")

reg_status_var = tkinter.StringVar(value = "Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered",
                                       variable = reg_status_var, onvalue = "Registered", offvalue = "Not Registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text = "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text = "# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value = "Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept terms & conditions.",
                                  variable = accept_var, onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row=0, column=0)

#button
button  = tkinter.Button(frame, text = "Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()