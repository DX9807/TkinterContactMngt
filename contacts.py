import tkinter as tk
import sqlite3 as s
#from tkinter import Listbox


contacts_root=tk.Tk()



contacts_root.title('ContactsMngt')

contacts_root.iconbitmap('C.ico')
contacts_root.maxsize(width=500,height=500)   #defining max height and width of the window
contacts_root.minsize(width=400,height=500)

#main function.............................................................................................
def mainfunc():
    con=s.connect('contacts.db')
    cursur=s.Cursor(con)

    cursur.execute('CREATE TABLE IF NOT EXISTS contacts(name TEXT NOT NULL,mobile INTEGER NOT NULL,tel INTEGER,email TEXT)')

    #This is to a view a contact
    #----------------------------------------------------------------------------------------------------------

    def contact_view_func():
        contacts_view_frame=tk.Frame(master=contacts_root,bg='grey')
        contacts_view_frame.pack(side='right')
        contact_name1=tk.Label(master=contacts_view_frame,text='Name :'+ contact_name_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_name1.grid(row=0,column=0)
        contact_number1=tk.Label(master=contacts_view_frame,text='Mobile :'+ contact_number_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_number1.grid(row=1,column=0)
        contact_tel1=tk.Label(master=contacts_view_frame,text='Tel :'+ contact_tel_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_tel1.grid(row=2,column=0)
        contact_email1=tk.Label(master=contacts_view_frame,text='Email :'+ contact_email_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_email1.grid(row=3,column=0)


    #This to create a frame for deleting a contact from the list.
    #----------------------------------------------------------------------------------------------------------


    def contact_delete_form_frame():
        contact_delete_form=tk.Frame(master=contacts_root,)
        contact_delete_form.pack(side='top')
        contact_delete=tk.Label(master=contact_delete_form,text='Name  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_delete.grid(row=0,column=0)
        contact_delete=tk.Entry(master=contact_delete_form,text='',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_delete.grid(row=0,column=1)



        #Contact delete button for deleting a contact from the list...........
        contact_dlete_button=tk.Button(master=contacts_delete_form,text='Delete',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=contact_delete_func)


    #creating the list of all contacts....................
    #--------------------------------------------------------------------------------------------------------------

    def list_of_all_contacts_func():
        contact_list_frame=tk.Frame(master=contacts_root,bg='grey')
        contact_list_frame.pack(side='right')
        listbox=tk.Listbox(master=contact_list_frame,bg='grey',)
        listbox.grid(row=0,column=0)
        listbox.insert("ID",)
        listbox.insert("Contact Name")
        cursur.execute('SELECT * FROM contacts')
        result=cursur.fetchall()
        #value for the calling function
        name=contact_name_entry.get()
        for(id,name,mobile,tel,email) in result:
            listbox.insert(id,)
            listbox.insert(name,)
            detail_button=tk.Button(master=listbox,text='Details',command=show_details_func and listbox.destroy(),bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            detail_button.pack(side='right')

    #---------------------------------------------------------------------------------------------------------------

    def update_contact_func():
        name=contact_name_entry.get()
        mobile=contact_number_entry.get()
        tel=contact_tel_entry.get()
        email=contact_email_entry.get()

        show_details_func(name)

        contacts_create_frame=tk.Frame(master=contacts_root,)
        contacts_create_frame.pack(side='top',)

        contact_name=tk.Label(master=contacts_create_frame,text='Name :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_name.grid(row=0,column=0)
        out_contact_name_entry=tk.Entry(master=contacts_create_frame,text='Name',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_name_entry.grid(row=0,column=1)

        contact_number=tk.Label(master=contacts_create_frame,text='Mobile:',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_number.grid(row=1,column=0)
        out_contact_number_entry=tk.Entry(master=contacts_create_frame,text='Mobile',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_number_entry.grid(row=1,column=1)

        contact_tel=tk.Label(master=contacts_create_frame,text='Tel   :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_tel.grid(row=2,column=0)
        out_contact_tel_entry=tk.Entry(master=contacts_create_frame,text='Tel',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_tel_entry.grid(row=2,column=1)

        contact_email=tk.Label(master=contacts_create_frame,text='Email  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_email.grid(row=3,column=0)
        out_contact_email_entry=tk.Entry(master=contacts_create_frame,text='Email',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_email_entry.grid(row=3,column=1)

        out_contact_name_entry.set(name)
        out_contact_number_entry.set(mobile)
        out_contact_tel_entry.set(tel)
        out_contact_email_entry.set(email)


        def contact_update():
            cursur.execute('INSERT INTO contacts VALUES(null,?,?,?,?)',(out_contact_name_entry.get(),out_contact_number_entry.get(),out_contact_tel_entry.get(),out_contact_email_entry.get()))
            con.commit()

        update_contact_button=tk.Button(master=listbox,text='Update',command=show_details_func and listbox.destroy(),bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))



    #--------------------------------------------------------------------------------------------------------------

    #These are database functions...............for accessing the database..........................................

    #---------------------------------------------------------------------------------------------------------------


    def contact_delete_func():
        cursur.execute('DELETE FROM contacts WHERE name=?',(contact_name_entry.get(),))
        con.commit()



    def show_details_func(name):
        cursur.execute('SELECT name,mobile,tel,email FROM contacts WHERE name=?',(name,))
        one_result=cursur.fetchone()
        listboxF=tk.Listbox(master=contacts_root,)
        listboxF.pack(side='bottom')
        for (id,name,mobile,tel,email) in one_result:
            listboxF.insert('ID  :',id)
            listboxF.insert('Name  :',name)
            listboxF.insert('Mobile  :',mobile)
            listboxF.insert('Tel  :',tel)
            listboxF.insert('Email  :',email)
            back_button=tk.Button(master=listboxF,text='Back',command=list_of_all_contacts_func,bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            back_button.grid(row=6,column=4)

    '''
    def contact_list():
        cursur.execute('SELECT * FROM contacts')
        re=cursur.fetchall()
        print(re[1][1])
    '''

    def contact_insert():
        cursur.execute('INSERT INTO contacts VALUES(?,?,?,?)',(contact_name_entry.get(),contact_number_entry.get(),contact_tel_entry.get(),contact_email_entry.get()))
        con.commit()


mainfunc()
#----------------------------------------------------------------------------------------------------------------

#Creating contact form to take user entries......
#------------------------------------------------------------------------------------------------------
contacts_create_frame=tk.Frame(master=contacts_root,)
contacts_create_frame.pack(side='top',)

contact_name=tk.Label(master=contacts_create_frame,text='Name :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_name.grid(row=0,column=0)
contact_name_entry=tk.Entry(master=contacts_create_frame,text='Name',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_name_entry.grid(row=0,column=1)

contact_number=tk.Label(master=contacts_create_frame,text='Mobile:',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_number.grid(row=1,column=0)
contact_number_entry=tk.Entry(master=contacts_create_frame,text='Mobile',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_number_entry.grid(row=1,column=1)

contact_tel=tk.Label(master=contacts_create_frame,text='Tel   :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_tel.grid(row=2,column=0)
contact_tel_entry=tk.Entry(master=contacts_create_frame,text='Tel',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_tel_entry.grid(row=2,column=1)

contact_email=tk.Label(master=contacts_create_frame,text='Email  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_email.grid(row=3,column=0)
contact_email_entry=tk.Entry(master=contacts_create_frame,text='Email',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
contact_email_entry.grid(row=3,column=1)

#Creating a sumbit button for the contact.....
contact_sumbit_button=tk.Button(master=contacts_create_frame,text='View',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command= contact_view_func)
contact_sumbit_button.grid(row=6,column=2,columnspan=4)

contact_sumbit_button=tk.Button(master=contacts_create_frame,text='Add',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command= contact_insert)
contact_sumbit_button.grid(row=6,column=1,columnspan=4)






#defining a frame in the main window
#-----------------------------------------------------------------------------------------------------

def aapheader():
    contacts_frame=tk.Frame(master=contacts_root,bg='#e8edb6',)
    contacts_frame.pack(side='top',)
    contacts_add=tk.Button(master=contacts_frame,text="Add",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),)
    contacts_add.grid(row=0,column=0)
    contacts_view=tk.Button(master=contacts_frame,text="View",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=contact_view_func)
    contacts_view.grid(row=0,column=1)
    contacts_all=tk.Button(master=contacts_frame,text="Contact List",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=list_of_all_contacts_func)
    contacts_all.grid(row=0,column=2)
    contacts_remove=tk.Button(master=contacts_frame,text="Remove",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=contact_delete_form_frame)
    contacts_remove.grid(row=0,column=3)
    contacts_update=tk.Button(master=contacts_frame,text="Update",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=update_contact_func)
    contacts_update.grid(row=0,column=4)

appheader()





contacts_root.mainloop()

cursur.close()
con.close()
