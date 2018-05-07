#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Simple Raspberry Micro Dot Phat hack to display current played song on radio perfecto (rock French radio)

This code is under MIT licence
Code by DarKou (inspired by Brunus - https://github.com/Brunus-V/ircbot )
'''

import schedule
import sys
import time
import urllib
import json
from Queue import Queue
from microdotphat import write_string, set_decimal, set_rotate180, clear, show, scroll

print("""Radio Perfecto

Displays current played song from this fucking radio!

Press Ctrl+C to exit.
""")

titleBus = Queue()
titleBus.put('')

def readStream():
        currentTitle = titleBus.get()
        
        url = "https://rc1.nobexinc.com//nowplaying.ashx?stationid=70642"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
                
        title = data['artist'] + ' - ' + data['songName']
        
        if (title != currentTitle):
                write_string(" # " + title, kerning=False)
                titleBus.put(title)
        else:
                titleBus.put(currentTitle)
  
schedule.every(5).seconds.do(readStream)

while True:
        schedule.run_pending()
        scroll()
        show()
        time.sleep(0.1)
