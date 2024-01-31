import requests
from bs4 import BeautifulSoup


class checkIEMI:
    url = 'http://nw-restriction.nttdocomo.co.jp/'
    url_data = ['top.php', 'search.php', 'result.php']
    data = {}
    switchStr = {
        '◯': "ネットワーク利用制限の対象外です。",
        '△': '利用できますが、代金債務の不履行等により利用制限となる可能性があります。',
        '×': '利用制限中です。',
        '-': 'IMEI（製造番号）が確認できません。'
    }

    def __init__(self, IMEI):
        self.data['productno'] = IMEI

    def getData(self):
        return self.data

    def setData(self, IMEI):
        self.data['productno'] = IMEI

    def Run(self):
        session = requests.Session()
        rep01 = session.get(self.url + self.url_data[0])
        rep02 = session.post(self.url + self.url_data[1], data=self.getData())
        str = self.soupString(rep02)
        return str

    def soupString(self, rep):
        soup = BeautifulSoup(rep.text, 'html.parser')
        back_string = soup.find_all('div', class_='result-panel')
        return back_string[1].string



