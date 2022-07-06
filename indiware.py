import logging as log
import xml.etree.ElementTree as ET
import os, requests, sys, time

from os import remove
from sys import exit


def errorexit():
    log.info('EXIT')
    try:
        #Datei schließen
        pass
    except:
        pass
    sys.exit(0)



def download(s_time):

    log.debug('download(' + str(s_time) + ') start')

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
        errorexit()

def klassen():
    log.debug('klassen() start')

    try:
        tree = ET.parse('plan.xml')
        root = tree.getroot()

        l_klassen = []
        for klasse in root.iter('Kurz'):
            l_klassen.append(klasse.text)

        return l_klassen
        log.debug('klassen() end')
            
    except:
        log.error('klassen()')
        errorexit()


def kurse(s_klasse):

    log.debug('kurse(' + s_klasse + ') start')

    try:
        tree = ET.parse('plan.xml')
        root = tree.getroot()

        d_kurse = {None: None}
        s_klasse = str(s_klasse)
        
        for klasse in root.iter('Kl'):
            if str(klasse[0].text) == s_klasse:
                for kurs in klasse[3]:
                    print('1')
                    print(kurs[0].tag, '-', kurs[0].attrib)
                    d_kurse[kurs[0].text] = kurs[0].attrib['KLe']

                break

        return d_kurse
        log.debug('kurse() end')

    except:
        log.error('kurse()')
        errorexit()



def wrif(l_stunde):

    log.debug('wirf(')
    for i in range(len(l_stunde)):
        log.debug(str(l_stunde[i]))
    log.debug(') start')
    print('start')

    try:
        tree = ET.parse('plan.xml')
        root = tree.getroot()

        l_raumbl = []

        for zeit in range(len(l_stunde)):
            i_stunde = int(l_stunde[zeit])
            for stunde in root.iter('Std'):
                if int(stunde[0].text) == i_stunde:
                    raum = stunde.find('Ra')
                    l_raumbl.append(raum.text)

        l_raumbls = []
        for anz in range(len(l_raumbl)):
            e_raumbl = l_raumbl[anz]
            if e_raumbl == None:
                pass
            elif e_raumbl == 'TH1':
                pass
            elif e_raumbl == 'TH2':
                pass
            else:
                l_raumbls.append(int(e_raumbl))
        l_raumbls.sort()
                
        return l_raumbls

        

    except:
        errorexit()



if __name__ == '__main__':

    try:
        os.remove('logs\latest.log')
    except:
        pass

    
    log.basicConfig(filename='logs\latest.log', encoding='utf-8', level=log.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s')
    log.info('START')

    l_klassen = klassen()
    print(l_klassen)
    print()
    
    #download('20')
    
    d_kurse = kurse('5a')
    print(d_kurse)
    print()
    l_raumbl = wrif([1,2])
    print(l_raumbl)



    print('Programm beendet')
    log.info('EXIT')
    sys.exit(0)





"""def jdata():
    import json
    try:
        d = open('data.json','w')
    except:
        print('fehler')
        errorexit()
    finally:
        d.close()"""
