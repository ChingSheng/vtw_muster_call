from scripts.auto_g0v_hackmd import G0V_HACK_MD_Script
from scripts.auto_kktix import VTW_KKTIX_Script

hackMdScript = G0V_HACK_MD_Script()
url = hackMdScript.run()
vtwScript = VTW_KKTIX_Script(url)
vtwScript.run()


