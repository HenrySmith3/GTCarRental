from tkinter import *
import time
import pymysql
import sqlDrivingPlans


class Register():
    def run(self, username):
        self.username= username
        self.root=Tk()


        myWin=self.root
        root = self.root

        frame=Frame(root, borderwidth=1, relief=SOLID)
        frame.pack(side=TOP)
        frame2=Frame(root, borderwidth=1, relief=SOLID)
        frame2.pack(side=TOP)
        frame3=Frame(root, borderwidth=1, relief=SOLID)
        frame3.pack(side=TOP)
        self.connectMySQL()
        cursor = self.db.cursor()
        sql =  "SELECT * "


        sql += "FROM gt_student, payment_information "


        sql += "WHERE gt_student.username =  %s "


        sql += "AND payment_information.username =  %s "
        cursor.execute(sql, (username, username))
        results = ["","","","","","","","","","","","","","",""]
        for item in cursor:
            results = item


            #for i in range(4):


            #    self.listboxes[i].insert(END,item[i] if (item[i] != None) else "None")
        self.results = results
        print(results)
        self.db.commit()

        self.geninfo = Label(frame, text="General Information")


        self.geninfo.grid(column=1, row=0, columnspan=4, sticky=N+S+E+W)

        self.refreshBTN = Button(frame, text="Info Not Appearing?", command=self.refresh)

        self.refreshBTN.grid(column=5, row=0)

        self.firstname = Label(frame, text="First Name:")


        self.firstname.grid(column=0, row=1, columnspan=2)
        self.firstname1 = StringVar()
        self.firstname2 = Entry(frame,  textvariable=self.firstname1)
        self.firstname1.set(results[4])
        self.firstname2.insert(0, results[4])
        


        self.firstname2.grid(column=3, row=1, columnspan=2)





        self.mi = Label(frame, text="Middle Initial:")


        self.mi.grid(column=0, row=2, columnspan=2)


        self.mi1 = StringVar()


        self.mi2 = Entry(frame, text="...", textvariable=self.mi1)

        self.mi2.insert(0, results[5])
        self.mi2.grid(column=3, row=2, columnspan=2)





        self.lastname = Label(frame, text="Last Name:")


        self.lastname.grid(column=0, row=3, columnspan=2)


        self.lastname1 = StringVar()


        self.lastname2 = Entry(frame, text="...", textvariable=self.lastname1)
        self.lastname2.grid(column=3, row=3, columnspan=2)
        self.lastname2.insert(0, results[6])




        self.email = Label(frame, text="Email Address:")


        self.email.grid(column=0, row=4, columnspan=2)


        self.email1 = StringVar()


        self.email2 = Entry(frame, text="...", textvariable=self.email1)


        self.email1.set(results[1])

        self.email2.grid(column=3, row=4, columnspan=2)
        self.email2.insert(0, results[1])

        self.phone = Label(frame, text="Phone Number:")


        self.phone.grid(column=0, row=5, columnspan=2)


        self.phone1 = StringVar()


        self.phone2 = Entry(frame, text="...", textvariable=self.phone1)


        self.phone1.set(results[7])


        self.phone2.grid(column=3, row=5, columnspan=2)

        self.phone2.insert(0, results[7])



        self.address = Label(frame, text="Address:")


        self.address.grid(column=0, row=6, columnspan=2)


        self.address1 = StringVar()


        self.address2 = Entry(frame, text="...", textvariable=self.address1)


        self.address1.set(results[2])


        self.address2.grid(column=3, row=6, columnspan=2)

        self.address2.insert(0, results[2])









        self.meminfo = Label(frame2, text="Membership Information")


        self.meminfo.grid(column=1, row=0, columnspan=1, sticky=N+S+E+W)





        self.choose = Label(frame2, text="CHOOSE A PLAN")


        self.choose.grid(column=1, row=1, columnspan=1, sticky=N+S+E+W)

        self.planButton = Button(frame2, text="View Plans", command=self.viewPlans)

        self.planButton.grid(column=2, row=1)

        self.v=IntVar()


        self.occdriv = Radiobutton(frame2, text="Occasional Driving", variable=self.v, value=1, bg="yellow")


        self.occdriv.grid(column=0, row=2)





        self.freqdriv = Radiobutton(frame2, text="Frequent Driving", variable=self.v, value=2, bg="yellow")


        self.freqdriv.grid(column=1, row=2)





        self.dailydriv = Radiobutton(frame2, text="Daily Driving", variable=self.v, value=3, bg="yellow")


        self.dailydriv.grid(column=2, row=2)

        self.v.set(1)


        if results[3] == "Occasional":


            self.v.set(1)


        elif results[3] == "Frequent":


            self.v.set(2)


        elif results[3] == "Daily":


            self.v.set(3)









        self.payinfo = Label(frame3, text="Payment Information")


        self.payinfo.grid(column=1, row=0, columnspan=4, sticky=N+S+E+W)





        self.name = Label(frame3, text="Name on Card:")


        self.name.grid(column=0, row=1, columnspan=2)


        self.name1 = StringVar()


        self.name2 = Entry(frame3, text="...", textvariable=self.name1)


        self.name1.set(results[11])


        self.name2.grid(column=3, row=1, columnspan=2)
        self.name2.insert(0, results[11])



        self.cc = Label(frame3, text="Card Number:")


        self.cc.grid(column=0, row=2, columnspan=2)


        self.cc1 = StringVar()


        self.cc2 = Entry(frame3, text="...", textvariable=self.cc1)


        self.cc1.set(results[13])


        self.cc2.grid(column=3, row=2, columnspan=2)


        self.cc2.insert(0, results[13])


        self.ccv = Label(frame3, text="CCV:")


        self.ccv.grid(column=0, row=3, columnspan=2)


        self.ccv1 = StringVar()


        self.ccv2 = Entry(frame3, text="...", textvariable=self.ccv1)


        self.ccv1.set(results[12])


        self.ccv2.grid(column=3, row=3, columnspan=2)

        self.ccv2.insert(0, results[12])



        self.exdate = Label(frame3, text="Expiry Date:")


        self.exdate.grid(column=0, row=4, columnspan=2)


        self.exdate1 = StringVar()


        self.exdate2 = Entry(frame3, text="...", textvariable=self.exdate1)


        self.exdate1.set(results[10])


        self.exdate2.grid(column=3, row=4, columnspan=2)

        self.exdate2.insert(0, results[10])



        self.bill = Label(frame3, text="Billing Address:")


        self.bill.grid(column=0, row=5, columnspan=2)


        self.bill1 = StringVar()


        self.bill2 = Entry(frame3, text="...", textvariable=self.bill1)


        self.bill1.set(results[9])


        self.bill2.grid(column=3, row=5, columnspan=2)
        self.bill2.insert(0, results[9])
        self.button = Button(root, text="Submit", command=self.buttonHandler)


        self.button.pack()
        myWin.mainloop()

    def viewPlans(self):
        sqlDrivingPlans.Register().run()
    def refresh(self):
        print("results", self.results)
        print(self.firstname1.get())
        self.firstname1.set(self.results[4])
        self.mi1.set(self.results[5])
        self.lastname1.set(self.results[6])
        self.email1.set(self.results[1])
        self.phone1.set(self.results[7])
        self.address1.set(self.results[2])
        if self.results[3] == "Occasional":
                self.v.set(1)
        elif self.results[3] == "Frequent":
            self.v.set(2)
        elif self.results[3] == "Daily":
            self.v.set(3)
        self.name1.set(self.results[11])
        self.cc1.set(self.results[13])
        self.ccv1.set(self.results[12])
        self.exdate1.set(self.results[10])
        self.bill1.set(self.results[9])
        self.root.update_idletasks()
        self.root.mainloop()
    def buttonHandler(self):

        self.connectMySQL()

        cursor = self.db.cursor()

        sql =  "UPDATE gt_student SET "

        sql += "gt_student.first_name=IFNULL(%s, gt_student.first_name), "

        sql += "gt_student.middle_initial=IFNULL(%s, gt_student.middle_initial), "

        sql += "gt_student.last_name=IFNULL(%s, gt_student.last_name), "

        sql += "gt_student.email=IFNULL(%s, gt_student.email), "

        sql += "gt_student.phone=IFNULL(%s, gt_student.phone), "

        sql += "gt_student.plan_type=IFNULL(%s, gt_student.plan_type) "

        sql += "WHERE gt_student.username = %s "

        planType = ""

        if self.v.get() == 1:

            planType = "Occasional"

        elif self.v.get() == 2:

            planType = "Frequent"

        elif self.v.get() == 3:

            planType = "Daily"

        cursor.execute(sql, (self.firstname1.get(),


                             self.mi1.get(),


                             self.lastname1.get(),


                             self.email1.get(),


                             self.phone1.get(),


                             planType,


                             self.username))

        self.db.commit()


        self.connectMySQL()

        cursor = self.db.cursor()

        sql = "UPDATE payment_information SET "

        sql += "payment_information.name_on_card=IFNULL(%s, payment_information.name_on_card), "

        sql += "payment_information.billing_address=IFNULL(%s, payment_information.billing_address), "

        sql += "payment_information.expiration_date=IFNULL(%s, payment_information.expiration_date), "

        sql += "payment_information.card_number=IFNULL(%s,  payment_information.card_number), "

        sql += "payment_information.ccv=IFNULL(%s, payment_information.ccv) "

        sql += "WHERE payment_information.username = %s"
        cursor.execute(sql, (self.name1.get(),
                             self.bill1.get(),
                             self.exdate1.get(),
                             self.cc1.get(),
                             self.ccv1.get(),
                             self.username))


        self.db.commit()
#        sqlDrivingPlans.Register().run()

    def connectMySQL(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu", user="cs4400_Group_18", passwd= "_gohAEAP", db="cs4400_Group_18")
#            messagebox.showwarning("Internet Connection", "Connected!")
        except:
            messagebox.showwarning("Internet Connection", "Please check your internet connection")


