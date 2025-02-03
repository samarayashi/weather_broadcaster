from os import path, getenv
import logging
from time import sleep
from dotenv import load_dotenv

from utils import get_json_content
from weather_broadcaster import WeatherBroadcaster
from notification_models import get_notification_model


logger = logging.getLogger(__name__)
CURRENT_PATH = path.dirname(path.abspath(__file__))
HOUR = 60 * 60


# 加載 .env 文件，讀取環境變數
load_dotenv()
OWM_API_KEY = getenv("OWM_API_KEY")


def main():
    user_data = get_json_content(path.join(CURRENT_PATH, 'user_data.json'))
    weather_broadcaster = WeatherBroadcaster(OWM_API_KEY)
    
    for user, user_info in user_data.items():
        try:
            model = get_notification_model(user_info['model_type'])
            observer = model(user_info)
            logger.info('user: {} register'.format(user))
            weather_broadcaster.register_observer(observer)
        except Exception as err:
            logger.error('fail with model {} error: {}'.format(
                user_info.get('model_type'), err))
    while True:
        try:
            weather_broadcaster.notify_all_observers()
            sleep(HOUR)
        except KeyboardInterrupt:
            logger.warning('keyboard interrupt\n')
            break
        except Exception as e:
            logger.error('main exception: {}'.format(e))
            break


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s')
    main()
