# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:57:43 2020

@author: Lucija
"""

import datetime, pytz

pocetno_vrijeme = datetime.datetime(2020,10,10,16,5,25)
krajnje_vrijeme=datetime.datetime(2020,10,11,6,10,25)
vrem_zona_pocetka = pytz.timezone('America/New_York')
vrem_zona_kraj = pytz.timezone('Europe/Berlin')

def let(pocetno_vrijeme,vrem_zona_pocetka,krajnje_vrijeme,vrem_zona_kraj):
    pocetno_vrijeme = vrem_zona_pocetka.localize(pocetno_vrijeme)
    krajnje_vrijeme = vrem_zona_kraj.localize(krajnje_vrijeme)
    trajanje_leta=krajnje_vrijeme-pocetno_vrijeme
    print(trajanje_leta)
    
let(pocetno_vrijeme,vrem_zona_pocetka,krajnje_vrijeme,vrem_zona_kraj)
    