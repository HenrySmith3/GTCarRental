
from tkinter import *
import pymysql

class Register():
    def run(self):

        myWin = Tk()

        self.label = Label(myWin, text="Frequent Users Report")
        self.label.pack(side=TOP)
        self.listboxes = []
        for i in range(3):
            self.listboxes += [Listbox(myWin, width=40)]
            self.listboxes[i].pack(side=LEFT)
        index = 0
        for i in ["Username",
                  "Driving Plan",
                  "Number of Reservations per Month"]:
            self.listboxes[index].insert(END, i)
            index += 1
        v = IntVar()
        """
        for i in range(10):
            for j in range(3):
                self.listboxes[j].insert(END, i)"""
        
        self.connectMySQL()
               
        cursor = self.db.cursor()    
        sql =  "SELECT reservation.username, plan_type, COUNT( * ) FROM reservation "
        sql += "LEFT JOIN gt_student ON reservation.username = gt_student.username "
        sql += "WHERE reservation.pickup_date BETWEEN DATE_ADD( NOW( ) , INTERVAL -3 MONTH) AND NOW( ) "
        sql += "GROUP BY reservation.username "
        sql += "ORDER BY COUNT( * ) DESC LIMIT 0 , 5 "
        cursor.execute(sql)

        for item in cursor:
            print(item)
            for i in range(3):
                self.listboxes[i].insert(END,item[i] if (item[i] != None) else "None")
        self.db.commit()

    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
            #messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")


