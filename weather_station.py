import pyowm
import logging
from requests import Timeout

from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class WeatherStation(ABC):
    # document: https://pyowm.readthedocs.io/en/latest/pyowm.weatherapi25.html
    def __init__(self, owm_api_key=None):
        self._owm_api_key = owm_api_key
        self._owm = None

    @abstractmethod
    def register_observer(self, user, model):
        pass

    @abstractmethod
    def notify(self):
        pass

    @property
    def owm(self):
        try:
            if not self._owm:
                self._owm = pyowm.OWM(self._owm_api_key)
        except Timeout as err:
            logger.error(
                "WeatherStation owm fail with TimeOut error {}".format(err))
        return self._owm

    def get_data_by_coord(self, lon, lat):
        mgr = self.owm.weather_manager()
        observations = mgr.weather_around_coords(lat=lat, lon=lon)
        return observations[0].weather.to_dict()
