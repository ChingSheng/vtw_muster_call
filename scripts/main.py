from scripts.auto_g0v_hackmd import G0V_HACK_MD_Script
from scripts.auto_kktix import VTW_KKTIX_Script

hack_md_script = G0V_HACK_MD_Script()
hack_md_url = hack_md_script.run()
vtw_script = VTW_KKTIX_Script(hack_md_url)
kktix_url = vtw_script.run()

print hack_md_url
print kktix_url

# TODO:
    # Post on Facebook
    # Post on Slack
    # Post on vtw.link