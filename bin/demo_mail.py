import smtplib
import webbrowser
recepient=input("Enter the recepient's email: ")
x=input("Will there be a subject in the email? ")
x_n=["no","not really","nope","nah",""]
x_y=["yes","yep","yeas","yeah"]
if x.lower() in x_n:
    print("Alright, no subject it is, so enter the body of the email to be sent!")
    sub=""
    body=input("Here: ")
elif x.lower() in x_y:
    print("Alright, enter the subject of the email then!")
    sub=input("Here: ")
    print("and now the body!")
    body=input("Here: ")

def sendMail(sndr_mail,sndr_pw,rcpnt,msg_sub,msg_body):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sndr_mail, sndr_pw)
        subject=msg_sub
        body=msg_body
        msg=f'Subject: {subject}\n\n{body}'
        try:
            smtp.sendmail(sndr_mail,rcpnt,msg)
            print("Email Sent Successfully!")
        except:
            print("Connection to the email server was unsuccessful! Please check the account credentials and also make sure that \"Less Secure Apps\" for your google account is turned on in order for the program to function! Please Note that we do not save your account info to ourselves and hence we cannot possibly compromise your information but that cannot be said for other 'less secure apps', hence it's solely your call. P.S. we'd soon update the email operation to work more safely and securely, so if you don't mind you can wait for future updates.")
            y=input("But if you're okay with all of this, enter 'YES' or 'OK' and a webpage will be prompted with an option to turn on \"Less Secure Apps\" for your google account and just by clicking on that the program will be good to go! Else enter 'NO' and act wise!")
            if y.lower()=="yes" or y.lower()=="ok" or y.lower()=="okay":
                print("Great! Here you go!")
                webbrowser.open("https://myaccount.google.com/lesssecureapps?")
                return
            elif y.lower()=="no" or y.lower()=="nope":
                print("Alright!")
                return
