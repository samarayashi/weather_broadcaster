import requests
import logging

from utils import trans_temp_kelvin_to_Celsius

logger = logging.getLogger(__name__)
LINE_URL = 'https://notify-api.line.me/api/notify'


def _enrich_message(msg):
    return str({
        'temperature': trans_temp_kelvin_to_Celsius(
            msg.get('temperature', {}).get('temp', 'Null')),
        'humidity': msg.get('humidity', 'Null'),
        'status': msg.get('status', 'Null'),
    })


def notify(token, msg):
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': _enrich_message(msg)}
    response = requests.post(LINE_URL, headers=headers, params=payload)
    return response.status_code


def main():
    line_token = 'eAop04vpYNyNY9FYSNhlZMOoLZkf5O6evz879oApZWF'
    msg = {'reference_time': 1609519734, 'sunset_time': 1609578968, 'sunrise_time': 1609540754, 'clouds': 75, 'rain': {}, 'snow': {}, 'wind': {'speed': 1.5, 'deg': 110}, 'humidity': 87, 'pressure': {'press': 1024, 'sea_level': None}, 'temperature': {'temp': 286.18, 'temp_kf': None, 'temp_max': 286.48, 'temp_min': 285.93}, 'status': 'Clouds', 'detailed_status': 'broken clouds', 'weather_code': 803, 'weather_icon_name': '04n', 'visibility_distance': 10000, 'dewpoint': None, 'humidex': None, 'heat_index': None}
    status_code = notify(line_token, msg)
    print(status_code)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s')
    main()