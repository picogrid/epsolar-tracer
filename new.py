import minimalmodbus
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyXRUSB0'
ser.timeout = 1

instrument = minimalmodbus.Instrument('')
