from tkinter import*
import urllib.request
from tkinter import messagebox
import pymysql
import time

class Register():
    def run(self, username):
        self.username = username
        rootWin = Toplevel()
        self.mywin = rootWin
        frame = Frame(self.mywin)
        frame.grid(row =2, column = 2)
        self.mywin.title("Maintence Requests")

        #get locations
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql = "SELECT DISTINCT location_name FROM location"
        cursor.execute(sql)
        self.locations = []
        for item in cursor:
            self.locations += [item[0]]
        sql = "SELECT DISTINCT vehicle_sno FROM car_information"
        cursor.execute(sql)
        self.vehicle_snos = []
        for item in cursor:
            self.vehicle_snos += [item[0]]
        self.db.commit()
        
        loc = Label(self.mywin, text = "Choose Location")
        loc.grid(row = 0, column = 0)
        car = Label(self.mywin, text = "Choose a Car")
        car.grid(row = 1, column = 0)
        desc = Label(self.mywin, text = "Brief Description of Problem :")
        desc.grid(row = 2, column = 0)
        self.variable = StringVar(self.mywin)
        OM1 = OptionMenu(self.mywin, self.variable, *tuple(self.locations))
        OM1.grid(row = 0, column = 2, columnspan = 3)
        self.variable2 = StringVar(self.mywin)
        OM2 = OptionMenu(self.mywin, self.variable2, *tuple(self.vehicle_snos))
        OM2.grid(row = 1, column = 2, columnspan = 3)
        #scrollbar = Scrollbar(self.mywin)
        #scrollbar.pack(side = RIGHT, fill = Y)
        self.entbox = Entry(frame, state = "normal")
        self.entbox.grid(row = 2, column = 2, columnspan = 3)
        submit = Button(self.mywin, text = "Submit Request", command=self.buttonHandler)
        submit.grid(row = 3, column = 4, columnspan = 2)
        #entbox.insert(END, "ENTER SOME INFO")
        
        #frame.config( yscrollcommand = scrollbar.set)
        
        #scrollbar.config(self.mywin, command = frame.yview)

    def rentalRequest(self):
        
        self.mywin.title("Rental Change Request")
        label = Label(self.mywin, text = "Enter Username: ")
        label.pack(side = TOP)
        e = Entry(self.mywin, state = "normal")
        e.pack(side = TOP)
        
        frame = Frame(self.mywin, borderwidth = 1, relief = SOLID)
        frame.pack(side = LEFT)
        frame2 = Frame(self.mywin, borderwidth = 1, relief = SOLID)
        frame2.pack(side = LEFT)
        title = Label(frame, text = "Rental Information")
        title.grid(row = 0, column = 1)
        L1 = Label(frame, text = "Car Model:")
        L1.grid(row = 1, column = 0)
        L2 = Label(frame, text = "Location:")
        L2.grid(row = 2, column = 0)
        L3 = Label(frame, text = "Original Return Time:")
        L3.grid(row = 3, column = 0)
        L4 = Label(frame, text = "New Arrival Time:")
        L4.grid(row = 4, column = 0)
        
        var1 = StringVar(frame)
        var2 = StringVar(frame)
        E1 = Entry(frame, state = "normal")
        E1.grid(row = 1, column = 1, columnspan = 2)
        E2 = Entry(frame, state = "normal")
        E2.grid(row = 2, column = 1, columnspan = 2)
        date1 = OptionMenu(frame, var1, "one", "two")
        date1.grid(row = 3, column = 1)
        time1 = OptionMenu(frame, var2, "one", "two")
        time1.grid(row = 3, column = 2)
        date2 = OptionMenu(frame, var1, "one", "two")
        date2.grid(row = 4, column = 1)
        time2 = OptionMenu(frame, var2, "one", "two")
        time2.grid(row = 4, column = 2)
        b1 = Button(frame, text = "Update")
        b1.grid(row = 5, column = 4)

        title2 = Label(frame2, text = "User Affected")
        title2.grid(row = 0, column = 1)
        uname = Label(frame2, text = "Username: ")
        uname.grid(row = 1, column = 0)
        oPTime = Label(frame2, text = "Original pick up time: ")
        oPTime.grid(row = 2, column = 0)
        oRTime = Label(frame2, text = "Original return time: ")
        oRTime.grid(row =3, column = 0)
        email = Label(frame2, text = "Email Address: ")
        email.grid(row = 4, column = 0)
        phone = Label(frame2, text = "Phone No: ")
        phone.grid(row =5, column = 0)
        user = Entry(frame2, state = "readonly")
        user.grid(row = 1, column = 1, columnspan = 2)
        opt = StringVar(frame2)
        opt2 = StringVar(frame2)
        ort = StringVar(frame2)
        ort2 = StringVar(frame2)
        OPT = OptionMenu(frame2, opt, "one")
        OPT.grid(row = 2, column = 1)
        OPT2 = OptionMenu(frame2, opt2, "one")
        OPT2.grid(row = 2, column = 2)
        ORT = OptionMenu(frame2, ort, "one")
        ORT.grid(row = 3, column = 1)
        ORT2 = OptionMenu(frame2, ort2, "one")
        ORT2.grid(row = 3, column = 2)
        mail = Entry(frame2, state = "readonly")
        mail.grid(row = 4, column = 1, columnspan = 2)
        no = Entry(frame2, state = "readonly")
        no.grid(row = 5, column = 1, columnspan = 2)
        cancel = Button(frame2, text = "Cancel Reservation")
        cancel.grid(row = 6, column = 0, columnspan = 2)
        show = Button(frame2, text = "Show car availability")
        show.grid(row = 6, column = 2, columnspan = 2)

    def buttonHandler(self):
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql = "INSERT INTO maintenance_request VALUES (%s, %s, %s, %s) "
        cursor.execute(sql, (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
                             self.variable2.get(), self.entbox.get(), self.username))
        self.db.commit()
        self.mywin.destroy()

    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")




