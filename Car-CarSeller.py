car_list= list[str]
with open("cars.csv",mode="r+") as file:
            car_list=file.readlines()
            file.close()

class Car:
    row=int
    manufacturer=str
    model=str
    year=str
    mileage=str
    engine=str
    transmission=str
    drivetrain=str
    mpg=str
    exterior_color=str
    interior_color=str
    in_accident=bool
    price=int or float
           
    def __init__ (self, row:int):
        #creates list of the each feature that is between a comma in the given row then assigns them based on the location of the needed variables
        features=car_list[row].split(",")
        self.row=row
        self.manufacturer=features[0]
        self.model=features[1]
        self.year=features[2]
        self.mileage=(features[3])
        self.engine=features[4]
        self.transmission=features[5]
        self.drivetrain=features[6]
        self.mpg=(features[8])
        self.exterior_color=features[9]
        self.interior_color=features[10]
        self.in_accident=bool(features[11])
        self.price=features[19]

        
    def Paint(self,colorname: str):
        self.exterior_color=colorname
    
    def Repair(self, old_part: str, new_part: str):
        if old_part=='engine':
            self.engine=new_part
        elif old_part=='transmission':
            self.transmission=new_part
        elif old_part=='drivetrain':
            self.drivetrain=new_part
    
    def Reupholster(self, colorname:str):
        self.interior_color=colorname
    
    def Drive(self, miles: float):
        self.mileage=str(float(self.mileage)+miles)
    
    def Modify_Price(self,price:int):
        if price>=1:
            self.price=float(price)
        else:
            self.price=float(self.price)-price
            print("is this the chosen price? (yes/no) "+str(self.price))
            answer=input().lower
            if answer=="no":
                answer=input("enter new price or discount ")
                self.Modify_Price(self,answer)
    def __str__(self):
        return("row "+str(self.row)+", "+self.manufacturer+", "+self.model+", "+self.year)




class Seller:
    name=str
    rating=int or float
    inventory=list()
    def __init__(self,row:int):
        features=car_list[row].split(",")
        self.name=features[14]
        self.rating=features[15]
    def Buy(self,car: Car):
        self.inventory.append(car)

    def Sell(self,car: Car):
        self.inventory.remove(car)
    def PrintInv(self):
        for car in self.inventory:
            print(car)
    def __str__(self):
        return(self.name)





CarObjectList=list()
SellerList=list()
sellers=0
line=0
#creates a list of the first 5000 cars in the csv and a list for their sellers
for car in car_list[1:5001]:
    CarObjectList.append(Car(row=line))
    SellerList.append(Seller(row=line))
    
    #I really could not get it to automatically make a list of all the sellers and their inventory and removing duplicate sellers so this part doesnt work correctly     
    if sellers<1 or not(SellerList[0:sellers-1].__contains__(SellerList[sellers])):
        SellerList[sellers].Buy(CarObjectList[line])
        sellers+=1
    else:
        index=[x.name for x in SellerList].index(SellerList[sellers].name)
        SellerList[index].Buy(CarObjectList[line])
        SellerList.pop()
    
    
    print(line)
    line+=1

print("\n")


print("all done!")
