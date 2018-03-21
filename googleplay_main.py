from gp_data import GPDataCSV
from datetime import datetime
from send_mail import SendGmail
from crawl_gp import Crawl
from stat_module import StatModule

today = datetime.now().strftime("%Y-%m-%d")

### 오늘 데이터 리퀘스트
crawl = Crawl()
today_data = crawl.crawlGP()
#print(today_data)

### CSV 읽기
gp_data = GPDataCSV()
old_data = gp_data.read()
#print(old_data)

### 분석
stat = StatModule()
analyzedList = []
(analyzedList, need_save) = stat.analysis(today, today_data, old_data)
#print(analyzedList)

### 오늘 자료 저장
if need_save:
    title_list = []
    for item in today_data:
        title_list.append(item["game"])
    gp_data.save(today, title_list)


dayOfWeekToday = datetime.now().strftime("%A")

####메일 보내기
myAccount = 'eunbi.alert@gmail.com'
myPw = 'eunbialert123'
sendTo = 'eunbi66@ncsoft.com'
subject = '{} 국내 Google Play Top 50'.format(today)

gmail = SendGmail(myAccount, myPw, sendTo, subject)

for i in analyzedList:
    gmail.html += "<tr><td align='center'>{}</td><td>{}</td><td>{}</td><td align='center'>{}</td></tr>\n".format(i['rank'], i['game'], i['company'], i['delta'])
gmail.html += "</table></body>"
#<td><img src ='https:{}' width='50px' height='50px'></td>

#gmail.send() if dayOfWeekToday == "Monday" else None
gmail.send()