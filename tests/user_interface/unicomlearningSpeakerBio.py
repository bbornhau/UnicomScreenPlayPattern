"""
Locators for the Unicom speaker page.
"""


from screenpy import Target

BIO_PARAGRAPH = Target.the("Speakers BIO").located_by(
    '//p[1]'  
)

