from tkinter import *
from fpdf import FPDF
from datetime import date, datetime 

def function():
    now = datetime.now()
    currentYear = now.strftime("%Y")
    
    studentName = str(entryBox1.get())
    fatherName = str(entryBox2.get())
    motherName = str(entryBox3.get())
    DOB = str(entryBox4.get())
    blood = str(entryBox5.get())
    mobile = str(entryBox6.get())
    email = str(entryBox7.get())
    clas = ""

    ch1 = DOB[6]
    ch2 = DOB[7]
    ch3 = DOB[8]
    ch4 = DOB[9]
    year = ch1 + ch2 + ch3 + ch4 
    year = int(year)
    currentYear = int(currentYear)
    age = currentYear - year 
    
    if(age==4):clas="LKG"
    elif(age==5):clas="KG"
    elif(age==6):clas="CLASS 1"
    elif(age==7):clas="CLASS 2"
    elif(age==8):clas="CLASS 3"
    elif(age==9):clas="CLASS 4"
    elif(age==10):clas="CLASS 5"
    elif(age==11):clas="CLASS 6"
    elif(age==12):clas="CLASS 7"
    elif(age==13):clas="CLASS 8"
    elif(age==14):clas="CLASS 9"
    elif(age==15):clas="CLASS 10"
    elif(age==16):clas="CLASS 11"
    elif(age==17):clas="CLASS 12"


    ageString = str(age)
    
    txt1 = "Student's Name : " + studentName
    txt2 = "Student's Father's Name : " + fatherName
    txt3 = "Student's Mother's Name : " + motherName
    txt4 = "Student's DOB : " + DOB
    txt5 = "Student's Age : " + ageString
    txt6 = "Student's Class : " + clas
    txt7 = "Blood Group : " + blood
    txt8 = "Contact No. : " + mobile
    txt9 = "Email ID : " + email
    
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(200,20,txt="Student Admission Slip",ln=1,align="C")
    pdf.set_font("Times",'I',size = 15)
    pdf.cell(200,10,txt=txt1,ln=2,align="L")
    pdf.cell(200,10,txt=txt2,ln=3,align="L")
    pdf.cell(200,10,txt=txt3,ln=4,align="L")
    pdf.cell(200,10,txt=txt4,ln=5,align="L")
    pdf.cell(200,10,txt=txt5,ln=6,align="L")
    pdf.cell(200,10,txt=txt6,ln=7,align="L")
    pdf.cell(200,10,txt=txt7,ln=8,align="L")
    pdf.cell(200,10,txt=txt8,ln=9,align="L")
    pdf.cell(200,10,txt=txt9,ln=10,align="L")
        
    pdf.output("slip.pdf")



window = Tk()
window.geometry("500x380")
window.title("School Admission ")

bgImg = PhotoImage(file="bg.png")
bgLabel = Label(window,image=bgImg).pack()

label1 = Label(window,text="Delhi  Public  School",font=("Algerian",27),fg="Black",bg="Light Gray")
label1.place(x=65)

label2 = Label(window,text="Enter Name of the Candididate " ,font=("Times New Roman",15),bg="Light Gray")
label2.place(x=7,y=75)

label3 = Label(window,text="Enter Father's Name :" ,font=("Times New Roman",15),bg="Light Gray")
label3.place(x=7,y=110)

label4 = Label(window,text="Enter Mother's Name : " ,font=("Times New Roman",15),bg="Light Gray")
label4.place(x=7,y=145)

label5 = Label(window,text="Enter DOB of the Candidate : " ,font=("Times New Roman",15),bg="Light Gray")
label5.place(x=7,y=180)

label6 = Label(window,text="Enter Blood Group of the Candidate" ,font=("Times New Roman",15),bg="Light Gray")
label6.place(x=7,y=215)

label7 = Label(window,text="Enter Contact Number : " ,font=("Times New Roman",15),bg="Light Gray")
label7.place(x=7,y=250)

label8 = Label(window,text="Enter Email ID : " ,font=("Times New Roman",15),bg="Light Gray")
label8.place(x=7,y=285)


entryBox1 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox1.place(x=308,y=75)

entryBox2 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox2.place(x=308,y=113)

entryBox3 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox3.place(x=308,y=148)

entryBox4 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox4.place(x=308,y=183)

entryBox5 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox5.place(x=308,y=218)

entryBox6 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox6.place(x=308,y=253)

entryBox7 = Entry(window,bd="2",width = "20",bg="Light Grey",fg="Black",font=("Times New Roman",13))
entryBox7.place(x=308,y=288)

submitButton = Button(window,text="Submit",width="15",bg="Black",fg="White",font=("Cambria",15),command=function)
submitButton.place(x = 235,y=325)

window.mainloop()

