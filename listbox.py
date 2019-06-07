from tkinter import*

root=Tk()
ls=[(1,'Subodh '),(2,'Shakti'),(3,'Shivam'),(4,'Shubham')]


listb=Listbox(master=root,)
for id,name in ls:
    listb.insert(id,name)
listb.pack(side='top')


root.mainloop()
