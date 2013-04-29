from tkinter import *
import pymysql

class Register():
    def run(self):
        myWin = Toplevel()
        self.mywin = myWin
        self.mywin.title("Manage Cars")
        frame1 = Frame(self.mywin, bd = 1, relief = "sunken")
        frame1.pack(side = "left")
        frame2 = Frame(self.mywin, bd = 1, relief = "sunken")
        frame2.pack(side="left")
        title = Label(frame1, text = "ADD CAR")
        title.grid(row = 0, column = 1)
        l1 = Label(frame1, text = "Vehicle Sno:")
        l1.grid(row = 2, column = 0, sticky = "w")
        l2 = Label(frame1, text = "Car Model")
        l2.grid(row = 3, column = 0, sticky = "w")
        l3 = Label(frame1, text = "Car Type")
        l3.grid(row = 4, column = 0, sticky = "w")
        l4 = Label(frame1, text = "Location")
        l4.grid(row = 5, column = 0, sticky = "w")
        l5 = Label(frame1, text = "Color")
        l5.grid(row = 6, column = 0, sticky = "w")
        l6 = Label(frame1, text = "Hourly Rate:")
        l6.grid(row = 7, column = 0, sticky = "w")
        l7 = Label(frame1, text = "Daily Rate:")
        l7.grid(row = 8, column = 0, sticky = "w")
        l8 = Label(frame1, text = "Seating Capacity:")
        l8.grid(row = 9, column = 0, sticky = "w")
        l9 = Label(frame1, text = "Transmission Type:")
        l9.grid(row = 10, column = 0, sticky = "w")
        l10 = Label(frame1, text = "Bluetooth Connectivity:")
        l10.grid(row = 11, column = 0, sticky = "w")
        l11 = Label(frame1, text = "Auxilary Cable:")
        l11.grid(row = 12, column = 0, sticky = "w")

        self.sno = StringVar()
        self.model = StringVar()
        self.cType = StringVar()
        self.loc = StringVar()
        self.color = StringVar()
        self.hrate = StringVar()
        self.drate = StringVar()
        self.scap = StringVar()
        self.transType = StringVar()
        self.blue = StringVar()
        self.aux = StringVar()
        e1 = Entry(frame1, state = "normal", textvariable = self.sno, width = 20)
        e1.grid(row = 2, column = 1)
        e2 = Entry(frame1, state = "normal", textvariable = self.model, width = 20)
        e2.grid(row = 3, column = 1)
        e3 = OptionMenu(frame1, self.cType, "Hybrid", "Sedan", "SUV", "Sports Car", "Motorcycle", "Convertible", "Van")
        e3.grid(row = 4, column = 1)
        self.connectMySQL()
        cursor = self.db.cursor()
        sql = "SELECT location_name FROM location" 
        cursor.execute(sql)
        locations = []
        for item in cursor:
            locations += [item[0]]
        e4 = OptionMenu(frame1, self.loc, *tuple(locations))
        e4.grid(row = 5, column = 1)
        e5 = Entry(frame1, state = "normal", textvariable = self.color, width = 20)
        e5.grid(row = 6, column = 1)
        e6 = Entry(frame1, state = "normal", textvariable = self.hrate, width = 20)
        e6.grid(row = 7, column = 1)
        e7 = Entry(frame1, state = "normal", textvariable = self.drate, width = 20)
        e7.grid(row = 8, column = 1)
        e8 = Entry(frame1, state = "normal", textvariable = self.scap, width = 20)
        e8.grid(row = 9, column = 1)
        e9 = OptionMenu(frame1, self.transType, "Automatic", "Manual")
        e9.grid(row = 10, column = 1)
        e10 = OptionMenu(frame1, self.blue, "Yes", "NO")
        e10.grid(row = 11, column = 1)
        e11 = OptionMenu(frame1,self.aux, "Yes", "No")
        e11.grid(row = 12, column = 1)

        b = Button(frame1, text = "Add", command = self.addCar)
        b.grid(row = 13, column = 2)


        titler = Label(frame2, text = "CHANGE CAR LOCATION")
        titler.grid(row = 0, column = 1)

        self.currLoc = StringVar()
        self.chCar = StringVar()
        lr1 = Label(frame2, text = "Choose Current Location:")
        lr1.grid(row = 2, column = 0, sticky = "w")
        lr2 = Label(frame2, text = "Choose car:")
        lr2.grid(row = 3, column = 0, sticky = "w")
        self.entr1 = OptionMenu(frame2, self.currLoc, "Graduate Liv", "CRC", "Peters", "Student Cent", "North Ave", "CULC")
        self.entr1.grid(row = 2, column = 1)
        self.entr2 = OptionMenu(frame2, self.chCar, "Civic", "Toyota")
        self.entr2.grid(row = 3, column = 1)
        button = Button(frame2, text = "GO", command = self.getDisc)
        button.grid(row = 3, column = 2)
        button2 = Button(frame2, text = "go", command = self.Change)
        button2.grid(row = 2, column = 2)

        inFrame = Frame(frame2, bd = 1, relief = "sunken")
        inFrame.grid(row =5 , column =0, rowspan = 5, columnspan = 3)
        ntitle = Label(inFrame, text = "Brief Description")
        ntitle.grid(row = 0, column = 1)
        car = Label(inFrame, text = "Car Type:")
        car.grid(row = 1, column = 0, sticky = "w")
        color = Label(inFrame, text = "Color:")
        color.grid(row = 2, column = 0, sticky = "w")
        seat = Label(inFrame, text = "Seating Capacity:")
        seat.grid(row = 3, column = 0, sticky = "w")
        trans = Label(inFrame, text = "Transmission Type:")
        trans.grid(row = 4, column = 0, sticky =  "w")

        self.carType = StringVar()
        self.nColor = StringVar()
        self.nSeatCap = StringVar()
        self.nTranType = StringVar()
        carent = Entry(inFrame, state = "readonly",textvariable = self.carType, width =20)
        carent.grid(row = 1, column = 1)
        colorent = Entry(inFrame, state ="readonly", textvariable = self.nColor, width = 20)
        colorent.grid(row = 2, column = 1)
        seatent = Entry(inFrame, state = "readonly", textvariable = self.nSeatCap, width = 20)
        seatent.grid(row = 3, column = 1)
        transent = Entry(inFrame, state = "readonly", textvariable = self.nTranType, width = 20)
        transent.grid(row = 4, column = 1)


        self.newLoc = StringVar()
        lr3 = Label(frame2, text = "Choose a new location")
        lr3.grid(row = 12, column = 0, sticky = "w")
        om = OptionMenu(frame2, self.newLoc, "Graduate Liv", "CRC", "Peters", "Student Cent", "North Ave", "CULC")
        om.grid(row = 12, column = 1)
        b2 = Button(frame2, text = "Submit Changes", command = self.newLocation)
        b2.grid(row = 13, column = 2)

    def Connect(self):
        try:
            self.con = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            return(self.con)
        
        except:
            messagebox.showwarning("Warning", "Could not connect. Please check your internet connection.")

    def addCar(self):
        self.Connect()
        cursor = self.con.cursor()
        sno = self.sno.get()
        aux = self.aux.get()
        transType = self.transType.get()
        scap = self.scap.get()
        blue = self.blue.get()
        drate = self.drate.get()
        hrate = self.hrate.get()
        color = self.color.get()
        cType = self.cType.get()
        model = self.model.get()
        loc = self.loc.get()
        query = ("INSERT INTO car_information (vehicle_sno, auxilary_cable, transmission_type, seating_capacity, blue_tooth_connectivity, daily_rate, hourly_rate, color, type, model_name, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (sno, aux, transType, scap, blue, drate, hrate, color, cType, model, loc))
        self.con.commit()
        self.con.close()
        
    def Change(self):
        self.Connect()
        cursor = self.con.cursor()
        a = []
        currLoc = self.currLoc.get()
        query = ("SELECT model_name FROM car_information WHERE location = %s")
        cursor.execute(query, currLoc)
        for item in cursor:
            a.append(item)
        menu = self.entr2["menu"]
        menu.delete(0, "end")
        for string in a:
            menu.add_command(label = string, command = lambda value = string:
                             self.chCar.set(value))
        print(menu)
        self.con.close()
            

    def getDisc(self):
        self.Connect()
        cursor = self.con.cursor()
        currLoc = self.currLoc.get()
        a = []
        b = []
        c = []
        d = []
        chCar = self.chCar.get()
        chCar = chCar[2:-3]
        queryTy = ("SELECT type FROM car_information WHERE model_name = %s")
        cursor.execute(queryTy, chCar)
        for item in cursor:
            a.append(item)
        ctype = str(a[0][0])
        self.carType.set(ctype)

        queryC = ("SELECT color FROM car_information WHERE model_name = %s")
        cursor.execute(queryC, chCar)
        for item in cursor:
            b.append(item)
        color = str(b[0][0])
        self.nColor.set(color)

        querySC = ("SELECT seating_capacity FROM car_information WHERE model_name = %s")
        cursor.execute(querySC, chCar)
        for item in cursor:
            c.append(item)
        seat = str(c[0][0])
        self.nSeatCap.set(seat)

        queryTr = ("SELECT transmission_type FROM car_information WHERE model_name = %s")
        cursor.execute(queryTr, chCar)
        for item in cursor:
            d.append(item)
        tran = str(d[0][0])
        self.nTranType.set(tran)
        self.con.close()

    def newLocation(self):
        self.Connect()
        cursor = self.con.cursor()
        chCar = self.chCar.get()
        chCar = chCar[2:-3]
        newLoc = self.newLoc.get()

        querylc = ("UPDATE car_information SET location = %s WHERE model_name = %s")
        cursor.execute(querylc, (newLoc, chCar))
        self.con.commit()
        self.con.close()
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
#            messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")
        
