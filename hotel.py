
#if program gives an error, please change os.system('clear') to os.system('cls')

import random
import os
import csv
av_rooms=list(range(1,101))                      #available rooms
data=[]                      #array to store objects

def pau_cl():
    wait=input("Press any Key To continue")                          #pause and cleaer command
    os.system('clear')
    
class Guest:

    def __init__(self):
        self.name=None
        self.age=None
        self.email=None
        self.contact=None                         #constructor initialzing to none
        self.nights=None
        self.food=None
        self.coupon=None
        self.cost=None
        self.hasPoolAccess=None
        self.hasLoungeAccess=None
        self.writing_c=None
    
    def calculateCost_assignLev(self):
        self.cost=self.nights*700
        if(self.food=="Y"):
            self.cost+=self.nights*200
            if(self.coupon==1):                                              #method to calculate cost depending on nights, food option, and if coupon is issued
                self.cost-=200
        if(self.cost>=5000):
            self.level="Platinum"
        elif(self.cost>=4000 and self.cost<5000):
            self.level="Gold"
        else:
            self.level="Silver"
        
    def priviliges(self):                                           #method to show the privileges according to level
        if(self.level=="Platinum"):
            print("As you're spending more than 3000Rs. in our Hotel, You qualify as a Platinum member and have Access to Swimming Pool, Private Lounge and Free Breakfast.")
            self.hasPoolAccess=True                                 #these variable arent used in the actual program, but can be used in later updates
            self.hasLoungeAccess=True
            
        elif(self.level=="Gold"):
            print("As you're spending more than 2000Rs. in our Hotel, You qualify as a Gold member and have Access to Swimming Pool and Free Breakfast")
            self.hasPoolAccess=True
        else:
            print("As a Silver Member, you qualify for free breakfast in our Hotel. ")

    def assignRoom(self):
        self.room_no=random.choice(av_rooms)                             #method to assign a random room and then remove it from available room list
        av_rooms.remove(self.room_no)
        
    def book_room(self):
        self.contact=input("Enter Contact:") 
        j=self.search(self.contact)
        if(j!=-1):
            print("Given Contact is already checked in, please try again")
            pau_cl()
            Menu()
        self.name=input("Enter Name:")
        self.age=input("Enter Age:")
        self.email=input("Enter Email:")
        self.nights=int(input("Enter no of Nights of stay:"))                                     #method to get input and book a room 
        self.food=input("Enter Y/N for Food Service, costs 200 a day.")                           #here contact no is being used as a key attribute
        self.coupon=0                                                                             #also it is assumed the same contact doesnt recheckin in one run of program
        if(self.food=="Y" or self.food=='y'):                                                     #any other input other than Y in self.food defaults to N
            self.food="Y"
            self.random_coupons()
        else:
            self.food="N"
            self.writing_c="N"                                                                    #variable to write to csv if coupon was used or not
        self.calculateCost_assignLev()
        self.assignRoom()
        data.append(self)                                                                   
        self.priviliges()
        pau_cl()

    def random_coupons(self):                                                                 #method to randomize coupons,0-2 means no coupon, 3 means a 200 coupon
        self.coupon=random.randint(0,3)
        self.writing_c="N"
        if(self.coupon==3):
            self.writing_c="Y"
            print("Congratulations, You have been issued a Lunch/Dinner coupon of 200. The amount will be deducted from your final Bill.")

    def search(self, con):                                                    #search function used for billing etc.
        for i in range(data.__len__()):
            if(data[i].contact == con):
                return i
        return -1                                              #returns -1 if not found

    def Billing(self):
        con=input("Enter Contact No:")
        index=self.search(con)
        if(index>=0):
            print("Name=",data[index].name)
            print("Age=",data[index].age)
            print("RoomNo=",data[index].room_no)
            print("Level=",data[index].level)
            print("E-Mail=",data[index].email)
            print("Contact=",data[index].contact)                           # it is assumed in one run of the program, a person with same contact doesnt recheckin
            print("No. of Nights=",data[index].nights)                      #method to print out all data of person after searching 
            print("Food=",data[index].food)
            if(data[index].food=="Y"):
                print("Cost per night=700+200")
            else:
                print("Cost per night=700")
            if(data[index].coupon==3):
                print("200 Rs. OFF for 1 meal")
            print("Sub-Total=",data[index].cost)
            print("Net-Total=",round(data[index].cost*1.4))
            print("\n")
            av_rooms.append(data[index].room_no)
            print("Thank You for the Stay")
            pau_cl()
        else:
            print("Data Not Found")
            pau_cl()

def write_csv():
    with open("hotel.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        headers = ['Contact','Name','Age','RoomNo', 'Level','Email','Nights','Food','Coupon','SubTotal','NetTotal']       #write to csv overwrites the file,doesnt append it
        writer.writerow(headers)
        for guest in data:
            writer.writerow([guest.contact,guest.name,guest.age,guest.room_no,guest.level,guest.email,guest.nights,guest.food,guest.writing_c,guest.cost,guest.cost*1.4])

        
def Menu():
    while(1):
        print("Welcome to Matrix Inn") 
        print("1 Booking")                                       #menu function on a loop
        print("2 Bill Generation")
        print("3 Show Level and Privileges")
        print("4 Write to CSV") 
        print("0 Exit")
        print("Enter your choice:")
        ch=int(input())
        if(ch==1):
            os.system('clear')
            p1=Guest()
            p1.book_room()
            del p1
        elif(ch==2):
            os.system('clear')
            p2=Guest()
            p2.Billing()
            del p2
        elif(ch==3):
            os.system('clear')
            p3=Guest()
            cont=input("Please Enter Contact No.:")
            index=p3.search(cont)
            if(index==-1):
                print("Data not found/Not Checked In")
                pau_cl()
            else:
                data[index].priviliges()
                pau_cl()
        elif(ch==4):
            os.system('clear')
            write_csv()
            print("Done")
            pau_cl()
        elif(ch==0):
            quit()
        
#driver code
Menu()

