# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:26:56 2020

@author: Lucija
"""

import datetime, pytz

pocetno_vrijeme = datetime.datetime(2020,10,10,16,5,25)
vrem_zona_pocetka = pytz.timezone('America/New_York')
pocetno_vrijeme = vrem_zona_pocetka.localize(pocetno_vrijeme)
trajanje_leta = datetime.timedelta(hours=8, minutes=5)
vrem_zona_kraj = pytz.timezone('Europe/Berlin')

def dolazak(pocetno_vrijeme,vrem_zona_pocetka,trajanje_leta,vrem_zona_kraj):
    vrijeme_dolaska1 = pocetno_vrijeme + trajanje_leta
    vrijeme_dolaska_cilj = vrijeme_dolaska1.astimezone(vrem_zona_kraj)
    print(vrijeme_dolaska_cilj)
    
dolazak(pocetno_vrijeme,vrem_zona_pocetka,trajanje_leta,vrem_zona_kraj)