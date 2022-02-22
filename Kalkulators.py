from tkinter import*
mansLogs=Tk()

def btnClick(number):
    current=e.get() # nolasa esošo skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber) # ievieto displejā
    return 0

def btnCommand(command):
    global number #jāiegaumē skaitlis un darbība
    global num1
    global mathOp #matemātisks operātors
    mathOp = command #+,-,*,/
    num1=int(e.get())
    e.delete(0,END)
    return 0

def btnEquals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1 - num2
    elif mathOp=="X":
        result=num1 * num2
    else:
        result=num1/num2
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def btnClear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0
    


e=Entry(mansLogs,width=15,font=("Arial Black",20))
btn0=Button(mansLogs, width=1, text="0",padx="40", pady="20", command=lambda:btnClick(0))
btn1=Button(mansLogs, width=1, text="1",padx="40", pady="20", command=lambda:btnClick(1))
btn2=Button(mansLogs, width=1, text="2",padx="40", pady="20", command=lambda:btnClick(2))
btn3=Button(mansLogs, width=1, text="3",padx="40", pady="20", command=lambda:btnClick(3))
btn4=Button(mansLogs, width=1, text="4",padx="40", pady="20", command=lambda:btnClick(4))
btn5=Button(mansLogs, width=1, text="5",padx="40", pady="20", command=lambda:btnClick(5))
btn6=Button(mansLogs, width=1, text="6",padx="40", pady="20", command=lambda:btnClick(6))
btn7=Button(mansLogs, width=1, text="7",padx="40", pady="20", command=lambda:btnClick(7))
btn8=Button(mansLogs, width=1, text="8",padx="40", pady="20", command=lambda:btnClick(8))
btn9=Button(mansLogs, width=1, text="9",padx="40", pady="20", command=lambda:btnClick(9))
btnplus=Button(mansLogs, width=1, text="+",padx="40", pady="20", command=lambda:btnCommand("+"))
btnminus=Button(mansLogs, width=1, text="-",padx="40", pady="20", command=lambda:btnCommand("-"))
btntimes=Button(mansLogs, width=1, text="X",padx="40", pady="20", command=lambda:btnCommand("X"))
btndevide=Button(mansLogs, width=1, text="/",padx="40", pady="20", command=lambda:btnCommand("/"))
btnequals=Button(mansLogs, width=1, text="=",padx="40", pady="20", command=btnEquals)
btnclear=Button(mansLogs, width=1, text="C",padx="40", pady="20", command=btnClear)

e.grid(row=0,column=0,columnspan=4)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2) 
btntimes.grid(row=1,column=3)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btndevide.grid(row=2,column=3)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btnminus.grid(row=3,column=3)

btn0.grid(row=4,column=0)
btnclear.grid(row=4,column=1)
btnequals.grid(row=4,column=2)
btnplus.grid(row=4,column=3)


mansLogs.mainloop()