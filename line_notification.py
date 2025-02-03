import requests

class LineNotification:
    LINE_API_URL = "https://api.line.me/v2/bot/message/push"

    def __init__(self, channel_token):
        """
        初始化 LINE Messaging API 通知工具

        :param line_token: LINE Channel Access Token
        :param user_id: 接收訊息的使用者 ID
        """
        self._line_token = channel_token

    def notify(self, user_id, msg):
        """
        發送訊息到 LINE

        :param msg: 要發送的訊息內容
        :return: LINE API 的回應狀態碼與回應數據
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._line_token}",
        }

        payload = {
            "to": user_id,
            "messages": [
                {"type": "text", "text": msg}
            ],
        }

        response = requests.post(self.LINE_API_URL, headers=headers, json=payload)
        return response.status_code, response.json()