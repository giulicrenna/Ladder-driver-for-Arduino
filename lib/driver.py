import serial

serial_port = serial.Serial('COM3', 9600)

def controller(input_):
    if input_ == 'ON1':
        val = 'a'
        serial_port.write(val)
    elif input_ == 'ON2':
        val = 'b'
        serial_port.write(val)
    elif input_ == 'ON3':
        val = 'c'
        serial_port.write(val)
    elif input_ == 'ON4':
        val = 'd'
        serial_port.write(val)
    elif input_ == 'ON5':
        val = 'e'
        serial_port.write(val)
    elif input_ == 'ON6':
        val = 'f'
        serial_port.write(val)
    elif input_ == 'ON7':
        val = 'g'
        serial_port.write(val)
    elif input_ == 'ON8':
        val = 'h'
        serial_port.write(val)


if __name__ == "__main__":  
    controller()


