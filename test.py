from phue import Bridge

br = Bridge('192.168.1.30')
br.connect()

lightSelection = 5
br.set_light(lightSelection,'bri', 254)
#br.set_light(lightSelection,'sat', 100)
br.set_light(lightSelection,"xy",[0.23,0.04])