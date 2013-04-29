
from tkinter import *
import pymysql
from datetime import datetime

class Register():
    def __init__(self, myWin):
        self.myWin=myWin

        self.userNamev = StringVar()
        self.EmailV = StringVar()
        self.PhoneV = StringVar()
        self.carModelV = StringVar()
        self.LocationV = StringVar()
        self.ORTimeV = StringVar()
        self.OPTV = StringVar()
        self.ORTV = StringVar()
        self.UserNameV = StringVar()
        
      
        self.myWin.title("Rental Change Request")
        self.usernamelabel=Label(myWin,text="Enter User Name")
        self.usernamelabel.grid(column=0, row=0, sticky="E")
        self.userNamev=StringVar()
        self.userNameEntry=Entry(myWin, state="normal",width=20, textvariable=self.userNamev)
        self.userNameEntry.grid(row=0,column=1, sticky="W")
        self.go = Button(myWin, text = "GO", command = self.RCUserCheck)
        self.go.grid(column = 1, row = 0)
        
        
        myFrameR=Frame(myWin, bd=1, relief="sunken")
        myFrameR.grid(column=0, row=1)
        myFrameL=Frame(myWin, bd=1, relief="sunken")
        myFrameL.grid(column=1, row=1)
        self.yearL1b=Label(myFrameL, text="20")
        self.yearL1b.grid(row=2, column=4, sticky="W")


        self.yearL2=Label(myFrameL, text="20")
        self.yearL2.grid(row=3, column=4, sticky="W")

        self.CancelReservation=Button(myFrameL, text="Cancel Reservation")
        self.CancelReservation.grid(column=2, row=6, sticky="E")
        self.CarAvailibility=Button(myFrameL, text="Car Availibility")
        self.CarAvailibility.grid(column=3, row=6, sticky="E")        
        myFrameL=Frame(myWin)
        myFrameL.grid(column=1, row=1)

        #Labels Right Side
        self.labelRental=Label(myFrameR,text="Rental Information")
        self.labelRental.grid(column=0,row=0,columnspan=3,sticky="N")
        self.carModelL=Label(myFrameR,text="Car Model:")
        self.carModelL.grid(column=0,row=1,sticky=W)
        self.LocationL=Label(myFrameR,text="Location: ")
        self.LocationL.grid(column=0,row=2, sticky=W)
        self.ReturnTimeL=Label(myFrameR,text="Original Return Time: ")
        self.ReturnTimeL.grid(column=0,row=3, sticky=W)
        self.ArrivalTimeL=Label(myFrameR,text="New Arrival Time:")
        self.ArrivalTimeL.grid(column=0,row=5, sticky=W)
    
        self.y2=Label(myFrameR, text = "20")
        self.y2.grid(row = 5, column = 3, sticky = "E")
        #Entrys Right Side
        self.carModelV=StringVar()
        self.carModelE=Entry(myFrameR, state="readonly", width=20, textvariable=self.carModelV)
        self.carModelE.grid(row=1,column=1, sticky=W)
        self.LocationV=StringVar()
        self.LocationE=Entry(myFrameR, state="readonly", width=20, textvariable=self.LocationV)
        self.LocationE.grid(row=2, column=1, sticky=W)
        self.ORTime = Entry(myFrameR, state = "readonly", width = 20, textvariable = self.ORTimeV)
        self.ORTime.grid(row = 3, column = 1, sticky = W)

        #String Variables
        self.ORvar=StringVar(myFrameR)
        self.ORvar2=StringVar(myFrameR)
        self.Year1=StringVar(myFrameR)
        self.NA1var=StringVar(myFrameR)
        self.NA2var=StringVar(myFrameR)
        self.Year2var=StringVar(myFrameR)
        self.PU1var=StringVar(myFrameR)
        self.PU2var=StringVar(myFrameR)
        self.Year3var=StringVar(myFrameR)
        self.RD1var=StringVar(myFrameR)
        self.RD2var=StringVar(myFrameR)
        self.Year4var=StringVar(myFrameR)
        self.t1var=StringVar(myFrameR)
        self.t2var=StringVar(myFrameR)
        self.t3var=StringVar(myFrameR)
        self.t4var=StringVar(myFrameR)
        self.t5var=StringVar(myFrameR)
        self.t6var=StringVar(myFrameR)
        self.t1lvar=StringVar(myFrameL)
        self.t2lvar=StringVar(myFrameL)
        self.t3lvar=StringVar(myFrameL)
        self.t4lvar=StringVar(myFrameL)
        self.t5lvar=StringVar(myFrameL)
        self.t6lvar=StringVar(myFrameL)
                                                  

        self.listboxNA1=OptionMenu(myFrameR, self.NA1var, "01","02","03","04","05","06","07","08","09","10","11","12")
        self.listboxNA1.grid(row=5,column=1)

        self.listboxNA2=OptionMenu(myFrameR, self.NA2var, "01","02","03","04","05","06", "07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.listboxNA2.grid(row=5,column=2)

        self.listboxNAYear=OptionMenu(myFrameR, self.Year2var, "00", "01","02","03","04","05","06", "07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.listboxNAYear.grid(row=5,column=4)


        self.listboxt4r=OptionMenu(myFrameR, self.t4var,"01:", "02:", "03:", "04:", "05:", "06:", "07:", "08:", "09:","10:","11:","12:")
        self.listboxt4r.grid(row =6, column =1)

        self.listbox5r=OptionMenu(myFrameR, self.t5var, "00", "01", "02", "03","04", "05", "06", "07", "08", "09","10", "11", "12", "13","14", "15", "16", "17", "18", "19","20", "21", "22", "23","24", "25", "26", "27", "28", "29","30", "31", "32", "33","34", "35", "36", "37", "38", "39","40", "41", "42", "43","44", "45", "46", "47", "48", "49","50", "51", "52", "53","54", "55", "56", "57", "58", "59")
        self.listbox5r.grid(row = 6, column =2)

        self.listbox6r=OptionMenu(myFrameR, self.t6var, "AM", "PM")
        self.listbox6r.grid(row = 6, column = 3)

        


        self.UpdateButton=Button(myFrameR,text="Update", command = self.affected)
        self.UpdateButton.grid(column=3, row=7, columnspan=2, sticky="W")
        #Labels Left Side
        self.UserAffectedL=Label(myFrameL,text="User Affected:")
        self.UserAffectedL.grid(column=1,row=0,sticky="W")
        self.UserNameL=Label(myFrameL,text="Username:")
        self.UserNameL.grid(column=0,row=1,sticky="W")
        self.OriginalPickUpL=Label(myFrameL,text="Original Pick Up Time: ")
        self.OriginalPickUpL.grid(column=0,row=2, sticky=W)
        self.OriginalReturnTimeL=Label(myFrameL,text="Original Return Time: ")
        self.OriginalReturnTimeL.grid(column=0,row=3, sticky="W")
        self.EmailL=Label(myFrameL,text="Email Address:")
        self.EmailL.grid(column=0,row=4, sticky="W")
        self.PhoneL=Label(myFrameL,text="Phone Number:")
        self.PhoneL.grid(column=0,row=5, sticky="W")
        #Entrys Left Side
        self.UserNameV=StringVar()
        self.UserNameE=Entry(myFrameL, state="readonly", width=20, textvariable=self.UserNameV)
        self.UserNameE.grid(row=1,column=1, sticky="E")
        OPT = Entry(myFrameL, state = "readonly", width = 20, textvariable = self.OPTV)
        OPT.grid(row = 2, column =1)
        ORT = Entry(myFrameL, state = "readonly", width = 20, textvariable = self.ORTV)
        ORT.grid(row = 3, column = 1)
        

        self.EmailV=StringVar()
        self.EmailE=Entry(myFrameL, state="readonly", width=20, textvariable=self.EmailV)
        self.EmailE.grid(row=4, column=1, sticky="E")
        self.PhoneV=StringVar()
        self.PhoneE=Entry(myFrameL, state="readonly", width=20, textvariable=self.PhoneV)
        self.PhoneE.grid(row=5, column=1, sticky="E")
        self.CancelReservation=Button(myFrameL, text="Cancel Reservation")
        self.CancelReservation.grid(column=2, row=8, sticky="E")
        self.CarAvailibility=Button(myFrameL, text="Car Availibility")
        self.CarAvailibility.grid(column=3, row=8, sticky="E")        
        myFrameL=Frame(myWin)
        myFrameL.grid(column=1, row=1)

    def Connect(self):
        try:
            self.con = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            return(self.con)
        
        except:
            messagebox.showwarning("Warning", "Could not connect. Please check your internet connection.")


    def RCUserCheck(self):
        self.Connect()
        cursor = self.con.cursor()
        x = self.userNamev.get()
        sql="SELECT car_information.type, reservation.location_name, reservation.pickup_date, reservation.return_date, car_information.vehicle_sno "
        sql+="FROM reservation LEFT JOIN car_information ON car_information.vehicle_sno = reservation.vehicle_sno "
        sql+="WHERE reservation.vehicle_sno = (SELECT reservation.vehicle_sno FROM reservation "
        sql+="WHERE reservation.pickup_date = (SELECT MIN( reservation.pickup_date ) FROM reservation "
        sql+="WHERE reservation.username =  %s AND reservation.pickup_date > (NOW( )))) AND reservation.username =  %s"
        cursor.execute(sql,(x,x))
        aList=[]            
        for items in cursor:
            aList.append(items)
            print(aList)    
        #self.carModelV.set(aList[)
        if aList != []:
            self.carModelV.set(aList[0][0])
            self.LocationV.set(aList[0][1])
            self.ORTimeV.set(aList[0][3])
            self.affectedPUDate = aList[0][3]
            self.affectedSno = aList[0][4]
            timeStamp=aList[0][2]
            print("t",timeStamp)
            SNO=aList[0][3]
            print(SNO)
            
        
        
                   
                                   
                                   
    
        
        """a = []
        b = []
        c = []
        d = []
        querySNO = ("SELECT vehicle_sno FROM reservation WHERE username = %s")
        cursor.execute(querySNO, x)
        for item in cursor:
            a.append(item)
        sno = str(a[0][0])
        
    
        queryType = ("SELECT type FROM car_information WHERE vehicle_sno = %s")
        cursor.execute(queryType, sno)
        for item in cursor:
            b.append(item)
        ty= b[0][0]
        ty = str(ty)
            
        self.carModelV.set(ty)

        queryLoc = ("SELECT location_name FROM reservation WHERE vehicle_sno = %s")
        cursor.execute(queryLoc, sno)
        for item in cursor:
            c.append(item)
        loc = c[0][0]
        loc = str(loc)

        self.LocationV.set(loc)

        queryOTime = ("SELECT return_date FROM reservation WHERE vehicle_sno = %s")
        cursor.execute(queryOTime, sno)
        for item in cursor:
            d.append(item)
        time = d[0][0]
        time = str(time)

        self.ORTimeV.set(time)"""

        self.con.close()

    def newArrival(self):
        self.date = "20"
        year = self.Year2var.get()
        self.date = self.date + year+"-"
        month = self.NA1var.get()
        self.date = self.date+month+"-"
        day = self.NA2var.get()
        self.date = self.date+day+" "

        self.time()
        self.date = self.date+self.t
        #print(self.date)
        return self.date
        
    def time(self):
        y = self.t6var.get()
        hour = self.t4var.get()
        minu = self.t5var.get()
        hour = hour[0:2]

        if y =="PM":
            hour = int(hour)
            hour = hour + 12
            hour = str(hour)
            self.t = hour
        #if y == "AM":
            #hour = int(hour)
            #if y == 12:
                #hour = hour +12
                #print(hour)
        else:
            self.t = hour
            
        self.t = self.t+":"+minu+":00"

        return self.t
    
        
                
            
            
        
        
        
        
        
        

    def affected(self):
        self.newArrival()
        self.Connect()
        cursor = self.con.cursor()
        date = self.date
        dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        dates = []
        newdates = []
        
        a = []
        b = []
        cl = []
        d = []
        e = []
        f = []
        sql = "SELECT reservation.username, reservation.pickup_date, reservation.return_date, gt_student.email, gt_student.phone "
        sql+= "FROM reservation LEFT JOIN gt_student ON reservation.username= gt_student.username "
        sql+= "WHERE reservation.vehicle_sno = %s "
        sql+= "AND reservation.pickup_date < %s "
        sql+= "AND reservation.return_date > %s "
        cursor.execute(sql, (self.affectedSno, self.affectedPUDate, self.affectedPUDate))
        results = []
        for item in cursor:
            results = item
        if results != []:
            self.affectedUser = results[0]
            self.affectePickup = results[1]
            self.UserNameV.set(results[0])
            self.OPTV.set(results[1])
            self.ORTV.set(results[2])
            self.emailV.set(results[3])
            self.phoneV.set(results[4])
        
"""
        queryTRY = ("SELECT pickup_date FROM reservation")
        cursor.execute(queryTRY)
        
        for item in cursor:
            dates.append(item)
        for item in dates:
            c = item[0]
            diff = dt - c
            print(diff)
            #days = DateTime.Compare(dt, c)
            if diff.days > 0:
                newdates.append(c)
            #print(type(c))
        newc = datetime.strftime(c, "%Y-%m-%d %H:%M:%S")
        #print(type(newc))
        print(newc)
        
                
        
        querySNO = ("SELECT vehicle_sno FROM reservation WHERE pickup_date = %s")
        cursor.execute(querySNO, newc)
        for item in cursor:
            a.append(item)
        print(a)
        sno = a[0][0]
        sno = str(sno)

        queryUser = ("SELECT username FROM reservation WHERE vehicle_sno = %s")
        cursor.execute(queryUser, sno)
        for item in cursor:
            b.append(item)
        user = b[0][0]
        user = str(user)


        self.UserNameV.set(user)

        queryOPT = ("SELECT pickup_date FROM reservation WHERE vehicle_sno = %s")
        cursor.execute(queryOPT, sno)
        for item in cursor:
            cl.append(item)
        OPT = cl[0][0]
        OPT = str(OPT)
        self.OPTV.set(OPT)

        queryORT = ("SELECT return_date FROM reservation WHERE vehicle_sno = %s")
        cursor.execute(queryORT, sno)
        for item in cursor:
            d.append(item)
        ORT = d[0][0]
        ORT = str(ORT)
        self.ORTV.set(ORT)

        queryEmail = ("SELECT email FROM gt_student WHERE username = %s")
        cursor.execute(queryEmail, user)
        for item in cursor:
            e.append(item)
        email = e[0][0]
        email = str(email)
        self.EmailV.set(email)

        queryPhone = ("SELECT phone FROM gt_student WHERE username = %s")
        cursor.execute(queryPhone, user)
        for item in cursor:
            f.append(item)
        phone = f[0][0]
        phone = str(phone)
        self.PhoneV.set(phone)
"""
##        def deleter(self):
##        self.affected()
##        self.Connect()
##        cursor = self.con.cursor()
##        sqlDelete="Delete From reservation WHERE viechle_sno=%s "
##        sql+="AND username.user=%s "
##        sql+="AND reservation.pickup_date=%s"
##        cursor.execute(sqlDelete,querySNO,queryUser)
##        
        
        
        

    
   


myWin= Tk()
gui=Register(myWin)
myWin.mainloop()
        

