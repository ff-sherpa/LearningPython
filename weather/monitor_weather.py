# monitor_weather.py
# Analyze weather data based on Bridgeport, WV GPS coordinates.
# Alert when certain thresholds are met.
import json

json_file = "weather_data.json"

json_data = open(json_file)
data = json.load(json_data)

for hrs in data['hourly']['data']:
    # check precip
    if hrs['precipProbability'] > 0.5:
        print "RAIN ALERT: Precip probability > 75% at:" , hrs['time'], " Close windows"
        break

# check current temp
if data['currently']['temperature']>75:
    print("HEAT ALERT: Temp greater than 75!  Turn on gable fan")
elif data['currently']['temperature']<32:
    # FROST ALERT
    if data['currently']['dewPoint']<45 and data['currently']['windSpeed']<5 and data['currently']['visibility']>10:
        print("FROST ALERT: Cover delicate plants")
    else:
        print("FREEZE ALERT: Temp less than 32!  Turn off outside water")
    
json_data.close()
