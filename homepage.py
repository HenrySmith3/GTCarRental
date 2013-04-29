from tkinter import *
import newRental
import personalinfo
import rentalinfo

class Register():
    def run(self, username):
        self.username = username
        self.myWin=Tk()

        self.myWin.title("Homepage")
        myFrame=Frame(self.myWin)
        myFrame.pack()
        self.v=StringVar()
        self.v.set(1)
        self.RentaCar=Radiobutton(myFrame, text="Rent a Car", variable=self.v, value=1).pack(anchor=W)
        self.Getinfo=Radiobutton(myFrame, text="Enter/ View Personal Information", variable=self.v, value=2).pack(anchor=W)
        self.RentalInfo=Radiobutton(myFrame, text="Get Rental Info", variable=self.v, value=3).pack(anchor=W)
        self.NextButton=Button(myFrame, text="Next", command=self.onto).pack(anchor=E)
        #self.myWinHomepage.withdraw()

    def onto(self):
        option=self.v.get()
        if int(option)==1:
            newRental.Register().run(self.username)
        elif int(option)==2:
            personalinfo.Register().run(self.username)
        elif int(option)==3:
            rentalinfo.Register().run(self.username)
            
