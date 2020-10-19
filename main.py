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
def get_geolocation():
    import geoip2.database

    reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
    if check_ip_is_valid(visitor_ip_address(request)):
        response = reader.city('216.58.223.110')

        print(response.country.iso_code)
        print(response.country.name)
        print(response.country.names['zh-CN'])
        print(response.subdivisions.most_specific.name)
        print(response.subdivisions.most_specific.iso_code)
        print(response.city.name)
        print(response.postal.code)
        print(response.location.latitude)
        print(response.location.longitude)

        reader.close()
try:
    get_geolocation()
except Exception as e:
    print(e)
    pass
