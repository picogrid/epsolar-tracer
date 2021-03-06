#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import time
import struct

# import the server implementation
from pyepsolartracer.registers import registers,coils
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registerByName

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# choose the serial client
client = EPsolarTracerClient()
client.connect()
print(client.read_device_info())

def encode(value):
    # FIXME handle 2 word registers
    rawvalue = int(value * 100)
    if rawvalue < 0:
        rawvalue = (-rawvalue - 1) ^ 0xffff
        #print rawvalue
    return rawvalue

def decode(response):
    if hasattr(response, "getRegister"):
        mask = rawvalue = lastvalue = 0
        for i in range(2):
            lastvalue = response.getRegister(i)
            rawvalue = rawvalue | (lastvalue << (i * 16))
            mask = (mask << 16) | 0xffff
        if (lastvalue & 0x8000) == 0x8000:
            #print rawvalue
            rawvalue = -(rawvalue ^ mask) - 1
        return (1.0 * rawvalue / 100)
    log.info ("No value for register")
    return None

rq = client.client.write_registers(0x9000, [0], unit=0x1)
rr = client.read_input("Battery Type")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 9001 (Battery capacity) 150 Ah 
# 9002 (Temp. Compensation coefficient) -2C (encoding bugs mean this is encoded as +2C) - Changed to 0 following Simpliphi feedback
rq = client.client.write_registers(0x9001, [150, encode(0)], unit=0x1)

rr = client.read_input("Battery Capacity")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Temperature compensation coefficient")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

## 9003 to 900E must be written together
# 9003 (Over voltage disconnect) - 60
# 9004 (Charging limit voltage) - 58.4
# 9005 (Over voltage reconnect) - 58.4
# 9006 (Equalize charging voltage) - 56
# 9007 (Boost charging voltage) - 56 - Changed to 55V following Simpliphi feedback
# 9008 (Float charging voltage) - 54
# 9009 (Boost reconnect charging voltage) - 53.5 
# 900A (Low voltage reconnect voltage) - 53
# 900B (Under voltage warning recover voltage) - 50
# 900C (Under voltage warning voltage) - 49
# 900D (Low voltage disconnect voltage) - 51.0
# 900E (Discharge limit voltage) 48

rq = client.client.write_registers(0x9003, [encode(60), encode(58.4), encode(58.4), encode(56), encode(55), encode(54), encode(53.5), encode(53), encode(50), encode(49), encode(51), encode(48)], unit=0x1)
# assert(not rq.isError())

rr = client.read_input("Over voltage disconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Charging limit voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Over voltage reconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Equalization voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)
    rr = client.read_input("Boost voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Float voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Boost reconnect voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Low voltage reconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)
    rr = client.read_input("Under voltage recover")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Under voltage warning")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Low voltage disconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Discharging limit voltage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 9017 (Battery upper temperature limit) - 60
# 9018 (Battery lower temperature limit) - -20
# 9019 (Device over temperature) - 85
# 901A (Device recovery temperature) - 75
rq = client.client.write_registers(0x9017, [encode(60), encode(-20), encode(85), encode(75)], unit=0x1)
assert(not rq.isError())

rr = client.read_input("Battery temperature warning upper limit")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Battery temperature warning lower limit")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Controller inner temperature upper limit")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Controller inner temperature upper limit recover")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 9067 Battery rated voltage level - 0 = auto recognize, 4 = 48V
rq = client.client.write_registers(0x9067, [4], unit=0x1)
assert(not rq.isError())

rr = client.read_input("Battery rated voltage code")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 906B (Equalize duration)
# 906C (Boost Duration) - Changed to 6 mins following Simpliphi feedback
rq = client.client.write_registers(0x906B, [180, 6], unit=0x1)
assert(not rq.isError())

rr = client.read_input("Equalize duration")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Boost duration")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 906D (Battery discharge)
# 906E (Battery charge)
rq = client.client.write_registers(0x906D, [0, 100], unit=0x1)

rr = client.read_input("Discharging percentage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Charging percentage")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rq = client.client.write_registers(0x9070, [0], unit=0x1)
rr = client.read_input("Management modes of battery charging and discharging")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

client.close()


