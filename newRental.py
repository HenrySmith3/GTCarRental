from tkinter import *
from tkinter import _setit
from datetime import *
import availability
import pymysql
class Register():
    def run(self, username):
        self.username = username
        myWin=Toplevel()
        self.RentCar=myWin
        myFrame=Frame(myWin)
        myFrame.pack()
        self.PickUp=Label(myFrame, text="Pick Up Time:")
        self.PickUp.grid(row=0, column=0, sticky="W")
        self.Return=Label(myFrame, text="Drop Off Time:")
        self.Return.grid(row=1, column=0, sticky="W")
        self.Location=Label(myFrame, text="Location:")
        self.Location.grid(row=2, column=0, sticky="W")
        self.Cars=Label(myFrame, text="Cars:")
        self.Cars.grid(row=3, column=0, sticky="W")

        self.PUM=Label(myFrame, text="Month")
        self.PUM.grid(row=0, column=1, sticky="W")
        self.PUD=Label(myFrame, text="Day")
        self.PUD.grid(row=0, column=3, sticky="W")
        self.PUY=Label(myFrame, text="Year    20:")
        self.PUY.grid(row=0, column=5, sticky="W")
        self.PUT=Label(myFrame, text="Time")
        self.PUT.grid(row=0, column=7, sticky="W")

        self.DUM=Label(myFrame, text="Month")
        self.DUM.grid(row=1, column=1, sticky="W")
        self.DUD=Label(myFrame, text="Day")
        self.DUD.grid(row=1, column=3, sticky="W")
        self.DUY=Label(myFrame, text="Year    20:")
        self.DUY.grid(row=1, column=5, sticky="W")
        self.DUT=Label(myFrame, text="Time")
        self.DUT.grid(row=1, column=7, sticky="W")

        
        self.PUmonth=StringVar()
        self.PUday=StringVar()
        self.PUyear=StringVar()
        self.PUtimea=StringVar()
        self.PUtimeb=StringVar()
        self.PUtimec=StringVar()
        
        
        self.OMPUMonth=OptionMenu(myFrame, self.PUmonth, "Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec")
        self.OMPUMonth.grid(row=0,column=2)

        self.OMPUday=OptionMenu(myFrame, self.PUday, "01","02","03","04","05","06", "07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.OMPUday.grid(row=0,column=4)

        self.OMPUyear=OptionMenu(myFrame, self.PUyear, "13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.OMPUyear.grid(row=0,column=6)

        self.OMPUtimea=OptionMenu(myFrame, self.PUtimea,"01:", "02:", "03:", "04:", "05:", "06:", "07:", "08:", "09:","10:","11:","12:")
        self.OMPUtimea.grid(row =0, column =8)

        self.OMPUtimeb=OptionMenu(myFrame, self.PUtimeb, "00", "01", "02", "03","04", "05", "06", "07", "08", "09","10", "11", "12", "13","14", "15", "16", "17", "18", "19","20", "21", "22", "23","24", "25", "26", "27", "28", "29","30", "31", "32", "33","34", "35", "36", "37", "38", "39","40", "41", "42", "43","44", "45", "46", "47", "48", "49","50", "51", "52", "53","54", "55", "56", "57", "58", "59")
        self.OMPUtimeb.grid(row = 0, column =9)

        self.OMPUtimec=OptionMenu(myFrame, self.PUtimec, "AM", "PM")
        self.OMPUtimec.grid(row = 0, column = 10)

        self.DUmonth=StringVar()
        self.DUday=StringVar()
        self.DUyear=StringVar()
        self.DUtimea=StringVar()
        self.DUtimeb=StringVar()
        self.DUtimec=StringVar()
        self.Location=StringVar()
        self.Type=StringVar()

        
        self.OMDUMonth=OptionMenu(myFrame, self.DUmonth, "Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec")
        self.OMDUMonth.grid(row=1,column=2)

        self.OMDUday=OptionMenu(myFrame, self.DUday, "01","02","03","04","05","06", "07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.OMDUday.grid(row=1,column=4)

        self.OMDUyear=OptionMenu(myFrame, self.DUyear, "13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.OMDUyear.grid(row=1,column=6)

        self.OMDUtimea=OptionMenu(myFrame, self.DUtimea,"01:", "02:", "03:", "04:", "05:", "06:", "07:", "08:", "09:","10:","11:","12:")
        self.OMDUtimea.grid(row =1, column =8)

        self.OMDUtimeb=OptionMenu(myFrame, self.DUtimeb, "00", "01", "02", "03","04", "05", "06", "07", "08", "09","10", "11", "12", "13","14", "15", "16", "17", "18", "19","20", "21", "22", "23","24", "25", "26", "27", "28", "29","30", "31", "32", "33","34", "35", "36", "37", "38", "39","40", "41", "42", "43","44", "45", "46", "47", "48", "49","50", "51", "52", "53","54", "55", "56", "57", "58", "59")
        self.OMDUtimeb.grid(row = 1, column =9)

        self.OMDUtimec=OptionMenu(myFrame, self.DUtimec, "AM", "PM")
        self.OMDUtimec.grid(row = 1, column =10)

        self.SearchButton=Button(myFrame, text="Search", command=self.search).grid(row=5, column=5, sticky="E")
        
        self.OMLocation=OptionMenu(myFrame, self.Location,"")
        self.OMLocation.grid(column=2, row=2)
        self.places()
        self.OMCar=OptionMenu(myFrame, self.Type,"")
        self.OMCar.grid(column=2, row=3)
        self.cars()
        #self.RentCar.withdraw()

        
    def places(self):
        db = self.connectMySQL()
        placeList=[]
        cursor = self.db.cursor()    
        sql ="SELECT DISTINCT location_name FROM location"
        cursor.execute(sql)
        for item in cursor:
            placeList.append(item)
        self.placeList=placeList
        counter=0
        for item in self.placeList:
            print (item)
            self.OMLocation['menu'].insert('end','command', label=item[0], command=_setit(self.Location, item[0]))
            counter+=1
        self.db.close()
        
 
        
    def cars(self):
        self.connectMySQL()
        typeList=[]
        cursor = self.db.cursor()    
        sql ="SELECT DISTINCT type FROM car_information"
        cursor.execute(sql)
        for item in cursor:
            typeList.append(item)
        self.typeList=typeList
        counter=0
        for item in self.typeList:
            print (item)
            self.OMCar['menu'].insert('end','command', label=item[0], command=_setit(self.Type, item[0]))
            counter+=1
        self.db.close()

    def search(self):
        self.RentCar.destroy()
        PUhours = int(self.PUtimea.get()[:-1])
        if self.PUtimec.get() == "PM":
            PUhours += 12
        DUhours = int(self.DUtimea.get()[:-1])
        if self.DUtimec.get() == "PM":
            DUhours += 12
        
        availability.Register().run(datetime(int("20"+self.PUyear.get()),
                                             self.monthToInt(self.PUmonth.get()),
                                             int(self.PUday.get()),
                                             PUhours,
                                             int(self.DUtimeb.get())),
                                    datetime(int("20"+self.DUyear.get()),
                                             self.monthToInt(self.DUmonth.get()),
                                             int(self.DUday.get()),
                                             DUhours,
                                             int(self.DUtimeb.get())),
                                    self.Type.get(),
                                    self.Location.get(),
                                    self.username)
                                    
                                             

    
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
#            messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")
    def monthToInt(self, month):
        if (month == "Jan"): return 1
        elif (month== "Feb"): return 2
        elif (month== "Mar"): return 3
        elif (month== "Apr"): return 4
        elif (month== "May"): return 5
        elif (month== "June"): return 6
        elif (month== "July"): return 7
        elif (month== "Aug"): return 8
        elif (month== "Sept"): return 9
        elif (month== "Oct"): return 10
        elif (month== "Nov"): return 11
        elif (month== "Dec"): return 12
        return 0

