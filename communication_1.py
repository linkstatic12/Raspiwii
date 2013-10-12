import serial,time
ser=serial.Serial()
ser.port="/dev/ttyUSB0"
BASIC="\x24\x4d\x3c\x00"
MSP_IDT=BASIC+"\x64\x64"
MSP_STATUS=BASIC+"\x63\x63"
MSP_RAW_IMU=BASIC+"\x66\x66"
MSP_SERVO=BASIC+"\x67\x67"
MSP_MOTOR=BASIC+"\x68\x68"
MSP_RC=BASIC+"\x69\x69"
MSP_RAW_GPS=BASIC+"\x70\x70"
MSP_COMP_GPS=BASIC+"\x71\x71"
MSP_ATTITUDE=BASIC+"\x72\x72"
MSP_ALTITUDE=BASIC+"\x73\x73"
MSP_BAT=BASIC+"\x74\x74"

CURRENT=MSP_STATUS
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
        ser.write(CURRENT)
        print("Writing to "+ser.portstr+" "+CURRENT)
        time.sleep(0.5)
        numOfLines=0
        while True:
            response=ser.readline()
            #print(type(response))
            
            print(response.encode("hex"))
            numOfLines=numOfLines+1
    
            if(numOfLines>=1):
                break
        ser.close()
    except Exception,e1:
        print("Error communicating..."+str(e1))
else:
    print("Cannot open serial port")

    

