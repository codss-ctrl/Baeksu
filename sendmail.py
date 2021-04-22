import smtplib                           
from email.mime.text import MIMEText

class SendMail:
    def sendmail(self, recvEmail, title, content):
        smtpName = "smtp.naver.com"                   
        smtpPort = 587                              
        
        sendEmail = "dnjohn@naver.com"
        password = "eoejrxptmxm!"
        
        msg = MIMEText(content)                     
        msg['From'] = sendEmail
        msg['To'] = recvEmail
        msg['Subject'] = title
        
        print(msg.as_string())                        
        
        s = smtplib.SMTP(smtpName , smtpPort)         
        s.starttls()                                
        s.login(sendEmail , password)                
        s.sendmail(sendEmail, recvEmail, msg.as_string())  
        s.close()                                     