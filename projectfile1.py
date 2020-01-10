from Tkinter import *
root=Tk()
root.geometry('700x400')
Label(root,text='Project',font=('Chela One',25),fg='Purple').grid(row=1,column=0)
Label(root,text='Project Name :: PHONEBOOK',font=('Chela One',22),fg='Purple').grid(row=2,column=1)
Label(root,text='My First Project',font=('Chela One',20),fg='Purple').grid(row=3,column=1)
Label(root,text='Manasvi Soni 181b119',font=('Chela One',20),fg='Purple').grid(row=4,column=1)

def close(e=1):
      root.destroy()
      
      
      
    
      
root.bind('<Motion>',close)
root.mainloop()
