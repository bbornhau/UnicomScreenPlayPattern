"""
"""

from screenpy import Actor
from screenpy.actions import Enter, Wait, Pause, Click
from screenpy.pacing import beat
from selenium.webdriver.common.keys import Keys
from screenpy.actions import Open,Pause
from ..user_interface.unicomlearningHomePage import TOPBARNAV_SPEAKERS,ADT_TITLE,URL


class OpenTheHomePage:
	"""
	
	"""

	@staticmethod
	def ofADTMarch() -> "OpenTheHomePage":
		return OpenTheHomePage()
	
	
	@beat("{0} opens the Homepage of ADT March")
	def perform_as(self, the_actor: Actor) -> None:
		"""
		Visit the about page

		Args:
			the_actor: the actor who will perform this task.
		"""
	
		the_actor.attempts_to(
			Open.their_browser_on(URL),
			Wait.for_the(TOPBARNAV_SPEAKERS)
		)
	
