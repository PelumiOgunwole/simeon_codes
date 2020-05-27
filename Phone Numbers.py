
"""The aim of this project is to search for amount of phone numbers starting with prefix (0803) in a 10 million population"""
import random,re
myZero="0"
pattern="^(0803)"
pattern2 = "0803\d{7}"
box,box1=[],[]
number=0
regex2=0
class Phone_Numbers():
    def scope(self):
        count = 0
        global number
        global regex2
        for r in range(10000000):# Check in 10^7 numbers
            initials = random.randint(1111, 9999)
            rear = random.randint(1111111, 9999999)
            number = myZero + str(initials) + str(rear)
            "Use the regex to find numbers starting with 0803 and regex2 to print the numbers out"
            regex = re.findall(pattern, number)
            regex2 = re.findall(pattern2, number)
            if regex:
                box.append(regex)
            else:
                box.append(0)
            if regex2:
                box1.append(regex2)
            else:
                box1.append(0)
        for cout in box:
            if cout == ['0803']:
                count += 1
        print("The count of Numbers starting with 0803 is: ", count)

        x=list(filter(lambda j: j!=0,box1))
        print("Phone Numbers starting with 0803: ",*x,sep='\n')


phone=Phone_Numbers()
phone.scope()