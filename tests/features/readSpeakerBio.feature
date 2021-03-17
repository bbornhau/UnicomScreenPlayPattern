
Feature: read speaker bio for the 2021 ADT-March conference
	As a conference participant,
	I want to be able to visit the speaker about page,
	So I can read the speaker bio

	Background:
		Given the user is on the unicomlearning homepage
	@successful
	Scenario: read speaker bio page 
		When the user visits the about page of the speaker called "Bernd Bornhausen" 
		Then the user should be able to read the speaker bio
	
	@failure
	Scenario: read speaker bio page failure
		When the user visits the about page of the speaker called "Thomas Mueller" 
		Then the user should be able to read the speaker bio