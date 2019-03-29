#Esta aplicacion nos permite consumir paginas web
#con web scarping
#Implementacion por SwankySniperGG
#MIT
#github.com/

from bs4 import BeautifulSoup
import json
from scrapscript import simple_get

class loadPUC:
    result = {
        'cuentas': [],
        'total': 0
    }

    def merge(self, lis):
        result = ''
        for l in lis:
            result = result + l
        return result

    def mergeNames(self, lis):
        result = ''
        for l in lis:
            result = result + ' ' + l
        return result


    def __init__(self):
        dictionary = self.result
        i = 1
        while i < 10:
            url = 'https://puc.com.co/'+str(i)
            print(url, end = '')
            if (i == 1):
                tipo = 'Debito'
            if (i == 2):
                tipo = 'Credito'
            if (i == 3):
                tipo = 'Credito'
            if (i == 4):
                tipo = 'Credito'
            if (i == 5):
                tipo = 'Debito'
            if (i == 6):
                tipo = 'Debito'
            if (i == 7):
                tipo = 'Debito'
            if (i == 8):
                tipo = 'Debito'
            if (i == 9):
                tipo = 'Credito'
            raw_html = simple_get(url)
            html = BeautifulSoup(raw_html, 'html.parser')
            if raw_html is not None:
                print(' Status - OK')
                x = html.h1.string
                x = x.split(' ')
                try:
                    y = html.find('div', class_='col-md-7').p.string
                except:
                    y = None
                dictionary['total'] = dictionary['total'] + 1 
                dictionary['cuentas'].append({
                    'nombre': self.mergeNames(x[1:]),
                    'codigo': x[0],
                    'descripcion':y,
                    'tipo':tipo,
                    'hijos': []
                })
                lis = html.find_all('span', class_='code')
                for l in lis[1:]:
                    url = 'https://puc.com.co/'+l.string
                    print(url, end = '')
                    raw_html = simple_get(url)
                    html = BeautifulSoup(raw_html, 'html.parser')
                    if raw_html is not None:
                        print(' Status - OK')
                        x = html.h1.string
                        x = x.split(' ')
                        try:
                            y = html.find('div', class_='col-md-7').p.string
                        except:
                            y = None
                        dictionary['total'] = dictionary['total'] + 1 
                        dictionary['cuentas'][-1]['hijos'].append({
                            'nombre': self.mergeNames(x[1:]),
                            'codigo': self.merge(x[0][-2:]),
                            'descripcion':y,
                            'tipo':tipo,
                            'hijos': []
                        })
                        lis = html.find_all('span', class_='code')
                        for l in lis[2:]:
                            url = 'https://puc.com.co/'+l.string
                            print(url, end = '')
                            raw_html = simple_get(url)
                            html = BeautifulSoup(raw_html, 'html.parser')
                            if raw_html is not None:
                                print(' Status - OK')
                                x = html.h1.string
                                x = x.split(' ')
                                try:
                                    y = html.find('div', class_='col-md-7').p.string
                                except:
                                    y = None
                                dictionary['total'] = dictionary['total'] + 1 
                                dictionary['cuentas'][-1]['hijos'][-1]['hijos'].append({
                                    'nombre': self.mergeNames(x[1:]),
                                    'codigo': self.merge(x[0][-2:]),
                                    'descripcion':y,
                                    'tipo':tipo,
                                    'hijos': []
                                })
                                lis = html.find_all('span', class_='code')
                                for l in lis[3:]:
                                    url = 'https://puc.com.co/'+l.string
                                    print(url, end = '')
                                    raw_html = simple_get(url)
                                    html = BeautifulSoup(raw_html, 'html.parser')
                                    if raw_html is not None:
                                        print(' Status - OK')
                                        x = html.h1.string
                                        x = x.split(' ')
                                        dictionary['total'] = dictionary['total'] + 1 
                                        dictionary['cuentas'][-1]['hijos'][-1]['hijos'][-1]['hijos'].append({
                                            'nombre': self.mergeNames(x[1:]),
                                            'codigo': self.merge(x[0][-2:]),
                                            'descripcion': None,
                                            'tipo':tipo,
                                            'hijos': []
                                        })
                                    else:
                                        print(' Status - Not found')
                            else:
                                print(' Status - Not found')
                    else:
                        print(' Status - Not found')
            else:
                print(' Status - Not found')
            i = i + 1
        with open('result.json', 'w') as fp:
            json.dump(dictionary, fp)

if __name__ == '__main__':
    loadPUC()