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
from pymodbus.pdu import ModbusRequest, ModbusResponse

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class CustomModbusRequest(ModbusRequest):

    function_code = 10

    def __init__(self, address):
        ModbusResponse.__init__(self)
        self.address = address
        self.count = 1

    def encode(self):
        return struct.pack('>HH', self.address, self.count)

    def decode(self, data):
        self.address, self.count = struct.unpack('>HH', data)

    def execute(self, context):
        if not (1 <= self.count <= 0x7d0):
            return self.doException(merror.IllegalValue)
        if not context.validate(self.function_code, self.address, self.count):
            return self.doException(merror.IllegalAddress)
        values = context.getValues(self.function_code, self.address, self.count)
        return CustomModbusResponse(values)


# choose the serial client
client = EPsolarTracerClient()
client.connect()

request = CustomModbusRequest(0x900D)

client.close()



# rr = client.client.write_registers(0x900D, 48, unit=client.unit)

# rr = client.write_output("Low voltage disconnect", 48.0)
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)

# rr = client.read_input("Low voltage disconnect")
# if hasattr(rr, "getRegister"):
#     print "read_holding_registers:", rr.getRegister(0)
# else:
#     print "read_holding_registers:", str(rr)
