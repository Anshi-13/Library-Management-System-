from tkinter import *
import mysql.connector
from tkinter import ttk, messagebox

def bookRegister():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="library")
    con=mydb.cursor()
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    try:
        insertBooks = "insert into books values (%s,%s,%s,%s)"
        val=(bid,title,author,status)
    
        con.execute(insertBooks,val)
        mydb.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    root.destroy()

def addBook():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="library")
    con=mydb.cursor()
    
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def View():
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="library")
    con=mydb.cursor()
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-80s%-100s%-100s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.10,rely=0.1)
    Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    try:
        getBooks = "select * from books"
        con.execute(getBooks)
        record=con.fetchall()
        
        for i in record:
            
            Label(labelFrame,text="%-10s%-80s%-100s%-100s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.10,rely=y)
            y+=0.1
            mydb.close()
       
    except:
        messagebox.showinfo("ERROR","Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def deleteBook():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="library")
    con=mydb.cursor()
    bid = bookInfo1.get()
    try:
        deleteSql = "delete from books where bid =%s"
        book_id=(bid,)
        con.execute(deleteSql,book_id)
        mydb.commit()
        lastid=con.lastrowid
        messagebox.showinfo("Done","Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Information","Please check Book ID")
        mydb.close()
    bookInfo1.delete(0, END)
    root.destroy()

def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def issue():
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="library")
    con=mydb.cursor()
    
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status,book_id
    
    bid =inf1.get()
    issueto = inf2.get()
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    try:
        extract="select status from books where bid=%s"
        bookid=(bid,)
        con.execute(extract,(bid,))
        con.fetchone()
        if extract=="avail":
            status=False
        else:
            status=True
            
    except Exception as e:
        print(e)
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into books_issued values (%s,%s)"
    bookid=bid
    val1=(bookid,issueto)
    updateStatus = "update books set status = 'issued' where bid = %s"
    val2=(bid,)
    st=status
    try:
        try:
            st==False
            messagebox.showinfo("Success","Book issued Successfully")
            con.execute(issueSql,val1)
            mydb.commit()
            con.execute(updateStatus,val2)
            mydb.commit()
            root.destroy()
        except Exception as n:
            print(n)
            messagebox.showinfo("Message","Book Already Issued")
            root.destroy()
    except Exception as e:
        print(e)
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


global bookInfo1,bookInfo2,bookInfo3,bookInfo4
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

Canvas1 = Canvas(root)
Canvas1.config(bg="#8B8B69")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)


root.mainloop()
