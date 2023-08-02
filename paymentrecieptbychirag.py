from tkinter import *
root = Tk()
root.geometry("300x150")

def reciept():
    top = Toplevel()
    top.geometry("300x150")

    top.config(background='white')
    price1 = 100
    qty1 = 2
    total1 = price1*qty1

    price2 = 200
    qty2 = 1
    total2 = price1*qty2

    l = Label(top,text='------RECIEPT------')
    l.pack()
    l.config(background='white')

    heading = Label(top,text='PRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(background='white')

    item1 = Label(top,text=f'{price1}\t{qty1}\t{total2}')
    item1.pack()
    item1.config(background='white')

    item2 = Label(top,text=f'{price2}\t{qty2}\t{total2}')
    item2.pack()
    item2.config(background='white')

b = Button(root,text='Print reciept' , command=reciept)
b.pack(padx=10,pady=10)
root.mainloop()
    
    