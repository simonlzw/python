import subprocess

def ping(host):
    result = subprocess.run('ping -c 2 %s &> /dev/null' % host , shell=True)
    if result.returncode == 0 :
        return '%s:up' % host
    else:
        return '%s:down' % host

if __name__ == '__main__' :
    print(ping("127.0.0.1"))