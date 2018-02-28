import requests
from bs4 import BeautifulSoup

headers = {
    'origin': 'https://play.google.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'x-chrome-uma-enabled': '1',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'accept': '*/*',
    'referer': 'https://play.google.com/store/apps/category/GAME/collection/topgrossing',
    'authority': 'play.google.com',
    'cookie': 'CONSENT=YES+KR.ko+20170618-09-0; _ga=GA1.3.404577345.1482201926; HSID=A6gbrJD3QEbGLKhAf; SSID=Ae2gq7pAe6vdZWs1H; APISID=vkx3lTWWyu8zHHa2/AzheEi-WweguWpESu; SAPISID=jmqT1l2YZrBN9Vac/ArdiIb_nbzJMVg5vT; SID=twX-YB33seIrUZTzKFa6sVpD9x8FRlvZeTZl01bPkqfK1jWyR3InZYBxiKcafoInLR2E3w.; __gads=ID=298db27ae87b7f98:T=1519191117:S=ALNI_MZhKGW1f_hJ9Fc4Rt1uP_a3FU6Ouw; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=eunbi896@gmail.com; _gid=GA1.3.1203932228.1519716785; PLAY_PREFS=CqUMCP7B6Z_xDxKbDAoCS1IQiqKRtp0sGtwLEhMYOvEBrQLhA8UEgQWMBeMF5QXoBdcGkJWBBpGVgQaSlYEGlZWBBpeVgQaklYEGuJWBBsCVgQbBlYEGxJWBBsWVgQbHlYEGyJWBBsmVgQbMlYEGzZWBBs6VgQbUlYEG2JWBBt2VgQbxlYEG-JWBBvuVgQb_lYEGgpaBBoSWgQaHloEGipaBBo6WgQaQloEGlpaBBpmWgQacloEGoZaBBqKWgQajloEGpJaBBu6XgQbvl4EGgZiBBoWYgQaJmIEGi5iBBr6YgQarm4EGrZuBBsibgQbKm4EGy5uBBtWbgQa8nYEG3Z2BBuedgQaQnoEGy6GBBsyhgQbNoYEG4qKBBvOigQaLo4EGmqSBBp6kgQb9pIEG_qSBBu2lgQbGpoEG_qaBBoCngQaCp4EGhKeBBoangQaIp4EGiqeBBs-ngQbyqIEG9KiBBrysgQbWr4EGwbCBBoeygQaJsoEG1rKBBpy0gQbut4EGjsCBBqLAgQbAwIEGwcCBBvLAgQajwYEG1sKBBvjHgQbuyIEGqsqBBtjMgQbdzYEGhs6BBqHPgQbE0oEGldWBBtrYgQbi2IEGk9mBBvLbgQbY5IEG3OSBBpflgQa46IEGz-uBBrDsgQbX9YEGuvuBBrD_gQbB_4EGxv-BBsf_gQbI_4EG1YOCBsiEgga5hoIGpoeCBqeHggbth4IG-42CBomOggbLkYIGlZiCBpmaggbBmoIG95qCBp2eggbVnoIGuqCCBrugggb2ooIG4qSCBpKlggarpYIGzaWCBvKnggaeqIIGtKiCBq22ggb4uIIGxrmCBsK7ggaPv4IG6sCCBrzBggaQy4IGkcuCBs3LggbRy4IG3MyCBtjQggbz0YIGi9KCBtfTggbd04IGjNaCBoHYggaG2oIGkNqCBpvaggaj2oIGrduCBq7bggaY3IIGsdyCBurdggb43YIG79-CBqbhggbQ4YIG5OGCBuXhggaW6YIGo-2CBoXuggaz7oIGjPCCBrHwggaW8YIGvvGCBuv2ggat-IIGs_iCBvb6ggbe-4IG3_uCBuP7ggaF_IIG2_yCBtz8ggb__IIGgf2CBoL_ggaAgIMGiYGDBtyBgwbygYMGgYKDBuiEgwbXh4MGm4iDBtCIgwbwiIMG842DBoWPgwaQj4MG2ZGDBvyRgwb8koMGrJWDBriVgwadloMGnpaDBsCWgwbjloMG3JeDBuGZgwbimYMG55mDBtuagwaZm4MG7ZuDBu6bgwbQnIMG9J6DBpWfgwbGn4MG05-DBpiggwaboIMG_aCDBtaigwa5o4MG56uDBuCugwaMr4MG7K-DBpawgwaVtIMGrbSDBri2gwajt4MG8beDBp24gwafuIMGobiDBqO4gwaluIMGrbiDBq-4gwa4uIMGwLiDBsK4gwbgvIMG9LyDBvW8gwb2vIMGrr6DBs2-gwawwYMG9MGDBsnCgwazxoMGuMaDBuTGgwatyIMGnsmDBpvKgwacyoMGqcqDBvXLgwb-zYMGutCDBujQgwbp0IMG7NODBvnTgwbr1IMGh9WDBpbVgwbP1oMG19aDBuvWgwaQ14MG4teDBuPXgwbp14MG0dmDBoTcgwas3IMGit2DBo7dgwaC3oMGgt-DBpTfgwbh34MGleGDBu_jgwaU5YMG_-WDBpDmgwbf6IMGmuuDBsjsgwbq7IMGle6DBt_ugwbj74MGpPKDBtH0gwbB9YMG-PeDBor4gwaN-IMGl_iDBt75gwae-oMGrfqDBsH6gwbH-oMG_PuDBpP8gwar_IMGlv2DBp39gwaM_oMGk_6DBpj-gwbt_4MGkYCEBqOAhAangYQG04GEBvSBhAaGg4QG1oOEBvqDhAaNhIQGqYSEBsSEhAb_hoQG4oeEBqKIhAbpiYQGhoqEBqiLhAbEi4QGnYyEBvaMhAaRjoQGlI6EBv6OhAaYj4QGx4-EBoSQhAaakIQGnpCEBvaQhAbVkYQG7pOEBvGWhAafl4QG8peEBp6YhAafmIQGKPWxt7GdLDokN2I4N2JjNjAtMDRmMi00YjJhLTg0OTUtOTc3MmFkNDZhNWRmQAFIAA:S:ANO1ljJvckrv4ktKQw; _gat=1; 1P_JAR=2018-2-27-10; NID=124=OQ2fg9D6gczFuRzH1Rb4NjFelpRFeNjauNEsqLcrtxR-2o6IezQXFxcsrMxAN4ZfJBSepVOtrnUNADBO4L1pR30jKs-zO58jQeenppvBAC_5P2IzRYM_hnoirrI3eExqZDf-h3vFlK_4UYgF7Uulot4Hzt7MRwrfFi8Q_VS9C147s_neMz3dLcDAnP3ymrICO5TAIDuX_x6yOxG3Wh0Tv0HRa8IuukpWm6v3j-70siw; S=billing-ui-v3=JzjgUmlppoeJeEW-pdT88Nz9yAO0yQ6a:billing-ui-v3-efe=JzjgUmlppoeJeEW-pdT88Nz9yAO0yQ6a; SIDCC=AAiTGe9oZ1vLFxuqfw8CGbCB-C-XlGpKvHA04gFTnAd5yAl7vQPa7ljeTcXkt09k5OKlVp5Plio',
    'x-client-data': 'CIq2yQEIorbJAQjBtskBCKmdygEIqKPKAQ==',
}

params = (
    ('authuser', '0'),
)

data = [
  ('ipf', '1'),
  ('xhr', '1'),
  ('token', 'Gndz2ZYUX59AcvZBKWliyLXHKfo:1519726648111'),
]

response = requests.post('https://play.google.com/store/apps/category/GAME/collection/topgrossing', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://play.google.com/store/apps/category/GAME/collection/topgrossing?authuser=0', headers=headers, data=data)

bs = BeautifulSoup(response.text, "html.parser")
a = bs.find_all(class_ = "title")
b = bs.find_all(class_ = "subtitle")
print(a)
print(b)
info = {}
i = 0
print(len(a))
l = []
while i < 50:
    txt = a[i].text
    txt2 = b[i+1].text
    info = {
        "rank" : txt.split()[0].strip().replace(".", ""),
        "game" : " ".join(txt.split()[1:]).strip(),
        "company" : txt2
    }
    l.append(info)
    i += 1
print(l)

import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

today = datetime.now().strftime("%Y-%m-%d")

msg = ""

html = """
    <table style='border: 1px solid #333; border-collapse: collapse; '>
    <style>
    td { border : 1px solid #333; span: 3px; }
    </style>
"""
link = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
for i in l:
#    msg += "{}. {}, {}".format(i["rank"], i["game"], i["company"]) + "\n"
    html += f"<tr><td>{i['rank']}</td><td>{i['game']}</td><td>{i['company']}</td><td><img src='{link}' width='200px' height='100px' /></td></tr>\n"
html += "</table>"

print(html)
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()  # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('eunbi.alert@gmail.com', 'eunbialert123')

msg = MIMEMultipart('alternative')
msg['Subject'] = '구글플레이 매출 순위 {}'.format(today)
msg['To'] = 'eunbi66@ncsoft.com'
part2 = MIMEText(html, 'html')
msg.attach(part2)
smtp.sendmail('eunbi.alert@gmail.com', 'eunbi66@ncsoft.com', msg.as_string())

smtp.quit()
