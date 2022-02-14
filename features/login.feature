Feature: Safaricom Taleo Net Login
    Scenario Outline: Login to Safaricom Taleo Net with My Valid Credentials
        Given I launch chrome browser
        When I open safaricomtaleonet homepage
        And I click on sign in
        Then I should be taken to the login page
        When I enter my username "<username>" and password "<password>"
        And I click on login button
        Then I should be taken to my dashboard

        Examples:
            | username | password |
            | "yourusername" | "yourpassword" |
