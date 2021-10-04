import socket
import os
import pathlib

# Global constants
# HOST = '127.0.0.1' # local connections only
HOST = ''  # Opens connections to any IPv4 address on the network
PORT = 8080
DOC_ROOT = os.path.join(os.getcwd(), "docs")


def serve_file(filepath, connection):

    if filepath[0] == "/":
        filepath = filepath[1:]

    content_type = "text/html"

    if filepath[-3:] == "png":
        content_type = "image/png"

    print(f"Serving {filepath}...")
    full_filepath = os.path.join(DOC_ROOT, filepath)

    try:
        with open(full_filepath, "rb") as f:
            response = "HTTP/1.1 200 OK\n" \
                       f"Content-Length: {os.path.getsize(full_filepath)}\n" \
                       f"Content-Type: {content_type}\n" \
                       "Connection: Closed\n\n".encode("utf-8")

            response += f.read()
            s = connection.send(response)
        return s
    except Exception as e:
        print(e)
        print("Serving 404..")
        response_html = """
        <html>
        <head><title>404 Not Found</title></head>
        <body bgcolor="white">
        <center><h1>404 Not Found</h1></center>
        <hr><center><a href="/">Back to home</a></center>
        </body>
        </html>
        """
        response = "HTTP/1.1 404 Not Found\n"\
                    "Content-Type: text/html\n"\
                    f"Content-Length: {len(response_html)}\n"\
                    "Connection: Closed\n\n"
        response += response_html
        s = connection.send(response.encode("utf-8"))
        return s

def listen_for_request(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen()
            print(f"Listening on port {port}..")
            print(f"Visit http://{local_ip}:{port}/ via a web browser to see my page!\n")
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
                        file_requested = data.decode("utf-8").split("\n")[0].split(" ")[1]
                        print(f"Page requested: {file_requested}")
                        if file_requested == "/":
                            file_requested = "index.html"
                        serve_file(file_requested, conn)

        except Exception as e:
            print("Exception raised, closing socket!")
            s.close()
            raise e


new_port = input(f"Set a port to listen on (Press Enter for {PORT}): ")
if new_port:
    PORT = int(new_port)  #TODO: Fix this - it works but breaks the rule for a PORT constant

# HTML connections are closed as soon as a request has been sent, so we need to use a loop to start listening for the
# next one.
while True:
    try:
        listen_for_request(HOST, PORT)
    except Exception as e:
        print(e)
        break


