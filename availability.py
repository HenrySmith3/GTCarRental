from datetime import *
from time import *
from tkinter import *
import pymysql
import homepage

class Register():
    def run(self, pickupDate, returnDate, carType, location, username):
#example: run(myWin, datetime(2017,4,20,10,00,00), datetime(2017,4,20,00,00,00), "Sedan", "Peters", "hsmith41")

        self.username = username
        myWin = Toplevel()
        self.myWin = myWin
        self.pickupDateString = pickupDate.strftime("%Y-%m-%d %H:%M:%S")
        self.returnDateString = returnDate.strftime("%Y-%m-%d %H:%M:%S")
        self.label = Label(myWin, text="Availability")
        self.label.pack(side=TOP)
        button = Button(myWin, text="Reserve", command=self.reserve)
        button.pack(side=BOTTOM)
        self.listboxes = []
        widths = [14,10,10,12,17,17,17,8,15,16,10,12,18,15]
        for i in range(14):
            self.listboxes += [Listbox(myWin, width=widths[i], font=('Helvetica', 8))]
            self.listboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Reservation #",
                  "Car Model",
                  "Car Type",
                  "Location",
                  "Hourly Rate (Occ)",
                  "Hourly Rate (Freq)",
                  "Discount Rate (Daily)",
                  "Daily Rate",
                  "Seating Capacity",
                  "Transmission Type",
                  "Bluetooth",
                  "Auxillary Cable",
                  "Available Until",
                  "Estimated Cost"]:
            self.listboxes[index].insert(END, i)
            index += 1
        v = IntVar()
        """
        for i in range(10):
            for j in range(13):
                self.listboxes[j].insert(END, i)
            
            b = Radiobutton(myWin, variable=v, value=i)
            self.listboxes[13].insert(END, b)"""

        self.variable = StringVar()
        self.selectionMenu = OptionMenu(myWin, self.variable,"")
        self.selectionMenu.pack()
        menu = self.selectionMenu["menu"]
        menu.delete(0, "end")
        
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql = "SELECT plan_type FROM gt_student "  
        sql += "WHERE gt_student.username = %s"

        
        
        cursor.execute(sql, (username))
        planType = ""
        for item in cursor:
            planType = item[0]
        
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql = "SELECT * FROM car_information "  
        sql += "LEFT JOIN reservation "
        sql += "ON car_information.vehicle_sno= reservation.vehicle_sno "
        sql += "WHERE ((reservation.pickup_date NOT BETWEEN %s AND %s "
        sql += "AND reservation.return_date NOT BETWEEN %s AND %s) "
        sql += "OR (reservation.pickup_date IS NULL)) "
        sql += "AND car_information.type = %s "
        sql += "GROUP BY car_information.location "
        sql += "ORDER BY CASE WHEN car_information.location=%s then 0 else 1 end "

        
        
        cursor.execute(sql, (self.pickupDateString, self.returnDateString,
                             self.pickupDateString, self.returnDateString,
                             carType, location))
        count=1
        self.vehicle_snos = [0]
        for item in cursor:
            print(item)
            self.vehicle_snos += [item[0]]
            self.insertToColumn(count, 0)
            self.insertToColumn(item[9],1)
            self.insertToColumn(item[8],2)
            self.insertToColumn(item[11],3)
            self.insertToColumn(self.formatMoney(item[6]),4)
            self.insertToColumn(self.formatMoney(item[6]*.9),5)
            self.insertToColumn(self.formatMoney(item[5]*.9),6)
            self.insertToColumn(self.formatMoney(item[5]),7)
            self.insertToColumn(item[3],8)
            self.insertToColumn(item[2],9)
            self.insertToColumn(item[4],10)
            self.insertToColumn(item[1],11) 
            self.insertToColumn(item[13],12)
            estimatedCost = item[6]
            if planType.lower() == "frequent":
                estimatedCost *= .9
                estimatedCost *= (pickupDate-returnDate).total_seconds()/(60*60)
            elif planType.lower() == "daily":
                estimatedCost = item[5]*.9
                estimatedCost *= (pickupDate-returnDate).days
            estimatedCost = self.formatMoney(estimatedCost)
            
            self.insertToColumn(estimatedCost,13)
            count += 1
            #for i in range(13):
            #    self.listboxes[i].insert(END,item[i] if (item[i] != None) else "None")
        self.db.commit()
        for i in range(count-1):
            string = i+1
            menu.add_command(label=string, 
                             command=lambda value=string:
                                  self.variable.set(value))


        
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")

    def insertToColumn(self, toInsert, column):
        self.listboxes[column].insert(END,toInsert if (toInsert != None) else "None")
    def formatMoney(self, number):
        adjusted = number/100.0
        return ('%.2f' % adjusted)
    def reserve(self):        
        self.connectMySQL()
               
        cursor = self.db.cursor() 
        sql = "INSERT INTO  `cs4400_Group_18`.`reservation` ( "
        sql +="`pickup_date` ,`return_date` ,`late_by` ,`estimated_cost` , "
        sql +="`return_status` ,`extended_time` ,`late_fees` ,`location_name` , "
        sql +="`vehicle_sno` , `username`) "
        sql +=" VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (self.pickupDateString, self.returnDateString, "NULL",
                             self.listboxes[13].get(self.variable.get()), "N", "NULL", "NULL",
                             self.listboxes[3].get(self.variable.get()),
                             self.vehicle_snos[int(self.variable.get())],
                             self.username))
        self.myWin.destroy()
    
