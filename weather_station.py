import pyowm
import json
import logging
from requests import Timeout


logger = logging.getLogger(__name__)


class WeatherStation():
    # document: https://pyowm.readthedocs.io/en/latest/pyowm.weatherapi25.html
    def __init__(self, owm_api_key=None):
        self._owm_api_key = owm_api_key
        self._owm = None

    @property
    def owm(self):
        try:
            if not self._owm:
                self._owm = pyowm.OWM(self._owm_api_key)
        except Timeout as err:
            logger.error('WeatherStation owm fail with TimeOut error {}'.format(err))
        return self._owm

    def get_data_by_coord(self, lon, lat):
        mgr = self.owm.weather_manager()
        observations = mgr.weather_around_coords(lat=lat, lon=lon)
        return observations[0].weather.to_dict()

def main():
    api_key = '747f8dc657f2dbe2909e9cfc6e554669'
    longitude, latitude = 121.5681, 24.9828  # 恆光橋
    weather_station = WeatherStation(owm_api_key=api_key)
    weather_data = weather_station.get_data_by_coord(lon=longitude, lat=latitude)
    logger.info('weather station getting lon: {}, lat:{} data:{}'.format(
        longitude, latitude, weather_data))


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s')
    main()