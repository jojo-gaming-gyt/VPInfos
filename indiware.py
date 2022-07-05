def download(s_time):

    log.debug('download(' + s_time + ') start')
    import requests

    try:
        data = {
            "username":"oberstufe",
            "password":"QTAPm3U8",
            "authorization":"Basic b2JlcnN0dWZlOlFUQVBtM1U4",
            "cookie":"AuswalKL=12"
            }

        url = "https://www.johanneum-hoy.de/indiware/mobil/mobdaten/PlanKl" + s_time + '.xml'
        r = requests.get(url, headers=data)
        code = 'Status Code:' + str(r.status_code)

        print(code)
        log.debug(code)
        log.debug('download() end')


    except:
        print('Download fehlgeschlagen')
        log.error('download()')
        log.info('EXIT')
        sys.exit(0)

def klakur():

    log.debug('klakur() start')
    import xml.etree.ElementTree as ET

    try:
        tree = ET.parse('web.xml')
        root = tree.getroot()

        d_klakur = {}
        for klasse in root.iter('Kurz'):
            l_kurs = list('')
            for kurs in root[2][len(d_klakur)].iter('KKz'):
                l_kurs.append(str(kurs.text))
                d_klakur[str(klasse.text)] = l_kurs

        return d_klakur
        log.debug('klakur() end')

    except:
        log.error('klakur()')
        log.info('EXIT')
        sys.exit(0)

def jdata():
    import json
    try:
        d = open('data.json','w')
    except:
        print('fehler')
        sys.exit(0)
    finally:
        d.close()




if __name__ == '__main__':
    import logging as log
    import sys, time

    log.basicConfig(filename='logs\latest.log', encoding='utf-8', level=log.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s')
    log.info('START')


    #download('20')
    #d_klakur = klakur()




    log.info('EXIT')
    sys.exit(0)
