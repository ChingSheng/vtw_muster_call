from scripts.auto_g0v_hackmd import G0vHackMdScript
from scripts.auto_kktix import VtwKKTixScript

hack_md_script = G0vHackMdScript()
hack_md_url = hack_md_script.run()
vtw_script = VtwKKTixScript(hack_md_url)
kktix_url = vtw_script.run()

print hack_md_url
print kktix_url

# TODO:
    # Post on Facebook
    # Post on Slack
    # Post on vtw.link