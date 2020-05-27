from tkinter import *
root=Tk()
root.title("Danny's Calculator")
e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def clicker(number):
    current=e.get()
    e.delete(0,END)# delete former input as new ones are typed
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)

def buttonadd():
    global math
    math="addition"
    no1=e.get()
    global f_num
    f_num=float(no1)
    e.delete(0,END)
def button_equal():
    no2=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+float(no2))
    if math=="subtracting":
        e.insert(0,f_num-float(no2))
    if math=="dividing":
        e.insert(0,f_num/float(no2))
    if math=="multiplying":
        e.insert(0,f_num*float(no2))
def minus():
    global math
    math = "subtracting"
    no1 = e.get()
    global f_num
    f_num = float(no1)
    e.delete(0, END)
def multiply():
    global math
    math = "multiplying"
    no1 = e.get()
    global f_num
    f_num = float(no1)
    e.delete(0, END)
def divide():
    global math
    math = "dividing"
    no1 = e.get()
    global f_num
    f_num = float(no1)
    e.delete(0, END)
button1=Button(root,text="1",padx=40,pady=10,command=lambda:clicker(1))
button2=Button(root,text="2",padx=40,pady=10,command=lambda:clicker(2))
button3=Button(root,text="3",padx=40,pady=10,command=lambda:clicker(3))
button4=Button(root,text="4",padx=40,pady=10,command=lambda:clicker(4))
button5=Button(root,text="5",padx=40,pady=10,command=lambda:clicker(5))
button6=Button(root,text="6",padx=40,pady=10,command=lambda:clicker(6))
button7=Button(root,text="7",padx=40,pady=10,command=lambda:clicker(7))
button8=Button(root,text="8",padx=40,pady=10,command=lambda:clicker(8))
button9=Button(root,text="9",padx=40,pady=10,command=lambda:clicker(9))
button0=Button(root,text="0",padx=40,pady=10,command=lambda:clicker(0))
buttonAdd=Button(root,text="+",padx=38,pady=10,command=buttonadd)
buttonEqualto=Button(root,text="=",padx=39,pady=10,command=button_equal)
buttonClear=Button(root,text="CE",padx=36,pady=10,command=button_clear)# needs no parameter
buttonMinus=Button(root,text="-",padx=40,pady=10,command=minus)# needs no parameter
buttonDivide=Button(root,text="/",padx=40,pady=10,command=divide)# needs no parameter
buttonMultiply=Button(root,text="*",padx=40,pady=10,command=multiply)# needs no parameter



# put buttons on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1,columnspan=1)
buttonAdd.grid(row=4,column=3,columnspan=1)
buttonEqualto.grid(row=4,column=0,columnspan=1)
buttonClear.grid(row=4,column=2)
buttonMinus.grid(row=3,column=3)
buttonDivide.grid(row=1,column=3)
buttonMultiply.grid(row=2,column=3)
root.mainloop()