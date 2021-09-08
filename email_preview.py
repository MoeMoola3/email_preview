import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import email

pop3server = 'pop.gmail.com'
username = 'te3621057@gmail.com'
password = 'rzhwjfidshiqyelj'
pop3server = poplib.POP3_SSL(pop3server) # open connection
print (pop3server.getwelcome()) #show welcome message
pop3server.user(username)
pop3server.pass_(password)
pop3info = pop3server.stat() #access mailbox status
mailcount = pop3info[0] #total email
print("Total no. of Emails : " , mailcount)
print ("\n\n")

 

mails = pop3server.list()
index = len(mails)


for i in range(mailcount+1)[1:]:
    resp, lines, octets = pop3server.retr(i)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # now parse out the email object.
    msg = Parser().parsestr(msg_content)
    # get email from, to, subject attribute value.
    email_from = msg.get('From')
    # email_to = msg.get('To')
    email_subject = msg.get('Subject')


    sliced = (pop3server.list()[1][i-1])[2:]
    convToStr = str(sliced)

    print('email no: '+ str(i))
    print('From: ' + email_from)
    print('Subject: ' + email_subject)
    print('Size of email: ' + convToStr[2:-1]+' bytes')


    print("\n\n")


chosenInput = input("Would you like to delete an email ")
if(chosenInput=='y'):           
    pop3server.quit()

    #from here use imaplib
    import imaplib

    my_email = "te3621057@gmail.com"
    app_generated_password = "rzhwjfidshiqyelj"

    #initialize IMAP object for Gmail
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    #login to gmail with credentials
    imap.login(my_email, app_generated_password)

    imap.select("INBOX")

    status, message_id_list = imap.search(None, 'ALL')

    #convert the string ids to list of email ids
    messages = message_id_list[0].split(b' ')

    # print(messages)
    
    input2 = input("Select the email number you would like to delete: ")
    intConv = int(input2)-1
    

    imap.store(messages[intConv], "+FLAGS", "\\Deleted")
    imap.expunge()

    print("Email "+input2+" has been deleted")

    # close the mailbox
    imap.close()

    # logout from the account
    imap.logout()
