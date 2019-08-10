# -*- coding: UTF-8 -*-
import sys
sys.path.append('../')

from apscheduler.schedulers.blocking import BlockingScheduler
from scripts.auto_g0v_hackmd import G0vHackMdScript
from scripts.auto_kktix import VtwKKTixScript
from auto_slack_bot import AutoSlackBot

def timed_job():
    print 'This job is run every three minutes.'
    hack_md_script = G0vHackMdScript()
    hack_md_url = hack_md_script.run()
    vtw_script = VtwKKTixScript(hack_md_url)
    kktix_url = vtw_script.run()
    print hack_md_url
    print kktix_url

    slack_bot = AutoSlackBot(kktix_url, hack_md_url)
    slack_bot.run()

sched = BlockingScheduler(timezone='Asia/Taipei')
sched.add_job(timed_job, 'cron', day_of_week='wed', hour=21, minute=30)
sched.start()

# TODO:
# Post on Facebook
# Post on vtw.link
