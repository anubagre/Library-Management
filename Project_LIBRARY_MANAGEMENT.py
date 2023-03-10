import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='tiger', database='ab')
mycursor=mydb.cursor()
import datetime

#Function to create table DOCTOR
def crt_books():
    mycursor.execute("CREATE TABLE BOOKS(Book_Code char(6), Book_Name char(30), Publisher char(30)"
                     ", Author char(30), No_of_copies integer(4))")
    mycursor.execute("INSERT INTO BOOKS VALUES('1506', 'Computer Networks', 'Thakur Publications', 'Saurabh Singhai', 3)")
    mycursor.execute("INSERT INTO BOOKS VALUES('1203', 'Data Structure', 'McGraw', 'Lipischute', 2)")
    mycursor.execute("INSERT INTO BOOKS VALUES('2101', 'COBOL', 'John W', 'Stern', 5)")                                         
    mydb.commit()
    print('Table BOOK created in MySQL')
crt_books()

#Function to create BOOK_ISSUE
def crt_bi():
    mycursor.execute("CREATE TABLE BOOK_ISSUE(Member_Code char(6), Member_Name char(30), Book_Code char(6), Date_Of_Issue date,"
                     "Date_Of_Return date)")
    mycursor.execute("INSERT INTO BOOK_ISSUE VALUES('M0023', 'Ankit Sen', '1506', '2020-11-19', '2021-12-19')")
    mycursor.execute("INSERT INTO BOOK_ISSUE VALUES('M0024', 'Saket Verma', '1506', '2020-10-09', '2021-10-27')")
    mycursor.execute("INSERT INTO BOOK_ISSUE VALUES('M0027', 'Surbhi Sharma', '2101', '2020-11-02', '2021-11-20')")
    mydb.commit()
    print('Table BOOK_ISSUE created in MySQL')
crt_bi()

#Function to display content of table
def tab_menu():
    opt=int(input('Choose Table to view content (1. BOOKS   2. BOOK_ISSUE):'))
    while True:
        if opt==1:
            mycursor.execute('select * from BOOKS')
            output=mycursor.fetchall()
            print('(Book_Code, Book_Name, Publisher, Author, No_of_copies)')
            for x in output:
                print(x)
            break
        
        elif opt==2:
            mycursor.execute('Select * from BOOK_ISSUE')
            output=mycursor.fetchall()
            print('(Member_Code, Member Name, Book_Code, Date_Of_Issue, Date_Of_Return)')
            for x in output:
                print(x)
            break
        
        else:
            print('Invalid Option! Press 1 or 2')
            tab_menu()

#Date Function
def date():
    print("Enter Date_Of_Issue")
    yr=int(input("Year:"))
    m=int(input("Month:"))
    d=int(input("Date:"))
    doi=datetime.date(yr,m,d)

    print('Enter Date of Return:')
    y=int(input('Year='))
    m=int(input('Month='))
    d=int(input('Date='))
    dor=datetime.date(y,m,d)
    
# Function to update issue details in mySQL
def issue_update():
    s=(input("Enter Member_Code : "))
    rl=(s,)
    sql="select * from BOOK_ISSUE where Member_Code=%s"
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    print("(Member_Code, Member_Name, Book_Code, Date_Of_Issue, Date_Of_Return)")
    for x in res:
        print(x)
    date()
    sql1="Update book_issue set Date_Of_Return=%s where Member_Code=%s and Date_Of_Issue=%s"
    r=[dor,s,doi]
    mycursor.execute(sql1,r)
    mydb.commit()


#Function to add records
def add_book():
    opt=int(input('Choose Table to add content (1. BOOKS     2. BOOK_ISSUE):'))
    while True:
        if opt==1:
            b_code=int(input('Enter Book Code:'))
            b_name=input('Enter name of the book')
            p_name=input('Enter name of the publisher')
            a_name=input('Enter name of the author')
            no=int(input('Enter no. of copies:'))
            s=[b_code, b_name, p_name, a_name, no]
            sql='INSERT INTO BOOKS(Book_Code, Book_Name, Publisher, Author, No_of_copies) VALUES(%s, %s, %s, %s, %s)'
            mycursor.execute(sql,s)
            print('Record Added')
            break
            
        elif opt==2:
            m_code=input('Enter Member Code:')
            m_name=input('Enter Member Name:')
            b_code=input('Enter Book Code:')
            date()
            s=[m_code, m_name, b_code, doi, dor]
            sql='INSERT INTO BOOK_ISSUE(Member_Code, Member_Name, Book_Code, Date_Of_Issue, Date_Of_Return)'
            'VALUES(%s, %s, %s, %s, %s)'
            mycursor.execute(sql,s)
            print('Record Added')
            break
            
        else:
            print('Invalid Option! Press 1 or 2')
            add_book()

    
# Function to update books
def book_update():
    s=int(input("Enter Book_Code: "))
    ad=str(s)
    rl=(s,)
    sql="select * from BOOKS where Book_Code=%s"
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    print('(Book_Code, Book_Name, Publisher, Author, No_of_copies)')
    for x in res:
        print(x)

    nf=int(input("Enter updated no. of copies of book:"))
    sql1="Update BOOKS set No_of_copies=%s where Book_Code=%s"
    r=[nf, ad]
    mycursor.execute(sql1,r)
    mydb.commit()


# Function to delete book details 
def delbook():
    b_code=int(input("Enter the code of the book to be deleted:"))
    rl=(b_code,)
    sql="Delete from BOOKS where Book_Code=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    print("Record deleted from the table")


#Function to search a book for issuing
def search():
    c=input('Enter Book_Code:')
    c1=(c,)
    sql='select No_of_copies from BOOKS where Book_Code=%s'
    mycursor.execute(sql,c1)
    output=mycursor.fetchall()
    print(output)
    sql1='select count(*) from BOOK_ISSUE where Book_Code=%s and Date_Of_Return is NULL'
    mycursor.execute(sql1,c1)
    output1=mycursor.fetchall()
    print(output1)
    if output[0]>output1[0]:
        print('Available to Issue')
    else:
        print('Not Available')


#Function to calculate fine
def fine():
    dy=int(input('Enter number of extra days the book was kept for:'))
    fn=dy*2
    print('Total fine to be paid=Rs.',fn)

    
# Function8 to create csv file of student details
def csv_file():
    import pandas as pd
    df1=pd.read_sql("select * from BOOKS", mydb)
    df1.to_csv("E:\\DATA_PRJ\\Books.csv")
    print("Books CSV file created in D:\\DATA_PRJ")


# Mainmenu Function
def MAINMENU():
    while True:
        print("_____________________________________________________")
        print("*      LIBRARY MANAGEMENT DATABASE SYSTEM           *")
        print("_____________________________________________________")
        print("1. Add Records")
        print("2. Update Records")
        print("3. Display")
        print("4. Delete")
        print("5. Search for a book")
        print("6. Calculate fine")
        print("7. To Create CSV File")
        print("8. Exit")
        print("_____________________________________________________")
        userInput=int(input("Enter your choice : "))
        if(userInput == 1):
            add_book()
        elif(userInput == 2):
            opt=int(input('Choose Table to update content (1. BOOKS     2. BOOK_ISSUE):'))
            if opt==1:
                book_update()
            elif opt==2:
                issue_update()
            else:
                print('Invalid Option')
        elif(userInput == 3):
            tab_menu()
        elif(userInput == 4):
            delbook()
        elif(userInput==5):
             search()
        elif(userInput==6):
            fine()
        elif(userInput==7):
            csv_file()
        elif(userInput==8):
            print("Exiting")
            break
        else:
            print('Invalid Option')
        print('\n'*3)
            
# Mainmenu Function Call
MAINMENU()
