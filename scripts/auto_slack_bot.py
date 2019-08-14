# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')

from scripts.setting import account
from scripts.content import slack_post_content
import requests
import json


class AutoSlackBot:
    def __init__(self, kktix_url, hack_md_url):
        self.kktix_url = kktix_url
        self.hack_md_url = hack_md_url
        self.slack_bot_webhook = account.slack_bot_hook_url

    def run(self):
        dict_headers = {'Content-type': 'application/json'}

        payload = {
            "icon_emoji": ":vtaiwan:",
            "username": slack_post_content.bot_name.decode('utf8'),
            "text": slack_post_content.title_text.format(self.kktix_url, self.hack_md_url, slack_post_content.jitsi_link).decode('utf8'),
            "attachments": [
                {
                    "color": "#36a64f",
                    "title": slack_post_content.kktix_title.decode('utf8'),
                    "title_link": self.kktix_url,
                    "text": slack_post_content.kktix_description.decode('utf8'),
                    "thumb_url": slack_post_content.kktix_thumb_url
                },
                {
                    "color": "#36a64f",
                    "title": slack_post_content.hack_md_title.decode('utf8'),
                    "title_link": self.hack_md_url,
                    "image_url": slack_post_content.hack_md_thumb_url
                },
                {
                    "color": "#36a64f",
                    "title": slack_post_content.jitsi_title.decode('utf8'),
                    "title_link": slack_post_content.jitsi_link,
                    "thumb_url": slack_post_content.jitsi_md_thumb_url
                }
            ]
        }

        json_payload = json.dumps(payload)
        result = requests.post(self.slack_bot_webhook, data=json_payload, headers=dict_headers)
        print(result.text)
