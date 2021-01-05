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
log.setLevel(logging.DEBUG)

# choose the serial client
client = EPsolarTracerClient()
client.connect()
print(client.read_device_info())

rr = client.read_input("Low voltage disconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Low voltage reconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

client.close()

# rr = client.client.write_registers(0x900D, 48, unit=client.unit)

# rr = client.write_output("Low voltage disconnect", 48.0)
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

rr = client.read_input("Low voltage disconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)

rr = client.read_input("Low voltage reconnect")
if hasattr(rr, "getRegister"):
    print "read_holding_registers:", rr.getRegister(0)
else:
    print "read_holding_registers:", str(rr)


# log.debug("Write to a holding register and read back")
# register = registerByName("Low voltage disconnect")
# values = register.encode(48)
# rq = client.client.write_register(register.address, values, unit=0x1)
# rr = client.client.read_holding_registers(0x900D, 0x30, unit=0x1)
# print(rq)
# assert(not rq.isError())            # test that we are not an error
# assert(rr.registers[0] == 0x30)       # test the expected value

