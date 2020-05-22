*** Settings ***
Documentation   A test suite for publishing new fact about cats into Slack channel
Library     src/services/news/CatFactsService.py
Library     src/services/slack/SlackWebClient.py
Library     src/services/slack/SlackDomainPage.py

*** Variables ***
${base_url}  https://cat-fact.herokuapp.com


*** Test Cases ***
Put random fact about cat to Nice Project Slack's channel
    ${catfact}=    CatFactsService.Get Random Fact
    SlackDomainPage.Run Slack Web Client
    SlackDomainPage.Click Launch Slack Button
    SlackDomainPage.Open Workspace   NiceProject
    SlackWebClient.Select Channel   rotary-ranorex-playground
    SlackWebClient.Write Post       ${catfact}