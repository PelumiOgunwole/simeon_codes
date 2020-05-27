import random
import pandas as pd

class EmptyQueueError(Exception):
    pass

class Participants:
    @ classmethod
    def Names(cls):
        name=input("Insert Your Full Name: ").upper()
        return name

    @staticmethod
    def number():
        number = int(input("Insert your phone Number:"))
        return number
    def account(self):
        acctDetails = input("Insert your Verified Account Number: ")
        return acctDetails
    def mail(self):
        email = input("Insert your email: ").lower()
        return email
    def Address(self):
        Address = input("Insert your Home Address: ")
        return Address
    def identity(self):
        ID = random.randint(1111, 9999)
        return ID



class Ponzi_Scheme(Participants):
    def __init__(self):
        super().__init__()
        self.initAmount=5000
        self.Total_Amount = 0
        self.items = []
        self.front = 0
        self.others=[]


    def isEmpty(self):
        return self.items==[]

    def Add_Participant(self):
        new = self.items.append(Participants.Names())
        return new

    def total_Amount(self):
        if len(self.items) >3:
            y=len(self.items)+1-self.front
            r= y * self.initAmount
            return r
        else:
            y=len(self.items)-self.front
            z= y * self.initAmount
            return z

    def Remove_Participant(self):

        if self.isEmpty():
            raise EmptyQueueError("The queue is Empty")

        remainder=self.total_Amount()- 10000
        print(remainder)
        if remainder >= 5000: # This consider is to ensure that there is no zero balance, you can use it as it suits you
            x = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            return x

        else:print("No Payment Now, You wait till we have enough Members")


    def displayParticipants(self):
        print(list(self.items))


if __name__ == '__main__':
    ponzi=Ponzi_Scheme()
    par=Participants

    while True:
        print("Choose Y to pay OR N not to pay")
        print("You are to pay the sum of $5,000 to participate in this scheme")
        choices = input("Do you want to pay for registeration or not? ").upper()
        if choices == 'Y':

            print("Welcome ", "to Uncle Boscho's Ponzi Scheme")

            print("Registration Successful, Congrats. You are on your way to gain whooping sum of $15000")
            print("please provide other details")
            newParticipant = ponzi.Add_Participant()
            Y=ponzi.total_Amount()
            print("Total Amount is: ",Y)
            ponzi.displayParticipants()
            remove=ponzi.Remove_Participant()
            if remove==None:
                print("Nobody is receiving payment.")
            else:
                print("The Participant paid is: ",remove,"and he is credited $",10000)
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
                print("Paid Members:\t\t\t\t ", "Amount Paid:\t\t\t\t", "Phone Number:\t\t\t\t", "Email:\t\t\t\t",
                      "I.D:\t\t\t\t", "Account No:\t\t\t\t")
                print("\t\t", remove, "\t\t\t", Participants.number(), "\t\t\t")
        elif choices == "N":
            print("Come back later when you have your registration fees. Thanks")
            break
