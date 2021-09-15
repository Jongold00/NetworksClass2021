
import socket

def main():
    HOST = 'proj1.3700.network'  # The server's hostname or IP address
    PORT = 27993
    NUID = '001450798'


    HELLO_msg = "ex_string HELLO " + NUID + "\n"


    # framework code courtesy of https://realpython.com/python-sockets/


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(HELLO_msg.encode())
        data = s.recv(8192)
        print(data.decode())
        #conn, addr = s.accept()
        """ with conn:
            while True:
                #data = conn.recv(8192)
                if not data:
                    break


                msg_type = data.split()[0]

                SendMessage(msg_type)
                if (msg_type == 'FIND'):
                    token_count = GetTokenOccurance(data.split()[1], data.split()[2])
                    msg = 'COUNT ' + token_count + '\n'
                    s.send(msg)
                if (msg_type == 'BYE'):
                    print(data.split()[1])

                conn.sendall(data)
 """
    #print('Received', repr(data))

def SendMessage(msg_type):
    return
    

def GetTokenOccurance(token, message):
    return  message.count(token)



if __name__ == "__main__":
    main()







