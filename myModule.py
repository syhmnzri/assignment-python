def Calc(hrs):
    if hrs<=1:
        totalPrice= 1
    
    elif hrs>1:
        totalPrice= 1.5*hrs+1
        
    return totalPrice

def display(delPlateNum, total):
    print("\n")
    print("----PAYMENT INFO----")
    print("Plate number: "+delPlateNum)
    print("Total price: RM",total)
    print("\n")
    print("---  Thankyou!  ---")
    print("\n")
    
    myfile= open("receipt.txt","w")
    myfile.write("----PAYMENT INFO----\n")
    myfile.write("Plate number: "+delPlateNum+"\n")
    myfile.write("Total price: RM"+str(total)+"\n")
    myfile.write("\n")
    myfile.write("---  Thankyou!  ---")
    myfile.close
    