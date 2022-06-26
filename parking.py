#Parking Management System

import myModule

print("Welcome to Parking Centre!")

parking= {'A':10, 'B':10, 'C':10}
carSection= {}
cars= []
carlist= ()
totalPrice= 0

class user():
    def _init_(self,section,plateNum):
        self.section= section
        self.plateNum= plateNum
    
    def Enter(section,plateNum):
        if parking[section]>0:
            parking[section]= parking[section]-1
            
            registerPN= open("carsPN.txt","w")
            registerCS= open("cars&section.txt","w")
            cars.append(plateNum)
            carSection[plateNum]= section
            
            for x in cars:
                registerPN.write(x+"\n")
                
            for key,value in carSection.items():
                registerCS.write("%s:%s\n"%(key,value))
            
            registerPN.close()
            registerCS.close()
            
        else:
            print("Parking is full")
            
class customer(user):
    def _init_(self,section,hrs):
        self.section= section
        self.hrs=hrs
    
    def Exit(section,hrs,delPlateNum):
         if updateParking== section:
            if parking[section]<10:
                parking[section]= parking[section]+1
                totalPrice= myModule.Calc(hrs)
                myModule.display(delPlateNum,totalPrice)
                
                return totalPrice
            
            else:
                print("Wrong section. Please enter again.")

def availibility(): 
    print("-----Parking Available-----")
    print("Section A: ",parking['A'])
    print("Section B: ",parking['B'])
    print("Section C: ",parking['C'])

def createTuple(*args):
    x=args
    return x

while(True):
    status= int(input("Enter parking(1)\nExit parking(2)\nCheck availibility(3)\nExit Menu(0):"))
    
    if status== 1: #To enter parking
        section= input("Choose section (A/B/C):")
        plateNum= input("Enter plate number:")
        
        if section=='A' or section=='B' or section=='C':
            user.Enter(section,plateNum)
            
        else:
            print("Wrong input.")
        
               
    elif status== 2: #To exit parking
        delPlateNum= input("Enter your registered plate number:")
        
        if y==delPlateNum or x==delPlateNum:
            for y in cars:
                registerPN= open("carsPN.txt","w")
                cars.remove(delPlateNum)
                
                for x in cars:
                    registerPN.write(x+"\n")
                registerPN.close()

                hrs= int(input("Enter hours of parking: "))
                updateParking= input("Enter your parking section (A/B/C):")
                
                customer.Exit(updateParking,hrs,delPlateNum)
                
        
                for x in carSection:
                    del carSection[delPlateNum]
                    registerCS= open("cars&section.txt","w")
                    carSection[plateNum]= section
                    
                    for key,value in carSection.items():
                        registerCS.write("%s:%s\n"%(key,value))
                
                    registerCS.close()
                        
        else:
            print("Your plate number is not in the record")
        
        
    elif status== 3: #To check availibility of parking and display car entered
        availibility()
        myfile= open("carsPN.txt","r")
        x= myfile.readlines()
        carlist= createTuple(x)
        myfile.close()
        print("Cars entered.")
        print(carlist)
        
    elif status!= 0:
        print("Wrong input.")
        

    else:
        exit()