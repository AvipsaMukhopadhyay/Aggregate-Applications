from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root = Tk()
root.geometry("600x500")
root.minsize(600,500)
root.title("Applications Aggregate")

def newfile():
    newroot = Tk()
    newroot.geometry("600x500")
    newroot.minsize(600,500)
    mymen = Menu(newroot)
    m1 = Menu(mymen,tearoff=0)

    m1.add_command(label="new file",command=newfile)
    m1.add_separator()
    m1.add_command(label="exit",command=quit)
    mymen.add_cascade(label="file",menu=m1)
    newroot.config(menu=mymen)


    m3 = Menu(mymen,tearoff=0)
    m3.add_command(label="Help",command=helpm)
    mymen.add_cascade(label = "Help",menu=m3)
    newroot.config(menu=mymen)



    Label(newroot,text = "GO AS YOU LIKE",font=("CHARLESWORTH",19,"bold")).pack()
    Label(newroot,text = "Welcome to go as you  like, choose what application you want to work, we have a list of these. Enjoy Your Work").pack(pady=50)
    b1 = Button(newroot,text="Calculator",command=calc)
    b1.pack(pady=20)
    b2 = Button(newroot,text="Notepad",command=notpd)
    b2.pack(pady=20)

    
    newroot.mainloop()


        
def helpm():
    a = tmsg.showinfo("About","This is an application consisting of simple but scattered apps in phone")


def rate():
    a = tmsg.askquestion("Rate us","was your experience good?")
    if a == "yes":
        tmsg.showinfo("experience","Thanks rate us on playstore please")
    else:
       val = tmsg.askokcancel("experience","We are sorry please tell us what's wrong")
       print(val)
       if val:
           typerate()
def typerate():
    nwroot = Tk()
    nwroot.geometry("600x500")
    nwroot.minsize(600,500)
    def storeval():
        Label(nwroot,text="Your Response is Submitted. Thanks for feedback.").grid(row=5,column=6)
        Button(nwroot,text="ok",command=nwroot.destroy).grid(row=6,column=6)
    ev=Label(nwroot,text="Please tell about your exprience in details")
    ev.grid()
    evals = StringVar()
    ementry = Entry(nwroot,textvariable = evals)
    ementry.grid(row=2,column=6)
    Button(nwroot,text="Submit",command=storeval).grid(row=3,column=6)
    nwroot.mainloop()

def calc():
    nroot= Tk()
    def click(event):
        text = event.widget.cget("text")
        if text=="=":
            try:
                val = eval(scr.get())
                sc.set(val)
                scr.delete(0,END)
                scr.insert(END,str(val))
            except:
                sc.set("error")
        elif text=="C":
            sc.set("")
            scr.delete(0,END)
        else:
            sc.set(sc.get()+text)
            scr.delete(0,END)
            scr.insert(END,sc.get())
    nroot.geometry("300x400")
    nroot.maxsize(300,400)
    nroot.minsize(300,400)
    nroot.title("Calculator by avi")
    sc = StringVar()
    sc.set("")
    scr = Entry(nroot,text=sc,font=("CHARLESWORTH",19,"bold"))
    scr.pack(fill="x",ipadx=16,ipady=20,pady=10,padx=10)
    f = Frame(nroot,bg="white")
    f.pack()
    b=Button(f,text="7",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b.pack(side="left",padx=1,pady=1)
    b.bind("<Button-1>",click)
    b1=Button(f,text="8",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b1.pack(side="left",padx=1,pady=1)
    b1.bind("<Button-1>",click)
    b2=Button(f,text="9",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b2.pack(side="left",padx=1,pady=1)
    b2.bind("<Button-1>",click)
    b3=Button(f,text="/",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b3.pack(side="left",padx=1,pady=1)
    b3.bind("<Button-1>",click)
    b4=Button(f,text="C",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b4.pack(side="left",padx=1,pady=1)
    b4.bind("<Button-1>",click)
    f = Frame(nroot,bg="white")
    f.pack()
    b=Button(f,text="6",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b.pack(side="left",padx=2,pady=1)
    b.bind("<Button-1>",click)
    b1=Button(f,text="5",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b1.pack(side="left",padx=2,pady=1)
    b1.bind("<Button-1>",click)
    b2=Button(f,text="4",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b2.pack(side="left",padx=2,pady=1)
    b2.bind("<Button-1>",click)
    b3=Button(f,text="*",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b3.pack(side="left",padx=2,pady=1)
    b3.bind("<Button-1>",click)
    b4=Button(f,text="(",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b4.pack(side="left",padx=2,pady=1)
    b4.bind("<Button-1>",click)
    f = Frame(nroot,bg="white")
    f.pack()
    b=Button(f,text="1",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b.pack(side="left",padx=2,pady=1)
    b.bind("<Button-1>",click)
    b1=Button(f,text="2",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b1.pack(side="left",padx=2,pady=1)
    b1.bind("<Button-1>",click)
    b2=Button(f,text="3",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b2.pack(side="left",padx=2,pady=1)
    b2.bind("<Button-1>",click)
    b3=Button(f,text="-",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b3.pack(side="left",padx=2,pady=1)
    b3.bind("<Button-1>",click)
    b4=Button(f,text=")",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b4.pack(side="left",padx=2,pady=1)
    b4.bind("<Button-1>",click)
    f = Frame(nroot,bg="white")
    f.pack()
    b=Button(f,text="0",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b.pack(side="left",padx=1,pady=1)
    b.bind("<Button-1>",click)
    b1=Button(f,text="00",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b1.pack(side="left",padx=1,pady=1)
    b1.bind("<Button-1>",click)
    b2=Button(f,text=".",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b2.pack(side="left",padx=1,pady=1)
    b2.bind("<Button-1>",click)
    b3=Button(f,text="+",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b3.pack(side="left",padx=1,pady=1)
    b3.bind("<Button-1>",click)
    b4=Button(f,text="=",font=("CHARLESWORTH",19,"bold"),padx=10,pady=5)
    b4.pack(side="left",padx=1,pady=1)
    b4.bind("<Button-1>",click)

    
    nroot.mainloop()
def notpd():
    def save():
        global file
        file = None
        if file == None:
            file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt", filetypes=[("All files","*.*"),("Text Documents","*.txt")])
            if file == "":
                file = None
            else:
                f=open(file,"w")
                f.write(t.get(1.0,END))
                f.close()
                rootnew.title(os.path.basename(file)+ "-notepad")
                print("file saved")
        else:
            f=open(file,"w")
            f.write(t.get(1.0,END))
            f.close()
    def nfm():
        neroot = Tk()
        neroot.geometry("500x500")
        neroot.title("Untitled")
        t = Text(neroot,font=("CHARLESWORTH",13))
        file = None
        t.pack(expand = True,fill=BOTH)
        mm = Menu(neroot)
    
        m = Menu(mm,tearoff=0)
        m.add_command(label="new file",command=nfm)
        m.add_command(label="open",command=openf)
        m.add_command(label="save",command=save)
        m.add_separator()
        m.add_command(label="exit",command=neroot.destroy)
        mm.add_cascade(label="file",menu=m)
        neroot.config(menu=mm)

        m1 = Menu(mm,tearoff=0)
        m1.add_command(label="copy",command=copym)
        m1.add_command(label="paste",command=pastem)
        m1.add_command(label="cut",command=cutm)
        mm.add_cascade(label="edit",menu=m1)
        neroot.config(menu=mm)

        m2 = Menu(mm,tearoff=0)
        m2.add_command(label="about",command=aboutm)
        mm.add_cascade(label="Help",menu=m2)
        neroot.config(menu=mm)
    
        Scr = Scrollbar(t)
        Scr.pack(side = RIGHT,fill= Y)
        Scr.config(command=t.yview)
        t.config(yscrollcommand=Scr.set)
    
        neroot.mainloop()
    def copym():
        t.event_generate("<<Copy>>")
    def cutm():
        t.event_generate("<<Cut>>")

    def aboutm():
        tmsg.showinfo("Notepad","Notepad : Write your heart. always learning. Notepad by avi")
    def pastem():
        t.event_generate("<<Paste>>")
    def openf():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file = None
        else:
            rootnew.title(os.path.basename(file))
            t.delete(1.0,END)
            f=open(file,"r")
            t.insert(1.0,f.read())
            f.close()
    rootnew = Tk()
    rootnew.geometry("500x500")
    rootnew.title("Untitled")
    t = Text(rootnew,font=("CHARLESWORTH",13))
    file = None
    t.pack(expand = True,fill=BOTH)
    mm = Menu(rootnew)
    
    m = Menu(mm,tearoff=0)
    m.add_command(label="new file",command=nfm)
    m.add_command(label="open",command=openf)
    m.add_command(label="save",command=save)
    m.add_separator()
    m.add_command(label="exit",command=rootnew.destroy)
    mm.add_cascade(label="file",menu=m)
    rootnew.config(menu=mm)

    m1 = Menu(mm,tearoff=0)
    m1.add_command(label="copy",command=copym)
    m1.add_command(label="paste",command=pastem)
    m1.add_command(label="cut",command=cutm)
    mm.add_cascade(label="edit",menu=m1)
    rootnew.config(menu=mm)

    m2 = Menu(mm,tearoff=0)
    m2.add_command(label="about",command=aboutm)
    mm.add_cascade(label="Help",menu=m2)
    rootnew.config(menu=mm)
    
    Scr = Scrollbar(t)
    Scr.pack(side = RIGHT,fill= Y)
    Scr.config(command=t.yview)
    t.config(yscrollcommand=Scr.set)
    
    rootnew.mainloop()

def cons():
    rootn = Tk()
    rootn.geometry("300x300")
    rootn.title("contact saver")

    def savec():
        def storval():
            n = namev.get()
            p = phentry.get()
            e = ementry.get()
            contact_info = f"{n}\t{p}\t{e}\n"
            try:
                with open("contacts.txt", "a") as f:
                    f.write(contact_info)
            except:
                pass
            Label(rooth,text="Contact Saved").grid(row=11,column=6,pady=10)
            Button(rooth,text="OK",command=rooth.destroy).grid(row=12,column=6,pady=10)
        
        rooth = Tk()
        rooth.geometry("450x500")
        Label(rooth,text="Save contact",font=("CHARLESWORTH",19,"bold"),pady=15).grid(row=0,column=6)
        Label(rooth,text="Contact Name").grid(row=1,column=1,pady=20,ipady=5,ipadx=10)
        nm=StringVar()
        namev = Entry(rooth,textvariable=nm)
        namev.grid(row=1,column=7)
        Label(rooth,text="Phone Number").grid(row=4,column=1,pady=20,ipady=5,ipadx=10)
        phval = StringVar()
        phentry = Entry(rooth,textvariable=phval)
        phentry.grid(row=4,column=7)
        Label(rooth,text="E-mail ID").grid(row=7,column=1,pady=20,ipady=5,ipadx=10)
        emval= StringVar()
        ementry = Entry(rooth,textvariable = emval)
        ementry.grid(row=7,column=7)
        Button(rooth,text="Save",command=storval).grid(row=9,column=6,pady=20,ipady=5,ipadx=10)

        rooth.mainloop()
    
    def seec():
        rooths = Tk()
        rooths.geometry("500x500")
        try:
            with open("contacts.txt","r") as f:
                a=f.read()
        except:
            pass
        Label(rooths,text=a).pack()
        rooths.mainloop()

    def delc():
        rooth = Tk()
        rooth.geometry("500x500")
        def delete():
            try:
                with open("contacts.txt", "r") as f, open("cons.txt", "w") as fl:
                    contacts = f.readlines()
                    for line in contacts:
                        data = line.split()
                        if data and nmv.get() != data[0]:
                            fl.write(line)
            except Exception:
                pass
            os.remove("contacts.txt")
            os.rename("cons.txt", "contacts.txt")
            rooth.destroy()
            seec()
        Label(rooth,text="Delete contact",font=("CHARLESWORTH",19,"bold")).grid(row = 1, column = 6)
        Label(rooth,text="Name").grid(row = 3, column = 2)
        nm = StringVar()
        nmv = Entry(rooth,textvariable=nm)
        Button(rooth, text="Delete", command=delete).grid(row=5, column=6)
        nmv.grid(row=3,column=7)
        
        

        

        rooth.mainloop()
    Label(rootn,text="Contacts",font=("CHARLESWORTH",19,"bold")).pack(pady=20)
    Button(rootn,text="Save a new contact",command=savec).pack(pady = 20)
    Button(rootn,text="See contactlist",command=seec).pack(pady=20)
    Button(rootn,text="Delete a contact",command=delc).pack(pady=20)
    rootn.mainloop()
mymen = Menu(root)
m1 = Menu(mymen,tearoff=0)
m1.add_command(label="new",command=newfile)
m1.add_separator()
m1.add_command(label="exit",command=root.destroy)
mymen.add_cascade(label="file",menu=m1)
root.config(menu=mymen)


m3 = Menu(mymen,tearoff=0)
m3.add_command(label="About",command=helpm)
m3.add_command(label="Rate us",command=rate)
mymen.add_cascade(label="Help",menu=m3)
root.config(menu=mymen)


Label(text = "GO AS YOU LIKE",font=("CHARLESWORTH",19,"bold")).pack()
Label(text = "Welcome to go as you  like, choose what application you want to work, we have a list of these. Enjoy Your Work").pack(pady=50)
b1 = Button(text="Calculator",command=calc)
b1.pack(pady=20)
b2 = Button(text="Notepad",command=notpd)
b2.pack(pady=20)
b3 = Button(text="contact saver",command=cons)
b3.pack(pady=20)
root.mainloop()
