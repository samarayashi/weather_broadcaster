from os import path
import logging
import time

from weather_station import WeatherStation
from line_notification import notify


logger = logging.getLogger(__name__)
CURRENT_PATH = path.dirname(path.abspath(__file__))
HOUR = 60 * 60
users_data = [{
    "owm_api_key": "747f8dc657f2dbe2909e9cfc6e554669",
    "line_token": "eAop04vpYNyNY9FYSNhlZMOoLZkf5O6evz879oApZWF",
    "longitude": 121.5172,
    "latitude": 23.0472
}]


def main():
    while True:
        for user_data in users_data:
            weather_station = WeatherStation(user_data.get('owm_api_key'))
            weather_data = weather_station.get_data_by_coord(
                user_data.get('longitude', 0), user_data.get('latitude', 0)
            )
            status_code = notify(user_data.get('line_token'), weather_data)
            print(status_code)
        time.sleep(HOUR)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s')
    main()