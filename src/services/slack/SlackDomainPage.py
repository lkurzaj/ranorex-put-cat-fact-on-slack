from robot.api.deco import library, keyword
from ranorexlibrarynet.RanorexLibrary import RanorexProvider

@library
class SlackDomainPage:

    def __init__(self):
        self.ranorex = RanorexProvider("C:\\Program Files (x86)\\Ranorex\\Studio\\Bin")
        self.domain_name = "slack.com"
        self.__base_xpath = "/dom[@domain='%s']" % self.domain_name

    @keyword("Run Slack Web Client")
    def open_slack_app(self):
        self.ranorex.start_browser(self.domain_name, "chrome")

    @keyword("Click Launch Slack Button")
    def click_launch_slack_button(self):
        self.ranorex.click(self.__base_xpath + "//button[#'nav_work_btn']")

    @keyword("Open Workspace")
    def open_workspace(self, workspace_name):
        self.ranorex.click(self.__base_xpath + "//nav[#'workspace_dd']/?/?/ul//span[@innertext='%s']" % workspace_name)


