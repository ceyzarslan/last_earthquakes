import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.koeri.boun.edu.tr/scripts/sondepremler.asp'
response = requests.get(url)
if response.status_code == 200:
    content = response.content  # binary string olarak bir data döner
    soup = BeautifulSoup(content, "html.parser")
    pre = soup.find('pre')
    text = pre.text
    lines = text.splitlines()[7:-1]
    print(len(lines), lines)
    earthquakes = []
    for line in lines:
        # datayı ayıklayacağım
        cols = re.split("\\s{2,}", line)  # \s boşluk anlamına gelir 2 veya daha fazla boşluk varsa line böl
        print(cols)
        eq = {
            "Tarih_Saat" : cols[0],
            "enlem" : float(cols[1]),
            "boylam": float(cols[2]),
            "derinlik": float(cols[3]),
            "şiddet": float(cols[5]),
            "yer": cols[7]
        }
        earthquakes.append(eq)
    print(earthquakes)