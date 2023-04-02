# For documentation on socket library, see....
# https://docs.python.org/3/library/socket.html

import socket

TCP_PORT = 5005     # The port to use.
BUFFER_SIZE = 1024  # Packet size - 1024 is standard. With a buffer of 10 receives the
#message bit by bit

def server_socket(tcp_ip, tcp_port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # bind the socket to the tcp address and port and start to listen
        sock.bind((tcp_ip, tcp_port))
        sock.listen()
        print(f'#<INFO> Server Initialising on {tcp_ip}:{tcp_port}')
        print('#<INFO> Awaiting connection...\n')

        # wait for a client to connect
        conn, addr = sock.accept()
        print(f"#<INFO> A client on: {addr} has connected.\n")
        # process all incoming data from the client....
        try: #with this error handling the connection is not thrown as an error but caught
            while True:
                data = conn.recv(BUFFER_SIZE)
                if data:
                    data.decode()
                    # send a confirmation to the client

                #conn.sendall('Got that thanks!'.encode())
                if not data:
                    print('#<INFO> End of Data - Socket Exiting...')
                    conn.sendall('Got that thanks!'.encode())
                    break
            print(' + - + - + - + - \n')
        except Exception:
            print('Exitting connection..')
        conn.close()



def main():
    tcp_ip = '172.16.1.10'
    server_socket(tcp_ip, TCP_PORT)


if __name__ == '__main__':
    main()

# If anything unexpected happens (e.g. cannot receive message from client or
# the server will not start due to exceptions) make sure the server is not
# already running in the background.
#
# In Windows Command Prompt, type:
# cmd > netstat -ano | findstr 5005
#
# If that port (5005) is in use, kill it with the command
# cmd > tskill <process id>
# and run server.py again. Alternatively, use another port if 5005 is taken.
# If program hangs, use same method but select the process ID of the client,
# which is the PID that is only listed as established and not also as listening
