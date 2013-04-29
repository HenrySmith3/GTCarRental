from tkinter import *
import pymysql
import newUser
import homepage
import empHomepage
import sqlAdminReport

class Register():
    def run(self):
        self.myWin1=Tk()
        myWin=self.myWin1
        

        self.myWin1.title("GT Car Rental")
        myFrame=Frame(self.myWin1)
        myFrame.pack()

        self.labelname=Label(myFrame,text="User Name ")
        self.labelname.grid(column=0,row=1)
        self.labeluser=Label(myFrame,text="Password: ")
        self.labeluser.grid(column=0,row=2)
        self.entry1s=StringVar()

        self.entry1=Entry(myFrame, state="normal", width=30, textvariable=self.entry1s)
        self.entry1.grid(row=1,column=1)
        self.entry2s=StringVar()

        self.entry2=Entry(myFrame, state="normal", width= 30, textvariable=self.entry2s)
        self.entry2.grid(row=2,column=1)
        self.button1=Button(myFrame, text="New User?", command=self.toNewUser)
        self.button1.grid(column=2, row=4, sticky="e")
        self.button2=Button(myFrame, text="Login",command=self.logInCheck)
        self.button2.grid(column=3, row=4, sticky="e")
        myWin.mainloop()
    def logInCheck(self): 
        self.connectMySQL()
        
        cursor= self.db.cursor()
        username = self.entry1s.get() 
        password = self.entry2s.get()
        
        print(str(username))
        print(password)
        sql = "Select usertype FROM users WHERE username= %s  AND password = %s" 
        cursor.execute(sql, (username, password))
        usertype = ""
        for item in cursor:
            usertype = item[0]
        print (usertype)
        if usertype == "Georgia Tech student":
            messagebox.showinfo("Success!", "You have logged in successfully!")
            """info = []
            for item in cursor:
                info.append(item) 
            if info[0][2] == "None": 
                self.name = "User" 
            else: 
                self.name = info[0][2]"""
            self.myWin1.destroy()
            homepage.Register().run(username)
        elif usertype == "GTCR employees":
            messagebox.showinfo("Success!", "You have logged in as an employee!")
            self.myWin1.destroy()
            empHomepage.Register().run(username)
        elif usertype == "admin":
            messagebox.showinfo("Success!", "You have logged in as an admin!")
            sqlAdminReport.Register().run()            
        else: 
            messagebox.showerror("Error", "You've entered an invalid username/password combination. Please try again.")

        
    def toNewUser(self):
        self.myWin1.destroy()
        newUser.Register().run()


    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
#            messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")



gui= Register()
gui.run()
