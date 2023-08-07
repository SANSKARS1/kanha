from getpass import getpass
import pymysql as sql

db = sql.connect(host='localhost',user='root',port=3306,password='')
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
            i=0 
            x=0
            while i<len(user_details['Account number']):
                if account_number == user_details['Account number'][i] and password == user_details['password'][i]:
                    print("Account found !!")
                    x=i
                    break
                else:
                    i=i+1
            if account_number==user_details['Account number'][x] and password == user_details['password'][x]:
                while True:
                        choice = int(input("1. Credit  2. Debit 3. Change password  4. Check balance  5. Show details  6. Logout\n"))
                        print()
                        if choice ==1:         
                            credit_amt = int(input("Amount to be added in your account :  "))
                            user_details['Initial Balance'][i]+= credit_amt
                            print('Account balance is updated .....')
                            print()
                            print("Your account balance is : ", user_details['Initial Balance'][i])
                        elif choice ==2:
                            debit_amt = int(input("Amount to be debited from your account :  "))
                            user_details['Initial Balance'][i]-= debit_amt
                            print('Account balance is updated .....')
                            print()
                            print("Your account balance is : ", user_details['Initial Balance'][i])
                        elif choice ==3:
                            new_password = getpass("Enter your new password : ")
                            if len(new_password)>=8 and capital(password)>=1 and small(password)>=1 and sp(password)>=1 and nm(password)>=1:
                                user_details['password'][i] = new_password
                                print("New password set successfully")
                            else:
                                print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
                        elif choice==4:
                            print("Your current account balance is : " , user_details['Initial Balance'][i])
                        elif choice==5:
                            print("Your Account details : ")
                            print("Username : " , user_details['username'][i])
                            print("Password : " , user_details['password'][i])
                            print("Account Balance : " , user_details['Initial Balance'][i])
                            print("Account number : " , user_details['Account number'][i])
                        elif choice==6:
                            print("Logging out.....")
                            return
                        else:
                            print("Please choose correct option ..")
            else:
                print(" Invalid Account number or password  ! ")

def Signup():
#     user_details = {'username' : [] , 'password' : [] , 'Initial Balance' : [] , 'Account number' : []}
    
   
            for i in range(1,27):
                print("-",end=' ')
            print("Welcome as a new user",end=' ')
            for i in range(1,27):
                print("-",end=' ')
            print()
            username = input("1. username : ")
            cmd1 = f"insert into user_data values"
            while True:
                password = getpass('2. password : ')
                if len(password)>=8 and capital(password)>=1 and small(password)>=1 and sp(password)>=1 and nm(password)>=1:
                    user_details['password'].append(password)
                    break
                else:
                    print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
            Initial_balance = int(input("3. Initial Balance : "))
            if Initial_balance>=2000:
                user_details['Initial Balance'].append(Initial_balance)
                account_number = user_details['Account number'][-1]+1
                print()
                print("Congratulations , your account is successfully created ......")
                print()
                print("Welcome to our services ...")
                print()
                print('Your account number is : ', account_number)
                user_details['Account number'].append(account_number)
                
            else:
                print("We are sorry , but your minimum balance should be 2000")
def forgot_password():
    account_number = int(getpass("Enter a valid Account Number : "))
    x=0
    for i in range(len(user_details['Account number'])):
        if account_number==user_details['Account number'][i]:
            x=i
            break
        else: 
            pass
    if account_number==user_details['Account number'][x]:
        while True:
            new_password = getpass(f"Enter new password linked with Account number  : ")
            if len(new_password)>=8 and capital(new_password)>=1 and small(new_password)>=1 and sp(new_password)>=1 and nm(new_password)>=1:
                user_details['password'][x]=new_password
                print("Password reset successfully .....")
                break
            else:
                print(" Please enter a valid password ----- with (8 char long atleast , atleast 1 number , atleast 1 upper case , atleast 1 lower case , atleast 1 sp char )")
    else:
        print("Invalid account number !")
            
            
    
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
        
# result = BankApplication()
# if result==1:
#     print("Application closed")
