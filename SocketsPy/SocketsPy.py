#socket is present at transport layer result is moved to application layer
import socket
#creating socket
#in the below first socket is library and 2nd socket is method in that lib
#AF_INET is internet, SOCK_STREAM is stream to send and receive data to and from server
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
#connecting to the site from which we want to retrieve data
mysock.connect(('www.py4inf.com',80));
#requesting required document by mentioning GET then link Then Protocol type(HTTP/1.0)
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    #512 is buffer size, once the buffer is full it will be printed
    data=mysock.recv(512)
    if (len(data)<1):
        break;
    print data;
mysock.close();

#there is shorter procedure than this socket i.e using urllib
#open urllibPy.py to check the code
