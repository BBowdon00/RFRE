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

import numpy as np
import socket
import math
from textwrap import wrap
# from .msg_gen import create
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
        
        gr.sync_block.__init__(self,name="adsb_gen",in_sig=None,out_sig=[np.float32]) 
            # OUT_signal type = numpy.float


            ##encoded = main(lat, lon, alt, num, start_id)
            ##enc = "0b" + encoded
            ##enc = float(literal_eval(enc))
            

            #enc = float out to complex converter to osmocom
            # create XMLRPC Server?
            


    def set_lat(self, lat):
        '''
        Sets the internallatitude to lat
        '''
        self.lat = lat
    def set_lon(self, lon):
        '''
        Sets the internal longitude to lon (Changes xml)
        '''
        self.lon = lon

    def set_alt(self, alt):
        '''
        Sets the internal altitude to alt
        '''
        self.alt = alt
    
    def set_num(self, num):
        '''
        sets the number of 
        '''
        self.num = num
    

    def work(self, input_items, output_items):
        out = output_items[0]
        # <+signal processing here+>
        # Should put output items into out
        out[:] = np.float32(0)
        encoded = create(self.lat, self.lon, self.alt, self.num, self.start_id)

        if(len(encoded) < len(out)):
            encodedLen = len(encoded) - 1
        else:
            encodedLen = len(out) -1

        # for loop until testLen

        for i in range(0, encodedLen):
            if encoded[i] == "0":
                # add a numpy.float32 0
                # numpy.float32(0)
                out[i] = np.float32(0)
            else:
                # add a numpy. float32 1
                # numpy.float32(1)
                out[i] = np.float32(1)
        return len(output_items[0])

def create(latitude, longitude, altitude, number, start):
    encoded = ''

    icao = start
    
    alt = altitude
    lat = latitude
    lon = longitude
    num = number

    evenLocMsg = position(lat, lon, alt, False)
    oddLocMsg = position(lat, lon, alt, True)
    for i in range(0,num):

        addressMsg = aircraftID(icao)
        evenMsg = addressMsg + evenLocMsg
        oddMsg = addressMsg + oddLocMsg

        #evenCRC = crc(format(int(evenMsg, 2), 'x'))
        #oddCRC = crc(format(int(oddMsg, 2), 'x'))
        #evenMsg = evenMsg + format(int(evenCRC, 16), 'b')
        #oddMsg = oddMsg + format(int(oddCRC, 16), 'b')


        evenCRC = crc(evenMsg)
        oddCRC = crc(oddMsg)
        evenMsg = evenMsg + evenCRC
        oddMsg = oddMsg + oddCRC

        evenEncoded = encodeMsg(evenMsg)
        oddEncoded = encodeMsg(oddMsg)
        encoded += evenEncoded + oddEncoded
        
        # increment icao for next iteration
        icao = hex2int(icao)
        icao += 1
        icao = int2hex(icao)
    return encoded

    #method to generate aircraft ID fields (DF, CA, ICAO)
def aircraftID(icao):
    """
    generates DF, CA, and ICAO fields of ADS-B message
    DF (downlink format) Field: 5 Bits
    CA (Capability identifiers): 3 bits
    ICAO address: 24 bits

    """
    # enter icao of 6 hex

    #the message that we will be returning
    msg = ''

    #DF 17 is ADS-B
    df = format(17, 'b')

    #CA is 5 for to match type code later
    ca = format(5, 'b')

    #The full message
    msg = msg + df + ca + format(int(icao,16),'b')

    while (len(msg) < 32):
        msg = "0" + msg

    return msg

def hex2bin(hexstr):
    """Convert a hexdecimal string to binary string, with zero fillings."""
    num_of_bits = len(hexstr) * 4
    binstr = bin(int(hexstr, 16))[2:].zfill(int(num_of_bits))
    return binstr


def hex2int(hexstr):
    """Convert a hexdecimal string to integer."""
    return int(hexstr, 16)


def int2hex(n):
    """Convert a integer to hexadecimal string."""
    # strip 'L' for python 2
    return hex(n)[2:].rjust(6, "0").upper().rstrip("L")


def bin2int(binstr):
    """Convert a binary string to integer."""
    return int(binstr, 2)


def bin2hex(hexstr):
    """Convert a hexdecimal string to integer."""
    return int2hex(bin2int(hexstr))


def bin2np(binstr):
    """Convert a binary string to numpy array."""
    return np.array([int(i) for i in binstr])


def np2bin(npbin):
    """Convert a binary numpy array to string."""
    return np.array2string(npbin, separator="")[1:-1]

def adsbMod(x, y):
    """ADS-B Mod method"""
    return float(x - (y * math.floor(x/y)))


    #CRC method
def crc(msg):
    """
    Mode-S Cyclic Redundancy Check.
    Detect if bit error occurs in the Mode-S message. When encode option is on,
    the checksum is generated.
    Args:
        msg (string): 22 bytes hexadecimal message string
    Returns:
        int: message checksum, or partity bits (encoder)
    """
    # the CRC generator
    G = [int("11111111", 2), int("11111010", 2), int("00000100", 2), int("10000000", 2)]

    #adding crc bytes to messgae
    #msg = msg + "000000"
    msg = msg + "000000000000000000000000"

    #msgbin = hex2bin(msg)
    #msgbin_split = wrap(msgbin, 8)
    msgbin_split = wrap(msg, 8)
    mbytes = list(map(bin2int, msgbin_split))

    for ibyte in range(len(mbytes) - 3):
        for ibit in range(8):
            mask = 0x80 >> ibit
            bits = mbytes[ibyte] & mask

            if bits > 0:
                mbytes[ibyte] = mbytes[ibyte] ^ (G[0] >> ibit)
                mbytes[ibyte + 1] = mbytes[ibyte + 1] ^ (
                    0xFF & ((G[0] << 8 - ibit) | (G[1] >> ibit))
                )
                mbytes[ibyte + 2] = mbytes[ibyte + 2] ^ (
                    0xFF & ((G[1] << 8 - ibit) | (G[2] >> ibit))
                )
                mbytes[ibyte + 3] = mbytes[ibyte + 3] ^ (
                    0xFF & ((G[2] << 8 - ibit) | (G[3] >> ibit))
                )

    result = (mbytes[-3] << 16) | (mbytes[-2] << 8) | mbytes[-1]

    result = str(format(result, 'b'))

    while (len(result) < 24):
        result =  "0" + result

    #print(result)

    return result
    #eturn format(int(result, 2), 'x')


    #Position method (Lat, Lon, Alt)
def position(lat, lon, alt, odd):
    """
    Mode S extended positon generator.  
    Takes in lat, lon, and alt as ints
    Takes in odd as a boolean for even/odd frame

    Type code hard coded to 0x58

    returns a hex string
    """

    #perform altitude and TC math
    altitude = (alt + 1000)/25

    #explicitly casting as int because python can be dumb
    altitude = int(altitude)

    hold = (altitude & 0x00F)
    altitude = (altitude & 0xFF0) << 1
    altitude = (altitude | hold); #concatenate to the entire message
    altitude = (altitude | 0x010)
    altitude = (altitude | 0x58000) #Takes on the TC (0x58) field

    #formating altitude into bin string
    altitude = str(format(altitude, 'b'))

    #print("alt: " +  altitude)

    while (len(altitude) < 20):
        altitude = "0" + altitude

    #Calculate LatLon ------------------------

    #utc bit hardcoded to zero
    utcBit = "0"

    #cpr bit for even odd pairing
    if (odd):
        cpr = 1
        cprBit = "1"
    else:
        cpr = 0
        cprBit = "0"

    #NZ is hardcoded to 15 for our messages
    nz = 15

    #NB is hardcoded to 17 for 17 bits
    nb = 17

    #the latitude zone in the north south direction
    dlat = float(360.0 / (4.0 * nz - cpr))

    #print("dalt: " + str(dlat))

    #latitude for mod operations
    if lat < 0:
        modLat = lat + 360.0
    else:
        modLat = float(lat)

    #the y coordinate within the zone
    #int YZi = (int) Math.round(Math.pow(2, Nb) * ((modLat % Dlat)/ Dlat));
    #yZi = round(math.pow(2,nb)) * (adsbMod(modLat, dlat) / dlat)
    yZi = float(adsbMod(lat, dlat))
    yZi = yZi / dlat
    yZi = yZi * math.pow(2, nb)
    yZi = round(yZi)

    #print("yZi: " + str(yZi))


    #the latitude that the receiver will decode
    #rLat = dlat * ((yZi / math.pow(2, nb))) + math.floor(lat / dlat)
    rLat = float(yZi) / math.pow(2, nb)
    rLat = rLat + math.floor(lat / dlat)
    rLat = rLat * dlat

    #print("RLat: " + str(rLat))

    #NLat is based on latitude given
    if (abs(lat) > 87):
        nlLat = 1
    elif (abs(lat) == 87):
        nlLat = 2
    else:
        nlLat = math.floor((2*math.pi)/(math.acos(1 - ((1 - math.cos(math.pi / (2 * nz)))/(math.cos((math.pi / 180) * lat)**2)))))
        #nlLat = math.floor( math.pow * 2 * (math.pow(math.acos(1 - ((1 - math.cos(math.pi / (2 * nz))) / (math.pow(math.cos((math.pi / 180) * abs(float(rLat))), 2)))), -1)) )


    #Longitude calcs

    if ((nlLat - cpr) - cpr) > 0:
        dLon = 360.0 / (nlLat - cpr)
    else:
        dLon = 360.0

    #the X coordinates within the zone
    xZi = adsbMod(lon , dLon)
    xZi = xZi / dLon
    xZi = round(xZi * math.pow(2, nb))

    #make sure the values are nb bits
    yZi = adsbMod(yZi, pow(2,nb))
    xZi = adsbMod(xZi, pow(2, nb))

    #print("yZi: " + str(yZi))
    #print(str(format(int(yZi), 'x')))
    yBin = str(format(int(yZi), 'b'))

    while (len(yBin) < 17):
        yBin = "0" + yBin

    #print("xZi: " + str(xZi))
    #print(str(format(int(xZi), 'x')))
    xBin = str(format(int(xZi), 'b'))

    while (len(xBin) < 17):
        xBin = "0" + xBin

    locMsg = altitude + utcBit + cprBit + yBin + xBin

    #print("bin: " + locMsg)
    #print("hex: " + str(format(int(locMsg,2), 'x')))


    return locMsg

    #converts our string into the encoding style needed to transmit
def encodeMsg(msg):
    """
    Mode S encoder that converts the given binary message into the Mode S encoding
    Also adds preamble.

    Returns a binary string of the preamble and encoded message - note needs to transmit at 2Mbps
    """

    #the message preamble to turn on IFF reciever
    preamble = "1010000101000000"

    #end spce to give us room for when we transmit back to back
    endSpace = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    encodedMsg = ""

    for i in range(0, len(msg)):
        if (msg[i] == '1'):
            encodedMsg = encodedMsg + "10"
        else:
            encodedMsg = encodedMsg + "01"

    return preamble + encodedMsg + endSpace