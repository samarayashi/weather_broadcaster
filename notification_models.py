import logging
from abc import ABC, abstractmethod

from line_notification import LineNotification
from utils import trans_temp_k2c

logger = logging.getLogger(__name__)

def get_notification_model(model_type):
    if model_type == 'PremiumModelNotification':
        return PremiumModelNotification
    else:
        return GeneralModelNotification
    
def common_message_formatter(msg):
    return {
        'temperature': trans_temp_k2c(
            msg.get('temperature', {}).get('temp', 'Null')),
        'humidity': msg.get('humidity', 'Null'),
        'status': msg.get('status', 'Null'),
    }

class NotificationBase(ABC, LineNotification):
    """通知基類（抽象類別），提供共用的初始化和 notify 方法"""
    
    def __init__(self, channel_token, user_data):
        super().__init__(channel_token)
        self.user_data = user_data

    @abstractmethod
    def _complete_message(self, msg):
        """強制子類別實作"""
        pass

    def notify(self, msg):
        """發送通知"""
        complete_message = self._complete_message(msg)
        logger.info('user: {} notify message: {}'.format(
            self.user_data.get('user', 'NAME_IS_NEEDED'), complete_message))
        return super().notify(self.user_data['user_id'], complete_message)


class GeneralModelNotification(NotificationBase):
    """一般會員通知"""
    
    def _complete_message(self, msg):
        return str({
            'user': self.user_data.get('user', 'Null'),
            **common_message_formatter(msg)
        })


class PremiumModelNotification(NotificationBase):
    """高級會員通知"""
    
    def _complete_message(self, msg):
        return str({
            'user': self.user_data.get('user', 'Null'),
            **common_message_formatter(msg),
            'detailed_status': msg.get('detailed_status', 'Null'),
            'wind speed': msg.get('wind', {}).get('speed', 'Null')
        })