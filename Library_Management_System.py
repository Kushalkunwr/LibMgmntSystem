from datetime import datetime

#function for taking the input from user
def start():
    exitApp= False

    while exitApp == False:
        display_book()
        print("Enter '1' to borrow a book")
        print("Enter '2' to return a book")
        print("Enter '3' to exit")
        ansOption=int(input("Please enter a value: "))
        if ansOption==1:
            borrowBook()

        elif ansOption==2:
            returnBook()

        elif ansOption==3:
            print("\n***************************************************************************")
            print("Thank You For Using Library Management System")
            print("***************************************************************************\n")
            exitApp= True
        
        #for invalid input
        else:
            print("\n***************************************************************************")
            print("INVALID INPUT!!!!")
            print("Please provide value as 1,2 or 3.")
            print("***************************************************************************\n")   
           
#for reading the dictionary file
def bookDictionary():
    bookDict={}
    file= open("lib.txt","r")
    i=0
    for line in file:
        i=i+1
        line= line.replace("\n","")
        bookDict[i]=line.split(",")
    #print(bookDict)
    return(bookDict)
    file.close()
 
#for displaying list of books and its attributes
def display_book():
    print("--------------------------------------------------------------------------------")
    print("{:<12} {:<24} {:<20} {:<15} {:<15} ".format(" Book ID","Book_Name","Author","Quantity","Price"))
    print("--------------------------------------------------------------------------------")
    file=open("lib.txt","r")
    i=1
    for line in file:
        line= line.replace("\n","")
        line= line.split(",")
        ID= i
        name= line[0]
        author= line[1]
        quantity= line[2]
        price= line[3]
        i= i+1
        print("{:<12} {:<20} {:<22} {:<15} {:<15} ".format( ID, name, author , quantity ,price))
        print("--------------------------------------------------------------------------------")
    file.close()

#function for borrowing book
def borrowBook():
    display_book()
    print("\n***************************************************************************")
    print("\nYou will now borrow the book ")
    print("\n***************************************************************************")
    bookID=int(input("Enter the ID of book you want to borrow: "))
    containsBook = checkQuantity(bookID)
    if containsBook== True:
        bookToBorrow(bookID)
    else:
        borrowBook()

#checking if book avilable or not
def checkQuantity(bookID):
    bookDict= bookDictionary()
    while bookID> len(bookDict):
        print("\n***************************************************************************")
        print("Please enter a valid book ID")
        print("***************************************************************************\n")
        display_book()
        bookID=int(input("Enter the ID of book you want to borrow: "))
    book= bookDict[bookID]
    bookQuantity = int(book[2])
    if (bookQuantity==0):
        print("\n***************************************************************************")
        print("The book that you have entered is not available")
        print("***************************************************************************\n")
    else:
        print("\n***************************************************************************")
        print("The book you want is available to borrow")
        print("***************************************************************************\n")
        
        return True

#to ask user their information for borrowing
def bookToBorrow(bookID):
    bookBorrowed=[]
    addBook = "y"
    bookDict= bookDictionary()
    bookBorrowed.append(bookID)
    name= input("Enter your name: ")
    choosenBook=  bookDict[bookID]
    dateTime= datetime.now()
    borrowedMoment= dateTime.strftime("%d-%m-%y %H:%M:%S")
    updateQuantity(bookID)
    while addBook=="y" or addBook=="Y":
        display_book()
        addBook= input("Do you have another book you want to borrow(Y/N)? ")
        if addBook== "y" or addBook== "Y":
            display_book()
            bookID=int(input("Enter the ID of book you want to borrow: "))
            containsBook = checkQuantity(bookID)
            if containsBook== True:
                choosenBook= bookDict[bookID]
                booksBorrowed.append(bookID)
                updateQuantity(bookID)
                
    borrowReceipt(name, borrowedMoment, bookBorrowed)
    writeBorrowReciept(name,borrowedMoment,  bookBorrowed)

    
#function to update books
def updateQuantity(bookID):
    bookDict= bookDictionary()
    file= open("lib.txt","w")
    for i in bookDict.keys():
        bookName=bookDict[i][0]
        author=bookDict[i][1]
        quantity=bookDict[i][2]
        price= bookDict[i][3]
        if i==bookID:
            updatedQuantity= str(int(quantity)-1)
            fileLine= (bookName+","+author+","+updatedQuantity+","+price+"\n")
            file.write(fileLine)
        else:
            fileLine= (bookName+","+author+","+quantity+","+price+"\n")
            #print(fileLine)
            file.write(fileLine)
    file.close

#to print reciept of the books borrowed by customer
def borrowReceipt(name, borrowedMoment, booksBorrowed):
    book_dict= bookDictionary()
    print("\n***************************************************************************")
    print("Library Reciept")
    print("***************************************************************************\n")
    print("Name         : ",name)
    print("Date and Time: ",borrowedMoment)
    print("List of Books Borrowed: ")
    i=0
    totalAmount=0
    for bookID in booksBorrowed:
        i=i+1
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ int(bookPrice)
        
        print("                    ",book[0])
    print("Total items  : ",i)
    print("Total Price  : $"+str(totalAmount))
    print("***************************************************************************\n")

def writeBorrowReciept(name,borrowedMoment, booksBorrowed):
    book_dict= bookDictionary()
    nme= str(name)
    minute=str(datetime.now().minute)
    second=str(datetime.now().second)
    time= str(borrowedMoment)
    microsecond=str(datetime.now().microsecond)
    filename = nme+minute+second+microsecond
    file= open(filename,"w")
    file.write("\n***************************************************************************\n")
    file.write("Library Reciept")
    file.write("\n***************************************************************************\n")
    file.write("Name         : "+name)
    file.write("\nDate and Time: "+ time)
    file.write("\nList of Books Borrowed: ")
    i=0
    totalAmount=0
    for bookID in booksBorrowed:
        i=i+1
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ int(bookPrice)
        
        file.write("\n                   "+book[0])
    i= str(i)
    totalAmount= str(totalAmount)
    file.write("\nTotal items  : "+i)
    file.write("\nTotal Price  : $"+totalAmount)
    file.write("\n***************************************************************************\n")
 
#function for returning book
def returnBook():
    display_book()
    print("\n***************************************************************************\n")
    print("You will now return the book ")
    print("\n***************************************************************************\n")
    bookID=int(input("Enter the ID of book you want to return: "))
    if bookID<1:
        error
    bookToReturn(bookID)

#to ask user their information for returning
def bookToReturn(bookID):
    bookID= checkBookID(bookID)
    bookReturned=[]
    addBook = "y"
    bookDict= bookDictionary()
    bookReturned.append(bookID)
    name= input("Enter your name: ")
    fine= fineCheck()
    choosenBook=  bookDict[bookID]
    dateTime= datetime.now()
    returnedMoment= dateTime.strftime("%d-%m-%y %H:%M:%S")
    updateQuantityAfterReturn(bookID)
    while addBook=="y" or addBook=="Y":
        display_book()
        addBook= input("Do you have another book you want to return(Y/N)? ")
        if addBook== "y" or addBook== "Y":
            display_book()
            bookID=int(input("Enter the ID of book you want to return: "))
            bookID = checkBookID(bookID)
            choosenBook= bookDict[bookID]
            bookReturned.append(bookID)
            updateQuantityAfterReturn(bookID)
    returnReceipt(name, returnedMoment, bookReturned, fine)
    writeReturnReceipt(name, returnedMoment, bookReturned, fine)
    
#To check if it is library's book
def checkBookID(bookID):
    bookDict= bookDictionary()
    while bookID> len(bookDict):
        print("\n***************************************************************************")
        print("Please enter a valid book ID")
        print("***************************************************************************\n")
        display_book()
        bookID=int(input("Enter the ID of book you want to return: "))
    return bookID


#to check if the book return date is delayed
def fineCheck():
    fine=0.0
    period= int(input("After how many days are you returning the book?"))
    if period>10:
        fine= fine+ 0.5
    else:
        fine=fine+ 0.0
    return fine
#function to update books
def updateQuantityAfterReturn(bookID):
    bookDict= bookDictionary()
    file= open("lib.txt","w")
    for i in bookDict.keys():
        bookName=bookDict[i][0]
        author=bookDict[i][1]
        quantity=bookDict[i][2]
        price= bookDict[i][3]
        if i==bookID:
            updatedQuantity= str(int(quantity)+1)
            fileLine= (bookName+","+author+","+updatedQuantity+","+price+"\n")
            file.write(fileLine)
        else:
            fileLine= (bookName+","+author+","+quantity+","+price+"\n")
            #print(fileLine)
            file.write(fileLine)
    file.close

#to print reciept of the books returned by customer
def returnReceipt(name, returnedMoment, booksReturned, fine):
    book_dict= bookDictionary()
    print("\n***************************************************************************")
    print("Library Reciept")
    print("***************************************************************************\n")
    print("Name         : ",name)
    print("Date and Time: ",returnedMoment)
    print("List of Books Returned: ")
    i=0
    totalAmount= fine
    for bookID in booksReturned:
        i=i+1
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ float(bookPrice)
        
        print("                    ",book[0])
    print("Total items  : ",i)
    if fine== 0:
        print("Total Price  : $"+str(totalAmount))
    else:
        print("You will have to pay fine as you have exceeded the book return date&time")
        print("Total Price including fine is  : $"+str(totalAmount))

    print("***************************************************************************\n")
   
  
def writeReturnReceipt(name, returnedMoment, booksReturned, fine):
    book_dict= bookDictionary()
    nme= str(name)
    minute=str(datetime.now().minute)
    second=str(datetime.now().second)
    time= str(returnedMoment)
    microsecond=str(datetime.now().microsecond)
    filename = nme+minute+second+microsecond
    file= open(filename,"w")
    file.write("\n***************************************************************************\n")
    file.write("Library Reciept")
    file.write("\n***************************************************************************\n")
    file.write("Name         : "+name)
    file.write("\nDate and Time: "+ time)
    file.write("\nList of Books Returned: ")
    i=0
    totalAmount= fine
    for bookID in booksReturned:
        i=i+1
        book= book_dict[bookID]
        bookPrice = book[3].replace("$","")
        totalAmount =totalAmount+ int(bookPrice)
        
        file.write("\n                   "+book[0])
    i= str(i)
    totalAmount= str(totalAmount)
    file.write("\nTotal items  : "+i)
    if fine== 0:
        file.write("\nTotal Price  : $"+str(totalAmount))
    else:
        file.write("\nYou will have to pay fine as you have exceeded the book return date&time")
        file.write("\nTotal Price including fine is  : $"+str(totalAmount))
    file.write("\n***************************************************************************\n")

