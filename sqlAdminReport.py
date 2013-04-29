
from tkinter import *
import pymysql

class Register():
    def run(self):
        self.myWin = Tk()
        self.label = Label(self.myWin, text="Report for Last Three Months")
        self.label.pack(side=TOP)
        self.listboxes = []
        for i in range(5):
            self.listboxes += [Listbox(self.myWin, width=20)]
            self.listboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Vehicle Sno",
                  "Type",
                  "Car Model",
                  "Reservation Revenue",
                  "Late Fees Revenue"]:
            self.listboxes[index].insert(END, i)
            index += 1
        """v = IntVar()
        for i in range(10):
            for j in range(5):
                self.listboxes[j].insert(END, i)"""

        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql =  "SELECT reservation.vehicle_sno, "
        sql += "TYPE , model_name, SUM( estimated_cost ) AS total_cost, SUM( late_fees ) AS total_late "
        sql += "FROM reservation "
        sql += "LEFT JOIN car_information ON reservation.vehicle_sno "
        sql += "GROUP BY vehicle_sno "
        sql += "LIMIT 0 , 30 "
        cursor.execute(sql)

        for item in cursor:
            print(item)
            for i in range(5):
                self.listboxes[i].insert(END,item[i] if (item[i] != None) else "None")
        self.db.commit()
        

        
        #self.cancel2()


    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")


