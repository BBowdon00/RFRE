import xmlrpc.client

server = xmlrpc.client.ServerProxy("https://127.0.0.1:8080")

while(True):
    ans = input("Start new flood? (Y/N)")
    if ans == "Y":
        lat = float(input("Latitude? (enter a float)"))
        server.set_lat(lat) # Is this the correct way to set?
        lon = float(input("Longitude? (enter a float)"))
        server.set_lon(lon)
        alt = float(input("Altitude? (enter a float)"))
        server.set_alt(alt)
        num = input("Number of planes? (enter a hex value)")
        server.set_num(num)
    elif ans == "N":
        break
    else:
        print("Not a valid input... Exiting")
        break
