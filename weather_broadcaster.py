import logging
import pyowm
from requests import Timeout


logger = logging.getLogger(__name__)

class WeatherBroadcaster():
    def __init__(self, owm_api_key=None):
        self._owm_api_key = owm_api_key
        self._owm = None
        self.observers = [] 
    
    @property
    def owm(self):
        try:
            if not self._owm:
                self._owm = pyowm.OWM(self._owm_api_key)
        except Timeout as err:
            logger.error(
                "WeatherStation owm fail with TimeOut error {}".format(err))
        return self._owm
    
    
    def _get_data_by_coord(self, lon, lat):
        mgr = self.owm.weather_manager()
        observations = mgr.weather_around_coords(lat=lat, lon=lon)
        return observations[0].weather.to_dict()


    def register_observer(self, observer):
        '''註冊觀察者'''
        if isinstance(observer, list):
            self.observers.extend(observer)
        else:
            self.observers.append(observer)


    def notify_all_observers(self):
        '''通知所有觀察者'''
        for observer in self.observers:
            weather_data = self._get_data_by_coord(
                lon=observer.user_data.get('longitude', 0), 
                lat=observer.user_data.get('latitude', 0))
            observer.notify(weather_data)
