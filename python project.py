import csv
from prettytable import PrettyTable
table=PrettyTable()
other=PrettyTable()
class Maintenance:
  def __init__(self,name):
    self.name=name 
  def option(self,num):
    if num==0:
      pass

    elif num==1:
      p=open("/content/drive/MyDrive/python_iiit_project/Maintenance.csv","a")
      q=csv.writer(p)
      l=[input("Enter your name"),input("Enter your mobile number:"),self.name,input("Enter the problem:"),input("Enter the location:"),"UNSOLVED"]
      q.writerow(l)
      p.close()

    elif num==2:
      p=open("/content/drive/MyDrive/python_iiit_project/Maintenance.csv","r")
      q=csv.reader(p)
      Q=[]
      for problem in q:
        if problem:
          Q.append(problem) 
      p.close()    
      for i in range(6):
        table.add_column(Q[0][i],[x[i] for x in Q[1::] if x[2]==self.name])
      for i in range(6):
        other.add_column(Q[0][i],[x[i] for x in Q[1::] if x[2]!=self.name])  
      print(self.name,"problems:")  
      print(table)
      print("other problems:")
      print(other)
      for i in range(6):
        table.del_column(Q[0][i])
      for i in range(6):
        other.del_column(Q[0][i])  



      for i in Q[1::]:
        print("is",i[0],"'s complaint have been resolved yes/no?:" )
        tell=input()
        if tell=="yes":
          i[5]="RESOLVED"
      
      p=open("/content/drive/MyDrive/python_iiit_project/Maintenance.csv","w")
      q=csv.writer(p)
      q.writerows(Q)
      p.close()

      p=open("/content/drive/MyDrive/python_iiit_project/Maintenance.csv","r")
      q=csv.reader(p)
      Q=[]
      for problem in q:
        if problem:
          Q.append(problem) 
      p.close()    
      for i in range(6):
        table.add_column(Q[0][i],[x[i] for x in Q[1::] if x[2]==self.name])
      for i in range(6):
        other.add_column(Q[0][i],[x[i] for x in Q[1::] if x[2]!=self.name])  
      print(self.name,"problems:")  
      print(table)
      print("other problems:")
      print(other)
      for i in range(6):
        table.del_column(Q[0][i])
      for i in range(6):
        other.del_column(Q[0][i])  



    elif num==3:
      naam=input("enter your name")
      mob=input("enter your mobile no:")
      p=open("/content/drive/MyDrive/python_iiit_project/Maintenance.csv","r")
      q=csv.reader(p)
      Q=[]
      for problem in q:
        if problem:
          Q.append(problem) 
      p.close() 
      for i in range(6):
        table.add_column(Q[0][i],[x[i] for x in Q[1::] if x[0]==naam or x[1]==mob])
      print(table)  
      
    elif num==4:
      print("""-------------------------------------------------------------------------


      EMERGENCY CONTACT NUMBERS:
      1. ELECTRICAL ISSUE : 9786787698
      2. PLUMBING ISSUE : 0978675678
      3. CARPENTRY ISSUE : 9768756087
      4. HORTICULTURE ISSUE : 8796570978
      
      """) 


      

Electrical=Maintenance("electrical") 
Plumbing=Maintenance("plumbing") 
Carpentry=Maintenance("carpentry")
Horticulture=Maintenance("horticulture")
flag=1
while True:
  print("""------------------------------------------------------------------------



  WELCOME TO IIIT-NR MAINTAINANCE PORTAL""")

    
  print("""1. ELECTRICAL ISSUES
  2. PLUMBING ISSUES
  3. CARPENTRY ISSUES
  4. HORTICULTURE ISSUES
  
  
  -------------------------------------------------------------------------------""")

  n=int(input("Enter any number :"))
        
  

  print("""1. Want to file a complain
2. All complains
3. Track your complain
4. Emergency contact number
0. Home""")
  flag=int(input("Enter a number :"))
  if n==1:
    Electrical.option(flag)
  if n==2: 
    Plumbing.option(flag)
  if n==3:
    Carpentry.option(flag)
  if n==4:  
    Horticulture.option(flag)

  if flag==0:
    continue
