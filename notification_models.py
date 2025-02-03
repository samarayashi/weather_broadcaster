import logging
from line_notification import LineNotification
from utils import trans_temp_k2c

logger = logging.getLogger(__name__)

def get_notification_model(model_type):
    if model_type == 'PremiumModelNotification':
        return PremiumModelNotification
    else:
        return GeneralModelNotification
    
def commom_message_formatter(msg):
    return {
        'temperature': trans_temp_k2c(
            msg.get('temperature', {}).get('temp', 'Null')),
        'humidity': msg.get('humidity', 'Null'),
        'status': msg.get('status', 'Null'),
    }


class GeneralModelNotification(LineNotification):
    def __init__(self, channel_token, user_data):
        super().__init__(channel_token)
        self.user_data = user_data
        
    def _complete_message(self, msg):
        return str({
            'user': self.user_data.get('user', 'Null'),
            **commom_message_formatter(msg)
        })

    def notify(self, msg):
        logger.info('user: {} GeneralModel notify message: {}'.format(
            self.user_data.get('user', 'NAME_IS_NEEDED'), self._complete_message(msg)))
        return super().notify(self.user_data['user_id'],
            self._complete_message(msg))


class PremiumModelNotification(LineNotification):
    def __init__(self, channel_token, user_data):
        super().__init__(channel_token)
        self.user_data = user_data
        
    def _complete_message(self, msg):
        return str({
            'user': self.user_data.get('user', 'Null'),
            **commom_message_formatter(msg),
            'detailed_status': msg.get('detailed_status', 'Null'),
            'wind speed': msg.get('wind', {}).get('speed', 'Null')
        })

    def notify(self, msg):
        logger.info('user: {} GeneralModel notify message: {}'.format(
            self.user_data.get('user', 'NAME_IS_NEEDED'), self._complete_message(msg)))
        return super().notify(self.user_data['user_id'],
            self._complete_message(msg))