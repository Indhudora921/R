import mysql.connector

import datetime

indhu=mysql.connector.connect(

    host="localhost",
    user="root",
    password="root",
    
)
print()


#cursor.execute("create table customers_details (name varchar(255),account_number int,password int,amount int)")
#indhu.commit()
#print("success")

def insert_data(name,account_number,password,amount):

    sql="insert into customers details(name,account number,password,amount)values(%5,%5,%5,%5)"
    val=(name,account_number,password,amount,)

    mycursor.execute(sql,value)
    indhu.commit()

print("\t\t\t welcome to indian overseas bank atm \t\t\t")
print("1.deposit amount")
print("2.withdraw amount")
print("3.pin change")
print("\n")

x=datetime.datetime.now()
print(x)

print("1.English \n2.Tamil \n3.Hindi")

language=int(input("select the language:"))

if language==1:
   
    print("your language english")

elif language==2:
    
    print("your language tamil")

elif language==3:
    
    print("your language hindi")

else:
    print("incorrect choice")

try:

    print("select operations \n1.deposit \n2.withdraw \n3.pin change")

    user=int(input("select the number 1 to 3:"))


    if user==1:

       
        name=input("enter your name:").lower().strip()
        
        account_number=int(input("enter your account number:"))
        
        amount=int(input("enter deposit amount:"))
        
        password=int(input("enter your password:"))
        
        print("deposit is successfull")
        
        inser_data(name,account_number,password,amount)


    elif user==2:

        
        name=input("enter your name:").lower().strip()
        
        account_number=int(input("enter your account_number:"))
        
        amount=int(input("enter your withdraw amount:"))
        
        password=int(input("enter your password:"))
        
        print("your withdraw amount is successful")
        
        insert_data(name,account_number,password,amount)

    
    elif user==3:

        name=input("enter your name:").lower().strip()
    
        account_number=int(input("enter your account_number:"))
    
        mobile_number=int(input("enter your mobile number:"))
    
        password=int(input("entter your password:"))
        
        print("your password was changed successfully")
        
        insert_data(name,account_number,password,amount)

    
    else:
         
         print("incorrect choice")

except:

        print("give me number only")



      
















































