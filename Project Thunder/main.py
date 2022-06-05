from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
from GradientFrame import GradientFrame
import os

root = Tk()
root.title("Zapp")
root.geometry("450x560+500+200")
root.configure(bg="#bfadf0")
root.resizable(True,True)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+25+200')
    window.configure(bg="#bfadf0")
    window.resizable(True,True)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title='Select IMAGE file',
                                              filetype=(('file_type','*.txt'),('All files','*.*')))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('Waiting for incomming connectionsss...')
        conn,addr = s.accept()
        file = open(filename,'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print('Data has been transmitted successfullyy...')
        

    #icon
    image_icon1=PhotoImage(file="Image/send.png")
    window.iconphoto(False,image_icon1)

    Sbackground=PhotoImage(file="Image/sender.png")
    Label(window,image=Sbackground).place(x = -2,y = 0)
    

    Mbackground = PhotoImage(file="Image/id.png")
    Label(window,image = Mbackground, bg='#bfadf0').place(x=100, y=260)

    host = socket.gethostname()
    Label(window,text=f'ID: {host}',bg='white', fg='black').place(x=140, y=290)


    Button(window,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="+ SEND",width=8,height=1,font='arial 14 bold',bg='#000',fg="#fff",command=sender).place(x=300,y=150)
    
    window.mainloop()




def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+1000+200')
    main.configure(bg="#bfadf0")
    main.resizable(True,True)

    def receiver():
        ID = SenderID.get()
        filename1=incomming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file = open(filename1,'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully..!!!")


    #icon
    image_icon1=PhotoImage(file="Image/receive.png")
    main.iconphoto(False,image_icon1)

    Hbackground = PhotoImage(file="Image/receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    logo = PhotoImage(file='Image/profile.png')
    Label(main,image=logo,bg="#bfadf0").place(x=100,y=250)

    Label(main,text="Receive",font=('arial',10,'bold'),bg="#bfadf0").place(x=100,y=80)

    Label(main,text="Input the Sender's ID",font=('arial',10,'bold'),bg="#bfadf0").place(x=20,y=340)
    SenderID = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    Label(main,text="Filename for the incomming file ~ ",font=('arial',10,'bold'),bg="#bfadf0").place(x=20,y=420)
    incomming_file = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    incomming_file.place(x=20,y=450)

    imageicon = PhotoImage(file="Image/arrow.png")
    rr=Button(main,text="Receieve",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold", command=receiver)
    rr.place(x=20,y=500)
    
    main.mainloop()

#icon
image_icon = PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="File transfer",font=('Acumin Variable Concept',20,'bold'),bg="#bfadf0").place(x=20,y=30)

Frame(root,width=400, height=2, bg="#bfadf0").place(x=25,y=80)

send_image=PhotoImage(file="Image/send.png")
send=Button(root,image=send_image,bg="#bfadf0",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="Image/receive.png")
receive=Button(root,image=receive_image,bg="#bfadf0",bd=0,command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#bfadf0").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#bfadf0").place(x=300,y=200)

backgroundImage = PhotoImage(file="Image/background.png")
Label(root,image=backgroundImage).place(x=-2,y=323)
