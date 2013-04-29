from tkinter import *
import managecars
import sqlMaintenanceHistoryReport
import RentalChangeRequest
import sqlLocationPreferenceReport
import sqlFrequentUsersReport
import sqlMaintenanceHistoryReport
import RentalChangeRequest
import MaintenanceRequest

class Register():
    def run(self, username):
        self.username = username
        self.myWin=Tk()

        self.myWin.title("Homepage")
        myFrame=Frame(self.myWin)
        myFrame.pack()
        self.v=StringVar()
        self.v.set(1)
        self.RentaCar=Radiobutton(myFrame, text="Manage Cars", variable=self.v, value=1).pack(anchor=W)
        self.Getinfo=Radiobutton(myFrame, text="Maintenance Requests", variable=self.v, value=2).pack(anchor=W)
        self.RentalInfo=Radiobutton(myFrame, text="Rental Change Request", variable=self.v, value=3).pack(anchor=W)
        self.RentalInfo=Radiobutton(myFrame, text="View Reports", variable=self.v, value=4).pack(anchor=W)
        self.ReportVar=StringVar()
        self.ReportType=OptionMenu(myFrame, self.ReportVar,
        "Location Preference", "Frequent Users", "Maintenance History")
        self.ReportType.pack(anchor=E)
        self.NextButton=Button(myFrame, text="Next", command=self.onto).pack(anchor=E)
        #self.myWinHomepage.withdraw()

    def onto(self):
        option=self.v.get()
        if int(option)==1:
            managecars.Register().run()
        elif int(option)==2:
            MaintenanceRequest.Register().run(self.username)
        elif int(option)==3:
            RentalChangeRequest.Register().run()
        elif int(option)==4:
            choice = self.ReportVar.get()
            if choice == "Location Preference":
                sqlLocationPreferenceReport.Register().run()
            if choice == "Frequent Users":
                sqlFrequentUsersReport.Register().run()
            if choice == "Maintenance History":
                sqlMaintenanceHistoryReport.Register().run()
            
            
