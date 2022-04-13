from cProfile import label
from tkinter import *

def populate_list():
    print('Populate')

def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')

def clear_item():
    print('Clear')

# Create window object
app = Tk()

#Part1
part_text = StringVar()
part_label = Label(app, text='Test Name', font=('bold',20), pady=25)
part_label.grid(row=0,column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)
#Customer
Customer_text = StringVar()
Customer_label = Label(app, text='Customer Name', font=('bold',20))
Customer_label.grid(row=0,column=2, sticky=W)
Customer_entry = Entry(app, textvariable=Customer_text)
Customer_entry.grid(row=0,column=3)
#Retailer
Retailer_text = StringVar()
Retailer_label = Label(app, text='Retailer Name', font=('bold',20))
Retailer_label.grid(row=1,column=0, sticky=W)
Retailer_entry = Entry(app, textvariable=Retailer_text)
Retailer_entry.grid(row=1,column=1)
#Price
Price_text = StringVar()
Price_label = Label(app, text='Price', font=('bold',20))
Price_label.grid(row=1,column=2, sticky=W)
Price_entry = Entry(app, textvariable=Price_text)
Price_entry.grid(row=1,column=3)
#Parts List (Listbox)
parts_list = Listbox(app, height=8, width=60)
parts_list.grid(row=4, column=0,columnspan=3,rowspan=6, pady=20, padx=20)
# Create Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2,column=0,pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2,column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2,column=2)

clear_btn = Button(app, text='Clear Part', width=12, command=clear_item)
clear_btn.grid(row=2,column=3)

app.title('Test Manager')
app.geometry('1000x800')

# Populate data
populate_list()

app.mainloop()