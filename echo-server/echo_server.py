import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # TODO: You may find that if you repeatedly run the server script it fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections
    sock.bind(address)
    sock.listen(1)
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors

            # connection, addr = ('AddressFamily.AF_INET: 2', ("127.0.0.1", 10000))  # server_socket.accept()
            connection, client_address = sock.accept()
            try:
                print('starting try block', sys.stderr, 'connection from', client_address)
                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting

                    data = connection.recv(16)
                    # print(type(data))
                    print('received "{0}"'.format(data.decode('utf8')))
                    
                    # TODO: Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.
                    # if data:
                    connection.sendall(data)  # .encode('utf8'))
                    print('sent "{0}"'.format(data.decode('utf8')))
                    if len(data) < 16:
                        break
                    
                    # TODO: Check here to see whether you have received the end
                    # of the message. If you have, then break from the `while True`
                    # loop.
                    # 
                    # Figuring out whether or not you have received the end of the
                    # message is a trick we learned in the lesson: if you don't
                    # remember then ask your classmates or instructor for a clue.
                    # :)

            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                # TODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.
                connection.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
