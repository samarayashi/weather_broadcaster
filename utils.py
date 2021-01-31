import json


def get_json_content(path):
    with open(path, 'r') as js:
        content = json.load(js)
        js.close()
    return content


def trans_temp_kelvin_to_Celsius(temp):
    # 將溫度從絕對溫度轉成攝氏溫度
    return int(temp - 273.15)
