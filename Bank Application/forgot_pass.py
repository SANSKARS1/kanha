from getpass import getpass
import pymysql as sql


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


db = sql.connect(host='localhost' , port=3306, user='root' , passwd='', database='pydb3')
cursor = db.cursor()

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
forgot_password()        