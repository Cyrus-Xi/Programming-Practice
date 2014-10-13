#!/usr/bin/env python

"""
A simple web server, which allows for concurrency, implemented with low-level
libraries.

Responds to GET and HEAD HTTP requests appropriately.
Sends back appropriate header lines plus requested file content.
File may be located in subdirectories.
If file not found, responds with a 404 error.
Handles multiple connections with threading.
Also allows connections to stay alive or close themselves.
User can terminate program by typing 'STOP' in command line.
Explicitly handles various exceptions / errors.

Uses select library to allow user to pass in multiple port numbers.

Seems to work correctly: tested threading and multiple ports with
both web browser and multiple telnet connections.

By Cyrus Xi.
"""

from socket import socket, AF_INET, SOCK_STREAM, error
from sys import argv, exit, stdin
from os import curdir, sep
from thread import start_new_thread
from select import select


def reply_to_request(connect_socket):
    """
    Respond to HTTP request programmatically.

    :param connect_socket: client's connection socket
    """
    print '... connected!'
    while 1:
        request = connect_socket.recv(8192)

        # Get request type.
        if request.startswith('GET'):
            request_type = 'GET'
        elif request.startswith('HEAD'):
            request_type = 'HEAD'
        else:
            print 'Request must be either a GET or HEAD.'
            continue

        try:
            # filename is second item in first header line.
            fname = request.split()[1]
        # Empty request, try again next iteration.
        except IndexError:
            continue

        try:
            # Get right file using current directory as root.
            file_ = open(curdir + sep + fname)
            # Get file's contents.
            out = file_.read()

            # Prepare and send appropriate header lines.
            is_close = 'Connection: close' in request
            connect_socket.send('HTTP/1.1 200 OK\r\n')
            if is_close:
                connect_socket.send('Connection: close\r\n')
            else:
                connect_socket.send('Connection: keep-alive\r\n')
            # Get size of file and send.
            connect_socket.send('Content-Length: {0}\r\n'.format(len(out)))
            connect_socket.send('Content-Type: text/html\r\n')
            connect_socket.send('\r\n')

            # Send file's contents if GET request.
            if request_type == 'GET':
                for byte in out:
                    connect_socket.send(byte)

            # Connection: close
            if is_close:
                print 'Close connection!'
                break
            # Connection: keep-alive
            else:
                print 'Keep connection alive!'
                continue
        # File doesn't exist.
        except IOError:
            print 'File not found!'
            connect_socket.send('404 Not Found\r\n')
            continue
    connect_socket.close()


def main():
    """Instantiate web server and wait for connection requests."""
    # Get port numbers from command line. Else exit.
    if len(argv) > 1:
        # Convert to list of ints.
        port_nums = [int(arg) for arg in argv[1:]]
    else:
        print 'Please specify a port number or numbers to bind to. Exiting.'
        exit(1)

    # Instantiate a server socket for each port number.
    list_sockets = []
    try:
        for port in port_nums:
            print 'Server socket for port ' + str(port)
             # Create TCP socket.
            socket_ = socket(AF_INET, SOCK_STREAM)
            socket_.bind(('', port))
            socket_.listen(3)
            list_sockets.append(socket_)
    except error, (value, message):
        print 'Could not open socket: ' + message
        exit(1)

    input_ = [stdin] + list_sockets
    running = True

    while running:
        # Use select to handle multiple server sockets / ports.
        inready, outready, errready = select(input_, [], [])

        # Iterate over objects ready to be read.
        for s in inready:
            # Must be a server socket.
            if s != stdin:
                print 'We have a server socket.'
                try:
                    connection_socket, address = s.accept()
                    # Give socket own thread.
                    # Argument to function must be a tuple.
                    start_new_thread(reply_to_request, (connection_socket,))
                # Explicitly handle keyboard interrupt.
                except KeyboardInterrupt:
                    print '\nOk, exiting!'
                    # If connection_socket extant, close.
                    if connection_socket:
                        connection_socket.close()
                    running = False
            # Check if user wants program to terminate.
            else:
                print 'We have console input.'
                user_input = stdin.readline()
                if 'STOP' in user_input:
                    running = False

    # Clean-up.
    for socket_ in list_sockets:
        socket_.close()


if __name__ == '__main__':
    main()