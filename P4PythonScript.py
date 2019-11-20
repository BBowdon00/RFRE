import xmlrpc

server = xmrplc.client.ServerProxy("https://127.0.0.1:8080")

while(True):
    ans = raw_input("Start new flood? (Y/N)")
    if ans == "Y":
        lat = input("Latitude? (enter a float)")
        server.setLat(lat) # Is this the correct way to set?
        lon = input("Longitude? (enter a float)")
        server.setLon(lon)
        alt = input("Altitude? (enter a float)")
        server.setAlt(alt)
        num = input("Number of planes? (enter a integer)")
        server.setNum(num)
    elif ans == "N":
        break
    else:
        print("Not a valid input... Exiting")
        break