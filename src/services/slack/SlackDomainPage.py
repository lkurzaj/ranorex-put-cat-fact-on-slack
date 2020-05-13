from robot.api.deco import library, keyword
from lib.ranorex.src.RanorexLibrary import RanorexLibrary


@library
class SlackDomainPage:

    def __init__(self):
        self.ranorex = RanorexLibrary()
        self.domain_name = "slack.com"
        self.__base_xpath = "/dom[@domain='%s']" % self.domain_name

    @keyword("Run Slack Web Client")
    def open_slack_app(self):
        self.ranorex.start_browser(self.domain_name, "Chrome", "--new-window")

    @keyword("Click Launch Slack Button")
    def click_launch_slack_button(self):
        self.ranorex.click(self.__base_xpath + "//button[#'nav_work_btn']")

    @keyword("Open Workspace")
    def open_workspace(self, workspace_name):
        self.ranorex.click(self.__base_xpath + "//nav[#'workspace_dd']/?/?/ul//span[@innertext='%s']" % workspace_name)


