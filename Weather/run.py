from functions import Weather

a = Weather()
if a.onoff():
    a.opener()
    a.enter_values()

if a.onoff():
    a.get_values()
    a.convert()
    a.exit()
else:
    a.exit()



