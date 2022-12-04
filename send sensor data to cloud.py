
import serial
from time import *
import datetime, string
import Adafruit_DHT
Host = "api.thingspeak.com"
Port = "80"
API="IUKIV2ZREByERH7V47Q"
field1 = "field1"
field2 = "field2"
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
def readlineCR(port): 
	rv = "" 
	rv = port.read(1000) 
	return rv
def wifiCommand( sCmd, waitTm=1, sTerm='OK' ):
	lp = 0
	ret = ""
	print	
	print "Cmd: %s" % sCmd
	port.flushInput()
	port.write( sCmd + "\r\n" )
	ret = port.readline()	
	sleep( 0.2 )
	while( lp < waitTm ):
		while( port.inWaiting() ):
			ret = port.readline().strip( "\r\n" )
			print ret
			lp = 0
		if( ret == sTerm ): break
		if( ret == 'ERROR' ): break
		sleep( 1 )
		lp += 1
	return ret
isConnected=True;
while isConnected: 
	port.write("AT\r\n")
	returnedData=readlineCR(port)
	print(returnedData)
	if "OK" not in returnedData :
		time.sleep(20)
	else :
		isConnected=False
	
	port.write("AT+CWMODE=1\r\n")
	returnedData=readlineCR(port)
	print(returnedData)
	port.write("AT+CWJAP=\"AndroidAP_7822\",\"485088c2825f\"\r\n")
	returnedData=readlineCR(port)
	print(returnedData)		
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
    	    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        else :
            print("Failed to retrieve data from humidity sensor")
	port.write("AT+CIPMUX=1\r\n")
	returnedData=readlineCR(port)
	print(returnedData)		
	wifiCommand("AT+CIPSTART=0,\"TCP\",\""+ Host+"\","+Port,15,"OK")
	returnedData=readlineCR(port)
	print(returnedData)	
	cmd="Get /update?api_key="+API+"&"+field1+"="+str(20)+"&"+field2+"="+str(79)
	cmdLn=str(len(cmd)+4)
	wifiCommand("AT+CIPSEND=0,"+cmdLn,4,">")
	returnedData=readlineCR(port)
	print(returnedData)	
	port.write(cmd)
	port.write('\r')		
	returnedData=readlineCR(port)
	print(returnedData)
	Break
