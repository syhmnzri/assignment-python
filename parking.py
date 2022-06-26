#Parking Management System

import myModule #import iur self made module
import turtle   #import turtle library

# print("Welcome to Parking Centre!") 

# fontsize = turtle.Turtle()
# MyCar = turtle.Turtle()
# t = turtle.Turtle()

# t.fillcolor('yellow')
# t.begin_fill()
# t.speed(50)

# t.penup()
# t.forward(200)    #Forward turtle by 150 units
# t.left(90)        #Turn turtle by 90 degree
# t.forward(250)    #Forward turtle by 80 units
# t.left(90)        #Turn turtle by 90 degree
# t.forward(400)    #Forward turtle by 150 units
# t.left(90)        #Turn turtle by 90 degree
# t.forward(250)    #Forward turtle by 80 units
# t.left(90)        #Turn turtle by 90 degree
# t.forward(200)
# t.pendown()
# t.end_fill()
# t.hideturtle()

# fontsize.color('black')
# fontsize.write(" \nWELCOME\n TO THE\n PARKING!!", font=("Stencil", 48, "bold"), align= 'center')
# fontsize.hideturtle()

# MyCar.speed(50)
# # code for drawing rectangular upper body
# MyCar.color('black')
# MyCar.fillcolor('red')
# MyCar.penup()
# MyCar.goto(0,-105)
# MyCar.pendown()
# MyCar.begin_fill()
# MyCar.forward(300)
# MyCar.left(90)
# MyCar.forward(50)
# MyCar.left(90)
# MyCar.forward(300)
# MyCar.left(90)
# MyCar.forward(50)
# MyCar.end_fill()

# # code for drawing window and roof
# MyCar.penup()
# MyCar.goto(100, -55)
# MyCar.pendown()
# MyCar.setheading(45)
# MyCar.forward(70)
# MyCar.setheading(0)
# MyCar.forward(100)
# MyCar.setheading(-45)
# MyCar.forward(70)
# MyCar.setheading(90)
# MyCar.penup()
# MyCar.goto(200,-55)
# MyCar.pendown()
# MyCar.forward(49.50)

# # code for drawing two tyres
# MyCar.penup()
# MyCar.goto(70, -105)
# MyCar.pendown()
# MyCar.color('black')
# MyCar.fillcolor('black')
# MyCar.begin_fill()
# MyCar.circle(20)
# MyCar.end_fill()
# MyCar.penup()
# MyCar.goto(280, -105)
# MyCar.pendown()
# MyCar.color('black')
# MyCar.fillcolor('black')
# MyCar.begin_fill()
# MyCar.circle(20)
# MyCar.end_fill()

# #code for the road
# MyCar.penup()
# MyCar.goto(20, -125)
# MyCar.pendown()
# MyCar.left(90)
# MyCar.backward(280)

# MyCar.hideturtle()

# turtle.done()

parking= {'A':10, 'B':10, 'C':10}                       #create dictionary for parking section availibility (A,B,C)
carSection= {}                                          #create dictionary for cars and its respective section
cars= []                                                #create list for list of cars entered the facility
carlist= ()                                             #create list of car to display when option 3 is chosen
totalPrice= 0                                           #initialize totalPrice=0

#create class for user
class user():                                           
    def _init_(self,section,plateNum):                  #initialize section and plateNum
        self.section= section
        self.plateNum= plateNum
    
    def Enter(section,plateNum):                        #function to register the car into system
        if parking[section]>0:                          #check availibility of chosen parking
            parking[section]= parking[section]-1
            
            registerPN= open("carsPN.txt","w")          #
            registerCS= open("cars&section.txt","w")    #open carPN.txt and cars&section.txt for writing process
            cars.append(plateNum)                       #insert plateNum into 'cars' list
            carSection[plateNum]= section               #insert plateNum and section into 'carSection' dictionary
            
            for x in cars:
                registerPN.write(x+"\n")                #write data in 'cars' list into carsPN.txt
                
            for key,value in carSection.items():
                registerCS.write("%s:%s\n"%(key,value)) #write key and value from 'carSection' dict into cars&section.txt
            
            registerPN.close()
            registerCS.close()
            1
        else:                                            #will display that parking is full
            print("Parking is full")

 #create new class
class customer(user):
    def _init_(self,section,hrs):                        #initialize section and hrs
        self.section= section
        self.hrs=hrs
    
    def Exit(section,hrs,delPlateNum):                   #function for exit process of car
         if updateParking== section:
            if parking[section]<10:                      #if parking section is less than 10, means that the user enter the right section
                parking[section]= parking[section]+1     #update parking availibility by adding 1 into section selected
                totalPrice= myModule.Calc(hrs)           #import function from 'myModule' to use calculated total price
                myModule.display(delPlateNum,totalPrice) #import function from 'myModule' to display customers receipt
                
                return totalPrice                        #return total price that has been calculated
            
            else:                                        #tell the user that the input is wrong
                print("Wrong section. Please enter again.")

#create new function to display number of parking left in each section
def availibility():                                      
    print("-----Parking Available-----")
    print("Section A: ",parking['A'])
    print("Section B: ",parking['B'])
    print("Section C: ",parking['C'])

#create new function that accepts arguments
def createTuple(*args):     
    x=args
    return x

#looping will continue until the user choose option'0'
while(True):
    status= int(input("Enter parking(1)\nExit parking(2)\nCheck availibility(3)\nExit Menu(0):"))
    
    #To enter parking
    if status== 1:
        section= input("Choose section (A/B/C):")
        plateNum= input("Enter plate number:")
        
        #to make sure that user is entering the right choice
        if section=='A' or section=='B' or section=='C':
            user.Enter(section,plateNum)                   #call function user.Enter()
            
        else:
            print("Wrong input.")
        
    #To exit parking
    elif status== 2:          
        delPlateNum= input("Enter your registered plate number:")
        
        if y==delPlateNum or x==delPlateNum:              #to update the cars inside carsPN.txt
            for y in cars:
                registerPN= open("carsPN.txt","w")        #open file carsPN.txt
                cars.remove(delPlateNum)                  #remove entered plate number
                
                for x in cars:                            #to rewrite the latest cars is list 'cars' into carsPN.txt
                    registerPN.write(x+"\n")
                registerPN.close()                        #close file carsPN.txt

                hrs= int(input("Enter hours of parking: "))
                updateParking= input("Enter your parking section (A/B/C):")
                
                customer.Exit(updateParking,hrs,delPlateNum) #call function customer.Exit()
                
        
                for x in carSection:
                    del carSection[delPlateNum]                 #delete cars entered by user from dictionary 'carSection'
                    registerCS= open("cars&section.txt","w")    #open file cars&section.txt
                    
                    for key,value in carSection.items():        #insert all date inside dictionary 'carSection' into cars&section.txt
                        registerCS.write("%s:%s\n"%(key,value))
                
                    registerCS.close()
                        
        else:
            print("Your plate number is not in the record")
        
    #To display availibility of parking and display car entered
    elif status== 3:
        availibility()                                   #call function 'availibility()'
        
        myfile= open("carsPN.txt","r")                   #open file carsPN.txt
        x= myfile.readlines()                            #read content in the files by line
        carlist= createTuple(x)                          #insert all the data that was read into tuple 'carlist'
        myfile.close()                                   #close file carsPN.txt
        print("Cars entered.")                           
        print(carlist)                                   #print tuple 'carlist'
    
    #to display wrong input and ask user to enter again correctly
    elif status!= 0:
        print("Wrong input. Please enter correctly")
    
    #to will terminate the program
    else:
        exit()