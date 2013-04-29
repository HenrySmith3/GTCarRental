from time import *
from datetime import *
from tkinter import *
import pymysql

class Register():
    def run(self, username):

        myWin = Toplevel()
        self.username = username
        self.canvas = Canvas(myWin)

        self.canvas.pack(side=TOP)
        self.innerCanvas = Canvas(self.canvas)
        self.innerCanvas.pack(side=BOTTOM)

        self.dateVar = StringVar()
        self.dateVar.set("Select Reservation")
        self.selectionMenu = OptionMenu(self.innerCanvas, self.dateVar, 1)
        self.selectionMenu.pack(side=TOP)
        
        self.label = Label(self.innerCanvas, text="Choose Return Time:   ")
        #self.label.grid(column=1, row=0)
        self.label.pack(side=LEFT)

        
        self.dateLabel = Label(self.innerCanvas, text="Date: ")
        self.dateLabel.pack(side=LEFT)
        #self.dateMenu = OptionMenu(self.innerCanvas, self.dateVar, "a","b","c")
        #self.dateMenu.pack(side=LEFT)

        #DATE MENU SHAMELESSLY STOLEN

        minutes = []
        for i in range(60):
            minutes += [i+1]
            
        self.OR2var = StringVar()
        self.listboxOR2=OptionMenu(self.innerCanvas, self.OR2var, *tuple(minutes[0:12]))
        self.listboxOR2.pack(side=LEFT)

        self.OR3var = StringVar()
        self.listboxOR3=OptionMenu(self.innerCanvas, self.OR3var, *tuple(minutes[0:31]))
        self.listboxOR3.pack(side=LEFT)
        self.yearlabel = Label(self.innerCanvas, text="20")
        self.yearlabel.pack(side=LEFT)
                               
        self.OR4var = StringVar()
        self.listboxOR4=OptionMenu(self.innerCanvas, self.OR4var, *tuple(minutes[12:]))
        self.listboxOR4.pack(side=LEFT)
        #END DATE SECTION

        self.timeLabel = Label(self.innerCanvas, text="Time: ")
        self.timeLabel.pack(side=LEFT)
        #self.timeVar = StringVar()
        #self.timeVar.set("b")
        #self.timeMenu = OptionMenu(self.innerCanvas, self.timeVar, "a","b","c")
        #self.timeMenu.pack(side=LEFT)

        self.OR5var = StringVar()
        self.listboxOR5=OptionMenu(self.innerCanvas, self.OR5var, *tuple(minutes[:12]))
        self.listboxOR5.pack(side=LEFT)

        self.OR6var = StringVar()
        self.listboxOR6=OptionMenu(self.innerCanvas, self.OR6var, *tuple(minutes))
        self.listboxOR6.pack(side=LEFT)

        self.OR7var = StringVar()
        self.listboxOR7=OptionMenu(self.innerCanvas, self.OR7var, "AM", "PM")
        self.listboxOR7.pack(side=LEFT)

        
        self.button = Button(self.innerCanvas, text="UPDATE", command=self.update)
        self.button.pack(side=LEFT)
        self.listboxes = []
        for i in range(6):
            self.listboxes += [Listbox(self.canvas, width=20)]
            self.listboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Reservation Number",
                  "Date",
                  "Reservation Time",
                  "Car",
                  "Location",
                  "Amount"]:
            self.listboxes[index].insert(END, i)
            index += 1
        self.radioButtonCanvas = Canvas(self.canvas)
        self.radioButtonCanvas.pack(side=LEFT)
        v = IntVar()


        #SQL SECTION

        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql =  "SELECT car_information.type, car_information.location, reservation.pickup_date, reservation.return_date, car_information.model_name, reservation.estimated_cost, car_information.vehicle_sno "
        sql += "FROM car_information "
        sql += "LEFT JOIN reservation ON car_information.vehicle_sno= reservation.vehicle_sno "
        sql += "WHERE reservation.return_date>NOW() "
        sql += "AND reservation.username = %s"

        cursor.execute(sql, (username))
        counter = 1
        self.vehicle_snos = []
        for item in cursor:
            print(item)
            self.insertToColumn(counter, 0)
            self.insertToColumn(item[2].strftime("%Y-%m-%d"), 1)
            self.insertToColumn(item[2].strftime("%H:%M:%S"), 2)
            self.insertToColumn(item[4], 3)
            self.insertToColumn(item[1], 4)
            self.insertToColumn(self.formatMoney(item[5]), 5)
            self.vehicle_snos += [item[6]]
            counter += 1
        menu = self.selectionMenu["menu"]
        menu.delete(0, "end")
        for i in range(counter-1):
            string = i+1
            menu.add_command(label=string, 
                             command=lambda value=string:
                                  self.dateVar.set(value))
        self.db.commit()

        """for i in range(10):
            for j in range(6):
                self.listboxes[j].insert(END, i)"""
            
            #b = Radiobutton(self.radioButtonCanvas, variable=v, value=i, height=1, pady=0)
            #b.pack(side=TOP)



        self.lowerCanvas = Canvas(myWin)
        self.lowerCanvas.pack(side=BOTTOM)

        self.lowerListboxes = []
        for i in range(6):
            self.lowerListboxes += [Listbox(self.lowerCanvas, width=20)]
            self.lowerListboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Date",
                  "Reservation Time",
                  "Car",
                  "Location",
                  "Amount",
                  "Return Status"]:
            self.lowerListboxes[index].insert(END, i)
            index += 1

            
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql =  "SELECT car_information.location, reservation.pickup_date, car_information.model_name, reservation.estimated_cost, reservation.return_status "
        sql += "FROM car_information "
        sql += "LEFT JOIN reservation ON car_information.vehicle_sno= reservation.vehicle_sno "
        sql += "WHERE reservation.return_date<NOW() "
        sql += "AND reservation.username = %s"

        cursor.execute(sql, (username))
        counter = 1
        for item in cursor:
            print(item)
            self.insertToColumnL(item[1].strftime("%Y-%m-%d"), 0)
            self.insertToColumnL(item[1].strftime("%H:%M:%S"), 1)
            self.insertToColumnL(item[2], 2)
            self.insertToColumnL(item[0], 3)
            self.insertToColumnL(self.formatMoney(item[3]), 4)
            self.insertToColumnL(item[4], 5)
            
            counter += 1
        """for i in range(10):
            for j in range(6):
                self.lowerListboxes[j].insert(END, i)"""


    def listboxOR(self):
        counter=1
        for item in ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]:
            self.listboxOR1.insert(counter, item)
            counter+=1

    def listboxORday(self):
        counter=1
        for item in range(1,32):
            self.listboxOR2.insert(counter, str(counter))
            counter+=1

    def listboxORhour(self):
        counter=1
        for item in range(1,25):
            self.listboxOR3.insert(counter, str(counter))
            counter+=1

    def listboxORminute(self):
        counter=1
        for item in range(1,61):
            self.listboxOR4.insert(counter, str(counter))
            counter+=1
    def lbyearOR(self):
        counter=1
        for item in range(1,32):
            if counter<10:
                
                self.listboxyearOR.insert(counter, str(0)+str(counter))
                
            else:
                self.listboxyearOR.insert(counter, str(counter))
            counter+=1

    def listboxNA(self):
        counter=1
        for item in ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]:
            self.listboxNA1.insert(counter, item)
            counter+=1

    def listboxNAday(self):
        counter=1
        for item in range(1,32):
            self.listboxNA2.insert(counter, str(counter))
            counter+=1
    def lbyearNA(self):
        counter=1
        for item in range(1,32):
            if counter<10:
                
                self.listboxyearNA.insert(counter, str(0)+str(counter))
                
            else:
                self.listboxyearNA.insert(counter, str(counter))
            counter+=1
###############################################
    def listboxPU(self):
        counter=1
        for item in ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]:
            self.listboxPU1.insert(counter, item)
            counter+=1

    def listboxPUday(self):
        counter=1
        for item in range(1,32):
            self.listboxPU2.insert(counter, str(counter))
            counter+=1
    def lbyearPU(self):
        counter=1
        for item in range(1,32):
            if counter<10:
                
                self.listboxyearPU.insert(counter, str(0)+str(counter))
                
            else:
                self.listboxyearPU.insert(counter, str(counter))
            counter+=1

    def listboxRT(self):
        counter=1
        for item in ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]:
            self.listboxRT1.insert(counter, item)
            counter+=1

    def listboxRTday(self):
        counter=1
        for item in range(1,32):
            self.listboxRT2.insert(counter, str(counter))
            counter+=1
    def lbyearRT(self):
        counter=1
        for item in range(1,32):
            if counter<10:
                
                self.listboxyearRT.insert(counter, str(0)+str(counter))
                
            else:
                self.listboxyearRT.insert(counter, str(counter))
            counter+=1
##
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        (print (selection))

    def update(self):
        self.connectMySQL()
        affectedCar = ""
        cursor = self.db.cursor()
        hours = int(self.OR5var.get())
        if self.OR7var.get() == "PM":
            hours += 12
        returnTime = datetime(int("20" + self.OR4var.get()),
                              int(self.OR2var.get()),
                              int(self.OR3var.get()),
                              hours,
                              int(self.OR6var.get()))
        returnTimeString = returnTime.strftime("%Y-%m-%d %H:%M:%S")
        affectedCar = self.vehicle_snos[int(self.dateVar.get())-1]
        affectedReservationReturnDate = ""
        #This query gets the return date for whoever this change effects
        sql =  "SELECT reservation.return_date FROM reservation "
        sql += "WHERE reservation.vehicle_sno = %s "
        sql += "AND reservation.return_date>NOW() "
        sql += "AND reservation.return_date< %s "
        cursor.execute(sql, (affectedCar, returnTimeString))
        for item in cursor:
            print(item)
            affectedReservationReturnDate = item[0]
        self.db.commit()
        

        oldCost = oldDate = hourlyRate = ""
        #This query gets the cost and date of the old reservation, as well as the hourly rate of the car.
        sql = "SELECT reservation.estimated_cost, reservation.return_date, car_information.hourly_rate "
        sql +="FROM reservation LEFT JOIN car_information ON reservation.vehicle_sno = car_information.vehicle_sno "
        sql +="WHERE reservation.vehicle_sno = %s AND reservation.username = %s "
        cursor.execute(sql, (affectedCar, self.username))
        for item in cursor:
            oldCost = item[0]
            oldDate = item[1]
            hourlyRate = item[2]

        
        newCost = oldCost+(((returnTime-oldDate).total_seconds()/(60*60))*hourlyRate)
        #This updates the table for the new cost of rental
        sql = "UPDATE reservation SET estimated_cost = %s,  "
        sql += "return_date= %s "
        sql += "WHERE vehicle_sno = %s AND return_date = %s "
        cursor.execute(sql, (newCost, returnTimeString, affectedCar, oldDate))

        #This figures out if there was a user that this effects
        sql = "SELECT username FROM reservation WHERE vehicle_sno = %s "
        sql += "AND pickup_date BETWEEN %s AND %s "
        cursor.execute(sql, (affectedCar, oldDate, returnTimeString))
        affectedUsers = []
        for item in cursor:
            affectedUsers += [item[0]]
            #popup message alerting that somebdy needs to be called

        #assigning late fees
        hoursLate = (returnTime-oldDate).total_seconds()/(60*60)*50
        if len(affectedUsers) is not 0:
            sql = "UPDATE reservation SET late_fees = %s "
            sql += "WHERE return_date = %s "
            sql += "AND username = %s"
            cursor.execute(sql(hoursLate, returnTimeString, self.username))
            self.db.commit()
            for user in affectedUsers:
                sql = "SELECT phone FROM gt_student WHERE username = %s"
                cursor.execute(sql, (user))
                for item in cursor:
                    messagebox.showinfo("Please call " + user + " at " + item[0] + ". His car will be late")
                           
    def insertToColumn(self, toInsert, column):
        self.listboxes[column].insert(END,toInsert if (toInsert != None) else "None")
    def insertToColumnL(self, toInsert, column):
        self.lowerListboxes[column].insert(END,toInsert if (toInsert != None) else "None")
        
    def formatMoney(self, number):
        adjusted = number/100.0
        return ('%.2f' % adjusted)
    
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")

