*** Settings ***
Documentation   A test suite for publishing new fact about cats into Slack channel
#Library     src/services/news/CatFactsService.py
Library     src/services/slack/SlackWebClient.py
Library     src/services/slack/SlackDomainPage.py
Library     lib/ranorex/src/RanorexLibrary.py      C:\\Program Files (x86)\\Ranorex\\Studio\\Bin

*** Variables ***
${base_url}  https://cat-fact.herokuapp.com


*** Test Cases ***
Put random fact about cat to Nice Project Slack's channel
    Get a random cat fact
    SlackDomainPage.Run Slack Web Client
    SlackDomainPage.Click Launch Slack Button
    SlackDomainPage.Open Workspace   NiceProject
    SlackWebClient.Select Channel   rotary-ranorex-playground
    SlackWebClient.Write Post       ${cat fact}
    Send Post

*** Keywords ***
Get a random cat fact
    ${resp}=  Evaluate  json.loads(urllib2.urlopen('${base_url}/facts/random').read())  modules=urllib2,json
    log  ${resp}
    log  ${resp['text']}
    set suite variable  ${cat fact}  ${resp['text']}

Send Post
    key_sequence   /dom[@domain='app.slack.com']//div[@role='main']//div[@class='ql-editor']  {Return}