import lab as l 
from tkinter import messagebox , ttk
import pyodbc


# ---------------------------------------------------------------------


def add_diagnosis():

    connection_string = f"""Driver={{SQL Server}};
    Server={"DESKTOP-CN9E67A"};
    Database={"lab"};
    Trusted_connection=yes;
    UID={"DESKTOP-CN9E67A"};
    PWD={"ahmed2003"}"""
    
    try :

        if l.textarea1.get("1.0",l.END)!="" and l.textarea2.get("1.0",l.END)!="" and l.textarea3.get("1.0",l.END)!="" and l.textarea4.get("1.0",l.END)!="" and l.en31.get()!="":
            conn = pyodbc.connect(connection_string)
            cur = conn.cursor()
            cur.execute("insert into diagnosis values (?,?,?,?,?)"
                    ,(l.textarea1.get("1.0",l.END)
                 ,l.textarea2.get("1.0",l.END)
                 ,l.textarea3.get("1.0",l.END)
                 ,l.textarea4.get("1.0",l.END)
                ,l.en31.get()))
      
            conn.commit()
            conn.close()

        else:
            messagebox.showwarning("Warning","Data is not complete.")
    
    except :
        
        messagebox.showwarning("Warning" , "This code is already exist")    
        
def clear():

    l.textarea1.delete("1.0",l.END)
    l.textarea2.delete("1.0",l.END)
    l.textarea3.delete("1.0",l.END)
    l.textarea4.delete("1.0",l.END)
    l.en31.delete(0,l.END)
    
    
# ----------------------------------------------------------------------    
    

def delete_dia():

    if l.en51.get() == "" :

        messagebox.showwarning("Warning","Enter a code first")

    else:    

        connection_string = f"""Driver={{SQL Server}};
        Server={"DESKTOP-CN9E67A"};
        Database={"lab"};
        Trusted_connection=yes;
        UID={"DESKTOP-CN9E67A"};
        PWD={"ahmed2003"}"""
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        
        cur.execute("select gross from diagnosis where code = ?", (l.en51.get()))
        rows = cur.fetchall()
         
        try :
            
            if rows ==  []:
                
                l.en51.delete(0,l.END)
                cur.close()
                raise ValueError
        
            else :
        
                cur.execute("delete from diagnosis where code = ?" , (l.en51.get()))
        
            x = messagebox.askyesno("warning","You will delete all patients who have that diagnosis , are you sure ?")
            if x ==True:
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Deleted Sucsessfully!")
                
            else:
                
                cur.close()    
                
        except :
            
          messagebox.showwarning("Warning", "This code is not correct")          

       
    l.en51.delete(0,l.END)        
            
# ---------------------------------------------------------------------


def dia_search():


    if l.en51.get() == "" :

        messagebox.showwarning("Warning","Enter a code first")
        
    else :
        
        try:

            connection_string = f"""Driver={{SQL Server}};
            Server={"DESKTOP-CN9E67A"};
            Database={"lab"};
            Trusted_connection=yes;
            UID={"DESKTOP-CN9E67A"};
            PWD={"ahmed2003"}"""
            conn = pyodbc.connect(connection_string)
            cur = conn.cursor()
            
            cur.execute("select gross from diagnosis where code = ?", (l.en51.get()))
            rows = cur.fetchall()
            
            if rows ==  []:
                
                l.en51.delete(0,l.END)                                      
                cur.close()
                raise ValueError
            
            else :
                
                    l.textarea1.delete("1.0",l.END)
                    for row in rows:
                        l.textarea1.insert(l.END,row[0])           

                    cur.execute("select microscope from diagnosis where code = ?", (l.en51.get()))
                    rows = cur.fetchall()
                    
                    l.textarea2.delete("1.0",l.END)
                    for row in rows:
                        l.textarea2.insert(l.END,row[0])

                    cur.execute("select conclusion from diagnosis where code = ?", (l.en51.get()))
                    rows = cur.fetchall()
            
                    l.textarea3.delete("1.0",l.END)
                    for row in rows:
                        l.textarea3.insert(l.END,row[0])

                    cur.execute("select nature from diagnosis where code = ?", (l.en51.get()))
                    rows = cur.fetchall()
            
                    l.textarea4.delete("1.0",l.END)
                    for row in rows:
                        l.textarea4.insert(l.END,row[0])

                    cur.execute("select code from diagnosis where code = ?", (l.en51.get()))
                    rows = cur.fetchall()
            
                    l.en31.delete(0,l.END)
                    for row in rows:
                        l.en31.insert(l.END,row[0])  
            cur.commit()                                       
            cur.close()

        except:
            messagebox.showwarning("Warning", "The code you search about is not correct")
            
    l.en51.delete(0,l.END)        
    
    
# -------------------------------------------------------------------



def update_dia():

    if l.en51.get() == "" :

        messagebox.showwarning("Warning","Enter a code first")  
        
    else :
        
        dia_search()
        
        connection_string = f"""Driver={{SQL Server}};
                Server={"DESKTOP-CN9E67A"};
                Database={"lab"};
                Trusted_connection=yes;
                UID={"DESKTOP-CN9E67A"};
                PWD={"ahmed2003"}"""
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor() 
        
        cur.execute("select code from diagnosis where code = ?", (l.en31.get()))
        rows = cur.fetchall()
            
        l.en51.delete(0,l.END)
        for row in rows:
            l.en51.insert(l.END,row[0])
            
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
           
                if l.textarea1.get("1.0",l.END)!="" and l.textarea2.get("1.0",l.END)!="" and l.textarea3.get("1.0",l.END)!="" and l.textarea4.get("1.0",l.END)!="" and l.en31.get()!="":
                    cur = conn.cursor()
                    cur.execute("UPDATE diagnosis SET gross = ? , microscope = ? , conclusion =? ,nature = ? , code =? WHERE code =?"
                    ,(l.textarea1.get("1.0",l.END)
                    ,l.textarea2.get("1.0",l.END)
                    ,l.textarea3.get("1.0",l.END)
                    ,l.textarea4.get("1.0",l.END)
                    ,l.en31.get()
                    ,l.en51.get()))
                    conn.commit()
                    conn.close()
                    btn_up_diagonsis.destroy()
                    l.en51.delete(0,l.END)
                    messagebox.showinfo("Info","Updated Sucsessfully!")
                    clear()

                else:
                    messagebox.showwarning("Warning","Data is not complete.")                                        
                    cur.close()   

            except:
                messagebox.showwarning("Warning", "Check the code you write again and maybe the code that you update is already exist")
                btn_up_diagonsis.destroy()
                l.en51.delete(0,l.END)         
                clear()        
                
        btn_up_diagonsis = l.Button(l.fr3
            ,text="Update"
            ,bd=2
            ,bg="#3CA59F"
            ,fg="white"
            ,font=("tajawal",11,"bold")
            ,width=15
            ,command=update)
        btn_up_diagonsis.place(x=115,y=620) 
        
        
# -------------------------------------------------------------


def pro_dia_all():

    pro = l.Tk()
    pro.geometry("300x300+600+150")
    pro.title("Screen Lab")
    pro.config(background="white")
    pro.resizable(False,False)
    pro.iconbitmap(r"D:\OneDrive\Desktop\My work\Lab-Project\icon3.ico")
    ti1 = l.Label(pro
    ,text="All Codes"
    ,bg="#0F6A65"
    ,font=("tajawal",14,"bold")
    ,fg="white")
    ti1.pack(fill=l.X)

    scroll_y=l.Scrollbar(pro
    ,orient=l.VERTICAL)

    patient_table = ttk.Treeview(pro
    ,columns=("Code")
    ,yscrollcommand=scroll_y.set)
            
    scroll_y.pack(fill=l.Y,side=l.LEFT)
    scroll_y.config(command=patient_table.yview)
    patient_table.place(x=18,y=29,width=283,height=270)
    
    patient_table["show"]="headings"
    patient_table.heading("Code",text="Code")

    patient_table.column("Code",width=100)


    connection_string = f"""Driver={{SQL Server}};
                Server={"DESKTOP-CN9E67A"};
                Database={"lab"};
                Trusted_connection=yes;
                UID={"DESKTOP-CN9E67A"};
                PWD={"ahmed2003"}"""
    conn = pyodbc.connect(connection_string)
    cur = conn.cursor() 

    cur.execute("select code from diagnosis")
    rows = cur.fetchall()

    if rows !=0 :
        patient_table.delete(*patient_table.get_children())
        
        for row in rows :
        
            patient_table.insert("",l.END,value=row[0])
            
        conn.commit()
        conn.close()

# ---------------------------------------------------------------                              