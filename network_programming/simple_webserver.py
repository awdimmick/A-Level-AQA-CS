import socket

LOCAL_IP = socket.gethostbyname(socket.gethostname())
HOST = ''
PORT = 5000

def send_response(connection):

    # Define content to send (HTML page contents)
    content = "<html><body>"\
        "<h1>Hello!</h1>"\
        "<p>Welcome to my webserver!"\
        "</body></html>"


    # Define HTTP Response header
    header = "HTTP/1.1 200 OK\n" \
        f"Content-Length: {len(content)}\n" \
        "Content-Type: text/html\n" \
        "Connection: Closed\n\n"
    
    # Compile response string
    response = header + content + "\n\n"

    # Send response
    connection.send(response.encode("utf-8"))

def listen_for_request():

    global HOST, PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Set options and bind to the socket
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))

            # Start listening for connections        
            print(f"Listening on port {PORT}...")
            print(f"Visit http://{LOCAL_IP}:{PORT}/ to see my webpage!")
            s.listen()

            # Accept incoming connection
            conn, addr = s.accept()

            with conn:
                request = ""
                while True:
                    # Receive the data (bytes) as decode to a string
                    data = conn.recv(1024)

                    if not data:
                        break

                    request += data.decode() 
                    if request[-4:] == "\r\n\r\n":   # End of HTTP request
                        break

                if request.startswith("GET / HTTP/1.1"):
                    print("HTTP GET request received.")
                    send_response(conn)
                        
                            
        except Exception as e:
            s.close()
            raise e


while True:
    try:
        listen_for_request()
    
    except Exception as e:
        print(f"Critical failure! Details: {e}")
        break
