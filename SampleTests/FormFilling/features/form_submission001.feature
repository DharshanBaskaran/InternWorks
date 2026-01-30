@regression
Feature: Training form submission
    @smoke @form
    Scenario: user fills the form and successfully submits
        Given user launches the training form successfully
        When user fills all required details
        And user views the pdf
        Then form should be submitted and print action should be triggered



    @form
    Scenario: user fills the form and successfully submits 2
        Given user launches the training form successfully 2
        When user fills all required details 2
        And user views the pdf 2
        Then form should be submitted and print action should be triggered 2


