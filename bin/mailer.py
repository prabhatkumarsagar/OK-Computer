import smtplib
import webbrowser
import usr_signup

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


def mail_sender():
    sender=usr_signup.info_out("email")
    if sender=="":
        print("Hey you haven't told me your email yet, you might wanna do it first if you want to proceed with this operation.")
        return
    sender_pass=usr_signup.info_out("password")
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
    try:
        sendMail(sender,sender_pass,recepient,sub,body)
    except:
        print("Uh-oh! It looks like i ran into some trouble doing that, you mind doing it later?")

#mail_sender()

def feedback_sender():
    sender=usr_signup.info_out("email")
    if sender=="":
        print("Hey you haven't told me your email yet, you might wanna do it first if you want to proceed with this operation.")
        return
    sender_pass=usr_signup.info_out("password")
    def pda_feedback(x,y):
        sendMail(sender,sender_pass,["sagarprabhatkumar@gmail.com","sagarprabhatkumar13@gmail.com","duttashaan107@gmail.com","duttashaan102@gmail.com"],x,y)
        #sendMail(sender,sender_pass,["sagarprabhatkumar@gmail.com","sagarprabhatkumar13@gmail.com"],x,y)
        return
    while True:
        print("\nWhat do you wanna feed-back? xD")
        print("1. Report a bug")
        print("2. Suggest Improvement")
        print("3. Get in touch with the developers")
        print("4. Something Else")
        print("5. Nothing (Exit)")
        x=input("Enter Choice: ")
        if x=="1":
            subject="Python Desktop Assitant Feedback - Bug Report"
            body=input("Please specify the bug you've encountered: ")
            try:
                pda_feedback(subject,body)
            except:
                print("Uh-oh! It looks like i ran into some trouble doing that, you mind doing it later?")
                return
        elif x=="2":
            subject="Python Desktop Assitant Feedback - Improvements Suggestion"
            body=input("Please explain verbosely what improvement would you like to see in the future updates: ")
            try:
                pda_feedback(subject,body)
            except:
                print("Uh-oh! It looks like i ran into some trouble doing that, you mind doing it later?")
                return
        elif x=="3":
            subject="Python Desktop Assitant Feedback - User Contact"
            body=input("What would you want to say to my developers: ")
            try:
                pda_feedback(subject,body)
            except:
                print("Uh-oh! It looks like i ran into some trouble doing that, you mind doing it later?")
                return
        elif x=="4":
            subject="Python Desktop Assitant Feedback - Feedback"
            body=input("What would you like to say: ")
            try:
                pda_feedback(subject,body)
            except:
                print("Uh-oh! It looks like i ran into some trouble doing that, you mind doing it later?")
                return
        elif x=="5":
            print("Alright, come back again when you have something to say!")
            break
        else:
            print("Invalid Input! Please try again!")
            continue
            
#feedback_sender()