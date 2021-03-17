from typing import Generator
import pytest

# issue here: same names imported from screenpy and pytest-BDD.
# Will change all annotations , see below for act and scene from screenpy
# into upper case
import pytest_bdd
from pytest_bdd import given as Given
from pytest_bdd import when as When
from pytest_bdd import then as Then
from pytest_bdd import scenarios, parsers, scenario
from screenpy.abilities import BrowseTheWeb
from screenpy.questions import Number,Text,Element
from screenpy import Actor, AnActor
from screenpy import given
from screenpy import  then
from screenpy import when
from screenpy import and_
from screenpy.resolutions import (
    ContainsTheText,
    ContainTheText,
    DoesNot,
    IsEqualTo,
    ReadsExactly,
	IsVisible,
	IsNot,
	IsEmpty
)
import time
from functools import partial

### here go our tasks and userinterface defintions as needed
from ..tasks.visitTheAboutPage import VisitTheAboutPage
from ..tasks.openTheHomePage import OpenTheHomePage
from ..user_interface.unicomlearningSpeakerBio import BIO_PARAGRAPH

	


@pytest.fixture(scope="function", name="TheUser")
def fixture_actor(browserFixture) -> Generator:
	"""Create the actor for our tests!"""	
	the_actor = Actor.named("The User").who_can(BrowseTheWeb.using(pytest.varDriver))
	yield the_actor
	the_actor.exit_stage_left()
	
scenario = partial(pytest_bdd.scenario, '../features/readSpeakerBio.feature')
@scenario('read speaker bio page')
def test_readSpeakerBio():
    pass
	
@scenario('read speaker bio page failure')
def test_failure():
	pass

@Given('the user is on the unicomlearning homepage')
def openUnicomlearningPage(TheUser: AnActor) -> None:
	"""Open Unicomlearning homepage in browser and verify it is open"""
	
	when(TheUser).was_able_to(
		OpenTheHomePage.ofADTMarch()
		)
		
@When(parsers.cfparse('the user visits the about page of the speaker called "{speakerName}"'))
def visitAboutPage(TheUser: AnActor,speakerName) -> None:
	when(TheUser).was_able_to(
	VisitTheAboutPage.ofTheSpeakerCalled(speakerName)
	)
	
	
@Then('the user should be able to read the speaker bio')
def verifyBio(TheUser: AnActor) -> None:
	bioParagraph=(
	"Bernd Bornhausen is the Director of Quality Assurance at Logibec, "
	"a leader in the development and implementation of IT ecosystems in healthcare. "
	"He has almost 25 years experience in information technology, his entire professional life, "
	"and he dedicated the last 15+ years to Software Quality Assurance. "
	"Working for international companies in three different countries, Germany, Switzerland and now Canada, "
	"has allowed him to gather a vast experience that he is eager to share with the testing community. "
	"Bernd was speaker at several test conferences and has been nominated judge for the North American Software Testing Awards in 2019 and 2020 "
	"and now for the India Testing Awards 2020."
	)
	then(TheUser).should_see_the((Text.of_the(BIO_PARAGRAPH), ReadsExactly(bioParagraph)))
	







