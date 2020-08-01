try:
    from serial import Serial, SerialException
except ImportError:
    print('\n\npyserial package not found\n\n')
else:
    from time import sleep
    try:
        from psutil import cpu_percent, virtual_memory
    except ImportError:
        print('\n\npsutil package not found\n\n')

    print("Enter the Serial port number below.\n")
    port = str(input('Port number: COM'))
    try:
        s = Serial('COM'+port, 9600)
        print('Process has started sucessfully!')
        while True:

            string = 'RAM:      ' + str(virtual_memory()[2]) + '%'
            string += '                         '
            string += 'CPU:      ' + str(cpu_percent()) + '%'

            string = string.strip()
            s.write(string.encode())
            sleep(1)

    except SerialException:
        print('Serial Exception: Port "' + port + '" couldn\'t be found!\nOr permission denied.')
        sleep(1)
