"""
"""

from screenpy import Actor
from screenpy.actions import Enter, Wait, Pause, Click
from screenpy.pacing import beat
from selenium.webdriver.common.keys import Keys

from ..user_interface.unicomlearningHomePage import TOPBARNAV_SPEAKERS,LINK_TO_SPEAKER_WITH_NAME


class VisitTheAboutPage:
	"""
	
	"""

	@staticmethod
	def ofTheSpeakerCalled(name: str) -> "VisitTheAboutPage":
		"""
		Supply speaker's name

		Args:
			name : string
		"""
		return VisitTheAboutPage(name)
	
	
	@beat("{0} visits the about page of speaker called '{name}'")
	def perform_as(self, the_actor: Actor) -> None:
		"""
		Visit the about page

		Args:
			the_actor: the actor who will perform this task.
		"""
		# speakerLink = pytest.varDriver.find_element_by_xpath('//*[@id="menu-main-menu-1"]/li[5]')
		# pytest.varDriver.execute_script("arguments[0].click();", speakerLink)

		the_actor.attempts_to(
			#Pause.for_(20000).milliseconds_because("The page needs to finish loading"),	
			Click.on_the(TOPBARNAV_SPEAKERS),
			Click.on_the(LINK_TO_SPEAKER_WITH_NAME(self.name))
			# Pause.for_(20000).milliseconds_because("The page needs to finish loading"),	
		)
	
		
		
	def __init__(self, name):
		self.name = name
