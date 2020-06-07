from tkinter import *
import tkinter as tk
import datetime
import calendar
from matplotlib import pyplot as plt
import numpy as np
import csv
from PIL import ImageTk, Image
from tkinter import messagebox



##-----------------------------------------------------LOGIN--------------------------------------------------------------------------------------------------------------------
class project:

       def __init__(self):
               global fname,roll,temp,student,subject,namestd,attendancepr,attendanceth
               global diclecpweek,diclabid,dicprpweek,dicprid,th,prc,w

               
       def login(self):
               parent=Tk()
               parent.title("Login")
               img = ImageTk.PhotoImage(Image.open("mainportal.gif"))
               panel = Label(parent, image = img)
               panel.pack(side = "bottom", fill = "both", expand = "yes")

               self.v=StringVar()
               self.w=StringVar()

               #accept division
               self.acdiv=Label(parent,text = "Division",width=10,height=1,bg="white",fg="green").place(x=20,y=182)
               self.divent=Entry(parent,textvariable=self.v,width=18).place(x=92,y=182)

               #accept roll number
               self.acroll=Label(parent,text = "Roll No",height=1,width=10,bg="white",fg="green").place(x=20,y=205)
               self.rollent=Entry(parent,textvariable=self.w,width=18).place(x=92,y=205)

               #submit
               self.submit=Button(parent, text = "Submit",height=1,width=10,activeforeground = "white",activebackground = "green",command=parent.destroy).place(x=90,y=231)
        
               parent.mainloop()

               #retrive value from entry boxes
               self.roll=(self.w.get())
               
               self.temp=self.v.get()
               self.fname=self.v.get()+'.csv'
               self.temp=self.temp.upper()

#---------------------------------------------EOF----------------------------------------------------------------------------------------------------------------------------


              
##-----------------------------------------CHECK ROLL NO IS PRESENT OR NOT-----------------------------------------------------------------------------------------------------

       def checkLogin(self):
               if len(self.temp)==0 or len(self.w.get())==0:
                   return 21
               else:
                    try:
                     self.roll=int(self.roll) 
                    except ValueError:
                       return 21
                    if self.temp=='TEC' and self.roll>300 and self.roll<370:
                          return 11
                    elif self.temp=='TEB' and self.roll>200 and self.roll<275:
                        return 11
                    elif self.temp=='TEA' and self.roll>100 and self.roll<183:
                        return 11
                    else:
                       return 21
##--------------------------------------------EOF-----------------------------------------------------------------------------------------------------------------------------

##---------------------------------------------##CHECK SUBJECT##------------------------------------------------------------------------------------------------

       def checkPractical(self):
               self.practicalid=self.prc.get()+"_lab"
               self.practicalid=self.practicalid.upper()
               if self.practicalid in self.dicprid:
                   self.practicalAtd()
               else:
                    root = Tk()
                    root.geometry("0x0")
                    messagebox.showinfo("Invalid", message="Enter valid Practical name!!",icon='warning',master=root)
                    root.destroy()
       def checkSubject(self):
               self.retval=str(self.th.get())
               self.retval=self.retval.upper()
               if self.retval in self.diclabid:
                   self.theory1()
               else:
                   root = Tk()
                   root.geometry("0x0")
                   messagebox.showinfo("Invalid", message="Enter valid Subject name !!",icon='warning',master=root)
                   root.destroy()      

##------------------------------------------------##EOF##--------------------------------------------------------------------------------------------------------
        
#-----------------------------------------ALL SUBJECT ATTENDANCE-------------------------------------------------------------------

       def allSubject(self):
            with open(self.fname) as self.f:
                self.data = ([self.row for self.row in csv.reader(self.f)])
                #self.subject=(self.data[0][2:12])
                self.student=(self.data[self.roll %100][2:12])
                self.namestd=(self.data[self.roll%100][1:2])
            self.namestd=''.join(self.namestd)
            self.subject=['CN','DBMS','ISEE','SDL','SEPM','TOC','CNL','DBMSL','SDLL','TOTAL']
       def a(self,num):
           for self.x in num:
              yield self.x

       def disAllSubAtd(self):
           self.r = 0
           self.colors = ['linen','peach Puff','linen','peach Puff','linen','peach Puff','linen','peach Puff','linen','peach Puff']
           self.x1=self.a(self.subject)
           self.x2=self.a(self.student)

           parent=Tk()

           parent.title("All subject")

           for self.i,self.j,self.k in zip(self.x1,self.x2,self.colors):
                    self.l1=Label(parent,text=self.i,width=15,bg=self.k,borderwidth=2, relief="groove").grid(row=self.r,column=0)
                    self.l2=Label(parent,text=self.j,width=15,bg=self.k,borderwidth=2, relief="groove").grid(row=self.r,column=1)
                    self.r = self.r + 1
                    self.B=Button(parent, text = "Exit",height=1, width=13,command=parent.destroy,bg="lightGrey",activebackground="red",font='Helvetica 9 bold',borderwidth=3, relief="groove").grid(row=21,column=1)
           parent.mainloop()


#------------------------------------------------------EOF----------------------------------------------------------------------------------------------------------------------


           

#-------------------------------------------GRAPHICAL VIEW----------------------------------------------------------------------------------------------------------------------
       def disGraph(self): 
          for self.i in range(0, len(self.student)): 
             self.student[self.i] = float(self.student[self.i]) 
          self.y_pos = np.arange(len(self.subject))
          self.colors = ['gold', 'green', 'magenta', 'cyan','purple','red','pink','black','darkorange','silver']
          plt.bar(self.y_pos, self.student,color=self.colors,align='center', alpha=1)
          plt.xticks(self.y_pos, self.subject)
          plt.ylabel('Attendance')
          plt.title('Attendance Report')
          plt.show()
#------------------------------------------------EOF--------------------------------------------------------------------------------------------------------------------------




#---------------------------------------------DICTIONARIES--------------------------------------------------------------------------------------------------------------------

       def dicts(self): 
          self.diclecpweek={'CN':4,'DBMS':3,'ISEE':3,'SDL':2,'SEPM':3,'TOC':3}
          self.diclabid={'CN':2,'DBMS':3,'ISEE':4,'SDL':5,'SEPM':6,'TOC':7}

          self.dicprpweek={'CN_LAB':2,'DBMS_LAB':4,'SDL_LAB':4}
          self.dicprid={'CN_LAB':8,'DBMS_LAB':9,'SDL_LAB':10}
#---------------------------------------------------EOF-----------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------PRACTICAL-------------------------------------------------------------------------------------------------------------
       def practicalAtd(self):
               global today,weeks,startday,diffdate,totalpr,prattd,attdreqpr,prtoattd,practicalid,prinweek

               #print(self.prc.get())
               #self.practicalid=self.prc.get()+"_lab"
               #self.practicalid=self.practicalid.upper()
               #print(self.practicalid)
               self.getPrcRow=int(self.dicprid.get(self.practicalid))                #row in csv file
               #print(self.getPrcRow)

               self.prinweek=self.dicprpweek.get(self.practicalid)              #practical in  a week
               #print(self.prinweek)
               self.rollid=int(self.roll%100)
               with open(self.fname) as self.filep:
                       self.datap=[self.rowp for self.rowp in csv.reader(self.filep)]
                       self.attendancepr=(self.datap[self.rollid][self.getPrcRow])              #attendance of practical
                      # print(self.attendancepr)
                       
               self.today=datetime.date.today()
               self.startday= datetime.date(2019, 6, 15)
               self.diffdate=self.today-self.startday
               #print((self.diffdate.days))    total days
               self.weeks=int(self.diffdate.days/7)
               #print(int(self.weeks))     total weeks

               self.attendancepr=float(self.attendancepr)
               self.totalpr=(self.weeks*self.prinweek)   #total lecture in semester
               #print(self.totalpr)
               self.prattd=int((self.totalpr*self.attendancepr)/100)#attended leture
               if(self.attendancepr<=75.0):
                   #print("Defaulter")
                   #print(self.prattd)#attended lecture
                   self.attdreqpr=75-self.attendancepr              #attendance require to make atleast 75%
                   #print(self.attdreqpr)
                   self.prtoattd=int((self.attdreqpr*self.totalpr/100)+1)          #practical to attend
                   #print(self.prtoattd)
                   self.showprinfo()
               else:
                   self.showprinfook()

       def showprinfo(self):
               parent = Tk()
               self.head=self.prc.get()
               parent.title(self.head.upper())
               T = Text(parent, height=5, width=30,font=("arial", 15))
               T.pack()
               self.head=self.prc.get()
               showText="\tSUBJECT: "+self.head.upper()+"\nAttendance         : "+str(self.attendancepr)+"\nTotal practicals    : "+str(self.totalpr)+"\nPractical Attended: "+str(self.prattd)+"\nPractical to attend: "+str(self.prtoattd)+" Lecture"
               T.insert(END, showText,'big')
               self.exit=Button(parent,text="Exit",width=10,bg="lightGrey",activebackground="red",command=parent.destroy).pack(anchor=NE)
               parent.mainloop()
               
       def showprinfook(self):
               parent = Tk()
               self.head=self.prc.get()
               parent.title(self.head.upper())
               T = Text(parent, height=5, width=30,font=("arial", 15))
               T.pack()
               self.head=self.prc.get()
               showText="\tSUBJECT: "+self.head.upper()+"\nAttendance         : "+str(self.attendancepr)+"\nTotal practicals    : "+str(self.totalpr)+"\nPractical Attended: "+str(self.prattd)
               T.insert(END, showText,'big')
               self.exit=Button(parent,text="Exit",width=10,bg="lightGrey",activebackground="red",command=parent.destroy).pack(anchor=NE)
               parent.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

          
#-------------------------------------------------THEORY----------------------------------------------------------------------------------------------------------------------

       def theory1(self):
               global today,startday,diffdate,weeks,totalec,lecattd,attdreq,lectoattd,subRow,retval
               
               self.retval=str(self.th.get())
               self.retval=self.retval.upper()
               #print(type(self.retval))
               #print(self.retval)
               self.subRow=(self.diclabid.get(self.retval))   #lecture row in csv
               #print(type(self.subRow))
               self.subRow=int(self.subRow)
               #print(self.subRow)
               #print(type(self.subRow))
               #print (self.getSubRow)   #int
               self.getLecinWeek=self.diclecpweek.get(self.retval)  #lectures in week  
               self.rollid=int(self.roll%100)
               with open(self.fname) as self.file:
                       self.datat=[self.rowt for self.rowt in csv.reader(self.file)]
                       self.attendanceth=(self.datat[self.rollid][(self.subRow)])
                       #print(self.attendanceth)

               self.today=datetime.date.today()
               #print(self.today)
               self.startday= datetime.date(2019, 6, 15)
               self.diffdate=self.today-self.startday
               #print((self.diffdate.days))    total days
               self.weeks=int(self.diffdate.days/7)
               #print(int(self.weeks))     total weeks
               #print(self.lecattd)#attended lecture
               self.attendanceth=float(self.attendanceth)
               self.totalec=(self.weeks*self.getLecinWeek)   #total lecture in semester
               #print(self.totalec)
               self.lecattd=int((self.totalec*self.attendanceth)/100)#attended leture
               if(self.attendanceth <=75.0):
                   self.attdreq=75-self.attendanceth              #attendance require to make atleast 75%
                   #print(self.attdreq)
                   self.lectoattd=int((self.attdreq*self.totalec/100)+1)
                   #print(self.lectoattd)
                   self.showthinfo()
               else:
                   self.showthinfook()


       def showthinfo(self):
               parent = Tk()
               self.head=self.th.get()
               parent.title(self.head.upper())
               T = Text(parent, height=5, width=30,font=("arial", 15))
               T.pack()
               self.head=self.th.get()
               showText="\tSUBJECT: "+self.head.upper()+"\nAttendance         : "+str(self.attendanceth)+"\nTotal Lectures    : "+str(self.totalec)+"\nLecture Attended: "+str(self.lecattd)+"\nLecture to attend: "+str(self.lectoattd)+" Lecture"
               T.insert(END, showText,'big')
               self.exit=Button(parent,text="Exit",width=10,bg="lightGrey",activebackground="red",command=parent.destroy).pack(anchor=NE)
               parent.mainloop()

       def showthinfook(self):
               parent = Tk()
               self.head=self.th.get()
               parent.title(self.head.upper())
               T = Text(parent, height=5, width=30,font=("arial", 15))
               T.pack()
               self.head=self.th.get()
               showText="\tSUBJECT: "+self.head.upper()+"\nAttendance         : "+str(self.attendanceth)+"\nTotal lectures    : "+str(self.totalec)+"\nLectures Attended: "+str(self.lecattd)
               T.insert(END, showText,'big')
               self.exit=Button(parent,text="Exit",width=10,bg="lightGrey",activebackground="red",command=parent.destroy).pack(anchor=NE)
               parent.mainloop()
              
#----------------------------------------------------------EOF------------------------------------------------------------------------------------------------------------------

       


#------------------------------------------------BUTTONS----------------------------------------------------------------------------------------------------------------------
       def buttons(self):
        
        self.roll_no=self.temp+str(self.roll)
        parent=Tk()
        self.th=StringVar()
        self.prc=StringVar()
        self.head="WELCOME "+str(self.namestd)
        parent.title("Select")   

        self.img = ImageTk.PhotoImage(Image.open("user3.gif"))
        self.panel = Label(parent, image =self.img)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")
        

        self.l1=Label(parent,height=3,width=120,bg="INDIANRED4",fg="white",font='Helvetica 10 bold').place(x=0,y=3)

        self.l2=Label(parent,text =self.head,justify=LEFT,height=3,width=32,bg="indianred4",fg="white",font='Helvetica 10 bold').place(x=0,y=3)

        self.b1=Button(parent, text = "EXIT ",height=3,width=10,bg="BISQUE",fg="black",font='Helvetica 9 bold',activebackground = "RED",command=parent.destroy).place(x=505,y=1)

        #name     

        self.l3=Label(parent,text=self.namestd,height=4,width=44,bg="GREY98",fg="black",font='Helvetica 10 bold',borderwidth=3, relief="groove").place(x=260,y=60)
        self.l4=Label(parent,text=" Name:",height=3,width=10,bg="GREY98",fg="black",font='Helvetica 10 bold').place(x=264,y=70)

        #dept
        self.l5=Label(parent,text = "Computer Department",height=4,width=44,bg="GREY98",fg="black",font='Helvetica 10 bold',borderwidth=3, relief="groove").place(x=260,y=127)
        self.l6=Label(parent,text = "  Department:",height=2,width=10,bg="GREY98",fg="black",font='Helvetica 10 bold').place(x=264,y=143)

        #roll number
        self.l7=Label(parent,text =self.roll_no,height=4,width=44,bg="GREY98",fg="black",font='Helvetica 10 bold',borderwidth=3, relief="groove").place(x=260,y=198)
        self.l8=Label(parent,text ="Roll Number: ",height=2,width=10,bg="GREY98",fg="black",font='Helvetica 10 bold').place(x=264,y=205)

        self.l9=Label(parent,height=15,width=76,bg="white",font='Helvetica 10 bold').place(x=4,y=250)

        self.b2=Button(parent, text = "All subject Attendance ",height=3,width=35,bg="LIGHTGREEN",fg="black",font='Helvetica 9 bold',activebackground = "GREY",command=self.disAllSubAtd).place(x=4,y=258)
        ##accept subject
        self.b3=Label(parent, text = "Theory Subject attendance ",height=1,width=35,bg="CYAN",fg="black",font='Helvetica 9 bold').place(x=5,y=312)
        self.l10=Label(parent,text="Subject").place(x=4,y=335)
        self.e10=Entry(parent,textvariable=self.th,width=30).place(x=50,y=335)
        self.bu3=Button(parent,text="Submit",command=self.checkSubject).place(x=180,y=350)

        self.b4=Label(parent, text = "Practical Attendance ",height=1,width=35,bg="yellow",fg="black",font='Helvetica 9 bold').place(x=5,y=378)
        self.l10=Label(parent,text="Practical: ").place(x=4,y=401)
        self.e10=Entry(parent,textvariable=self.prc,width=30).place(x=55,y=401)
        self.bu3=Button(parent,text="Submit",command=self.checkPractical).place(x=180,y=416)
        
        self.b5=Button(parent, text = "Graphical View ",height=3,width=35,bg="pink",fg="black",font='Helvetica 9 bold',activebackground = "grey",command=self.disGraph).place(x=4,y=438)

        parent.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

obj=project()
while True:
 obj.login()

 i=obj.checkLogin()
 if i==11:
    obj.allSubject()
    obj.dicts()
    obj.buttons()
    break
 else:
    root = Tk()
    root.geometry("0x0")
    messagebox.showinfo("Invalid", message="Provide correct information !!",icon='warning',master=root)
    root.destroy()

