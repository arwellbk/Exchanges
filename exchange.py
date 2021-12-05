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
    'Alış': get()['USD']['Alış'],
    'Satış': get()['USD']['Satış'],
    'Değişim': get()['USD']['Değişim']
}

eur = {
    'Alış': get()['EUR']['Alış'],
    'Satış': get()['EUR']['Satış'],
    'Değişim': get()['EUR']['Değişim']
}

gram = {
    'Alış': get()['gram-altin']['Alış'],
    'Satış': get()['gram-altin']['Satış'],
    'Değişim': get()['gram-altin']['Değişim']
}

ceyrek = {
    'Alış': get()['ceyrek-altin']['Alış'],
    'Satış': get()['ceyrek-altin']['Satış'],
    'Değişim': get()['ceyrek-altin']['Değişim']
}


def show():
    try:
        print()
        print("Döviz (TRY)".center(50, '*'))
        print(get()['Update_Date'].center(50, ' '))
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
''' arwell#4774 '''