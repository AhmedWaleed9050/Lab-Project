import lab as l 
from tkinter import messagebox
import pyodbc
import csv

def add_patient():
    
    try:
    
        connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
        
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()

        if l.en11.get()!="" and l.en12.get()!=0 and l.en13.get()!="" and l.en14.get()!="" and l.en15.get()!=""and l.en16.get()!="" and l.en18.get()!=0 and l.en19.get()!="" and l.en110.get()!="":

            cur.execute("insert into patients values (? , ? , ? , ? , ? , ? , ? , ? , ? , ?)"
            ,(l.en11.get()
            ,l.en12.get()
            ,l.en13.get()
            ,l.en14.get()
            ,l.en15.get()
            ,l.en16.get()
            ,l.en17.get()
            ,l.en18.get()
            ,l.en19.get()
            ,l.en110.get()))
            conn.commit()
            conn.close()

        else:
            messagebox.showwarning("Warning","Data is not complete.")

    except : 
        messagebox.showwarning("Warning","""        this diagonsis is not exist or the reference is already exist,
        if the problem is in diagonisis add it first
        ,but if it is in the reference add the previous biopsy no. 
        and change the name.""")
        
        
# -----------------------------------------------------------------        
        

def clear() :
    
    l.en11.delete(0,l.END)
    l.en12.delete(0,l.END)
    l.en13.delete(0,l.END) 
    l.en14.delete(0,l.END) 
    l.en15.delete(0,l.END) 
    l.en16.delete(0,l.END)
    l.en17.delete(0,l.END)
    l.en18.delete(0,l.END) 
    l.en19.delete(0,l.END)
    l.en110.delete(0,l.END) 
    
    
# ---------------------------------------------------------------  


def delete_patient():

    if l.en21.get() == "" :

        messagebox.showwarning("Warning","Enter a refrence first")

    else:    

        connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        
        cur.execute("select name from patients where lr_ref = ?", (l.en21.get()))
        rows = cur.fetchall()
         
        try :
            
            if rows ==  []:
                
                l.en51.delete(0,l.END)
                cur.close()
                raise ValueError
        
            else :
        
                cur.execute("delete from patients where lr_ref = ?" , (l.en21.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Deleted Sucsessfully!")
                
        except :
            
          messagebox.showwarning("Warning", "This reference is not correct")         

        l.en21.delete(0,l.END)                         


# ------------------------------------------------------------------- 

def pat_search():

    if l.en21.get() == "" :

        messagebox.showwarning("Warning","Enter a refrence first")
        
    else :
        
        connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        
        try:

            cur.execute("select name from patients where lr_ref = ?", (l.en21.get()))
            rows = cur.fetchall()
            
            if rows == [] :
                
                l.en21.delete(0,l.END)                                      
                cur.close()
                raise ValueError
            
            else :
                
                    l.en11.delete(0,l.END)
                    for row in rows:
                        l.en11.insert(l.END,row[0])
                        
                    cur.execute("select age from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en12.delete(0,l.END)
                    for row in rows:
                        l.en12.insert(l.END,row[0])
                        
                    cur.execute("select sex from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en13.delete(0,l.END)
                    for row in rows:
                        l.en13.insert(l.END,row[0])
                        
                    cur.execute("select rc_date from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en14.delete(0,l.END)
                    for row in rows:
                        l.en14.insert(l.END,row[0]) 
                        
                    cur.execute("select rp_date from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en15.delete(0,l.END)
                    for row in rows:
                        l.en15.insert(l.END,row[0])  
                        
                    cur.execute("select lr_ref from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en16.delete(0,l.END)
                    for row in rows:
                        l.en16.insert(l.END,row[0])  
                        
                    cur.execute("select pre_ref from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en17.delete(0,l.END)
                    for row in rows:
                        l.en17.insert(l.END,row[0])  
                        
                    cur.execute("select s_name from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en18.delete(0,l.END)
                    for row in rows:
                        l.en18.insert(l.END,row[0]) 
                        
                    cur.execute("select shareeha from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en19.delete(0,l.END)
                    for row in rows:
                        l.en19.insert(l.END,row[0]) 
                        
                    cur.execute("select code from patients where lr_ref = ?", (l.en21.get()))
                    rows = cur.fetchall()
                    
                    l.en110.delete(0,l.END)
                    for row in rows:
                        l.en110.insert(l.END,row[0])  
                        
            cur.commit()                                       
            cur.close()                                     

        except:
            messagebox.showwarning("Warning", "The reference you search about is not correct")
            
    l.en21.delete(0,l.END)         


# ---------------------------------------------------------------------   


def update_patient():   

    if l.en21.get() == "" :

        messagebox.showwarning("Warning","Enter a refrence first")
        l.en21.delete(0,l.END) 
        
    else :
        
        pat_search()
        
        connection_string = f"""Driver={{SQL Server}};
                Server={"DESKTOP-CN9E67A"};
                Database={"lab"};
                Trusted_connection=yes;
                UID={"DESKTOP-CN9E67A"};
                PWD={"ahmed2003"}"""
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor() 
        
        cur.execute("select lr_ref from patients where lr_ref = ?", (l.en16.get()))
        rows = cur.fetchall()
            
        l.en21.delete(0,l.END)
        for row in rows:
            l.en21.insert(l.END,row[0])
            
        cur.commit()                                       
        cur.close() 
        
        def update() :
           
            try :
           
                connection_string = f"""Driver={{SQL Server}};
                Server={"DESKTOP-CN9E67A"};
                Database={"lab"};
                Trusted_connection=yes;
                UID={"DESKTOP-CN9E67A"};
                PWD={"ahmed2003"}"""
                conn = pyodbc.connect(connection_string)
                cur = conn.cursor() 
           
                if l.en11.get()!="" and l.en12.get()!="" and l.en13.get()!="" and l.en14.get()!="" and l.en15.get()!="" and l.en16.get()!="" and l.en18.get()!="" and l.en19.get()!="" and l.en110.get()!="":
                    cur = conn.cursor()
                    cur.execute("UPDATE patients SET name = ? , age = ? , sex =? , rc_date = ? , rp_date = ? , lr_ref = ? , pre_ref = ? , s_name = ? , shareeha = ? , code = ?  WHERE lr_ref =?"
                    ,(l.en11.get()
                      ,l.en12.get()
                      ,l.en13.get()
                      ,l.en14.get()
                      ,l.en15.get()
                      ,l.en16.get()
                      ,l.en17.get()
                      ,l.en18.get()
                      ,l.en19.get()
                      ,l.en110.get()
                      ,l.en21.get()))
                    conn.commit()
                    conn.close()
                    btn_update_patients.destroy()
                    l.en21.delete(0,l.END)
                    messagebox.showinfo("Info","Updated Sucsessfully!")
                    clear()

                else:
                    messagebox.showwarning("Warning","Data is not complete.")                                        
                    cur.close()   

            except:
                messagebox.showwarning("Warning", "Check the reference you write again and maybe the reference that you update is already exist or the code that you updated is not correct")
                btn_update_patients.destroy()
                l.en21.delete(0,l.END)         
                clear() 
                
                
        btn_update_patients = l.Button(l.fr1
        ,text="Update"
        ,bd=2
        ,bg="#3CA59F"
        ,fg="white"
        ,font=("tajawal",11,"bold")
        ,width=31
        ,command=update)
        btn_update_patients.place(x=50,y=475) 
        
        
# ----------------------------------------------------------------------


def read_csv() :
    
    csv_file = r"D:\OneDrive\Desktop\My work\Lab-Project\patients data\patients_data.csv"
    
    pro = l.Tk()
    pro.geometry("840x645+200+40")
    pro.title("Screen Lab")
    pro.config(background="white")
    pro.resizable(False,False)
    pro.iconbitmap(r"D:\OneDrive\Desktop\My work\Lab-Project\icon3.ico")
    ti1 = l.Label(pro
    ,text="All Patients"
    ,bg="#0F6A65"
    ,font=("tajawal",14,"bold")
    ,fg="white")
    ti1.pack(fill=l.X) 
    
    fr = l.Frame(pro
    ,bg="White"
    ,height=622
    ,width=900)
    fr.place(x=0,y=30)
    
    scroll_y = l.Scrollbar(fr
    ,orient=l.VERTICAL)
    scroll_x = l.Scrollbar(fr
    ,orient=l.HORIZONTAL)

    textarea = l.Text(fr
    ,width=103
    ,height=37
    ,yscrollcommand=scroll_y.set
    ,xscrollcommand=scroll_x.set)
    scroll_y.pack(side=l.LEFT , fill=l.Y)
    scroll_x.pack(side=l.BOTTOM , fill=l.X)
    scroll_y.config(command=textarea.yview)
    scroll_x.config(command=textarea.xview)
    textarea.pack(fill=l.BOTH,expand=1)    

    with open(csv_file, mode='r',encoding="utf-8") as file:
        csvFile = csv.reader(file,delimiter=',')
        
        i = 0
        
        for lines in csvFile:
            
            for line in lines:
                
                textarea.insert(l.END,f"{line}  ") 
                
            if i % 9 == 0 :
                
               textarea.insert(l.END,"\n")       
                       
        
        
# --------------------------------------------------------------------- 


def csv_pat_all():
    
    csv_file = r"D:\OneDrive\Desktop\My work\Lab-Project\patients data\patients_data.csv"
    
    with open(csv_file, "w") as file:
    
        file.truncate()
        
    
    connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
    conn = pyodbc.connect(connection_string)
    cur = conn.cursor() 
    
    cur.execute("select* from patients")
    rows = cur.fetchall()
        
    with open(csv_file, 'w', encoding='UTF-8') as file:
            
            for row in rows :
                writer = csv.writer(file)
                writer.writerow(row)
                
    read_csv()    

# -------------------------------------------------------------------


def csv_pat_code():
    
    
    csv_file = r"D:\OneDrive\Desktop\My work\Lab-Project\patients data\patients_data.csv"
    
    with open(csv_file, "w") as file:
    
        file.truncate()
        
    
    connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
    conn = pyodbc.connect(connection_string)
    cur = conn.cursor() 
    
    cur.execute("select* from patients where code = ?" , l.en62.get())
    rows = cur.fetchall()
        
    with open(csv_file, 'w', encoding='UTF-8') as textfile:
            
            for row in rows :
                writer = csv.writer(textfile)
                writer.writerow(row)
                
                
    l.en62.delete(0,l.END)
    
    read_csv()

# ----------------------------------------------------------------------                                                                                                               