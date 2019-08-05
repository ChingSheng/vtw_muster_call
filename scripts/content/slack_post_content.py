# -*- coding: UTF-8 -*-
from scripts.utils.future_day import FutureDay

bot_name = "自動小松機器人"
title_text = "本次小松報名：\n歡迎直接編輯共筆～\n{0}\n{1}"

future_day = FutureDay()
wednesday_offset = 2
next_wednesday = future_day.next_weekend(wednesday_offset).strftime("%Y/%m/%d")

kktix_title = "KKTIX vTaiwan小松，快來報名吧！"
kktix_description = "時間：{0}".format(next_wednesday)
kktix_thumb_url = "https://t.kfs.io/assets/kktix-og-image-0b30b8444017c8a56ab631ac2975e92f.png"

hack_md_title = "HackMD共筆({0})".format(next_wednesday)
hack_md_thumb_url = "https://g0v.hackmd.io/favicon.png"