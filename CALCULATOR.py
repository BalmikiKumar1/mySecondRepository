
#complete calculator
from tkinter import *
root=Tk()
root.title("MY CALCULATOR")
# root.geometry("361x381+200+200")
root.maxsize(400,500)    #for calculator size(width,height)

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)
    
def btnClear():
    global val
    val=""
    data.set("")
    
def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)
    
val=""
data=StringVar()



display=Entry(root,textvariable=data,bd=29,justify="left",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7 ☻",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="cyan",command=lambda:btnClick(7),activebackground="yellow",activeforeground="red")
btn7.grid(row=1,column=0)
btn8=Button(root,text="8 ☺",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8),activebackground="green",activeforeground="red",bg="cyan")
btn8.grid(row=1,column=1)
btn9=Button(root,text="9 ♦",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9),activebackground="blue",activeforeground="red",bg="cyan")
btn9.grid(row=1,column=2)
btnadd=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("+"),activebackground="black",activeforeground="red",bg="cyan")
btnadd.grid(row=1,column=3)

btn4=Button(root,text="4 ♣",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4),activebackground="red",activeforeground="red",bg="cyan")
btn4.grid(row=2,column=0)
btn5=Button(root,text="5 ♀",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5),activebackground="brown",activeforeground="red",bg="cyan")
btn5.grid(row=2,column=1)
btn6=Button(root,text="6 ↓",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6),activebackground="mistyrose",activeforeground="red",bg="cyan")
btn6.grid(row=2,column=2)
btnmi=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("-"),activebackground="yellow",activeforeground="red",bg="cyan")
btnmi.grid(row=2,column=3)

btn1=Button(root,text="1 ♪",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1),activebackground="yellow",activeforeground="red",bg="cyan")
btn1.grid(row=3,column=0)
btn2=Button(root,text="2 ♫",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2),activebackground="blue",activeforeground="red",bg="cyan")
btn2.grid(row=3,column=1)
btn3=Button(root,text="3 ☼",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3),activebackground="yellow",activeforeground="red",bg="cyan")
btn3.grid(row=3,column=2)
btnmul=Button(root,text="x",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("*"),activebackground="red",activeforeground="red",bg="cyan")
btnmul.grid(row=3,column=3)

btnc=Button(root,text="CLEAR♥",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnClear,activebackground="yellow",activeforeground="red",bg="cyan",fg="red")
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0),activebackground="yellow",activeforeground="red",bg="cyan")
btn0.grid(row=4,column=1)
btnd=Button(root,text="÷",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("/"),activebackground="yellow",activeforeground="red",bg="cyan")
btnd.grid(row=4,column=3)
btne=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=36,command=btnEqual,activebackground="cyan",activeforeground="red",bg="green")
btne.grid(row=5,columnspan=4)

btnp=Button(root,text=".",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick("."),activebackground="yellow",activeforeground="red",bg="cyan")
btnp.grid(row=4,column=2)


root.mainloop()


# # #2nd calculator

# # from tkinter import *
# # root=Tk()
# # root.title("Calculator")
# # e=Entry(root,width=20,borderwidth=50,bg="yellow",font=("Ariel",19,"bold"))
# # e.grid(row=0,columnspan=4)

# # def number_input(number):
# #     cur_val=e.get()
# #     e.delete(0,END)
# #     e.insert(0,str(cur_val)+str(number))
    
# # def cls():
# #     e.delete(0,END)
    
# # def equal():
# #     x=e.get()
# #     e.delete(0,END)
    
# #     result=eval(x)
# #     e.insert(0,result)

# # Button(root,text="9",width=6,height=2,borderwidth=8,command=lambda:number_input(9)).grid(row=1,column=0)
# # Button(root,text="8",width=6,height=2,borderwidth=8,command=lambda:number_input(8)).grid(row=1,column=1)
# # Button(root,text="7",width=6,height=2,borderwidth=8,command=lambda:number_input(7)).grid(row=1,column=2)
# # Button(root,text="6",width=6,height=2,borderwidth=8,command=lambda:number_input(6)).grid(row=1,column=3)

# # Button(root,text="5",padx=20,pady=20,borderwidth=8,command=lambda:number_input(5)).grid(row=2,column=0)
# # Button(root,text="4",padx=20,pady=20,borderwidth=8,command=lambda:number_input(4)).grid(row=2,column=1)
# # Button(root,text="3",padx=20,pady=20,borderwidth=8,command=lambda:number_input(3)).grid(row=2,column=2)
# # Button(root,text="2",padx=20,pady=20,borderwidth=8,command=lambda:number_input(2)).grid(row=2,column=3)

# # Button(root,text="1",padx=20,pady=20,borderwidth=8,command=lambda:number_input(1)).grid(row=3,column=0)
# # Button(root,text="0",padx=20,pady=20,borderwidth=8,command=lambda:number_input(0)).grid(row=3,column=1)
# # Button(root,text="00",padx=17,pady=20,borderwidth=8,command=lambda:number_input(00)).grid(row=3,column=2)
# # Button(root,text=".",padx=20,pady=20,borderwidth=8,command=lambda:number_input(".")).grid(row=3,column=3)

# # Button(root,text="+",padx=20,pady=20,borderwidth=8,command=lambda:number_input("+")).grid(row=4,column=0)
# # Button(root,text="-",padx=20,pady=20,borderwidth=8,command=lambda:number_input("-")).grid(row=4,column=1)
# # Button(root,text="*",padx=20,pady=20,borderwidth=8,command=lambda:number_input("*")).grid(row=4,column=2)
# # Button(root,text="/",padx=20,pady=20,borderwidth=8,command=lambda:number_input("/")).grid(row=4,column=3)

# # Button(root,text="%",padx=20,pady=20,borderwidth=8,command=lambda:number_input("%")).grid(row=5,column=0)
# # Button(root,text="CLS",padx=20,pady=20,borderwidth=8,command=cls ,fg="red").grid(row=5,column=1)
# # Button(root,text="=",padx=20,pady=20,borderwidth=8,command=equal,bg="green").grid(row=5 ,column=2)
# # Button(root,text="SIN",padx=20,pady=20,borderwidth=8,command=bin,bg="green").grid(row=5,column=3)

# # root.mainloop()


# # from tkinter import *
# # from tkinter import messagebox
# # root=Tk()

# # root.title("messagebox")
# # title=("This page for customer feedback")
# # Text="can you like our customer service"
# # reply=messagebox.askquestion(title,Text)
# # if reply=="yes":
# #     print("good")
# # else:
# #     print("sorry")
# # root.mainloop()


