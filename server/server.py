import socket
import datetime
import threading
from server.analysis import analysis

HOST = '127.0.0.1'
PORT = 25566

INACTIVITY_MINUTES = 5

# Time declaration
last_time = datetime.datetime(2023, 1, 1, 0, 0, 0)

#It returns an empty string if <INACTIVITY_MINUTES> expire
def checkTime() -> str:
    global last_time
    current_time = datetime.datetime.now()
    time_difference_minutes = (current_time - last_time).total_seconds() / 60
    last_time = current_time
    if time_difference_minutes > INACTIVITY_MINUTES:
        return "\n\n--------------------------------------------------------\n" + current_time.strftime("%d/%m/%Y, %H:%M:%S") + "\n"
    else:
        return ""

def logToFile(ip : str, resultSTR : str):
    filename = ip + '.txt'
    with open(filename,'a') as f:
        f.write(checkTime() + resultSTR)
    f.close()

def handleClient(conn, addr):
    print('Connesso: ',addr)
    while True:
        data = conn.recv(1024)   # ConnectionResetError, BrokenPipeError
        if not data:
            continue
        ip, port = conn.getpeername()
        message = data.decode('utf-8')
        now = datetime.datetime.now().isoformat()
        #resultSTR = now + ',' + ip + ',' + message
        resultSTR = message
        print(resultSTR)
        logToFile(ip, resultSTR)

#Socket init
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST, PORT))
    except OSError():
        print("Error: port already in use")
    s.listen()
    while True:
        conn, addr = s.accept()
        
        print ("Starting clientThread")
        clientThread = threading.Thread(target=handleClient, args=(conn, addr))
        clientThread.start()

        ip, port = conn.getpeername()
        filename = "txtfiles/" + ip + ".txt"
        print ("Starting detectionThread   " + filename)
        detectionThread = threading.Thread(target=analysis(filename=filename), args=())
        detectionThread.start()


