print("- Automobile Directory -")
class Automobile:
    def addvehicle(self):
        make=input("Enter vehicle make: ")
        model=input("Enter model: ")
        year=int(input("Enter year: "))
        color=input("Enter color: ")
        mileage=input("Enter mileage: ")
        cost=int(input("Enter Cost:"))
        List=[]
        List.append(make)
        List.append(model)
        List.append(year)
        List.append(color)
        List.append(mileage)
        List.append(cost)
        return List
    def display(self):
        q=0
        for i in mainlist:
            print(q,":",end=" ")
            for j in i:
                print(j,end=" ")
            print()
            q+=1
    def modifyvehicle(self):
        z=int(input("Enter the id of car data u want to change"))
        List=obj.addvehicle()
        mainlist[z]=List
        print("Successfully updated ")
        print(mainlist)

mainlist=[]
obj=Automobile()
while True:
    print('Enter 1 to Add vehicle to directory')
    print('Enter 2 to Delete vehicle from directory')
    print('Enter 3 to display current vehicles in directory')
    print('Enter 4 to update vehicle in directory')
    print('Enter 5 to export directory')
    print('Enter 6 to quit')
    inp=input("Enter your choice: ")
    if inp=="1":
        rah=int(input("Enter the number of vehicles u want to add: "))
        for i in range(0,rah):
            print("Enter data of object %d"%(i+1))
            List=obj.addvehicle()
            mainlist.append(List)
    elif inp=="2":
        if len(List)<1:
            print("No vehicles in directory currently. ")
            continue
        obj.display()
        numm=int(input("Enter the id no to delete the vehicle: "))
        if numm-1>len(List):
            print("This is invalid ")
        else:
            del mainlist[numm]
            print()
            print("This vehicle is removed ")
    elif inp=="3":
        if len(List)<1:
            print("Directory is empty ")
            continue
        obj.display()
    elif inp=="4":
        if len(List)<1:
            print("No vehicles in directory currently. ")
            continue
        obj.modifyvehicle()
    elif inp=="5":
        with open("automobile.txt","w") as f:
            q=0
            for i in mainlist:
                f.write(str(q)+" ")
                for j in i:
                    f.write(str(j)+" ")
                f.write("\n")
                q+=1
            f.close()
    elif inp=="6":
        print('You have exited the program')
        break
    else:
        print("This is an invalid input. Enter a VALID choice ")
