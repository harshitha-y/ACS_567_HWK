import csv

class Data:
    
  def __init__(self, date=0, expense='', amount=0, category=''):
    self.date = date
    self.expense = expense
    self.amount = amount
    self.category = category
        
  def getdata(self):
    return self.date, self.expense, self.amount, self.category
    
  def update(self, date, expense, amount, category):
    self.date = date
    self.expense  = expense
    self.amount = amount
    self.category = category
    
class Manager:
    
  def __init__(self, date=0, expense='', amount=0, category=''):
    self.date = date
    self.expense = expense
    self.amount = amount
    self.category = category
    
  def read(self):
    with open('data2.csv','r', newline='')as file:
      csvFile = csv.reader(file, delimiter=',')
      #for lines in csvFile:
      #print(lines)
      data =list(csvFile)
      print("Sno. Date  Expense Type Amount  Category\n")
      
      for i in range (1,len(data)):
          print(i,data[i][0],data[i][1],data[i][2],data[i][3])
      #print(data)
      file.close()
  def write(self, dataobj):
      with open('data2.csv', 'a', newline='') as file:
        # creating a csv writer object
        csvwriter = csv.writer(file)
        row = [dataobj.date, dataobj.expense, dataobj.amount, dataobj.category]
        csvwriter.writerow(row)
        print("\nBill added sucessfully\n")
        file.close()
  def update(self,dataobj,row):
      with open('data2.csv', 'r', newline='') as file:
        csvFile=csv.reader(file)
        data =list(csvFile)
        data[row][0]=dataobj.date
        data[row][1]=dataobj.expense
        data[row][2]=dataobj.amount
        data[row][3]=dataobj.category
        file.close()
      with open('data2.csv', 'w', newline='') as file:
        # creating a csv writer object
        csvwriter = csv.writer(file)
        csvwriter.writerows(data)
        print("\nBill updated sucessfully\n")
        file.close()
  def delete(self,row):
      new=[]
      with open('data2.csv', 'r', newline='') as file:
        csvFile=csv.reader(file)
        data =list(csvFile)
        n=0
        for i in data:
            if n!=row:
                new.append(i)
            n+=1
        file.close
      with open('data2.csv', 'w', newline='') as file:
        # creating a csv writer object
        csvwriter = csv.writer(file)
        csvwriter.writerows(new)
        print("\nBill deleted successfully\n")
        file.close()
        
  def sort(self,n):
      with open('data2.csv', 'r', newline='') as file:
        csvFile=csv.reader(file)
        data =list(csvFile)
        data.pop(0)
        for i in range(0,len(data)):
            data[i][2]=int(data[i][2])
        if n==6:                                                                        #sort data by price from high to low
            data = sorted(data, key=lambda x: x[2], reverse ="True")
        if n==5:                                                                        #sort data by price from low to high
            data = sorted(data, key=lambda x: x[2])
        print("Sno. Date  Exp-Type Amount Category\n")
        for i in range (0,len(data)):
          print(i+1, data[i][0],data[i][1],data[i][2],data[i][3])
        #print(data)
        file.close()
  def analysis(self):
      with open('data2.csv', 'r', newline='') as file:
        csvFile=csv.reader(file)
        data =list(csvFile)
        mean=0
        s=0
        for i in range(1,len(data)):
            s+=1
            mean+=int(data[i][2])
        mean=(mean/s)
        data.pop(0)
        data = sorted(data, key=lambda x: x[2], reverse ="True")
        minimum=data[0][2]
        data = sorted(data, key=lambda x: x[2])
        maximum=data[0][2]
        
        print("Mean value of the expenses: ", mean)
        print("Mininum expense ", minimum)
        print("Maximum expense ", maximum)
        file.close()
        
      
        
class Menu:
    def mainmenu(self):
        choice=0
        m1 = Manager()
        while(choice!=8):
            choice=int(input("\nPick an option\n\n1. View bills\n2.Add a bill\n3.Change an existing bill\n4.Delete a bill\n\nDisplay and filter by:\n5.Amount (low to high)\n6.Amount(high to low)\n\n7.Analysis\n8.Exit\n"))
            if choice==1:
                
                m1.read()
            elif choice==2:

                print("Enter bill details\n")
                date = input("what is the date?\n")
                exp = input("what is the type of expense?\n")
                amt = int(input("what is the amount?\n"))
                cat = input("what is the category?\n")
                          
                d2= Data(date, exp, amt, cat)
                m1.write(d2)
                
            elif  choice==3:
                n= int(input("enter the serial number of the bill to change\n"))
                print("Enter bill details\n")
                date = input("what is the date?\n")
                exp = input("what is the type of expense?\n")
                amt = int(input("what is the amount?\n"))
                cat = input("what is the category?\n")
                d3= Data(date, exp, amt, cat)
                m1.update(d3,n)

            elif choice==4:
                n= int(input("enter the serial number of the bill to delete"))
                m1.delete(n)
            elif choice==5 or choice == 6:
                m1.sort(choice)
            elif choice==7:
                m1.analysis()
            elif choice==8:
                print("See you later\n")
                exit
            else:
                print("Invalid choice, try again!\n")

menu=Menu()
print("This is an application to manage your bills")
menu.mainmenu()
            

        
        
    
    
        
  

            















