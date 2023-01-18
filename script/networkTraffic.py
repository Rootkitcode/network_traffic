import psutil
from datetime import datetime
#R4c0d3 @Author

def network_traffic():
    #obtain the trafic network
    net_io_counters = psutil.net_io_counters()
    sent = net_io_counters.packets_sent
    recv = net_io_counters.bytes_recv
    #obtain the currently date and hour
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Date and hour: ", current_time)
    print("Packages sent: ", sent)
    print("Packages recv", recv)
    #now you obtain the protocols used
    net_connection = psutil.net_connections()
    for conn in net_connection:
        print("Protocols: ", conn.type)
        #here we obtain local and remote port
        if conn.raddr:
            print("Local port: ", conn.laddr.port)
        if conn.raddr:
            print("Remote port: ", conn.laddr.port)
network_traffic()