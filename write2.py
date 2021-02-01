#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import time

# import the server implementation
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient
#from test.testdata import ModbusMockClient as ModbusClient
from pymodbus.mei_message import *
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

rr = client.read_input("Battery Type")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 9001 (Battery capacity)
# 9002 (Temp. Compensation coefficient)
# rq = client.client.write_registers(0x9001, [150, encode(-2)], unit=0x1)

# rr = client.read_input("Battery Capacity")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# rr = client.read_input("Temperature compensation coefficient")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# # 9003 to 900E must be written together
# # 9003 (Over voltage disconnect) - 60
# # 9004 (Charging limit voltage) - 58.4
# # 9005 (Over voltage reconnect) - 58.4
# # 9006 (Equalization voltage) - 56
# # 9007 (Boost charging voltage) - 56
# # 9008 (Float charging voltage) - 54
# # 9009 (Boost reconnect charging voltage) - 53.5
# # 900A (Low voltage reconnect voltage) - 50 --> 53
# # 900B (Under voltage warning recover voltage) - 50
# # 900C (Under voltage warning voltage) - 49
# # 900D (Low voltage disconnect voltage) - 48 --> 51
# # 900E (Discharge limit voltage) 47.9

# rq = client.client.write_registers(0x9003, [encode(60), encode(58.4), encode(58.4), encode(56), encode(56), encode(54), encode(53.5), encode(53), encode(50), encode(49), encode(51), encode(47.9)], unit=0x1)
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



# # # 9010 (Lower temperature charging limit)
# # # 9011 (Lower temperature discharging limit)
# # rq = client.client.write_registers(0x9010, [encode(2), encode(-20)], unit=0x1)
# # assert(not rq.isError())

# # rr = client.client.read_holding_registers(0x9010, 2, unit = 0x01)
# # if hasattr(rr, "getRegister"):
# #     print "read_holding_registers:", rr.getRegister(0)
# # else:
# #     print "read_holding_registers:", str(rr)

# rr = client.client.read_holding_registers(0x9011, 2, unit = 0x01)
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# # 9017 (Battery upper temperature limit)
# # 9018 (Battery lower temperature limit)
# # 9019 (Device over temperature)
# # 901A (Device recovery temperature)
# rq = client.client.write_registers(0x9017, [encode(60), encode(-20), encode(85), encode(75)], unit=0x1)
# assert(not rq.isError())

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

rr = client.read_input("Battery rated voltage code")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# # 906B (Equalize duration)
# # 906C (Boost Duration)
# rq = client.client.write_registers(0x9067, [encode(0)], unit=0x1)

rr = client.read_input("Battery rated voltage code")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

# 906B (Equalize duration)
# 906C (Boost Duration)
# rq = client.client.write_registers(0x906B, [120, 120], unit=0x1)

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

# # 906D (Battery discharge)
# # 906E (Battery charge)
# rq = client.client.write_registers(0x906D, [30, 100], unit=0x1)

# rr = client.read_input("Discharging percentage")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# rr = client.read_input("Charging percentage")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# rq = client.client.write_registers(0x9070, [0], unit=0x1)
# rr = client.read_input("Management modes of battery charging and discharging")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)


client.close()


# log.debug("Write to a holding register and read back")
# register = registerByName("Low voltage disconnect")
# values = register.encode(48)
# rq = client.client.write_register(register.address, values, unit=0x1)
# rr = client.client.read_holding_registers(0x900D, 0x30, unit=0x1)
# print(rq)
# assert(not rq.isError())            # test that we are not an error
# assert(rr.registers[0] == 0x30)       # test the expected value

