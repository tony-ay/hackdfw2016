import time, urllib2, ssl
import serial

port = serial.Serial("COM4", 9600, timeout=0)

timeout = 0
old_time = None

while 1:
    url = "https://api.tropo.com/1.0/sessions?action=create&token=634f6b5a7364724947636d626c634b504754474f7a776d724a6a72755a486666507572566c664d4b46777256"
    var2 = "&sendToNumber=19567896427"
    try:
        data = port.readline()
        data = str(data).strip()
        if data != "0" and len(data) > 0:
            ctime = time.time()
            if old_time == None:
                old_time = ctime
            if timeout > 0:
                timeout -= ctime - old_time
                old_time = ctime
            else:
                timeout = 10
                var1 = ""
                for i in range(0, len(data)):
                    if data[i] == "1":
                        var1 += "main+door"
                    elif data[i] == "2":
                        if len(var1) > 0:
                            var1 += ",+"
                        var1 += "east+window"
                    elif data[i] == "3":
                        if len(var1) > 0:
                            var1 += ",+"
                        var1 += "north+window"
                    elif data[i] == "4":
                        if len(var1) > 0:
                            var1 += ",+"
                        var1 += "west+window"
                var1 = "&text=" + var1 + "+detected+object"
                #print var1
                url += var1 + var2
                try:
                    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                    result = urllib2.urlopen(url, context=gcontext)
                    print "notified"
                except urllib2.URLError, e:
                    print e
        print data
    except serial.SerialTimeoutException:
        print("Couldn't read data")
    time.sleep(1)