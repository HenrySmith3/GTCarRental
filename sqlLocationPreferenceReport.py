
from tkinter import *
import pymysql

class Register():
    def run(self):

        myWin = Tk()

        self.label = Label(myWin, text="Report for Last Three Months")
        self.label.pack(side=TOP)
        self.listboxes = []
        for i in range(4):
            self.listboxes += [Listbox(myWin, width=40)]
            self.listboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Month",
                  "Location",
                  "Number of Reservations",
                  "Total Number of Hours"]:
            self.listboxes[index].insert(END, i)
            index += 1
            """
        v = IntVar()
        for i in range(10):
            for j in range(4):
                self.listboxes[j].insert(END, i)"""
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql =  "(SELECT '3 months ago' as month, reservation.location_name, COUNT(*) as count, SUM(HOUR(TIMEDIFF(reservation.return_date , reservation.pickup_date))) as hours FROM reservation "
        sql += "WHERE reservation.pickup_date BETWEEN DATE_ADD(NOW(), INTERVAL -3 MONTH)  AND DATE_ADD(NOW(), INTERVAL -2 MONTH) "
        sql += "GROUP BY reservation.location_name "
        sql += "ORDER BY count DESC) "
        sql += "UNION "
        sql += "(SELECT '2 months ago' as month, reservation.location_name, COUNT(*) as count, SUM(HOUR(TIMEDIFF(reservation.return_date , reservation.pickup_date))) as hours FROM reservation "
        sql += "WHERE reservation.pickup_date BETWEEN DATE_ADD(NOW(), INTERVAL -2 MONTH)  AND DATE_ADD(NOW(), INTERVAL -1 MONTH) "
        sql += "GROUP BY reservation.location_name "
        sql += "ORDER BY count DESC) "
        sql += "UNION "
        sql += "(SELECT '1 month ago' as month, reservation.location_name, COUNT(*) as count, SUM(HOUR(TIMEDIFF(reservation.return_date , reservation.pickup_date))) as hours FROM reservation "
        sql += "WHERE reservation.pickup_date BETWEEN DATE_ADD(NOW(), INTERVAL -1 MONTH)  AND NOW() "
        sql += "GROUP BY reservation.location_name "
        sql += "ORDER BY count DESC) "


        cursor.execute(sql)

        for item in cursor:
            print(item)
            for i in range(4):
                self.listboxes[i].insert(END,item[i] if (item[i] != None) else "None")
        self.db.commit()
                
    
    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")
