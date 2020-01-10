from Tkinter import *
from projectfile1 import * 
import sqlite3

con=sqlite3.Connection("PHONEBOOK")
cur=con.cursor()
cur.execute("create table if not exists details1(contact_id INTEGER primary key AUTOINCREMENT,First_name varchar(20),Middle_name varchar(30),Last_name varchar(20),company varchar(20),address varchar(20),city varchar(20),pin number(10),website_url varchar(30),birth_date date)")
cur.execute("create table if not exists phone(contact_id INTEGER,contact_type varchar(20),phone_number number(10), FOREIGN KEY(contact_id) REFERENCES details1(contact_id))")
cur.execute("create table if not exists email(contact_id INTEGER,emailid_type varchar(20),email_id varchar(20),FOREIGN KEY(contact_id) REFERENCES details1(contact_id))")

root1=Tk()
root1.geometry('750x900')
img=PhotoImage(file='phone-number-icon-5.gif')
Label(root1,image=img).grid(row=0,column=2)
Label(root1,text='First Name',font=('Chela One',12)).grid(row=6,column=1)
e1=Entry(root1)
e1.grid(row=6,column=2)
Label(root1,text='Middle Name',font=('Chela One',12)).grid(row=7,column=1)
e2=Entry(root1)
e2.grid(row=7,column=2)
Label(root1,text='Last Name',font=('Chela One',12)).grid(row=8,column=1)
e3=Entry(root1)
e3.grid(row=8,column=2)
Label(root1,text='Company Name',font=('Chela One',12)).grid(row=9,column=1)
e4=Entry(root1)
e4.grid(row=9,column=2)
Label(root1,text='Address',font=('Chela One',12)).grid(row=10,column=1)
e5=Entry(root1)
e5.grid(row=10,column=2)
Label(root1,text='City',font=('Chela One',12)).grid(row=11,column=1)
e6=Entry(root1)
e6.grid(row=11,column=2)
Label(root1,text='Pincode',font=('Chela One',12)).grid(row=12,column=1)
e7=Entry(root1)
e7.grid(row=12,column=2)
Label(root1,text='Website URL',font=('Chela One',12)).grid(row=13,column=1)
e8=Entry(root1)
e8.grid(row=13,column=2)
Label(root1,text='Date of Birth',font=('Chela One',12)).grid(row=14,column=1)
e9=Entry(root1)
e9.grid(row=14,column=2)

#radiobuttons
Label(root1,text='Select PHONE Type',font=('Chela One',12),fg='Purple').grid(row=15,column=1)
v1=IntVar()
r=Radiobutton(root1,text='Office',variable=v1,value=1).grid(row=16,column=1)
r1=Radiobutton(root1,text='Home',variable=v1,value=2).grid(row=16,column=2)
r2=Radiobutton(root1,text='Mobile',variable=v1,value=3).grid(row=16,column=3)
Label(root1,text='Phone Number',font=('Chela One',15),fg='Purple').grid(row=19,column=1)
e10=Entry(root1)
e10.grid(row=20,column=2)
Label(root1,text='Select Email Type',font=('Chela One',15),fg='Purple').grid(row=21,column=1)
v2=IntVar()
r3=Radiobutton(root1,text='Office',variable=v2,value=1).grid(row=22,column=1)
r4=Radiobutton(root1,text='Personal',variable=v2,value=2).grid(row=22,column=2)
Label(root1,text='Email Id',font=('Chela One',12)).grid(row=23,column=1)
e11=Entry(root1)
e11.grid(row=24,column=2)

def save():
    cur.execute("insert into details1(first_name,Middle_name,last_name,company,address,city,pin,website_url,birth_date) values(?,?,?,?,?,?,?,?,?)",(str(e1.get()),str(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),str(e6.get()),str(e7.get()),str(e8.get()),str(e9.get())))
    cur.execute("insert into phone(contact_id,contact_type,phone_number) values((select max(contact_id) from details1),?,?)",(str(v1.get()),str(e10.get())))
    cur.execute("insert into email(contact_id,emailid_type,email_id) values((select max(contact_id) from details1),?,?)",(str(v2.get()),str(e11.get())))
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    con.commit()
    
def search():
    root2=Tk()
    Label(root2,text='Searching',font=('Chela One',17),fg='Purple').grid(row=1,column=1)
    Label(root2,text='Enter the name',font=('Arial',18)).grid(row=2,column=1)
    e=Entry(root2,width=60)
    e.grid(row=2,column=2)
    cur.execute("select first_name,Middle_name,last_name from details1 order by first_name asc,last_name asc")
    fetch_data1=cur.fetchall()
    lb1=Listbox(root2,width=60,height=20)
    lb1.grid(row=3,column=2)
    def close1():
        root2.destroy()
    Button(root2,text='close1',command=close1).grid(row=4,column=2)

    for info1 in fetch_data1:
        lb1.insert(END,info1)
    
    def retrive(r=1):
        lb3=Listbox(root2,width=60,height=20)
        lb3.grid(row=3,column=2)
        cur.execute("select first_name,last_name from details1 where first_name like(?) or last_name like(?)",('%'+str(e.get())+'%','%'+str(e.get())+'%'))
        fetch6=cur.fetchall()
        for j4 in fetch6:
            lb3.insert(END,j4)
        def retrive1(r=1):
            lb2=Listbox(root2,width=60,height=20)
            lb2.grid(row=3,column=2)
            item=lb3.curselection()
            for j in item:
                text=lb3.get(j)
                
            cur.execute("select contact_id from details1 where first_name=?",(str(text[0]),))
            fetch2=cur.fetchall()
            
            cur.execute("select first_name from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch3=cur.fetchall()

            for j1 in fetch3:
                lb2.insert(END,"First name : "+str(j1[0]))
            cur.execute("select Middle_name from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch5=cur.fetchall()
            
            for j5 in fetch5:
                lb2.insert(END,"Middle name "+str(j5[0]))
            cur.execute("select last_name from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch6=cur.fetchall()
            
            for j6 in fetch6:
                lb2.insert(END,"Last name : "+str(j6[0]))
            cur.execute("select company from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch7=cur.fetchall()
            
            for j7 in fetch7:
                lb2.insert(END,"Company : "+str(j7[0]))

            cur.execute("select address from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch8=cur.fetchall()
            for j8 in fetch8:
                lb2.insert(END,"Address : "+str(j8[0]))    

            cur.execute("select city from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch9=cur.fetchall()
            for j9 in fetch9:
                lb2.insert(END,"City : "+str(j9[0]))
            
            cur.execute("select pin from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch11=cur.fetchall()
            for j11 in fetch11:
                lb2.insert(END,"Pin : "+str(j11[0]))

            cur.execute("select website_url from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch12=cur.fetchall()
            for j12 in fetch12:
                lb2.insert(END,"Website_url : "+str(j12[0]))

            cur.execute("select birth_date from details1 where contact_id=?",(str(fetch2[0][0]),))
            fetch13=cur.fetchall()
            for j13 in fetch13:
                lb2.insert(END,"Birth_date : "+str(j13[0]))

            cur.execute("select contact_type from phone where contact_id=?",(str(fetch2[0][0]),))
            fetch14=cur.fetchall()
            for j14 in fetch14:
                lb2.insert(END,"Contact_type : "+str(j14[0]))

            cur.execute("select phone_number from phone where contact_id=?",(str(fetch2[0][0]),))
            fetch15=cur.fetchall()
            for j15 in fetch15:
                lb2.insert(END,"Phone_number : "+str(j15[0]))

            cur.execute("select emailid_type from email where contact_id=?",(str(fetch2[0][0]),))
            fetch16=cur.fetchall()
            for j16 in fetch16:
                lb2.insert(END,"Emailid_type : "+str(j16[0]))
            
            cur.execute("select email_id from email where contact_id=?",(str(fetch2[0][0]),))
            fetch17=cur.fetchall()
            for j17 in fetch17:
                lb2.insert(END,"Email_id : "+str(j17[0]))
            def delete_info():
                cur.execute("delete from details1 where contact_id=?",(str(fetch2[0][0]),))
                cur.execute("delete from phone where contact_id=?",(str(fetch2[0][0]),))
                cur.execute("delete from email where contact_id =?",(str(fetch2[0][0]),))
            Button(root2,text='delete_info',command=delete_info).grid(row=4,column=3)
            def close1():
                root2.destroy()
            Button(root2,text='close1',command=close1).grid(row=4,column=2)

            
            
        lb3.bind('<ButtonRelease-1>',retrive1)
    root2.bind('<KeyPress>',retrive)
    
    con.commit()
    root2.mainloop()
    
def close():
    root1.destroy()

#def fetch():
    #cur.execute("select * from details1 ")
    #fetch_data1=cur.fetchall()
    #lb1=Listbox(root1)
    #lb1.grid(row=12,column=8)
    #for info1 in fetch_data1:
    #   lb1.insert(END,info1)
    #con.commit()

Button(root1,text='Save',command=save).grid(row=25,column=1)
Button(root1,text='Search',command=search).grid(row=25,column=2)
Button(root1,text='Close',command=close).grid(row=25,column=3)
Button(root1,text='Edit').grid(row=25,column=4)


root1.mainloop()
#root2.mainloop()
#root.mainloop()
    
          
