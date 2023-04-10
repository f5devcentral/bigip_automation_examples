import sys

f = open('nginx.conf', 'r')
filedata = f.read()
f.close()

if 'waf-' in sys.argv[1]:
    f1 = open('nginx-waffler.conf', 'r')
    filedata1 = f1.read()
    f1.close()
    newdata = filedata1.replace("NginxDefaultPolicy.json", sys.argv[1])
else:
    newdata = filedata.replace("proxy_pass http://172.29.38.211:80$request_uri;",
                               "proxy_pass http://"+sys.argv[1]+":8080$request_uri;")
f = open('nginx.conf', 'w')
f.write(newdata)
f.close()
