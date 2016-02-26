import sys,socket,httplib
host = sys.argv[1]
port = int(sys.argv[2])
url = str(host)+":"+str(port)
try:
    c = httplib.HTTPConnection(url,timeout=10)
    c.request ("GET", "/loginImage.html")
    r2 = c.getresponse()
    r1 = r2.getheaders()
    WebServer = r2.getheader("server")
    ContentType = r2.getheader("content-type")
    d2 = r2.read()
    print "\n\nBanner :"
    print "Banner Fields :",r1
    print "\n\nWebServer Name :",WebServer
    print "Content Type :",ContentType
    print "\n\nResponse is : "
    print d2
    print "\n\n"
except :
    print "Unable to connect !!!"
