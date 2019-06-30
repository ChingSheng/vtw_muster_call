# -*- coding: UTF-8 -*-
from scripts.utils.future_day import FutureDay
from scripts.setting import account
import requests
import json


class AutoSlackBot:

    def __init__(self, kktix_url, hack_md_url):
        self.kktix_url = kktix_url
        self.hack_md_url = hack_md_url
        self.slack_bot_webhook = account.slack_bot_hook

    def run(self):
        future_day = FutureDay()
        wednesday_offset = 2
        next_wednesday = future_day.next_weekend(wednesday_offset).strftime("%Y/%m/%d")

        dict_headers = {'Content-type': 'application/json'}

        payload = {
            "icon_emoji": ":vtaiwan:",
            "username": "自動小松機器人".decode('utf8'),
            "text": "本週小松報名：\n歡迎直接編輯共筆～\n{0}\n{1}".format(self.kktix_url, self.hack_md_url).decode('utf8'),
            "attachments": [
                {
                    "color": "#36a64f",
                    "title": "KKTIX vTaiwan小松，快來報名吧！".decode('utf8'),
                    "title_link": self.kktix_url,
                    "text": "時間：{0}".format(next_wednesday).format('utf8'),
                    "thumb_url": "https://t.kfs.io/assets/kktix-og-image-0b30b8444017c8a56ab631ac2975e92f.png"
                },
                {
                    "color": "#36a64f",
                    "title": "HackMD共筆({0})".format(next_wednesday).decode('utf8'),
                    "title_link": self.hack_md_url,
                    "image_url": "https://g0v.hackmd.io/favicon.png"
                }
            ]
        }

        json_payload = json.dumps(payload)
        result = requests.post(self.slack_bot_webhook, data=json_payload, headers=dict_headers)
        print(result.text)




