from tkinter import *
from PIL import ImageTk, Image
import diag as d
import pat as p
import taqreer as t


root = Tk()
root.geometry("1365x703+100+50")
root.title("Screen Lab")
root.config(background="white")
root.resizable(False,False)
root.iconbitmap(r"D:\OneDrive\Desktop\My work\Lab-Project\icon3.ico")
title_root = Label(root
,text="Screen Lab System"
,bg="#0F6A65"
,font=("monospace",14,"bold")
,fg="white")
title_root.pack(fill=X)

# ------------------------- fisrt frame -------------------------    


fr1 = Frame(root
,bg="#0F4E4A"
,height=520
,width=365)
fr1.place(x=995,y=32)

title1 = Label(fr1
,text="Patient data"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title1.place(x=0,y=0,width=365,height=40)

lbl11 = Label(fr1
,text="Name :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl11.place(x=20, y=70)

en11 = Entry(fr1
,justify="center"
,font=1)
en11.place(x=90,y=71)

lbl12 = Label(fr1
,text="Age :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl12.place(x=20, y=110)

en12 = Entry(fr1
,justify="center")
en12.place(x=70,y=111)

lbl13 = Label(fr1
,text="Sex :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl13.place(x=20, y=150)

en13 = Entry(fr1
,justify="center")
en13.place(x=70,y=151)

lbl14 = Label(fr1
,text="Receiving date :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl14.place(x=20, y=190)

en14 = Entry(fr1
,justify="center")
en14.place(x=150,y=191)

lbl15 = Label(fr1
,text="Reporting date :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl15.place(x=20, y=230)

en15 = Entry(fr1
,justify="center")
en15.place(x=150,y=231)

lbl16 = Label(fr1
,text="Lab.Reference no. :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl16.place(x=20, y=270)

en16 = Entry(fr1
,justify="center")
en16.place(x=180,y=271)

lbl17 = Label(fr1
,text="Previous biopsy no. :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl17.place(x=20, y=310)

en17 = Entry(fr1
,justify="center")
en17.place(x=180,y=311)

lbl18 = Label(fr1
,text="Surgeon name :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl18.place(x=20, y=350)

en18 = Entry(fr1
,justify="center")
en18.place(x=150,y=351)


lbl19 = Label(fr1
,text="Number of slides :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl19.place(x=20, y=390)

en19 = Entry(fr1
,justify="center")
en19.place(x=165,y=391)

lbl110 = Label(fr1
,text="Code :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl110.place(x=20, y=430)

en110= Entry(fr1
,justify="center")
en110.place(x=80,y=431)

btn_add_patient = Button(fr1
,text="Add patient"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=15
,command=p.add_patient)
btn_add_patient.place(x=50,y=475)


btn_clear_patient = Button(fr1
,text="Clear"
,bd=2
,bg="#D6131C"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,command=p.clear)
btn_clear_patient.place(x=230,y=475)


# ---------------------------- socend frame --------------------------


fr2 = Frame(root
,bg="#0F4E4A"
,height=144
,width=365)
fr2.place(x=995,y=555)


title2 = Label(fr2
,text="About patient"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title2.place(x=0,y=0,width=365,height=40)

lbl21 = Label(fr2
,text="Enter the reference"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl21.place(x=118, y=45)

en21 = Entry(fr2
,justify="center"
,font=10)
en21.place(x=75,y=70)

btn_search_patient = Button(fr2
,text="Search"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,command=p.pat_search)
btn_search_patient.place(x=10,y=105)

btn_update_patient = Button(fr2
,text="Update"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,command=p.update_patient)
btn_update_patient.place(x=130,y=105)

btn_delete_patient = Button(fr2
,text="Delete"
,bd=2
,bg="#D6131C"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,command=p.delete_patient)
btn_delete_patient.place(x=250,y=105)


# ------------------------- third frame -----------------------------


fr3 = Frame(root
,bg="#0F4E4A"
,height=668
,width=365)
fr3.place(x=625,y=32)

title3 = Label(fr3
,text="Add Diagnosis"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title3.place(x=0,y=0,width=365,height=40)


lbl31 = Label(fr3
,text="GROSS"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl31.place(x=150, y=40)


fr31 = Frame(fr3
,bg="white")
fr31.place(x=7,y=70)


scroll_y1 = Scrollbar(fr31
,orient=VERTICAL)
textarea1 =Text(fr31
,width=41
,height=7
,yscrollcommand=scroll_y1.set)
scroll_y1.pack(side=LEFT , fill=Y)
scroll_y1.config(command=textarea1.yview)
textarea1.pack(fill=BOTH,expand=1)


lbl2 = Label(fr3
,text="MICROSCOPIC"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl2.place(x=130, y=195)


fr32 = Frame(fr3
,bg="white")
fr32.place(x=7,y=225)


scroll_y2 = Scrollbar(fr32
,orient=VERTICAL)

textarea2 = Text(fr32
,width=41
,height=7
,yscrollcommand=scroll_y2.set)
scroll_y2.pack(side=LEFT , fill=Y)
scroll_y2.config(command=textarea2.yview)
textarea2.pack(fill=BOTH,expand=1)


lbl33 = Label(fr3
,text="CONCLUSION"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl33.place(x=130, y=345)


fr33 = Frame(fr3
,bg="white")
fr33.place(x=7,y=375)


scroll_y3 = Scrollbar(fr33
,orient=VERTICAL)

textarea3 = Text(fr33
,width=41
,height=4
,yscrollcommand=scroll_y3.set)
scroll_y3.pack(side=LEFT , fill=Y)
scroll_y3.config(command=textarea3.yview)
textarea3.pack(fill=BOTH,expand=1)


lbl34 = Label(fr3
,text="NATURE OF SPECIMEN"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl34.place(x=110, y=450)


fr34 = Frame(fr3
,bg="white")
fr34.place(x=7,y=480)


scroll_y4 = Scrollbar(fr34
,orient=VERTICAL)

textarea4 = Text(fr34
,width=41
,height=2
,yscrollcommand=scroll_y4.set)
scroll_y4.pack(side=LEFT , fill=Y)
scroll_y4.config(command=textarea4.yview)
textarea4.pack(fill=BOTH,expand=1)


lbl35 = Label(fr3
,text="CODE"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl35.place(x=155, y=550)

en31 = Entry(fr3
,justify="center")
en31.place(x=120,y=580)

btn_add_diagonsis = Button(fr3
,text="Add"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=6
,command=d.add_diagnosis)
btn_add_diagonsis.place(x=115,y=620)

btn_clear_diagonsis = Button(fr3
,text="Clear"
,bd=2
,bg="#D6131C"
,fg="white"
,font=("monospace",11,"bold")
,width=6
,command=d.clear)
btn_clear_diagonsis.place(x=190,y=620)


# ------------------------ fourth frame ------------------------------


fr4 = Frame(root
,bg="#0F4E4A"
,height=145
,width=304)
fr4.place(x=5,y=555)

title4 = Label(fr4
,text="Report writing"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title4.place(x=0,y=0,width=307,height=40)

lbl41 = Label(fr4
,text="Enter the reference"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl41.place(x=95, y=45)

en41 = Entry(fr4
,justify="center"
,font=10)
en41.place(x=50,y=70)

btn_write_patient = Button(fr4
,text="Write"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,command=t.write_taqreer)
btn_write_patient.place(x=110,y=105)


# ------------------------------- fifth frame -----------------------------------


fr5 = Frame(root
,bg="#0F4E4A"
,height=145
,width=307)
fr5.place(x=313,y=555)

title5 = Label(fr5
,text="About diagnosis"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title5.place(x=0,y=0,width=307,height=40)

lbl51 = Label(fr5
,text="Enter the code"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl51.place(x=100, y=45)

en51 = Entry(fr5
,justify="center"
,font=10)
en51.place(x=45,y=70)

btn_search_diag = Button(fr5
,text="Search"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=7
,command=d.dia_search)
btn_search_diag.place(x=10,y=105)

btn_update_diag = Button(fr5
,text="Update"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=7
,command=d.update_dia)
btn_update_diag.place(x=120,y=105)

btn_delete_diag = Button(fr5
,text="Delete"
,bd=2
,bg="#D6131C"
,fg="white"
,font=("monospace",11,"bold")
,width=7
,command=d.delete_dia)
btn_delete_diag.place(x=225,y=105)


# ------------------------ 6th frame ------------------------------


fr6 = Frame(root
,bg="#0F4E4A"
,height=180
,width=615)
fr6.place(x=5,y=371)

title6 = Label(fr6
,text="Patients and Diagnosis"
,bg="#0E8881"
,font=("monospace",13,"bold")
,fg="white")
title6.place(x=0,y=0,width=615,height=40)

btn_all_diag = Button(fr6
,text="Showing all codes"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=20
,command=d.pro_dia_all)
btn_all_diag.place(x=100,y=55)

btn_all_patients = Button(fr6
,text="Showing all patients"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=20
,command=p.csv_pat_all)
btn_all_patients.place(x=330,y=55)

lbl61 = Label(fr6
,text="Pateints who have the same diagnosis"
,bg="#38967E"
,fg="white"
,font=("monospace",11,"bold"))
lbl61.place(x=0, y=100 , height=30 , width=615)

lbl62 = Label(fr6
,text="Enter the code :"
,bg="#0F4E4A"
,fg="white"
,font=("monospace",11,"bold"))
lbl62.place(x=110, y=145)

en62 = Entry(fr6
,justify="center")
en62.place(x=245,y=146)

btn_g = Button(fr6
,text="Search"
,bd=2
,bg="#3CA59F"
,fg="white"
,font=("monospace",11,"bold")
,width=10
,height=1
,command=p.csv_pat_code)
btn_g.place(x=395,y=140)


# -------------------------------- 7th frame -------------------------------


fr7 = Frame(root
,bg="black"
,height=335
,width=615)
fr7.place(x=5,y=32)


photo = ImageTk.PhotoImage(Image.open(r"D:\OneDrive\Desktop\My work\Lab-Project\photo2.jpg"))
panel = Label(root
,image=photo
,bg="white"
,borderwidth=10)
panel.place(x=190, y=90, width=200, height=200)


root.mainloop()