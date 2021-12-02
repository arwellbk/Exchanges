import requests
import json

doviz = requests.get('https://finans.truncgil.com/today.json').text.replace(
    '\u0131', 'i').replace('\u015f', 's').replace('\u011f', 'g').replace('\u00fc', 'ü')
doviz = json.loads(doviz)


def save():
    with open("data.json", "w") as f:
        json.dump(doviz, f)


def get():
    with open("data.json") as f:
        kurlar = json.load(f)
        return kurlar


usd = {
    'alis': get()['USD']['Alis'],
    'satis': get()['USD']['Satis'],
    'degisim': get()['USD']['Degisim']
}

eur = {
    'alis': get()['EUR']['Alis'],
    'satis': get()['EUR']['Satis'],
    'degisim': get()['EUR']['Degisim']
}

gram = {
    'alis': get()['gram-altin']['Alis'],
    'satis': get()['gram-altin']['Satis'],
    'degisim': get()['gram-altin']['Degisim']
}

ceyrek = {
    'alis': get()['ceyrek-altin']['Alis'],
    'satis': get()['ceyrek-altin']['Satis'],
    'degisim': get()['ceyrek-altin']['Degisim']
}


def show():
    try:  
        print("Döviz (TRY)".center(50, '*'))
        print(get()['Update_Date'].center(50, ' '))
        print(
            f'''Dolar\n--------------\nAlış: {str(usd['alis'])} TL\nSatış: {str(usd['satis'])} TL\nDeğişim: {str(usd['degisim'])}\n\n'''
        )
        print(
            f'''Euro\n--------------\nAlış: {str(eur['alis'])} TL\nSatış: {str(eur['satis'])} TL\nDeğişim: {str(eur['degisim'])}\n\n'''
        )
        print(
            f'''Çeyrek Altın\n--------------\nAlış: {str(ceyrek['alis'])} TL\nSatış: {str(ceyrek['satis'])} TL\nDeğişim: {str(ceyrek['degisim'])}\n\n'''
        )
        print(
            f'''Gram Altın\n--------------\nAlış: {str(gram['alis'])} TL\nSatış: {str(gram['satis'])} TL\nDeğişim: {str(gram['degisim'])}\n'''
        )
    except:
        pass

show()
''' arwell#4774 '''