import requests
import xmltodict

def coordinate():
    while True:
        full_address = input("住所を入力してください(q:quit):")
        if "q" == full_address:
            break
        try:
            url = 'http://www.geocoding.jp/api/'
            payload = {'q':full_address}
            result = requests.get(url, payload)
            print(result.text)
            resultdict = xmltodict.parse(result.text)
            print("緯度",resultdict["result"]["coordinate"]["lat"])
            print("経度",resultdict["result"]["coordinate"]["lng"])
        except Exception as others:
            print("存在しない住所です")

coordinate()