vtw 每週開活動小幫手 (vtw_muster_call)
---
### 環境設置
* Python 2.7
* 目前需要再Pycharm上面開啟（import module的問題，晚些時間修理一下）
* 當前使用的是[ChromeDriver 75.0.3770.90](http://chromedriver.chromium.org/downloads) (已放在專案中)

### 使用方式
1. 用pycharm 開啟此專案
2. 在script/setting/account 填入對應的帳號密碼
3. 承2, hack md帳號底下需要有名為"vTaiwan小松" 為標題的範本文件
4. 提供了slack webhook。當HackMD共筆與KKTIX活動均創建完成後，透過webhook可在g0v slack的 vTaiwan channel 發送活動連結訊息 (slack webhook的連結需要填入，[相關教學](https://api.slack.com/incoming-webhooks))
5. 執行 main.py檔案
