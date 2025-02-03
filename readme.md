# Weather Broadcaster

## 1. 專案描述

Weather Broadcaster 是一個基於 Python 的天氣推播系統，採用 **觀察者模式 (Observer Pattern)** 來監聽天氣數據，並向不同的使用者發送通知。通知透過 **LINE Messaging API** 傳送，以確保使用者能夠即時獲取最新的天氣資訊。

此專案的主要功能包括：

- 從 **OpenWeatherMap API** 獲取即時天氣數據。
- 使用 **觀察者模式** 管理多個通知訂閱者。
- 透過 **LINE Messaging API** 向使用者推送天氣資訊。
- 支援不同的通知模式，如高級模式與一般模式。

---

## 2. 觀察者模式解釋

**觀察者模式 (Observer Pattern)** 是一種設計模式，允許物件（Subject）維護一組觀察者（Observers），當物件的狀態變更時，自動通知所有觀察者。

在本專案中，

- `WeatherBroadcaster` 作為 **主題 (Subject)**，負責從 OpenWeatherMap 獲取天氣資訊。
- `PremiumModelNotification` 和 `GeneralModelNotification` 作為 **觀察者 (Observer)**，接收來自 WeatherBroadcaster 的天氣資訊。
- `LineNotification` 作為 **具體通知發送者**，負責將通知發送到 LINE。

這種設計模式允許系統在不修改 `WeatherBroadcaster` 的前提下，輕鬆擴展不同的通知模式。

---

## 3. 觀察者模式關係圖

```
WeatherBroadcaster (主題)
    ├── PremiumModelNotification (觀察者)
    │      └── LineNotification (發送 LINE 通知)
    └── GeneralModelNotification (觀察者)
           └── LineNotification (發送 LINE 通知)
```

這個架構確保了不同使用者可以訂閱不同的通知模式，且當 `WeatherBroadcaster` 更新天氣資訊時，所有訂閱者都會收到通知。

---

## 4. 專案啟動方式

### **環境設定**

1. 確保已安裝 Python 3。
2. 安裝必要的套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 在專案目錄下建立 `.env` 檔案，並填入您的 API 金鑰與 LINE 訪問權杖：
   ```
   OWM_API_KEY=your_openweathermap_api_key
   LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
   ```

### **執行程式**

1. 啟動天氣推播服務：
   ```bash
   python weather_broadcaster_broker.py
   ```

此時，系統會定期從 OpenWeatherMap 取得天氣數據，並根據使用者設定發送 LINE 通知。