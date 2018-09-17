
import requests
from requests.auth import HTTPBasicAuth
import datetime
import time
import json
link = 'http://softwareag10.cumulocity.com/measurement/measurements'

utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
mydate = datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


def send_data_via_http(values, username, password):

    voltage_data = {

        "c8y_VoltageMeasurement": {
            "V": {
                "value": values[0],
                "unit": "V"}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_VoltageMeasurement"
    }

    current_data = {

        "c8y_CurrentMeasurementmA": {
            "C": {
                "value": values[1]*1000,
                "unit": "mA"}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_CurrentMeasurementmA"
    }

    energy_data = {

        "c8y_EnergyMeasurement": {
            "E": {
                "value": values[2]*1000,
                "unit": "Wh"}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_EnergyMeasurement"
    }

    power_data = {

        "c8y_PowerMeasurement": {
            "P": {
                "value": values[3],
                "unit": "W"}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_PowerMeasurement"
    }

    frequency_data = {

        "c8y_FrequencyMeasurement": {
            "F": {
                "value": values[4],
                "unit": "Hz"}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_FrequencyMeasurement"
    }

    pf_data = {

        "c8y_PowerFactorMeasurement": {
            "PF": {
                "value": values[5],
                "unit": ""}
        },
        "time": str(mydate),
        "source": {
            "id": "4117240"},
        "type": "c8y_PowerFactorMeasurement"
    }

    #username = "softwareag10/muriithicliffernest@gmail.com"
    #password = "F3ilWau%ee.?89"
    r = requests.post(link, json=voltage_data, auth=HTTPBasicAuth(username, password))
    r = requests.post(link, json=current_data, auth=HTTPBasicAuth(username, password))
    r = requests.post(link, json=energy_data, auth=HTTPBasicAuth(username, password))
    r = requests.post(link, json=power_data, auth=HTTPBasicAuth(username, password))
    r = requests.post(link, json=frequency_data, auth=HTTPBasicAuth(username, password))
    r = requests.post(link, json=pf_data, auth=HTTPBasicAuth(username, password))
    print(r.status_code)

#send_data_via_http([0,0,0,0,0,0])




data2 = {

    "name": "Eastron Smart Meter ",
    "c8y_IsDevice": {},

}


#username = "softwareag10/muriithicliffernest@gmail.com"
#password = "F3ilWau%ee.?89"
#r = requests.post(link2, json = data2, auth=HTTPBasicAuth(username, password))

# #resp = r.json()
# #print(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.gst).replace(microsecond=1000).isoformat())
#
# print(r.reason)