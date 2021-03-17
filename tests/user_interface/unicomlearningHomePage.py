"""
Locators for the Unicom home  page.
"""


from screenpy import Target
URL="https://www.unicomlearning.com/2021/ADT-March/"

TOPBARNAV_SPEAKERS = Target.the("Top Navigation Speaker Link").located_by(
    '//*[@id="menu-main-menu-1"]/li[5]'  
)

ADT_TITLE=Target.the("ADT Homepage Title").located_by('//*[@id="rev_slider_1_1"]/ul/li/div[3]/div/div')

def LINK_TO_SPEAKER_WITH_NAME(speakerName)->Target:
	return Target.the('Link to Sepaker Pager with Name '+speakerName).located_by(
	'//a[contains(translate(.,"abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"),"'+speakerName.upper()+'")]'
	)