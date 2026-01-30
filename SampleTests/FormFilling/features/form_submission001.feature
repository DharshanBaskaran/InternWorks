Feature: Training form submission
    Scenario: user fills the form and successfully submits
        Given user launches the training form successfully
        When user fills all required details
        And user views the pdf
        Then form should be submitted and print action should be triggered


