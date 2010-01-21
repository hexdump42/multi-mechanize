#!/usr/bin/env python
#  Copyright (c) 2010 Corey Goldberg (corey@goldb.org)
#  License: GNU GPLv3


import mechanize
import time


class MechTransaction(object):
    def __init__(self):
        self.bytes_received = 0
        self.custom_timers = {}
    
    def run(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 Compatible')]
        
        start_timer = time.time()
        resp = br.open('http://www.example.com/')
        latency = time.time() - start_timer
        
        self.custom_timers['Example_Homepage'] = latency
        self.bytes_received += (len(resp.info()) + len(resp.get_data()))

        
if __name__ == '__main__':
    trans = MechTransaction()
    trans.run()
    print trans.bytes_received
    print trans.custom_timers