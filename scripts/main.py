# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')

from scripts.auto_g0v_hackmd import G0vHackMdScript
from scripts.auto_kktix import VtwKKTixScript
from auto_slack_bot import AutoSlackBot

hack_md_script = G0vHackMdScript()
hack_md_url = hack_md_script.run()
vtw_script = VtwKKTixScript(hack_md_url)
kktix_url = vtw_script.run()

print hack_md_url
print kktix_url

slack_bot = AutoSlackBot(kktix_url, hack_md_url)
slack_bot.run()

# TODO:
# Post on Facebook
# Post on vtw.link
