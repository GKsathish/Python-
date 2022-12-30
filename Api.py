

import smtplib,ssl
#from rcs_business_messaging import loggers
from email.mime.multipart import MIMEMultipart
import random
from email.mime.text import MIMEText
from flask import Flask, render_template, request, session
import pymysql
import encrypt_decrypt
import datetime
import uuid
import string
import json
import collections
app = Flask(__name__)
app.secret_key = "RCS#rbmStudio"



@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')


    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )



    cursor = mydb.cursor()
    cursor.execute('SELECT userid,username,status,password,role FROM TBL_USER_MASTER WHERE email_id = %s',
                   (username))

    account = cursor.fetchone()
    aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
    my_email = account[3]
    print(my_email)
    e = aes_encrypt.decrypt(my_email)
    d=e.decode("utf-8")
    if (account[2] == "APPROVED"):
        if(d==password):


            cursor = mydb.cursor()
            cursor.execute('SELECT agentname FROM TBL_Agent_MASTER WHERE agentid = %s',account[0])
            agents = cursor.fetchall()

            json_obj={
                    "status":"200",
                    "companyname":account[0],
                    "username" : account[1],
                    "email" : username,
                    "role" : account[4],
                    "agentname" : agents[0][0],
                    "Message":"sucess"
                }
            print("login Sucessfull : "+ username)
            return json_obj

        else:
            fail_resp={
                    "status":"404",
                    "Message":"fail"
                }
            print("login Failed : "+ username)
            return fail_resp

    # return render_template('campaign.php')
        mydb.commit()
        mydb.close()
    else:
        fail_resp={
                    "status":"404",
                    "Message":"fail"
                }
        print("login Failed : "+ username)
        return fail_resp







@app.route("/change_password", methods=['POST'])
def change_password():
    if request.method == 'POST':
        username = request.form.get('username')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')

        mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )


        cursor = mydb.cursor()
        cursor.execute('SELECT password FROM TBL_USER_MASTER WHERE email_id = %s',(username))
        account = cursor.fetchone()

        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        e = aes_encrypt.decrypt(account[0])
        password=e.decode("utf-8")
        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        e = aes_encrypt.decrypt(new_password)
        new_password = e.decode("utf-8")
        print(account)
        if account is None:
            print("Account is not available")
        else:
            cursor = mydb.cursor()
            cursor.execute('update TBL_USER_MASTER set password= %s where email_id= %s',(new_password, username))
            mydb.commit()
        if account is not None:
            json_obj={
                    "status":"200",
                    "Message":"Password Changed Successfully"
                }
            return json_obj
        else:
            fail_resp={
                    "status":"404",
                    "Message":"Current Password Doesn't match , please try again"
                }
            return fail_resp
    mydb.close()

@app.route('/ForgetPassword', methods=['POST'])
def ForgetPassword():
    email_id = request.form['email_id']

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )




    cursor = mydb.cursor()
    if email_id is not None:

        cursor = mydb.cursor()
        cursor.execute('select username,password from TBL_USER_MASTER where email_id= %s', (email_id))
        account = cursor.fetchone()
        print (account)
        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        e = aes_encrypt.decrypt(account[1])
        password=e.decode("utf-8")

        s = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        s.starttls(context=context)
      #  s.starttls()
        
        s.login("noreply@rbm.studio", "b4VZGdRTH")
        
        message = """\
Subject: rbm.studio<no-reply>
        

Hello """+str(account[0])+""",


        """+"""Here is Your Login details.
        username : """+str(email_id)+"""
        Password : """+str(password)+"""

        Please Don't share your Details."""+"""




Thanks and Regards,

Rbmstudio.
        """
        s.sendmail("help.rbmstudio@gmail.com", email_id, message)


       # msg = MIMEMultipart()
        #text = "Hello " +str(account[1]) + """!,
        
      #  """
      #  
       # password = "Here is your Password :   " + str(account[2])
       # 
      #  message = password + """
      #  Please Don't share the password
      #  """
        
      #  subject = "Forgot password"
      #  
      #  msg['Subject'] = subject
      #  
      #  msg.attach(MIMEText(text))
        
      #  msg.attach(MIMEText(message))
      #  
      #  s.sendmail("help.rbmstudio@gmail.com","ravuri.vidyasagar@pyrogroup.com" , msg=msg.as_string())
      






        print("Mail sent")

        s.quit()
        
        resp={
                "status":"200",
                "user":str(account[2])
             }
        
        return resp
    
    else:
        
        return "Invalid Email"





@app.route('/agent_registration', methods=['POST'])
def agent_registration():
    agentid = request.form.get('agentid')
    agentname = request.form.get('agentname')
    desciption = request.form.get('desciption')
    mobilenumber = request.form.get('mobilenumber')
    mobilelabel = request.form.get('mobilelabel')
    website = request.form.get('website')
    websitelabel = request.form.get('websitelabel')
    email = request.form.get('email')
    emaillabel = request.form.get('emaillabel')
    privacy_url = request.form.get('privacy_url')
    terms_url = request.form.get('terms_url')
    experince = request.form.get('experince')
    actions = request.form.get('actions')
    operators = request.form.get('operators')
    res = operators.strip('"]["')

    res = res.split('","')

    print(res[0])



    

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )

    
    cursor = mydb.cursor()
    test=    cursor.execute('INSERT INTO TBL_Agent_MASTER ( `agentid`, `agentname`, `desciption`, `mobilenumber`, `mobilelabel`, `website`, `websitelabel`, `email`, `emaillabel`, `privacy_url`, `terms_url`, `CDT`,status , exprince , actions) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now(),"Pending",%s,%s)',(agentid,agentname,desciption,mobilenumber,mobilelabel,website,websitelabel,email,emaillabel,privacy_url,terms_url,experince, actions))
    print(test)
    mydb.commit()
    






    for i in res:
        cursor = mydb.cursor()
        query = cursor.execute('INSERT INTO `TBL_OPERATOR_DETAILS`( `operator`, `status`, `agentname`, `cdt`) VALUES(%s,"Pending",%s,now())',(i,agentname))
        print(query)
        mydb.commit()


    resp={
            "status":"200"
        }
    return resp




@app.route('/user_registration', methods=['POST'])
def user_registration():
    userid = request.form.get('userid')
    username = request.form.get('username')
    password = request.form.get('password')
    mobile_number = request.form.get('mobile_number')
    email_id = request.form.get('email_id')
    role = request.form.get('role')

    aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
    e = aes_encrypt.encrypt(password)


    date=datetime.date.today()
    print(date)
    time = datetime.datetime.now().time()
    print (time)

    new_password = str(date)+password+str(time)

    print(new_password)
    print(new_password[10:-15])

    
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )




    cursor = mydb.cursor()
    test=    cursor.execute('INSERT INTO `TBL_USER_MASTER`(`userid`, `username`, `password`, `mobile_number`, `email_id`, `role`, `CDT`, `MDT`,status) VALUES(%s,%s,%s,%s,%s,%s,now(),now(),"Pending")',(userid,username,e,mobile_number,email_id,role))
    print(test)
    mydb.commit()

    resp={
        "status":"200"
        }

    return resp







@app.route('/add_balance', methods=['POST'])
def add_balance():
    username = request.form.get('username')
    balance = int(request.form.get('balance'))

   
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )





    cursor = mydb.cursor()
    cursor.execute("select userid from TBL_USER_MASTER where username= %s",(username))
    userid=cursor.fetchone()

    if userid is not None:
        cursor = mydb.cursor()
        cursor.execute("select Wallet_Balance from TBL_COMPANY_MASTER where user_id = %s",(userid))
        cur_balance = cursor.fetchone()

        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        d = aes_encrypt.decrypt(cur_balance[0])

        current_balance=d.decode("utf-8")

        print(current_balance)

        upadte_balance = str(float(current_balance)+balance)


        print("wallet balance : "+upadte_balance)

        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        wallet_balance = aes_encrypt.encrypt(upadte_balance)


        Transaction_Id = uuid.uuid1()

        cursor = mydb.cursor()
        cursor.execute("insert into RCS_TRANSACTION_DETAILS (User_Id,Transaction_Id,Campaign_Id,Transaction_Charge,Type,Current_Balance,Tax,Final_Balance,CDT,MDT) values(%s,%s,'','','Credit',%s,'0',%s,now(),now())",(userid,Transaction_Id,current_balance,upadte_balance))
        mydb.commit()


        cursor = mydb.cursor()
        cursor.execute("update  TBL_COMPANY_MASTER set Wallet_Balance = %s where user_id = %s",(wallet_balance,userid))
        mydb.commit()


        resp={
        "status":"200"
        }

        return resp
    else:
        resp={
        "status":"400"
        }


        return resp




@app.route('/reserve_balance', methods=['POST'])
def reserve_balance():
    username = request.form.get('username')
    message_count = int(request.form.get('message_count'))
    Campaign_Id = request.form.get('Campaign_Id')


    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )



    cursor = mydb.cursor()
    cursor.execute("select userid from TBL_USER_MASTER where username= %s",(username))
    userid=cursor.fetchone()


    if userid is not None:
        cursor = mydb.cursor()
        cursor.execute("select Wallet_Balance,Reserved_Balance,PPM from TBL_COMPANY_MASTER where user_id = %s",(userid))
        cur_balance = cursor.fetchone()

        balance = message_count * cur_balance[2]


        print(cur_balance[0],cur_balance[1],cur_balance[2])


        print("Reserve the Balance : "+str(balance))

        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        d = aes_encrypt.decrypt(cur_balance[0])

        current_wallet_balance = d.decode("utf-8")

        print("Current Wallet Balance : "+current_wallet_balance)


        if float(current_wallet_balance) > balance:
            reserve = aes_encrypt.decrypt(cur_balance[1])

            current_reserve_balance = reserve.decode("utf-8")

            print(current_reserve_balance)

            update_wallet_balance = str(float(current_wallet_balance)- float(balance))

            print("Detection After wallet Balance : "+update_wallet_balance)

            update_reserve_balance = str(float(current_reserve_balance)+float(balance))


#        update_reserve_balance = str(float(cur_balance[1])+balance)

            print("Current reserve balance : "+update_reserve_balance)


            aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
            w = aes_encrypt.encrypt(update_wallet_balance)

            wallet_balance = w.decode("utf-8")

           # print("Detection After wallet Balance : "+wallet_balance)


            r = aes_encrypt.encrypt(update_reserve_balance)

            reserve_balance = r.decode("utf-8")


          #  print(reserve_balance)

            cursor = mydb.cursor()
            cursor.execute("update  TBL_COMPANY_MASTER set Wallet_Balance = %s , Reserved_Balance = %s  where user_id = %s",(wallet_balance,reserve_balance,userid))

            mydb.commit()

            Transaction_Id = uuid.uuid1()

            cursor = mydb.cursor()
            cursor.execute("insert into RCS_TRANSACTION_DETAILS (User_Id,Transaction_Id,Campaign_Id,Transaction_Charge,Type,Current_Balance,Tax,Final_Balance,CDT,MDT) values(%s,%s,%s,%s,'Initial_charge',%s,'0',%s,now(),now())",(userid,Transaction_Id,Campaign_Id,balance,current_wallet_balance,update_wallet_balance))
            mydb.commit()
            resp={
                "status":200
                }

            return resp
        else:
            resp={
                "status":400

                }
            return resp
    else:
        resp={
                "status":400
                }
        return resp





@app.route('/getbalance', methods=['POST'])
def getbalance():
    username = request.form.get('username')



    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )

    print(username)
    cursor = mydb.cursor()
    cursor.execute('select userid, password from TBL_USER_MASTER where username = "swetha"')
    w = cursor.fetchone()
    userid = w[0]
    print(userid)
    aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
    p = aes_encrypt.decrypt(w[1])

    password_enc = p.decode("utf-8")
    if w  is not None:
        cursor = mydb.cursor()
        cursor.execute('select Wallet_Balance from TBL_COMPANY_MASTER where user_id = %s',(userid))
        wallet = cursor.fetchone()
        aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
        e = aes_encrypt.decrypt(wallet[0])
        wallet_balance = e.decode("utf-8")
        print ("Wallet Balance for  ",userid," is :: ",wallet_balance)
        json_obj={
                        "status" : "200",
                       "AGENT_NAME":userid,
                        "Wallet_Balance":wallet_balance,
                        "Message":"sucess"
                     }
        return json_obj
    else:
        fail_resp={
                        "status":"404",
                        "Message":"failed to fetch"
                    }
        return fail_resp



@app.route('/company_registration', methods=['POST'])
def company_registration():
    username = request.form.get('username')
    password = request.form.get('password')
    Comapany_name = request.form.get('userid')
    mobile_number = request.form.get('mobile_number')
    email_id = request.form.get('email_id')
    role = request.form.get('role')
    beneficiaryname = request.form.get('beneficiaryname')
    bankname = request.form.get('bankname')
    accountnumber = request.form.get('accountnumber')
    ifcscode = request.form.get('ifcscode')
    gstinnumber = request.form.get('gstinnumber')
    pancardnumber = request.form.get('pancardnumber')
    address = request.form.get('address')
    countryname = request.form.get('countryname')
    statename = request.form.get('statename')


    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )

    aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
    password_enc = aes_encrypt.encrypt(password)
    accountnumber_enc = aes_encrypt.encrypt(accountnumber)
    zero = aes_encrypt.encrypt('0')
    
    cursor = mydb.cursor()
    user = cursor.execute('INSERT INTO TBL_USER_MASTER(userid, username, password, mobile_number, email_id, role, CDT, MDT, status,token) VALUES (%s,%s,%s,%s,%s,%s,now(),now(),"pending","0")',(Comapany_name , username , password_enc, mobile_number , email_id , role ))
    print(user)

    mydb.commit()

    cursor = mydb.cursor()
    company = cursor.execute('INSERT INTO TBL_COMPANY_MASTER(user_id, agent_id, company_name, PPM, Wallet_Balance, Reserved_Balance, CDT, MDT,status) VALUES (%s,%s,%s,%s,%s,%s,now(),now(),"pending")',(Comapany_name ,Comapany_name , Comapany_name ,zero , zero , zero  ))
    print(company)

    mydb.commit()


    cursor = mydb.cursor()
    test = cursor.execute('INSERT INTO TBL_BANK_DETAILS(companyid, beneficaryname,accountnumber, bankname, ifsc_code, gstin_number, pan_number, address, state, country, cdt, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now(),"pending")',(Comapany_name , beneficiaryname , accountnumber , bankname , ifcscode , gstinnumber , pancardnumber , address , statename , countryname))
    print(test)
    
    mydb.commit()
    
    resp = {
        "status":"200"
        }
    return resp


@app.route('/Company_Approval', methods=['POST'])
def Company_Approval():
    username = request.form.get('email_id')
    status = request.form.get('status')
    

    print(username)
    print(status)

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
   


    cursor = mydb.cursor()
    result = cursor.execute('SELECT status ,userid from TBL_USER_MASTER  WHERE email_id = %s',(username))
    print(result)
        
    user_status = cursor.fetchone()
    print(user_status[0])
    print(user_status[1])

    cursor = mydb.cursor()
    result = cursor.execute('SELECT status from TBL_BANK_DETAILS  WHERE companyid = %s',(user_status[1]))
    print(result)

    bank_status = cursor.fetchone()

    
    if (bank_status == "APPROVED" and user_status[0] == "APPROVED" or bank_status == "Rejected" and user_status[0] == "Rejected"):
        resp = {
        "status":"400"
        }
        return resp
    elif (status == 'Sucess'):


        cursor = mydb.cursor()
        result = cursor.execute('UPDATE TBL_BANK_DETAILS SET status= "APPROVED" WHERE companyid = %s',(user_status[1]))
        print(result)

        mydb.commit()

        cursor = mydb.cursor()
        result = cursor.execute('UPDATE TBL_USER_MASTER SET status= "APPROVED" WHERE email_id = %s and userid = %s',(username,user_status[1]))
        print(result)

        mydb.commit()
    
        resp = {
        "status":"200"
        }
        return resp
    elif (status == 'Failed'):
        cursor = mydb.cursor()
        result = cursor.execute(' DELETE FROM TBL_BANK_DETAILS  WHERE companyid = %s',(user_status[1]))
        
        print(result)

        mydb.commit()

        cursor = mydb.cursor()
        result = cursor.execute('DELETE from  TBL_USER_MASTER  WHERE email_id = %s and userid = %s',(username,user_status[1]))
        print(result)

        mydb.commit()

        resp = {
        "status":"200"
        }

        return resp
    else:
        resp = {
        "status":"400"
        }

        return resp




@app.route('/User_Approval', methods=['POST'])
def User_Approval():
    username = request.form.get('email_id')
    status = request.form.get('status')


    print(username)
    print(status)

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )



    cursor = mydb.cursor()
    result = cursor.execute('SELECT status from TBL_USER_MASTER  WHERE email_id = %s',(username))
    print(result)

    user_status = cursor.fetchone()
    print(user_status)


    if (user_status == "APPROVED" or user_status == "Rejected"):
        resp = {
        "status":"400"
        }
        return resp
    elif (status == 'Sucess'):



        cursor = mydb.cursor()
        result = cursor.execute('UPDATE TBL_USER_MASTER SET status= "APPROVED" WHERE email_id = %s ',(username))
        print(result)

        mydb.commit()

        resp = {
        "status":"200"
        }
        return resp
    elif (status == 'Failed'):


        cursor = mydb.cursor()
        result = cursor.execute('DELETE from  TBL_USER_MASTER  WHERE email_id = %s',(username))
        print(result)

        mydb.commit()

        resp = {
        "status":"200"
        }

        return resp
    else:
        resp = {
        "status":"400"
        }

        return resp



@app.route('/Agent_Approval', methods=['POST'])
def Agent_Approval():
    agent_name = request.form.get('agent_name')
    status = request.form.get('status')


    print(agent_name)
    print(status)

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )



    cursor = mydb.cursor()
    result = cursor.execute('SELECT status FROM TBL_Agent_MASTER WHERE agentname = %s',(agent_name))
    print(result)

    user_status = cursor.fetchone()
    print(user_status)


    if (user_status == "APPROVED" or user_status == "Rejected"):
        resp = {
        "status":"400"
        }
        return resp
    elif (status == 'Sucess'):



        cursor = mydb.cursor()
        result = cursor.execute('UPDATE TBL_Agent_MASTER  SET status= "APPROVED" WHERE agentname = %s ',(agent_name))
        print(result)

        mydb.commit()

        resp = {
        "status":"200"
        }
        return resp
    elif (status == 'Failed'):


        cursor = mydb.cursor()
        result = cursor.execute('DELETE from TBL_Agent_MASTER  WHERE agentname = %s',(agent_name))
        print(result)
        mydb.commit()

        resp = {
        "status":"200"
        }

        return resp
    else:
        resp = {
        "status":"400"
        }

        return resp







@app.route('/invite_user', methods=['POST'])
def invite_user():
    username = request.form.get('username')
    company_name = request.form.get('company_name')
    email = request.form.get('email')
    mobile_number = request.form.get('mobile_number')
    role = request.form.get('role')
    

    token = str(uuid.uuid1())

    p = ''.join(random.choices(string.ascii_letters +string.punctuation+ string.digits, k = 10))    
    
    aes_encrypt = encrypt_decrypt.AES_ENCRYPT()
    e = aes_encrypt.encrypt(p) 
    password = e.decode("utf-8")

    print(password)

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )

    cursor = mydb.cursor()
    result = cursor.execute('INSERT INTO `TBL_USER_MASTER`( `userid`, `username`, `password`, `mobile_number`, `email_id`, `role`, `token`, `CDT`, `MDT`, `status`) values(%s,%s,%s,%s,%s,%s,%s,now(),now(),"IN ACTIVE")',(company_name,username,password,mobile_number,email,role,token))
    print(result)

    mydb.commit()

    if (result == 1):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "User Invitation"
        msg["From"] = "noreply@rbm.studio"
        msg["To"] = "sagarravuri2@gmail.com"

        s = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        s.starttls(context=context)
        s.login("noreply@rbm.studio", "b4VZGdRTH")

        html = """\
<style>
.rbmbnt {
    background: rgb(118 59 117);
    color: #fff;
    font-weight: bold;
    padding: 6px 33px;
    border: none;
    border-radius: 2px;
}


.rbmbnt {
    margin: 12px !important;
    width: 135px;
    float: right;
}


p {
    font-size: 20px;
    }
.main-panel {
    margin: 0px !important;
    width: 100% !important;
}

.content-wrapper {
    margin-top: 0px;
    width: 100%;
}

</style>
<div class="main-panel" style="padding-top: 30px !important;">
  <div class="content-wrapper" style="margin-top:-30px">
    <div class="page-header" style="margin-bottom: 0px;">
  <center>    <h3 class="page-title" style="color:#763b75;    margin: 10px 0;"> User Invitation </h3></center>
    </div>
	<form action="#" method="POST" enctype="multipart/form-data">

    <div class="row">
        <div class="col-md-8 ">
          <div class="card">
            <div class="card-body">
              <h4 class="card-title"></h4>
              <form class="forms-sample">
                <div class="form-group">
		  <div class="row rowcust">
                    <p>
Hello <b>"""+username+"""</b>,</p>
<br>

<p>
&emsp; &emsp; We’ve given you access to our portal so that you can manage your journey with us and get to know all the possibilities offered by  our product and service.
</p>
<p>
You are Invited By <b>"""+company_name+"""</b>, </p>
<p>
 please click on the following link to Accept your Invitation :  &ensp;      https://rbm.studio/v2/User_Invite.php?token="""+token+"""
</p>
<br>
<br>
<br>
<p>
Thanks & Regards,
</p>
<p>
RBM.STUDIO
</p>
                </div>
                <br>
              </form>
            </div>
          </div>
	</div>

"""


        part = MIMEText(html, "html")
        msg.attach(part)
        s.sendmail("help.rbmstudio@gmail.com", email, msg.as_string())
        print("Mail sent")

        s.quit()

        resp={
            "status" :"200",
            "email" : email
        }
        return resp
    else :
        resp={
            "status" :"400",
            "email" : email
        }
        return resp


@app.route('/dashboard', methods=['POST'])
def dashboard_gui():
    
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    agentname = request.form.get('agentname')
    cursor = mydb.cursor()
    cursor.execute('select sum(SENT_COUNT) as SENT_COUNT,sum(DLVD_COUNT) as DLVD_COUNT , sum(READ_COUNT) as READ_COUNT from TBL_Campaign_STATS where agentname=%s',(agentname))   
    x = cursor.fetchone()
    # cursor = mydb.close()
    # cursor = mydb.cursor()
    cursor.execute('SELECT count(1) as count FROM  TBL_Campaign_STATS INNER JOIN  TBL_Campaign_Master ON TBL_Campaign_STATS.campaignid=TBL_Campaign_Master.campaignid where TBL_Campaign_STATS.agentname =%s',(agentname))
    y = cursor.fetchone()
    mydb.close()
    response={
                "SENT_COUNT":x[0],
                "DLVD_COUNT":x[1],
                "READ_COUNT":x[2],
                "TOTAL_CAMPAIGNS":y[0]
             }
    return response







@app.route('/reports_gui', methods=['POST'])
def reports_gui():

    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    agentname = request.form.get('agentname')
    cursor = mydb.cursor()
    cursor.execute('SELECT TBL_Campaign_STATS.campaignid, TBL_Campaign_Master.Message_type,TBL_Campaign_Master.Description,TBL_Campaign_Master.nickname,TBL_Campaign_Master.MESSAGE,TBL_Campaign_STATS.CDT,TBL_Campaign_STATS.SENT_COUNT, TBL_Campaign_STATS.DLVD_COUNT, TBL_Campaign_STATS.READ_COUNT , TBL_Campaign_Master.status FROM  TBL_Campaign_STATS INNER JOIN  TBL_Campaign_Master ON TBL_Campaign_STATS.campaignid=TBL_Campaign_Master.campaignid where TBL_Campaign_STATS.agentname = %s  and length(TBL_Campaign_STATS.SENT_COUNT) ORDER BY TBL_Campaign_Master.id DESC',(agentname))
    x = cursor.fetchall()
    print(x)



    objects_list = []
    for row in x:
        d = collections.OrderedDict()
        d["campaign_id"] = row[0]
        d["msg_type"] = row[1]
        d["nickname"] = row[2]
        d["Title"] = row[3]
        d["Description"] = row[4]
        d["Date"] = row[5]
        d["sent_count"] = row[6]
        d["dlvd_count"] = row[7]
        d["read_count"] = row[8]
        d["Status"] = row[9]
        objects_list.append(d)
    print(objects_list)

    cursor = mydb.close()
    response={
                "status" : "200",
                "Reports"  : objects_list

             }
    return response




@app.route('/teams', methods=['POST'])
def userprofile_teams(): 
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    userid = request.form.get('userid')
    cursor = mydb.cursor()
    cursor.execute('SELECT username, email_id, role from TBL_USER_MASTER where userid =%s',(userid))   
    x = cursor.fetchone()
    cursor = mydb.close()
    response={
                "username":x[0],
                "email_id":x[1],
                "role":x[2]
             }
    return response


@app.route('/dashboardcampaigns', methods=['POST'])
def dashboard_campaigns():
    
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    agentname = request.form.get('agentname')
    cursor = mydb.cursor()
    cursor.execute('SELECT  campaignid, agentname ,CDT, nickname, status FROM TBL_Campaign_Master WHERE agentname = %s ORDER BY TBL_Campaign_Master.id  DESC limit 5',(agentname))   
    x = cursor.fetchall()
    cursor = mydb.close()
    
    list = []
    for row in x:
        a = collections.OrderedDict()
        a["campaignid"] = row[0]
        a["agentname"] = row[1]
        a["CDT"] = row[2]
        a["nickname"] = row[3]
        a["status"] = row[4]
        list.append(a)
    response={
                "response" : list
             }
    return response


@app.route('/agentapproval', methods=['POST'])
def Agent_approval(): 
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    cursor = mydb.cursor()
    cursor.execute('SELECT agentid, agentname, desciption, mobilenumber,  website,  email,  privacy_url, terms_url, CDT, status FROM TBL_Agent_MASTER ORDER BY id DESC')   
    x = cursor.fetchall()
    cursor = mydb.close()
    response={
                "reports":x
             }
    return response

@app.route('/testnumbers', methods=['POST'])
def test_numbers():
    
    mydb = pymysql.connect(
    host="10.77.75.15",
    user="rcs_stats",
    password="RCS#stats@123",
    database="rbmstudio"
    )
    agentname = request.form.get('agentname')
    cursor = mydb.cursor()
    cursor.execute('SELECT MOBILE_NUMBER, status FROM TBL_TEST_NUMBERS WHERE AGENTNAME = %s order by id desc limit 5',(agentname))   
    y = cursor.fetchall()
    cursor = mydb.close()
    testnumbers = []
    for row in y:
        b = collections.OrderedDict()
        b["MOBILE_NUMBER"] = row[0]
        b["status"] = row[1]
        testnumbers.append(b)
    response={
                "response" : testnumbers
             }
    return response






if __name__ == '__main__':
    app.run(threaded=True)
