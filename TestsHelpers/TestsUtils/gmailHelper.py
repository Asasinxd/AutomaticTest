import imaplib
import email
import json
from time import time

class GmailHelper():
    def __init__(self, host = None, port = None, password = None, email = None):
        self.mail = None
        self.host = host
        self.port = port
        self.password = password
        self.email = email
        self.emailWithCounter = email

        if (host == None) or (port == None) or (password == None) or (email == None):
            data = dict()
            with open('TestsHelpers/UserOauthInterface/JsonFiles/emailConfig.json', 'r') as data_file:
                data = json.load(data_file)
            if host == None: self.host = data["IMAP4"]["Gmail"]["host"]
            if port == None: self.port = data["IMAP4"]["Gmail"]["port"]
            if password == None: self.password = data["IMAP4"]["Gmail"]["password"]
            if email == None:
                self.email = data["IMAP4"]["Gmail"]["email"] + data["IMAP4"]["Gmail"]["domain"]
                self.emailWithCounter = data["IMAP4"]["Gmail"]["email"] + "+" + str(time()).replace(".", "") + data["IMAP4"]["Gmail"]["domain"]

    def logInAndSetUp(self):
        self.mail = imaplib.IMAP4_SSL(self.host, port = self.port)
        self.mail.login(self.email, self.password)
        self.mail.select('INBOX')
        print("Loged in, and set up mail")

    def removeAllMessages(self):
        _, data = self.mail.search(None, 'ALL')
        for num in data[0].split():
            self.mail.store(num, '+FLAGS', '\\Deleted')
        self.mail.expunge()
        print("Removed all massages")

    def getLastMail(self):
        print("Try to read last mail")
        _, response = self.mail.search(None, 'ALL')
        message = response[0].split()

        lastMessage = message[len(message) - 1]
        _, data = self.mail.fetch(lastMessage, '(RFC822)')
        mesg = self.getEmailMessage(email.message_from_bytes(data[0][1])).decode('utf-8')
        print("Readed last mail")
        return mesg

    def refresh(self):
        self.logOut()
        self.logInAndSetUp()
        print("Refreshed")

    def logOut(self):
        self.mail.close()
        self.mail.logout()
        print("Logged out and closed mail")

    def getEmailMessage(self, message):
        if message.is_multipart():
            return self.getEmailMessage(message.get_payload(0))
        else:
            return message.get_payload(None, True)
