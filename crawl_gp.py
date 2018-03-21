import requests
from bs4 import BeautifulSoup

class Crawl:
    def __init__(self):
        self.info = {}

    def crawlGP(self):
        headers = {
            'origin': 'https://play.google.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'accept': '*/*',
            'referer': 'https://play.google.com/store/apps/category/GAME/collection/topgrossing',
            'authority': 'play.google.com',
            'cookie': 'CONSENT=YES+KR.ko+20170618-09-0; _ga=GA1.3.1461945379.1495380591; SID=3QX7f3NzU1XLPxXSEwHsKzvRLWbdq2C2PxCKQlYo4AcuTxPv8ZzVPAYsbAPstC_60AlIJw.; HSID=AcGVd5uE9DrMrUS-S; SSID=AApZZivq9qm4aiKnt; APISID=TNKcCGUmhJ3Xc_7C/ATg4k46vIzRqgg8Qe; SAPISID=QRgMwWKj7EBNZIZg/A7qyAjPg5KQn3rLDg; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=eunbi.alert@gmail.com; PLAY_PREFS=Cq0MCPv_mbOwDBKjDAoCS1IQ0PL_n6IsGuQLERITFBUWGDrZAacCxATjBeUF6AXXBtkG3gbfBpCVgQaRlYEGkpWBBpSVgQaXlYEGpJWBBriVgQbAlYEGwZWBBsSVgQbFlYEGx5WBBsiVgQbOlYEGz5WBBtCVgQbUlYEG2ZWBBvKVgQb4lYEG-ZWBBoSWgQaJloEGipaBBo-WgQaQloEGnJaBBp2WgQaeloEGn5aBBqCWgQalloEGppaBBqeWgQasloEG7peBBu-XgQaFmIEGiZiBBouYgQa-mIEGq5uBBq2bgQbJm4EGypuBBsubgQbVm4EGvJ2BBt2dgQbnnYEGkJ6BBpaegQbiooEG86KBBoujgQaapIEGnqSBBuqlgQbGpoEG_qaBBoCngQaCp4EGhKeBBoangQaIp4EGiqeBBs6ogQbyqIEG9KiBBrysgQbWr4EGwbCBBoeygQaJsoEG1rKBBrG0gQbWuYEGjsCBBqLAgQbAwIEGwcCBBvLAgQbWwoEGjMWBBsrGgQb4x4EGqsqBBtjMgQbczIEG3c2BBobOgQahz4EGxNKBBpXVgQba2IEG4tiBBpPZgQby24EG2OSBBpflgQa46IEGz-uBBrDsgQbX9YEGuvuBBrD_gQa7_4EGxP-BBsn_gQbVg4IGyISCBrmGggamh4IGp4eCBuyHggbth4IG642CBvuNggaJjoIGy5GCBpWYggaPmoIGmZqCBsGaggb3moIGnZ6CBtWegga6oIIGu6CCBvaiggbipIIGkqWCBqulggbNpYIG8qeCBp6ogga0qIIGrbaCBvy5ggb-uYIG_7mCBsK7ggaPv4IG6sCCBrzBggaQy4IGkcuCBs3LggbRy4IG3MyCBtjQggbz0YIGi9KCBtvTggaB2IIGhtqCBo3aggab2oIGo9qCBq3bggau24IGxduCBpjcggax3IIG6t2CBvjdggbv34IGpOGCBtDhggbk4YIG5eGCBpbpggaj7YIGhe6CBrPuggaM8IIGsfCCBpbxgga-8YIG6_aCBq34ggaz-IIG9vqCBt77ggbf-4IG4_uCBoX8ggbb_IIG3PyCBv_8ggaB_YIGgv-CBoCAgwaJgYMG3IGDBvKBgwaBgoMG6YSDBpCFgwbXh4MGm4iDBtCIgwbwiIMG842DBoWPgwaQj4MGz5CDBt-QgwbZkYMG_JGDBvySgwaslYMGuJWDBp2WgwaeloMGwJaDBuOWgwbcl4MGmZuDBu2bgwbum4MG0JyDBvSegwaVn4MGxp-DBtOfgwaYoIMGm6CDBv2ggwbWooMGuaODBuergwbgroMGjK-DBuyvgwaWsIMGlbSDBpi0gwattIMGuLaDBqS3gwbxt4MGr7iDBri4gwbCuIMG4LyDBvS8gwb2vIMGsL6DBs2-gwa-wIMGsMGDBvLBgwbJwoMGuMaDBuTGgwatyIMGnsmDBpvKgwadyoMG9cuDBofNgwb-zYMGutCDBujQgwb504MG69SDBofVgwbP1oMG69aDBpHXgwbj14MG6deDBtHZgwas3IMGjt2DBoLfgwaR34MG4d-DBoDggwaZ4YMG7-ODBv_lgwaT5oMG1-iDBuLogwbw6IMGwemDBprrgwbI7IMG6uyDBpLugwaV7oMG4--DBqTygwbV9IMGz_WDBvT3gwaM-IMGjfiDBpf4gwbY-IMG3vmDBvr5gwaR-oMGq_qDBsP6gwaW_YMGjP6DBpGAhAajgIQGp4GEBsyBhAbdgYQG34GEBvSBhAaGg4QG1oOEBvqDhAaihIQGw4SEBteEhAbahoQG4oeEBumJhAapi4QGq4uEBqyLhAbEi4QG9oyEBoCOhAaUjoQGvY6EBv2OhAbHj4QGkZCEBuKQhAbQkYQG7ZGEBvyRhAbhkoQG7pOEBpyXhAafl4QGxJeEBs2XhAbzl4QGn5iEBqOYhAaDmYQGlZmEBqGZhAaimYQGvJmEBsGZhAbpmYQG9JqEBtGbhAbgm4QG-JuEBoechAbcnIQGlZ2EBuKdhAabnoQGp56EBrSehAbxnoQG4J-EBv2fhAYo0PT_n6IsOiRkNjQ0ZmNmNS0zZGU3LTRiNDctODUzYi1mNjg3NDEzODc0NGRAAUgA:S:ANO1ljJYcHwf49bP1g; _gid=GA1.3.595645777.1521022403; 1P_JAR=2018-3-14-10; NID=125=e9svU7Chn0Atca_XRwsMLyR-mMpcXnHA2KEZOxySDHXwkoqefLbWFuS-5htfIUj5rqJdyhrGkRJpUUTivamQ5C2zSciGvWEXhwD6_eyp01TN6PbxEXwyseD2iwjHlcpERyvz8MHQ_Uo5s72U9ePfqb5abySy6pjoy4KCvCP-Kfg1MQVcgho8KYUw6tXjQTJfWCg6zlZYTcfJUmnOmIhnlGAQ3WC7QMRvUBRXkeFT1e3WJyVoMiCcIfxUi0EQxS44xpdSQTW7yOkU00zb8Om_gHkBpzg; S=billing-ui-v3=6VGOYAibbJNrKWaZdlNgfO5gTc__HBQo:billing-ui-v3-efe=6VGOYAibbJNrKWaZdlNgfO5gTc__HBQo; SIDCC=AAiTGe8pwAVjCI25hqcTZCocUWTU_wrOAjBtg1O8peiUub_lFNhYtbY35uZzxEi5IaNNcSQEpg; _gat=1',
            'x-client-data': 'CJS2yQEIprbJAQjEtskBCIOYygEIqZ3KAQioo8oB',
        }

        params = (
            ('authuser', '0'),
        )

        data = [
            ('ipf', '1'),
            ('xhr', '1'),
            ('token', 'VoKulTzrKQrxJ8ZKio29YYCgXDY:1521022401111'),
        ]

        response = requests.post('https://play.google.com/store/apps/category/GAME/collection/topgrossing',
                                 headers=headers, params=params, data=data)

        bs = BeautifulSoup(response.text, "html.parser")
        a = bs.find_all(class_="title")
        b = bs.find_all(class_="subtitle")
        imglist = []

        for img in bs.find_all("img"):
            imglist.append(img.get("src"))

        i = 0
        l = []

        while i < 50:
            txt = a[i].text
            txt2 = b[i + 1].text
            info = {
                "rank": txt.split()[0].strip().replace(".", ""),
                "game": " ".join(txt.split()[1:]).strip(),
                "company": txt2,
                "img": imglist[i],
                "delta" : "-"
            }
            l.append(info)
            i += 1

        #print(l)
        return l
