# details={'PGE5526':'A','PSV3235':'B'}
  
# with open("test.txt", 'w') as f: 
#     for key, value in details.items(): 
#         f.write('%s:%s\n' % (key, value))

# x= input("Enter plate num")
# y= input("Section")

# if x!=y:
#     print("Yahoo")

# s= ['pge5526','psv3213']
# a= ('a','b')
# a= list(zip(s,a))
# print(a)

# carlist= ()

# def createTuple(*args):
#     x=args
#     return x

# while(True):
#     y= input("Enter data:")
#     x= input("Enter data:")
    
#     carlist= createTuple(y,x)

#     print(carlist)
    
#     myfile= open("test.txt","w")
#     for data in carlist:
#         myfile.write(carlist)
#     myfile.close
    
#     if y==0:
#         exit()

# print(carlist)
# while(True):
#     y= int(input("Enter data:"))
#     myfile= open("test.txt","w")
#     carlist.append(y)
#     for data in carlist:
#         myfile.write()

# listt= {'PGE5526':'A','PSV3323':'B'}

# myfile= open("test.txt","w")

# for x in listt:
#     myfile.write(listt)

# myfile.close()

test= {"PGE5526":"A","PSV3323":"B"}
test['PKN5254']="A"
print(test)

for x in test:
    if x=="PGE5527":
        print("yes")

# del test["PGE5526"]
# print(test)
myfile= open("test.txt","w")

for x,y in test.items():
    myfile.write("%s:%s\n"%(x,y))

myfile.close()


