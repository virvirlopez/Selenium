Feature: As an app user
    Make a tweet

    Background:
        Given: I am in the twitter front page
        When: I log in with the user vickiviki2 and the password maylopez
        Then: When I click the login button I log into twitter

    Scenario: Publish a tweet
        Given I write the tweet IAmUsingSelenium
        When I click on the Post button a tweet is created
