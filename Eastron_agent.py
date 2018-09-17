import serial
import struct
import binascii
import time
from cumulocity_REST import send_data_via_http
import serial.tools.list_ports
from com_ports import serial_ports


def convert_to_dec(data):
    value = struct.unpack('>f', binascii.unhexlify(data.replace(' ', '')))

    return value



def main():
    ports = serial_ports()
    password = "F3ilWau%ee.?89"

    commands = [[0x64, 0x04, 0x00, 0x00, 0x00, 0x02, 0x78, 0x3E], #voltage
                [0x64, 0x04, 0x00, 0x06, 0x00, 0x02, 0x98, 0x3F], #current
                [0x64, 0x04, 0x00, 0x48, 0x00, 0x02, 0xF8, 0x28], #energy
                [0x64, 0x04, 0x00, 0x0C, 0x00, 0x02, 0xB8, 0x3D], #power
                [0x64, 0x04, 0x00, 0x46, 0x00, 0x02, 0x99, 0xEB], #frequency
                [0x64, 0x04, 0x00, 0x3E, 0x00, 0x02, 0x19, 0xF2]  #power factor
                 ]


    print(ports)

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
        send_data_via_http(values)
        time.sleep(1)

    ser.close()
    print("Process Exited")


if __name__ == '__main__':

    main()
