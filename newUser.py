from tkinter import *
import pymysql
import Login
import personalinfo
import empHomepage
    

class Register():
    def run(self):
        self.myWin=Tk()
        myFrame=Frame(self.myWin)
        myFrame.pack()
        self.labeluser=Label(myFrame,text="User Name ")
        self.labeluser.grid(column=0,row=0)
        self.labelpassword=Label(myFrame,text="Password: ")
        self.labelpassword.grid(column=0,row=1)
        self.labelcpassword=Label(myFrame,text="Confirm Password: ")
        self.labelcpassword.grid(column=0,row=2)
        self.entryuserName=StringVar()
        self.labeltype=Label(myFrame, text="Type of User")
        self.labeltype.grid(column=0, row=3)
        self.entry1=Entry(myFrame, state="normal", width=30,textvariable=self.entryuserName)
        self.entry1.grid(row=0,column=1)
        self.entryPW=StringVar()

        self.entry2=Entry(myFrame, state="normal", width=30,textvariable=self.entryPW)
        self.entry2.grid(row=1,column=1)
        self.entryPWC=StringVar()

        self.entry3=Entry(myFrame, state="normal", width=30, textvariable=self.entryPWC)
        self.entry3.grid(row=2,column=1)

        self.entry4b=StringVar()
        self.Usertype =StringVar()
        self.listboxreg=OptionMenu(myFrame, self.Usertype,"Georgia Tech students / faculty", "GTCR employees")
        self.listboxreg.grid(row=3,column=1)
##        self.listboxregistration()
##        self.listboxreg.bind("<Double-Button-1>", self.OnDouble)                 
        self.button1=Button(myFrame, text="Cancel", command=self.backToLogin)
        self.button1.grid(column=2,sticky="e", row=4)
        self.button2=Button(myFrame, text="Register", command=self.registerNew)                   
        self.button2.grid(column=3,sticky="e", row=4)
        #self.myWin2.withdraw()

    def backToLogin(self):
        self.myWin.destroy()
        Login.Register().run()

    def registerNew(self):
        db = self.connectMySQL()
        UserName=self.entryuserName.get()
        print(UserName)
        PW=self.entryPW.get()
        print(PW)
        PWC=self.entryPWC.get()
        print(PWC)
        user=str(self.Usertype.get())
        print(user)
        self.connectMySQL()
        cursor = self.db.cursor()

        
        sqlname = "Select username FROM users"
        cursor.execute(sqlname)
        userdata= []
        for item in cursor:
            userdata.append(item)
        print(userdata)
        cursor.close()
        v=True
        for i in userdata:
            print(i)
            if UserName==i[0]:
                v= False
                if v==False:
                    print(i)       
        if UserName !="" or PW !="":
            if PW==PWC:
                if v!=False:
                    self.username=UserName
                    cursor = self.db.cursor()    
                    sql = "INSERT INTO users(username, password,usertype) VALUES (%s, %s,%s)"
                    print(UserName, PW)
                    cursor.execute(sql,(UserName,PW,user))
                    messagebox.showwarning("Registration Status","Succesful Registration")
                    self.myWin.destroy()
                    self.db.close()
                    print(user)
                    if user != "GTCR employees":
                        personalinfo.Register().run(UserName)
                    else:
                        empHomepage.Register().run(UserName)

                else:
                    messagebox.showwarning("Registration Status","Username already exist. Please try a different selection")


            else:
                messagebox.showwarning("Registration Status","Password check failed. Please enter the same password twice")

        else:
            messagebox.showwarning("Registration Status","Entry required for username and password")
    
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
#            messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")


