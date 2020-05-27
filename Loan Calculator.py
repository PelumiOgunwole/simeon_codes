"""A program to calculate payment to be made by a person who borrows money from a finacial institution """
from tkinter import *

class Loancalculator:
    def __init__(self):
        root = Tk()
        root.title("Loan Calculator")
        Label(root,text="Annual Interest RAte").grid(row=1,column=1,sticky=W)
        Label(root, text="Number Of Years").grid(row=2, column=1, sticky=W)
        Label(root, text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(root, text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(root, text="Total Payment").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar=IntVar()
        Entry(root,text=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
        self.noOfYears=IntVar()
        Entry(root, text=self.noOfYears, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar=IntVar()
        Entry(root, text=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar=IntVar()
        lblMonthlyPayment=Label(root, textvariable=self.monthlyPaymentVar, justify=RIGHT).grid(row=4, column=2,sticky=E)
        self.totalPaymentVar=IntVar()
        lblTotalPayment=Label(root,textvariable=self.totalPaymentVar,justify=RIGHT).grid(row=5,column=2,sticky=E)
        btComputePayment=Button(root,text="Compute Payment",command=self.computePayment).grid(row=6,column=2,sticky=E)
        root.mainloop()

    def monthPayment(self):
        annualInterestRate = self.annualInterestRateVar.get()
        noOfYears = self.noOfYears.get()
        monthlyInterestRate = (annualInterestRate / 12) / 100
        noOfMontlyPayments = noOfYears * 12
        monthlyPayment = self.loanAmountVar.get() * monthlyInterestRate / (
                1 - (1 + monthlyInterestRate) ** -noOfMontlyPayments)
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.3f"))
        return self.monthlyPaymentVar

    def computePayment(self):
        self.monthPayment()
        totalpayment = self.monthlyPaymentVar.get() * 12 * self.noOfYears.get()
        self.totalPaymentVar.set(format(totalpayment, "10.3f"))
        return self.totalPaymentVar

Loancalculator()


