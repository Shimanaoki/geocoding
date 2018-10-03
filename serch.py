import requests
import xmltodict

def coordinate():
    full_adress = input("Prease enter the adress:")
    url = 'http://www.geocoding.jp/api/'
    payload = {'q':full_adress}
    result = requests.get(url, payload)
    print(result.text)
    resultdict = xmltodict.parse(result.text)
    print("緯度",resultdict["result"]["coordinate"]["lat"])
    print("経度",resultdict["result"]["coordinate"]["lng"])

coordinate()