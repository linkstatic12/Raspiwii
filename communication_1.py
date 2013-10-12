import serial,time
ser=serial.Serial()
ser.port="/dev/ttyUSB0"
MSP_IDT="\x24\x4d\x3c\x00\x64\x64"
MSP_RAW_IMU="\x24\x4d\x3c\x00\x66\x66"
ser.baudrate=115200
ser.bytesize=serial.EIGHTBITS
ser.parity=serial.PARITY_NONE
serial.stopbits=serial.STOPBITS_ONE
ser.timeout=0
ser.xonxoff=False
ser.rtscts=False
ser.dsrdtr=False
ser.writeTimeout=2
try:
    ser.open()
except Exception,e:
    print("Error open serial port: "+str(e))
    exit()

if ser.isOpen():
    time.sleep(15)
    print("Serial port is open at"+ser.portstr)
    try:
        ser.flushInput()
        ser.flushOutput()
        ser.write(MSP_RAW_IMU)
        print("Writing to "+ser.portstr+" "+MSP_RAW_IMU)
        time.sleep(0.5)
        numOfLines=0
        while True:
            response=ser.readline()
            print(type(response))
            
            print(response.encode("hex"))
            numOfLines=numOfLines+1
    
            if(numOfLines>=1):
                break
        ser.close()
    except Exception,e1:
        print("Error communicating..."+str(e1))
else:
    print("Cannot open serial port")

    

