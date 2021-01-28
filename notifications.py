import logging

from line_notification import LineNotification
from utils import trans_temp_kelvin_to_Celsius


logger = logging.getLogger(__name__)


class GeneralModelNotification(LineNotification):
    def __init__(self, weather_broadcaster, user_data):
        self.user_data = user_data
        weather_broadcaster.register_observer(user_data.get('user'), self)
        super().__init__(line_token=user_data.get('line_token'))

    def notify(self, msg):
        logger.info('user: {} GeneralModel notify message: {}'.format(
            self.user_data.get('user', 'NAME_IS_NEEDED'), self._enrich_message(msg)))
        return super().notify(self._enrich_message(msg))

    def _enrich_message(self, msg):
        return str({
            'temperature': trans_temp_kelvin_to_Celsius(
                msg.get('temperature', {}).get('temp', 'Null')),
            'humidity': msg.get('humidity', 'Null'),
            'status': msg.get('status', 'Null'),
        })


class PremiumModelNotification(LineNotification):
    def __init__(self, weather_broadcaster, user_data):
        self.user_data = user_data
        weather_broadcaster.register_observer(user_data.get('user'), self)
        super().__init__(line_token=user_data.get('line_token'))

    def notify(self, msg):
        logger.info('user: {} PremiumModel notify message: {}'.format(
            self.user_data.get('user', 'NAME_IS_NEEDED'), self._enrich_message(msg)))
        return super().notify(self._enrich_message(msg))

    def _enrich_message(self, msg):
        return str({
            'temperature': trans_temp_kelvin_to_Celsius(
                msg.get('temperature', {}).get('temp', 'Null')),
            'humidity': msg.get('humidity', 'Null'),
            'detailed_status': msg.get('detailed_status', 'Null'),
            'wind speed': msg.get('wind', {}).get('speed', 'Null')
        })
