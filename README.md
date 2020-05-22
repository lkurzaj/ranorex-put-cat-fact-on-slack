# EXAMPLE PROJECT FOR ROBOT WITH RANOREX INTEGRATION

## Prerequisites
- Python 3.7
- PyCharm
- ranorexnet library

## Run Tests

Install dependencies using command:
```commandline
cd $ranorex-put-cat-fact-on-slack-root
python3 -m pip install -r requirements.txt
```

To run example test execute command:
```commandline
cd $ranorex-put-cat-fact-on-slack-root
python3 -m robot ./test/newsletter/PutFactAboutCatOnSlackChannel.robot
```