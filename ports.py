import psutil
import socket

def get_udp_and_tcp() :
    # infos sur les ports tcp et udp
    connectall = psutil.net_connections(kind='inet')

    # on sépare udp et tcp en écoute
    only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.type == socket.SOCK_STREAM and conn.status == psutil.CONN_LISTEN]
    only_udp_listening_ports = [conn.laddr.port for conn in connectall if conn.type == socket.SOCK_DGRAM and conn.status == psutil.CONN_LISTEN]

    # retire les doublons
    only_tcp_listening_ports = list(set(only_tcp_listening_ports))
    only_udp_listening_ports = list(set(only_udp_listening_ports))

    return {"TCP" : only_tcp_listening_ports, "UDP" : only_udp_listening_ports}
