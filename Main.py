import Library_Management_System
runApp= True

#introduction
print("***************************************************************************")
print("HELLO AND WELCOME TO LIBRARY MANAGEMENT SYSTEM")
print("***************************************************************************\n")

while runApp==True:# for running the program until the user exits
    try:  
        Library_Management_System.start()
        runApp= False
    #In case of any non integer input from the use   
    except:
        print("***************************************************************************")
        print("INVALID INPUT!!!! Please enter a valid input")
        print("***************************************************************************\n")

    
