#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 Bowdon Inc..
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import socket
import msg_gen
from gnuradio import gr

## Create socket somehow
## sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
## sock.setSoTimeout(0)
## sock.setblocking(false)

class adsb_gen(gr.sync_block):
    """
    docstring for block adsb_gen
    """
    def __init__(self, lat, lon, alt, num, start_id):
        
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.num = num
        self.start_id = start_id
        
        r.sync_block.__init__(self,
            name="adsb_gen",
            in_sig=None,
            out_sig=[numpy.float32]) 
            # OUT_signal type = numpy.float


            ##encoded = main(lat, lon, alt, num, start_id)
            ##enc = "0b" + encoded
            ##enc = float(literal_eval(enc))
            

            #enc = float out to complex converter to osmocom
            # create XMLRPC Server?
            


    def setLat(self, lat):
        '''
        Sets the internallatitude to lat
        '''
        self.lat = lat
    def setLon(self, lon):
        '''
        Sets the internal longitude to lon (Changes xml)
        '''
        self.lon = lon

    def setAlt(self, alt):
        '''
        Sets the internal altitude to alt
        '''
        self.alt = alt
    
    def setNum(self, num):
        '''
        sets the number of 
        '''
        self.num = num
    

    def work(self, input_items, output_items):
        out = output_items[0]
        # <+signal processing here+>
        # Should put output items into out
        out[:] = numpy.float32(0)
        encoded = msg_gen.create(self.lat, self.lon, self.alt, self.num, self.start_id)
        

        if(len(encoded) < len(out)):
            encodedLen = len(encoded) - 1
        else:
            encodedLen = len(out) -1

        # for loop until testLen

        for i in range(0, encodedLen):
            if x == "0":
                # add a numpy.float32 0
                # numpy.float32(0)
                out[i] = numpy.float32(0)
            else:
                # add a numpy. float32 1
                # numpy.float32(1)
                out[i] = numpy.float32(1)
        return len(output_items[0])
        