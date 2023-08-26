from flask import Flask , render_template , request
from flask import make_response , session
import pymysql as sql

db = sql.connect(host='localhost' , user='root' , port=3306 , password='' ,database='new_bank')
cursor = db.cursor()



class Password:
    def __init__(self,string):
        self.string = string
    def capital(self):
        y=0
        for x in self.string:
            for o in range(65,91):
                z=chr(o)
                if x==z:
                    y+=1
        return y            
    def small(self):
        y=0
        for x in self.string:
            for o in range(97,123):
                z=chr(o)
                if x==z:
                    y+=1
        return y            
    def sp(self):
        y=0 
        for x in self.string:
            for o in range(33,47):
                z=chr(o)
                if x==z:
                    y+=1
        return y            
    def nm(self):
        y=0
        for x in self.string:
            for o in range(48,57):
                z=chr(o)
                if x==z:
                    y+=1
        return y            

app = Flask(__name__)

app.secret_key = 'fakgsfichfseirinfs8wt4rm48r39w4ctrw5mtw95xtw85'

@app.route("/")
def index():
    # if request.cookies.get('email'):
    #     return render_template('success.html')
    if session.get('islogin'):
        return render_template('success.html')
    return render_template('home.html')

@app.route('/login/')
def login():
    # if request.cookies.get('email'):
    #     return render_template('success.html')
    if session.get('islogin'):
        return render_template('success.html')
    return render_template('login.html')

@app.route('/Signup/')
def sign():
    # if request.cookies.get('email'):
    #     return render_template('success.html')
    if session.get('islogin'):
        return render_template('success.html')
    return render_template('signup.html')

@app.route('/signup_form/', methods=['GET','POST'])
def signform():
    if request.method=='GET':
        return render_template('signup.html')
    elif request.method=='POST':
        firstname = request.form.get('first')
        lastname = request.form.get('last')
        email = request.form.get('email')
        balance = int(request.form.get("initial_balance"))
        password = request.form.get('password')
        commnd1 = f"select * from Bank where email_Address = '{email}'"
        cursor.execute(commnd1)
        d = cursor.fetchall()
        if d:
            msg = 'Email already exists ....Login now'
            return render_template('login.html',data=msg)
        else:
            a = Password(password)
            if (firstname!='' and lastname!='' and email!='' and password!=''  and balance!=''):
                if  balance>=2000:
                    if (a.capital()>=1 and a.nm()>=1 and a.small()>=1 and a.sp()>=1):
                        comnd3 = f"select Account_number from Bank order by Account_number;"
                        cursor.execute(comnd3)
                        aa = cursor.fetchall()
                        h = list(aa)
                        o=h[-1][0]
                        o+=1
                        commnd2 = f"insert into Bank values('{firstname}' ,'{lastname}', '{email}', '{password}' , {balance} ,{o})"
                        cursor.execute(commnd2)
                        db.commit()
                        msg = f'account created successfully.....ACCOUNT NUMBER : {o}  Login Now !!!'
                        return render_template ('signup.html' , variable_in_front_end= msg)
                        db.close()
                    else:
                        msg3 = "Password must includes uppercase,lowercase,special character(!,@,etc),nummbers(0-9)"
                        return render_template('signup.html' , d=msg3)
                else:
                    msg4 = "Minimum Balance required is : Rs2000"
                    return render_template('signup.html' , balance_kum = msg4)    
            else:
                msg2 = 'Fill all the fields ..'
                return render_template('signup.html',d2=msg2)

@app.route('/after/' , methods=['GET','POST']) 
def after():
    if request.method=='GET':
        return render_template('login.html')
    else:
        Account_number = request.form.get('Account_number')
        password = request.form.get('password')
        cmd = f"select * from Bank where Account_number='{Account_number}' and password='{password}'"
        cursor.execute(cmd)
        d = cursor.fetchall()
        if d:
            resp=  make_response(render_template('success.html'))
            resp.set_cookie('Act_number',Account_number)
            session['Account_number']=Account_number
            session['islogin'] = True
            return resp

            # resp.set_cookie('islogin','True')
        else:
            msg2 = "Invalid  Account_number / password entered ."
            return render_template('login.html',d=msg2)

@app.route('/logout/')
def logout():
    
    resp = make_response(render_template('login.html'))
    
    # resp.delete_cookie('email') 
    # resp.delete_cookie('islogin')
    # return resp
    session.pop('Account_number')
    session.pop('islogin')
    resp.delete_cookie('Act_number')
    return resp 

@app.route("/credit/" , methods=['POST' , 'GET'])
def credit():
    if request.method == 'GET':
        return render_template('credit.html')
    else:
        added = request.form.get('Amount_added')
        Account_number = request.cookies.get('Act_number')
        # Account_number  = request.form.get('Account_number')
        cmd1 = f"update Bank set Initial_Balance= Initial_Balance + {added} where Account_number = {Account_number}"
        cursor.execute(cmd1)
        db.commit()
        msg= 'Money added successfully'
        return render_template('credit.html',m=msg)

    # return render_template('after.html')
@app.route('/debit/' , methods = ['POST' , 'GET'])
def debit():
    if request.method =='GET':
        return render_template('debit.html') 
    else:
        debited = request.form.get('debit')
        # Account_number = request.form.get('Account_number')
        Account_number = request.cookies.get('Act_number')
        cmd1 = f"update Bank set Initial_Balance = Initial_Balance - {debited} where Account_number = {Account_number}"
        cursor.execute(cmd1)
        db.commit()
        msg= 'Money deducted successfully'
        return render_template('debit.html',m=msg)

@app.route('/change-password/' , methods=['POST','GET'])
def change_pass():
    if request.method =='GET':
        return render_template('change-password.html')
    else:
        current = request.form.get('currentPassword')
        new = request.form.get("newPassword")   
        confirm_new = request.form.get('confirmPassword')
        Account_number = request.cookies.get('Act_number')
        cmd9 = f"select password from Bank where Account_number={Account_number}"
        cursor.execute(cmd9)
        g = list(cursor.fetchall())
        p=g[0][0]
        a = Password(new)
        if new==confirm_new and current==p:
            if (a.capital()>=1 and a.nm()>=1 and a.small()>=1 and a.sp()>=1):
                cmd = f"update Bank set password = '{confirm_new}' where Account_number={Account_number}"
                cursor.execute(cmd)
                db.commit()
                ss = "Password changed successfully"
                return render_template('change-password.html',p=ss)
            else:
                msg = "Password must includes uppercase,lowercase,special character(!,@,etc),nummbers(0-9)" 
                return render_template('change-password.html', k=msg)
        else:
            m = "Password does not matches"
            return render_template('change-passsword.html',l=m)

@app.route('/check-balance/',methods = ['GET'])
def check_balance():
    Account_number = request.cookies.get('Act_number')
    cmd = f"select Initial_Balance from Bank where Account_number={Account_number}"
    cursor.execute(cmd)
    d = list(cursor.fetchall())
    j= d[0][0]
    msg  = f"Rs {j}"
    return render_template('check_balance.html', frnt=msg)

@app.route('/show/', methods=['GET'])
def show_details():
    Account_number= request.cookies.get('Act_number')
    cmd = f"select * from Bank where Account_number={Account_number};"
    cursor.execute(cmd)
    d = list(cursor.fetchall())
    name = d[0][0]+" "+d[0][1]
    email = d[0][2]
    passw = d[0][3]
    balance = d[0][4]
    Account = d[0][5]
    return render_template('show.html', n=name,e=email,p=passw,b=balance,a=Account)    
# return f"{firstname} {lastname} , {email} , {password}"

@app.route('/forgot/',methods=['GET','POST'])
def forgot():
    return render_template('forgot_password.html')
app.run(debug=True)