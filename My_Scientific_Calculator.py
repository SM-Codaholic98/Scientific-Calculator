from tkinter import *
import tkinter.messagebox as tkmsgbox
import math as m

root=Tk()

root.minsize(650,650)
root.maxsize(1550,1550)

root.title("Soham's Scientific Calculator")
root.iconbitmap("calculator.ico")

sc=StringVar()
sc=Entry(root,width=50,textvariable=sc,relief=SUNKEN,font="Arial")
sc.grid(row=0,column=0,columnspan=10,padx=11,pady=12)

def helper():
    help = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, sec, cosec, cot, log, ln, √, !, rad, degree, 1/x, π, e 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    tkmsgbox.showinfo("Help",help)

def abt():
    abt = "Thank you for using our app __/\__" 
    tkmsgbox.showinfo("About",abt)

def const():
    msg = '''If you press constants like:  π and e, 2 times, the result will be square of that constant. 
That means, number of times you press the constant, the result will be constant to the power of that number. '''
    tkmsgbox.showinfo("Help",msg)
   
    
mainmenu = Menu(root)

submenu = Menu(mainmenu,tearoff=0)
submenu.add_command(label="General",command=helper)
submenu.add_command(label="Constants",command=const)
mainmenu.add_cascade(label="Help",menu=submenu)

mainmenu.add_command(label="About",command=abt) 
mainmenu.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0,END)
    
    if text=="sin(rad)":
        sc.insert(0,m.sin(float(val)))
    elif text=="cos(rad)":
        sc.insert(0,m.cos(float(val)))  
    elif text=="tan(rad)":
        sc.insert(0,m.tan(float(val)))
        
    elif text=="sec(rad)":
        sc.insert(0,1/m.cos(float(val)))
    elif text=="cosec(rad)":
        sc.insert(0,1/m.sin(float(val)))  
    elif text=="cot(rad)":
        sc.insert(0,1/m.tan(float(val)))
        
    elif text=="sin(deg)":
        if float(val)==0:
            sc.insert(0,m.sin(float(val)))            
        else:
            result=180/float(val)
            sc.insert(0,m.sin(m.pi/result))
    elif text=="cos(deg)":
        if float(val)==0:
            sc.insert(0,m.cos(float(val)))
        else:
            result=180/float(val)
            sc.insert(0,m.cos(m.pi/result))  
    elif text=="tan(deg)":
        if float(val)==0:
            sc.insert(0,m.tan(float(val)))
        else:
            result=180/float(val)
            sc.insert(0,m.tan(m.pi/result))
        
    elif text=="sec(deg)":
        if float(val)==0:
            sc.insert(0,1/m.cos(float(val)))
        else:
            result=180/float(val)
            sc.insert(0,1/m.cos(m.pi/result))
    elif text=="cosec(deg)":
        if float(val)==0:
            sc.insert(0,1/m.sin(float(val)))
        else:
            result=180/float(val)
            sc.insert(0,1/m.sin(m.pi/result))  
    elif text=="cot(deg)":
        if float(val)==0:
            sc.insert(0,1/m.tan(float(val)))
        else:
            result=180/float(val)
            sc.insert(0,1/m.tan(m.pi/result))
        
    elif text=="sin^-1(rad)":
        sc.insert(0,m.asin(float(val)))
    elif text=="cos^-1(rad)":
        sc.insert(0,m.acos(float(val)))  
    elif text=="tan^-1(rad)":
        sc.insert(0,m.atan(float(val)))
        
    elif text=="sec^-1(rad)":
        sc.insert(0,1/m.acos(float(val)))
    elif text=="cosec^-1(rad)":
        sc.insert(0,1/m.asin(float(val)))  
    elif text=="cot^-1(rad)":
        sc.insert(0,1/m.atan(float(val)))
        
    elif text=="sin^-1(deg)":
        a=m.asin(float(val))
        result=m.degrees(a)
        sc.insert(0,result)
    elif text=="cos^-1(deg)":
        a=m.acos(float(val))
        result=m.degrees(a)
        sc.insert(0,result)  
    elif text=="tan^-1(deg)":
        a=m.atan(float(val))
        result=m.degrees(a)
        sc.insert(0,result)
        
    elif text=="sec^-1(deg)":
        a=m.acos(1/float(val))
        result=m.degrees(a)
        sc.insert(0,result)
    elif text=="cosec^-1(deg)":
        a=m.asin(1/float(val))
        sc.insert(0,result)  
    elif text=="cot^-1(deg)":
        a=m.atan(1/float(val))
        result=m.degrees(a)
        sc.insert(0,result)
        
        
    elif text=="sinh":
        sc.insert(0,m.sinh(float(val)))
    elif text=="cosh":
        sc.insert(0,m.cosh(float(val)))  
    elif text=="tanh":
        sc.insert(0,m.tanh(float(val)))
        
    elif text=="sech":
        sc.insert(0,1/m.cosh(float(val)))
    elif text=="cosech":
        sc.insert(0,1/m.sinh(float(val)))  
    elif text=="coth":
        sc.insert(0,1/m.tanh(float(val)))
        
    elif text=="sinh^-1":
        sc.insert(0,m.asinh(eval(val)))
    elif text=="cosh^-1":
        sc.insert(0,m.acosh(eval(val)))  
    elif text=="tanh^-1":
        sc.insert(0,m.atanh(eval(val)))
        
    elif text=="sech^-1":
        sc.insert(0,1/m.acosh(eval(val)))
    elif text=="cosech^-1":
        sc.insert(0,1/m.asinh(eval(val)))  
    elif text=="coth^-1":
        sc.insert(0,1/m.atanh(eval(val)))
                
    elif text=="log":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log10(float(val)))
    elif text=="ln":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log(float(val)))
    elif text=="√":
        sc.insert(0,m.sqrt(float(val)))
    elif text=="!":
        sc.insert(0,m.factorial(int(val)))
    elif text=="rad":
        sc.insert(0,m.radians(float(val)))
    elif text=="deg":
        sc.insert(0,m.degrees(float(val)))
    elif text=="1/x":
        if(val=="0"):
            sc.insert(0,"ꝏ")
        else:
            sc.insert(0,1/float(val))
    elif text=="π":
        if val=="":
             ans = str(m.pi)
             sc.insert(0,ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0,ans)

    elif text=="e":
        if val=="":
            sc.insert(0,str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))
            
    elif text=="x^-1":
        if(val=="0"):
            sc.insert(0,"ꝏ")
        else:
            sc.insert(0,1/float(val))
            
    elif text=="x^2":
        sc.insert(0,float(val)**2)
        
    elif text=="x^3":
        sc.insert(0,float(val)**3)
        
    elif text=="3√":
        sc.insert(0,float(val)**(1/3))
            
    # elif text=="nPr":
    #     result=m.factorial(int(val[0]))/(m.factorial(int(val[0]-val[1])))
    #     sc.insert(0,result)
        
    # elif text=="nCr":
    #     result=m.factorial(int(val[0]))/((m.factorial(int(val[0]-val[1])))*m.factorial(int(val[1])))
    #     sc.insert(0,result)
   

def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0,END)
    newValue = oldValue + text
    sc.insert(0,newValue)
              

def clr(event):
    sc.delete(0,END)
    

def backspace(event):
    entered = sc.get()
    length = len(entered)-1
    sc.delete(length,END)
    

def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^","**")
    answer = eval(answer)
    sc.delete(0,END)
    sc.insert(0,answer)
    
    

class Calculator:
    def __init__(self,txt,r,c,funcName,color="white"):
        self.var = Button(root,text=txt,padx=3,pady=5,fg="black",bg=color,width=10,font="Arial")
        self.var.bind("<Button-1>",funcName)
        self.var.grid(row=r,column=c)


btn0 = Calculator("sin(rad)",1,0,sciCal,"gray61")

btn1 = Calculator("cos(rad)",1,1,sciCal,"gray61")

btn2 = Calculator("tan(rad)",1,2,sciCal,"gray61")

btn00 = Calculator("sec(rad)",1,3,sciCal,"gray61")

btn10 = Calculator("cosec(rad)",1,4,sciCal,"gray61")

btn20 = Calculator("cot(rad)",2,0,sciCal,"gray61")

btn30 = Calculator("sin(deg)",2,1,sciCal,"gray61")

btn40 = Calculator("cos(deg)",2,2,sciCal,"gray61")

btn50 = Calculator("tan(deg)",2,3,sciCal,"gray61")

btn60 = Calculator("sec(deg)",2,4,sciCal,"gray61")

btn70 = Calculator("cosec(deg)",3,0,sciCal,"gray61")

btn80 = Calculator("cot(deg)",3,1,sciCal,"gray61")

btn3 = Calculator("log",3,2,sciCal,"dodgerblue2")

btn4 = Calculator("ln",3,3,sciCal,"dodgerblue2")

btn5 = Calculator("(",3,4,click,"yellow")

btn6 = Calculator(")",4,0,click,"yellow")

btn7 = Calculator("^",4,1,click,"yellow")

btn8 = Calculator("√",4,2,sciCal,"yellow")

btn9 = Calculator("!",4,3,sciCal,"yellow")

btn10 = Calculator("π",4,4,sciCal,"dodgerblue2")

btn11 = Calculator("1/x",5,0,sciCal,"green3")

btn12 = Calculator("deg",5,1,sciCal,"green3")

btn13 = Calculator("rad",5,2,sciCal,"green3")

btn14 = Calculator("e",5,3,sciCal,"dodgerblue2")

btn15 = Calculator("/",5,4,click,"yellow")

btn16 = Calculator("*",6,0,click,"yellow")

btn17 = Calculator("-",6,1,click,"yellow")

btn18 = Calculator("+",6,2,click,"yellow")

btn19 = Calculator("%",6,3,click,"yellow")

btn20 = Calculator("9",6,4,click)

btn21 = Calculator("8",7,0,click)

btn22 = Calculator("7",7,1,click)

btn23 = Calculator("6",7,2,click)

btn24 = Calculator("5",7,3,click)

btn25 = Calculator("4",7,4,click)

btn26 = Calculator("3",8,0,click)

btn27 = Calculator("2",8,1,click)

btn28 = Calculator("1",8,2,click)

btn29 = Calculator("0",8,3,click)

btn30 = Calculator("C",8,4,clr,"red")

btn31 = Calculator("⌦",9,0,backspace,"red")

btn32 = Calculator("00",9,1,click)

btn33 = Calculator(".",9,2,click,"yellow")

btn34 = Calculator("=",9,3,calculate,"yellow")

btn35 = Calculator("sin^-1(rad)",9,4,sciCal,"violet")

btn36 = Calculator("cos^-1(rad)",10,0,sciCal,"violet")

btn37 = Calculator("tan^-1(rad)",10,1,sciCal,"violet")

btn38 = Calculator("sec^-1(rad)",10,2,sciCal,"violet")

btn39 = Calculator("cosec^-1(rad)",10,3,sciCal,"violet")

btn40 = Calculator("cot^-1(rad)",10,4,sciCal,"violet")

btn41 = Calculator("sin^-1(deg)",11,0,sciCal,"violet")

btn42 = Calculator("cos^-1(deg)",11,1,sciCal,"violet")

btn43 = Calculator("tan^-1(deg)",11,2,sciCal,"violet")

btn44 = Calculator("sec^-1(deg)",11,3,sciCal,"violet")

btn45 = Calculator("cosec^-1(deg)",11,4,sciCal,"violet")

btn46 = Calculator("cot^-1(deg)",12,0,sciCal,"violet")

btn47 = Calculator("sinh",12,1,sciCal,"aqua")

btn48 = Calculator("cosh",12,2,sciCal,"aqua")

btn49 = Calculator("tanh",12,3,sciCal,"aqua")

btn50 = Calculator("sech",12,4,sciCal,"aqua")

btn51 = Calculator("cosech",13,0,sciCal,"aqua")

btn52 = Calculator("coth",13,1,sciCal,"aqua")

btn53 = Calculator("sinh^-1",13,2,sciCal,"aqua")

btn54 = Calculator("cosh^-1",13,3,sciCal,"aqua")

btn55 = Calculator("tanh^-1",13,4,sciCal,"aqua")

btn56 = Calculator("sech^-1",14,0,sciCal,"aqua")

btn57 = Calculator("cosech^-1",14,1,sciCal,"aqua")

btn58 = Calculator("coth^-1",14,2,sciCal,"aqua")

btn59 = Calculator("x^-1",14,3,sciCal,"green3")

btn60 = Calculator("x^2",14,4,sciCal,"green3")

btn61 = Calculator("x^3",15,0,sciCal,"green3")

btn62 = Calculator("3√",15,1,sciCal,"green3")

root.mainloop()