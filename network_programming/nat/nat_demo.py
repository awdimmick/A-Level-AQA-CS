from flask import Flask, request, render_template
from requests import get
import socket

app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_external_ip():

    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

@app.route('/')
def hello_world():  # put application's code here

    r = request

    return render_template("info.html", local_external_ip=get_external_ip(), local_internal_ip=get_local_ip(),
                           remote_external_ip = request.remote_addr, local_flask_port=5000,
                           remote_port=request.environ.get('REMOTE_PORT'))


if __name__ == '__main__':
    app.run(host="0.0.0.0")