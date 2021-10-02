import socket

HOST = '127.0.0.1'
PORT = 8888

new_port = input(f"Set a port to listen on (Press Enter for {PORT}): ")
if new_port:
    PORT = int(new_port)


html = "<html>\n<head><title>MyWebServer!</title></head>\
        <body>\n\
        <h1>Hello, World!</h1>\n\
        </body><p>Served by my own webserver, written in Python!</p>\n\
        </html>"

http_response = "HTTP/1.1 200 OK\n"\
                f"Content-Length: {len(html)}\n"\
                "Content-Type: text/html\n"\
                "Connection: Closed\n\n"

http_response += html

def serve_response(connection, response):
    print("Sending response...")
    print(http_response)
    if type(response) == str:
        response = response.encode("utf-8")
    connection.send(response)


def listen_for_request(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            s.listen()
            print(f"Listening on port {port}..")
            print(f"Visit http://{host}:{port}/ via a web browser to see my page!\n")
            conn, addr = s.accept() # Returns a connection and address object of the connected client
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024) # This is a blocking-call, should pause whilst it waits for a connection: https://realpython.com/python-sockets/#blocking-calls
                    if not data:
                        break
                    if b"GET" in data and b"HTTP/1.1" in data:
                        print("HTTP/1.1 GET request received:")
                        print("------------------------------")
                        print(data.decode("utf-8"))

                        serve_response(conn, http_response)

        except Exception as e:
            print(f"Exception raised: {e}")
            s.close()


while True:
    listen_for_request(HOST, PORT)

