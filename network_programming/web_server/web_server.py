import socket, os, pathlib

# Global constants
HOST = '127.0.0.1'
PORT = 8080
DOC_ROOT = os.path.join(os.getcwd(), "docs")


def serve_file(filepath, connection):

    if filepath[0] == "/":
        filepath = filepath[1:]

    print(f"Serving {filepath}...")
    full_filepath = os.path.join(DOC_ROOT, filepath)

    with open(full_filepath, "rb") as f:
        response = "HTTP/1.1 200 OK\n" \
                   f"Content-Length: {os.path.getsize(full_filepath)}\n" \
                   "Content-Type: text/html\n" \
                   "Connection: Closed\n\n".encode("utf-8")

        response += f.read()
        s = connection.send(response)
    return s


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


