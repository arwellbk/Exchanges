import requests
import json

doviz = requests.get('https://finans.truncgil.com/today.json', headers={"User-Agent":"Mozilla/5.0"}).content.decode("utf-8")
doviz = json.loads(doviz)


with open("data.json", "w") as f:
    json.dump(doviz, f, ensure_ascii=False)


def get():
    with open("data.json") as f:
        kurlar = json.load(f)
        return kurlar

data = get()


usd = {
    'Alış': data['USD']['Alış'],
    'Satış': data['USD']['Satış'],
    'Değişim': data['USD']['Değişim']
}

eur = {
    'Alış': data['EUR']['Alış'],
    'Satış': data['EUR']['Satış'],
    'Değişim': data['EUR']['Değişim']
}

gram = {
    'Alış': data['gram-altin']['Alış'],
    'Satış': data['gram-altin']['Satış'],
    'Değişim': data['gram-altin']['Değişim']
}

ceyrek = {
    'Alış': data['ceyrek-altin']['Alış'],
    'Satış': data['ceyrek-altin']['Satış'],
    'Değişim': data['ceyrek-altin']['Değişim']
}


def show():
    try:
        print()
        print("Döviz (TRY)".center(50, '*'))
        print(data['Update_Date'].center(50, ' '))
        print(
            f'''Dolar\n--------------\nAlış: {str(usd['Alış'])} TL\nSatış: {str(usd['Satış'])} TL\nDeğişim: {str(usd['Değişim'])}\n\n'''
        )
        print(
            f'''Euro\n--------------\nAlış: {str(eur['Alış'])} TL\nSatış: {str(eur['Satış'])} TL\nDeğişim: {str(eur['Değişim'])}\n\n'''
        )
        print(
            f'''Çeyrek Altın\n--------------\nAlış: {str(ceyrek['Alış'])} TL\nSatış: {str(ceyrek['Satış'])} TL\nDeğişim: {str(ceyrek['Değişim'])}\n\n'''
        )
        print(
            f'''Gram Altın\n--------------\nAlış: {str(gram['Alış'])} TL\nSatış: {str(gram['Satış'])} TL\nDeğişim: {str(gram['Değişim'])}\n'''
        )
    except:
        pass

show()
