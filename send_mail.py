import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendGmail:
    def __init__(self, account, pw, to, sbjt):
        self.html = """
            <body>매주 월요일 오전 9시 국내 구글플레이 게임 매출 Top 50 자동 발송 \n\n\n 
            <table style='border: 1px solid #333; border-collapse: collapse; '>
            <style>
            td { border : 1px solid #333; padding: 3px 5px 3px 5px; }
            th { border : 1px solid #333; padding: 3px 5px 3px 5px; }
            </style>
            <tr>
            <th>NO.</td>
            <th>TITLE</td>
            <th>COMPANY</td>
            <th>1WK △</td>
            </tr>\n
        """
        #<th>IMG</td>
        self.account = account
        self.password = pw
        self.sendTo = to
        self.subject = sbjt

    def send(self):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()  # say Hello
        smtp.starttls()  # TLS 사용시 필요
        smtp.login(self.account, self.password)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['To'] = self.sendTo

        part2 = MIMEText(self.html, 'html')

        msg.attach(part2)
        smtp.sendmail(self.account, self.sendTo, msg.as_string())

        smtp.quit()
