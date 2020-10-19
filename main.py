def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

print(visitor_ip_address(request))

def check_ip_is_valid(ip):
    import socket

    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid = False
    return ip_valid

print(check_ip_is_valid(visitor_ip_address(request)))
