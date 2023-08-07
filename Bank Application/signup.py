from getpass import getpass
import pymysql as sql

db = sql.connect(host='localhost',user='root',port=3306,password='' , database='pydb3')
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
                o=h[0][-1]
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
            
Signup()
 