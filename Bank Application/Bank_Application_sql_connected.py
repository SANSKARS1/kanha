from getpass import getpass
import pymysql as sql

db = sql.connect(host='localhost' , port=3306, user='root' , passwd='', database='pydb3')
cursor = db.cursor()
def capital(a):
    y=0
    for i in a:
        for o in range(65,91):
            x= chr(o)
            if i==x:
                y+=1
    return y
def small(a):
    y=0
    for i in a:
        for o in range(97,123):
            x= chr(o)
            if i==x:
                y+=1
    return y
def sp(a):
    y=0
    for i in a:
        for o in range(33,47):
            x= chr(o)
            if i==x:
                y+=1
    return y
def nm(a):
    y=0
    for i in a:
        for o in range(48,57):
            x= chr(o)
            if i==x:
                y+=1
    return y


def Login():

            account_number = int(input(" Please enter your valid Account number :  "))
            password = getpass(" Please enter your valid password :  ")
            # i=0 
            # x=0
            # while i<len(user_details['Account number']):
            #     # if account_number == user_details['Account number'][i] and password == user_details['password'][i]:
            #         print("Account found !!")
            #         x=i
            #         break
            #     else:
            #         i=i+1
            cmd1 = f"select * from user_data where Account_number = {account_number} and password= '{password}'"
            cursor.execute(cmd1)
            d= list(cursor.fetchall())
            db.commit()

            if d:
                print("Account found !!")
                
            # if account_number==user_details['Account number'][x] and password == user_details['password'][x]:
                while True:
                        choice = int(input("1. Credit  2. Debit 3. Change password  4. Check balance  5. Show details  6. Logout\n"))
                        print()
                        if choice ==1:         
                            credit_amt = int(input("Amount to be added in your account :  "))
                            cmd2 = f"update user_data set Initiall_Balance=Initiall_Balance+{credit_amt} where Account_number={account_number};"
                            cursor.execute(cmd2)
                            db.commit()

                            cmd3 = f"select Initiall_Balance from user_data where Account_number={account_number}"
                            cursor.execute(cmd3)
                            db.commit()

                            x = cursor.fetchall()
                            # user_details['Initial Balance'][i]+= credit_amt
                            print('Account balance is updated .....')
                            print()
                            print("Your account balance is : ", x[0][0])
                        elif choice ==2:
                            debit_amt = int(input("Amount to be debited from your account :  "))
                            # user_details['Initial Balance'][i]-= debit_amt
                            cmd4 = f"update user_data set Initiall_Balance=Initiall_Balance-{debit_amt} where Account_number={account_number}" 
                            cursor.execute(cmd4)
                            db.commit()

                            cmd5 = f"select Initiall_Balance from user_data where Account_number={account_number}"
                            cursor.execute(cmd5)
                            db.commit()

                            y = cursor.fetchall()
                            print('Account balance is updated .....')
                            print()
                            print("Your account balance is : ", y[0][0])
                        elif choice ==3:
                            new_password = getpass("Enter your new password : ")
                            if len(new_password)>=8 and capital(password)>=1 and small(password)>=1 and sp(password)>=1 and nm(password)>=1:
                                # user_details['password'][i] = new_password
                                cmd8 = f"update user_data set password='{new_password}' where Account_number={account_number}"
                                cursor.execute(cmd8)
                                db.commit()

                                print("New password set successfully")
                            else:
                                print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
                        elif choice==4:
                            cmd6= f"select Initiall_Balance from user_data where Account_number={account_number}"
                            cursor.execute(cmd6)
                            db.commit()
                            z = cursor.fetchall()                 
                            
                            print("Your current account balance is : " , z[0][0])
                        elif choice==5:
                            cmd7 = f"select * from user_data where Account_number={account_number}"
                            cursor.execute(cmd7)
                            db.commit()

                            xx = cursor.fetchall()
                            print("Your Account details : ")
                            print("Username : " , xx[0][0])
                            print("Password : " , xx[0][1])
                            print("Account Balance : " , xx[0][2])
                            print("Account number : " , xx[0][3])
                        elif choice==6:
                            print("Logging out.....")
                            return
                        else:
                            print("Please choose correct option ..")
            else:
                print(" Invalid Account number or password  ! ")

def forgot_password():
    account_number = int(getpass("Enter a valid Account Number : "))
    # x=0
    # for i in range(len(user_details['Account number'])):
    #     if account_number==user_details['Account number'][i]:
    #         x=i
    #         break
    #     else: 
    #         pass
    # if account_number==user_details['Account number'][x]:
    cmd1=f"select Account_number from user_data where Account_number = {account_number}"
    cursor.execute(cmd1)
    db.commit()
    d= cursor.fetchall()
    if d:
        while True:
            new_password = getpass(f"Enter new password linked with Account number  : ")
            if len(new_password)>=8 and capital(new_password)>=1 and small(new_password)>=1 and sp(new_password)>=1 and nm(new_password)>=1:
                # user_details['password'][x]=new_password
                cmd2 = f"update user_data set password='{new_password}' where Account_number={account_number}"
                cursor.execute(cmd2)
                db.commit()
                print("Password reset successfully .....")
                break
            else:
                print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
    else:
        print("Invalid account number !")
def Signup():
#     user_details = {'username' : [] , 'password' : [] , 'Initial Balance' : [] , 'Account number' : []}
    
   
            for i in range(1,27):
                print("-",end=' ')
            print("Welcome as a new user",end=' ')
            for i in range(1,27):
                print("-",end=' ')
            print()
            username = input("1. username : ")
            a= False
            while True:
                password = getpass('2. password : ')
                
                if len(password)>=8 and capital(password)>=1 and small(password)>=1 and sp(password)>=1 and nm(password)>=1:
                    a=True
                    break
                else:
                    print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
            Initial_balance = int(input("3. Initial Balance : "))
            b= False
            if Initial_balance>=2000:
                b=True
                cmd1  = f"select Account_number from user_data"
                cursor.execute(cmd1)
                d = cursor.fetchall()
                h = list(d)
                o=h[-1][0]
                o+=1
                # account_number = user_details['Account number'][-1]+1
                print()
                print("Congratulations , your account is successfully created ......")
                print()
                print("Welcome to our services ...")
                print()
                print('Your account number is : ', o)
                if a==True and b==True:
                    cmd2 = f"insert into user_data values('{username}','{password}' , {Initial_balance} , {o})"
                    cursor.execute(cmd2)
                    db.commit()
                    db.close()
                
            else:
                print("We are sorry , but your minimum balance should be 2000")
               
def BankApplication():
    print("                                         BANK APPLICATION                                         ")
    
    while True:
        print(" 1. Login\n 2. Signup\n 3. Forgot password\n 4. Exit")
        option = int(input())
        if option==1:
            Login()
        elif option==2:
            Signup()
        elif option==3:
            forgot_password()
        elif option==4:
            print("Closing Application ....")
            break
            
        else:
            print("Invalid option . Please choose a valid option")
BankApplication()            