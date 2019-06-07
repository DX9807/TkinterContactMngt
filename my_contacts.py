import tkinter as tk
import sqlite3 as s
#from tkinter import Listbox


contacts_root=tk.Tk()


contacts_root.title('ContactsMngt')

contacts_root.iconbitmap('C.ico')
#contacts_root.maxsize(width=800,height=500)   #defining max height and width of the window
contacts_root.minsize(width=400,height=500)

def main_again():
    for frame in contacts_root.winfo_children():
        frame.destroy()
    main()


def main():


    con=s.connect('contacts.db')
    cursur=s.Cursor(con)

    cursur.execute('CREATE TABLE IF NOT EXISTS contacts(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,mobile INTEGER NOT NULL,tel INTEGER,email TEXT)')


    #---------------------------------------------------------------------------------------------------------------

    def edit_contact_func():


        def edit():
            cursur.execute('SELECT * FROM contacts WHERE name=?',(contact_name_entry_edit.get(),))
            one_result=cursur.fetchone()

            out_contact_name_entry.insert(0,one_result[1])
            out_contact_number_entry.insert(0,one_result[2])
            out_contact_tel_entry.insert(0,one_result[3])
            out_contact_email_entry.insert(0,one_result[4])

    #-----------------------------------------------------------------------------------------------------------------------



        contacts_create_frame=tk.Frame(master=contacts_root,height=300,width=300)
        contacts_create_frame.grid(row=7,column=2)

        contact_name_edit=tk.Label(master=contacts_create_frame,text='Name :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_name_edit.grid(row=0,column=0,sticky='nsew')
        contact_name_entry_edit=tk.Entry(master=contacts_create_frame,text='Name',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_name_entry_edit.grid(row=0,column=1,sticky='nsew')

        edit_contact_button=tk.Button(master=contacts_create_frame,text='Edit',command=edit,bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        edit_contact_button.grid(row=1,column=0,sticky='nsew')

        contact_name=tk.Label(master=contacts_create_frame,text='Name',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_name.grid(row=2,column=0,sticky='nsew')
        out_contact_name_entry=tk.Entry(master=contacts_create_frame,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_name_entry.grid(row=2,column=1,sticky='nsew')

        contact_number=tk.Label(master=contacts_create_frame,text='Mobile:',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_number.grid(row=3,column=0,sticky='nsew')
        out_contact_number_entry=tk.Entry(master=contacts_create_frame,text='Mobile',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_number_entry.grid(row=3,column=1,sticky='nsew')

        contact_tel=tk.Label(master=contacts_create_frame,text='Tel   :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_tel.grid(row=4,column=0,sticky='nsew')
        out_contact_tel_entry=tk.Entry(master=contacts_create_frame,text='Tel',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_tel_entry.grid(row=4,column=1,sticky='nsew')

        contact_email=tk.Label(master=contacts_create_frame,text='Email  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_email.grid(row=5,column=0,sticky='nsew')
        out_contact_email_entry=tk.Entry(master=contacts_create_frame,text='Email',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        out_contact_email_entry.grid(row=5,column=1,sticky='nsew')




        def contact_update():
            if out_contact_name_entry.get()=='' or out_contact_name_entry.get()=='' or out_contact_tel_entry.get()=='' or out_contact_email_entry.get()=='':
                pass

            else:

                cursur.execute('UPDATE contacts SET name=?,mobile=?,tel=?,email=? WHERE name=?',(out_contact_name_entry.get(),out_contact_number_entry.get(),out_contact_tel_entry.get(),out_contact_email_entry.get(),contact_name_entry_edit.get(),))
                con.commit()


        update_contact_button=tk.Button(master=contacts_create_frame,text='Update',command=contact_update,bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        update_contact_button.grid(row=6,column=0,)



    #---------------------------------------------------------------------------------------------------------------
    def contact_delete_form_frame():
        contact_delete_form=tk.Frame(master=contacts_root,)
        contact_delete_form.grid(row=6,column=0,)
        contact_delete=tk.Label(master=contact_delete_form,text='Name  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_delete.grid(row=0,column=0)
        contact_delete_entry=tk.Entry(master=contact_delete_form,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_delete_entry.grid(row=0,column=1)


        #contact delete function-------------------------------------------------------------------------------

        def contact_delete_func():
            cursur.execute('DELETE FROM contacts WHERE name=?',(contact_delete_entry.get(),))
            con.commit()



        #Contact delete button for deleting a contact from the list...........
        contact_delete_button=tk.Button(master=contact_delete_form,text='Delete',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=contact_delete_func)
        contact_delete_button.grid(row=1,column=1,)



    #Inserting the contact into the database...............................................................
    '''
    def validate_float(var):
        new_value = var.get()
        try:
            new_value == '' or float(new_value)
            validate.old_value = new_value
        except:
            var.set(validate.old_value)
    validate.old_value = ''
    '''


    def contact_add_func():
        if contact_name_entry.get()=='' or contact_name_entry.get()=='' or contact_tel_entry.get()=='' or contact_email_entry.get()=='':
            print('Empty fields cant be inserted!!!!!!!!1')
        else:
            contact_insert()




    def contact_insert():
        cursur.execute('INSERT INTO contacts VALUES(null,?,?,?,?)',(contact_name_entry.get(),contact_number_entry.get(),contact_tel_entry.get(),contact_email_entry.get(),))
        con.commit()





    #This is to a view a contact...............................................................................
    #----------------------------------------------------------------------------------------------------------

    def contact_view_func():
        contacts_view_frame=tk.Frame(master=contacts_root,bg='grey')
        contacts_view_frame.grid(row=8,column=0,)

        if contact_name_entry.get()=='' or contact_name_entry.get()=='' or contact_tel_entry.get()=='' or contact_email_entry.get()=='':
            contact_name1=tk.Label(master=contacts_view_frame,text='Nothing to Display',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_name1.grid(row=0,column=0,sticky='nsew')

        else:

            contact_name1=tk.Label(master=contacts_view_frame,text='Contact-Details',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_name1.grid(row=0,column=0,sticky='nsew')

            contact_name1=tk.Label(master=contacts_view_frame,text='Name :'+ contact_name_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_name1.grid(row=1,column=0,sticky='nsew')
            contact_number1=tk.Label(master=contacts_view_frame,text='Mobile :'+ contact_number_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_number1.grid(row=2,column=0,sticky='nsew')
            contact_tel1=tk.Label(master=contacts_view_frame,text='Tel :'+ contact_tel_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_tel1.grid(row=3,column=0,sticky='nsew')
            contact_email1=tk.Label(master=contacts_view_frame,text='Email :'+ contact_email_entry.get(),fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
            contact_email1.grid(row=4,column=0,sticky='nsew')







    #creating the list of all contacts....................
    #--------------------------------------------------------------------------------------------------------------

    def list_of_all_contacts_func():
        contact_list_frame=tk.Frame(master=contacts_root,bg='grey',height=200,width=300)
        contact_list_frame.grid(row=0,column=2,)
        contact_list_label=tk.Label(master=contact_list_frame,text='Contact List',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        contact_list_label.grid(row=0,column=0,sticky='nsew')

       #making a scrollbar for the list..................................
        scrollbar=tk.Scrollbar(master=contact_list_frame,)
        scrollbar.grid(row=0,column=1,sticky='w')


       #....................................................................


        listbox=tk.Listbox(master=contact_list_frame,bg='white',font=('Verdana',15,'bold '),yscrollcommand=scrollbar.set)

        '''listbox.insert("ID")
        listbox.insert("Contact Name")'''
        cursur.execute('SELECT * FROM contacts')
        result=cursur.fetchall()
        #value for the calling function
        name=contact_name_entry.get()
        for(id,name,mobile,tel,email) in result:
            #listbox.insert(id,)
            listbox.insert(id,name)


        listbox.grid(row=1,column=0,sticky='nsew')


        scrollbar.configure(command=listbox.yview)

        #Refresh buton for refreshing the contact list........................................

        refresh_button=tk.Button(master=contact_list_frame,text='Refresh',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=list_of_all_contacts_func)
        refresh_button.grid(row=1,column=0,sticky='ne')



    #--------------------------------------------------------------------------------------------------------------
    '''
    def show_details_func(name):
        cursur.execute('SELECT * FROM contacts WHERE name=?',(name,))
        one_result=cursur.fetchone()
        lstb=tk.Listbox(master=)
        back_button=tk.Button(master=listboxF,text='Back',command=list_of_all_contacts_func,bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
        back_button.grid(row=6,column=4)



    '''
        #---------------------------------------------------------------------------------------------------------------








    contacts_frame=tk.Frame(master=contacts_root,bg='#e8edb6',)
    contacts_frame.grid(row=0,column=0,sticky='nesw')
    contacts_add=tk.Button(master=contacts_frame,text="Add",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=contact_add_func)
    contacts_add.grid(row=0,column=0,sticky='nsew')
    contacts_view=tk.Button(master=contacts_frame,text="View",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=contact_view_func)
    contacts_view.grid(row=0,column=1,sticky='nsew')
    contacts_all=tk.Button(master=contacts_frame,text="Contact List",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=list_of_all_contacts_func)
    contacts_all.grid(row=0,column=2,sticky='nsew')
    contacts_remove=tk.Button(master=contacts_frame,text="Remove",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=contact_delete_form_frame)
    contacts_remove.grid(row=0,column=3,sticky='nsew')
    contacts_update=tk.Button(master=contacts_frame,text="Edit",bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Times',15,'bold italic'),command=edit_contact_func)
    contacts_update.grid(row=0,column=4,sticky='nsew')
    contact_ok_button=tk.Button(master=contacts_frame,text='OK',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=main_again)
    contact_ok_button.grid(row=0,column=5,sticky='nsew')




    #Creating contact form to take user entries......
    #------------------------------------------------------------------------------------------------------
    contacts_create_frame=tk.Frame(master=contacts_frame,)
    contacts_create_frame.grid(row=1,column=0,sticky='nesw')

    contact_name=tk.Label(master=contacts_create_frame,text='Name :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_name.grid(row=0,column=0,sticky='nesw')
    contact_name_entry=tk.Entry(master=contacts_create_frame,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_name_entry.grid(row=0,column=1,sticky='nesw')

    contact_number=tk.Label(master=contacts_create_frame,text='Mobile:',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_number.grid(row=1,column=0,sticky='nesw')
    contact_number_entry=tk.Entry(master=contacts_create_frame,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_number_entry.grid(row=1,column=1,sticky='nesw')

    contact_tel=tk.Label(master=contacts_create_frame,text='Tel   :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_tel.grid(row=2,column=0,sticky='nesw')
    contact_tel_entry=tk.Entry(master=contacts_create_frame,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_tel_entry.grid(row=2,column=1,sticky='nesw')

    contact_email=tk.Label(master=contacts_create_frame,text='Email  :',bg='#dec4ef',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_email.grid(row=3,column=0,sticky='nesw')
    contact_email_entry=tk.Entry(master=contacts_create_frame,fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'))
    contact_email_entry.grid(row=3,column=1,sticky='nesw')

    #Creating a sumbit button for the contact.....
    contact_sumbit_button=tk.Button(master=contacts_create_frame,text='View',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=contact_view_func)
    contact_sumbit_button.grid(row=4,sticky='nesw')

    contact_sumbit_button=tk.Button(master=contacts_create_frame,text='Add',bg='#11c7f9',fg='black',bd='2',relief='sunken',font=('Verdana',15,'bold italic'),command=contact_add_func)
    contact_sumbit_button.grid(row=4,column=1,sticky='nesw')






main()





contacts_root.mainloop()

cursur.close()
con.close()
