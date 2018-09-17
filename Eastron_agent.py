import serial
import struct
import binascii
import time
from cumulocity_REST import send_data_via_http
import serial.tools.list_ports
from com_ports import serial_ports
import argparse


def convert_to_dec(data):
    value = struct.unpack('>f', binascii.unhexlify(data.replace(' ', '')))

    return value


def main():
    username = "softwareag10/muriithicliffernest@gmail.com"
    password = "F3ilWau%ee.?89"
    modbus_address = 100
    parser = argparse.ArgumentParser(
        description='Tenancy Details',
    )
    parser.add_argument("-u", "--username", help=" Cumulocity tenant username",
                        )

    parser.add_argument("-p", "--password", help=" Cumulocity tenant password",
                        )

    args = vars(parser.parse_args())
    if args['username']:
        username = args['username']
    if args['username']:
        password = args['password']
    print(username, password)
    ports = serial_ports()
    ports.append(0)
    while len(ports) > 1:
        commands = [[modbus_address, 0x04, 0x00, 0x00, 0x00, 0x02, 0x78, 0x3E], #voltage
                    [modbus_address, 0x04, 0x00, 0x06, 0x00, 0x02, 0x98, 0x3F], #current
                    [modbus_address, 0x04, 0x00, 0x48, 0x00, 0x02, 0xF8, 0x28], #energy
                    [modbus_address, 0x04, 0x00, 0x0C, 0x00, 0x02, 0xB8, 0x3D], #power
                    [modbus_address, 0x04, 0x00, 0x46, 0x00, 0x02, 0x99, 0xEB], #frequency
                    [modbus_address, 0x04, 0x00, 0x3E, 0x00, 0x02, 0x19, 0xF2]  #power factor
                     ]


        print(commands)

        ser = serial.Serial(
            port=ports[0],
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
        )

        print(ser.isOpen())
        values = [0, 0, 0, 0, 0, 0]
        #client = start_client()
        while ser.isOpen():
            j = 0
            while j < 6:
                data = serial.to_bytes(commands[j])
                #print(data)
                ser.write(data)
                i = 0
                s = []
                while i < 9:
                    s.append(str(ser.read(1).hex()))
                    i = i+1
                #print(s)
                #print(" ".join(s[3:7]))
                values[j] = convert_to_dec("".join(s[3:7]))[0]
                #print(convert_to_dec("".join(s[3:7]))[0])

                j = j + 1
            print(values)
            send_data_via_http(values,username,password)
            time.sleep(1)

        ser.close()
        print("Process Exited")
    while True:
        send_data_via_http([30, 30, 30, 30, 30, 30], username, password) #testing
        print("sent")
        time.sleep(10)
if __name__ == '__main__':
    main()
