from scripts.auto_g0v_hackmd import G0V_HACK_MD_Script
from scripts.auto_kktix import VTW_KKTIX_Script

hackMdScript = G0V_HACK_MD_Script()
hackMdUrl = hackMdScript.run()
vtwScript = VTW_KKTIX_Script(hackMdUrl)
kktixUrl = vtwScript.run()

print hackMdUrl
print kktixUrl

# TODO:
    # Post on Facebook
    # Post on Slack
    # Post on vtw.link