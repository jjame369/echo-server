import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):

    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # define server and the port to listen on.
    server_address = ('localhost', 10000)  # ('127.0.0.1', 10000)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.
    sock.connect(server_address)
    print('connected to socket')
    # you can use this variable to accumulate the entire message received back
    # from the server

    # received_message = sock.recv(4096)
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.
        # message = input("> ")
        # amount_received = 0
        # amount_expected = len(message)

        # while amount_received < amount_expected:
        #     chunk = sock.recv(16)
        #     amount_received += len(chunk)
        #     print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)

        sock.sendall(msg.encode('utf-8'))

        while True:
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message += chunk.decode('utf8')
            # if the chunk of info is less than 16 then you know it is the last message therefore break.
            if len(chunk) < 16:
                break

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket', file=log_buffer)
        sock.close()

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        # print(sys.argv[0])
        # print('entered the if statement')
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv
    client(msg)
