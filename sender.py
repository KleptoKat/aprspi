import kiss
import aprs

def main():
    frame = aprs.Frame()
    frame.source = aprs.Callsign('VA4CAN-1')
    frame.destination = aprs.Callsign('WIDE2-2')
    frame.path = [aprs.Callsign('VA4CAN-2')]
    frame.text = '>Hello World!'

    ki = kiss.TCPKISS(host='localhost', port=8001)
    ki.start()
    ki.write(frame.encode_kiss())
    


main();