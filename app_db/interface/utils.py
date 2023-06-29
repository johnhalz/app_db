import socket
import ipaddress

def ip_is_valid(ip_address: str) -> bool:
    '''Check if ip address is valid'''
    try:
        ip = ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def port_is_valid(port_number: int) -> bool:
    '''Verify if port number is valid'''
    try:
        port_number = int(port_number)
        if port_number < 0 or port_number > 65535:
            return False
    except ValueError:
        return False

    return True

def ip_is_reachable(ip_address: str, port_number: int, timeout: int = 2) -> bool:
    '''
    Check if address (ip_address:port_number) is reachable or
    not with a sepcified timeout.
    '''
    reachable = False

    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)  # Set a timeout value (in seconds)

        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port_number))
        if result == 0:
            reachable = True

    except socket.error as e:
        print(f"Error occurred while checking IP accessibility: {e}")

    finally:
        sock.close()

    return reachable
