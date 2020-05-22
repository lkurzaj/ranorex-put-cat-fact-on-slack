from robot.api.deco import library, keyword
from ranorexlibrarynet.RanorexLibrary import RanorexProvider

@library
class SlackWebClient:

    def __init__(self):
        self.ranorex = RanorexProvider("C:\\Program Files (x86)\\Ranorex\\Studio\\Bin")
        self.__base_xpath = "/dom[@domain='app.slack.com']"
        self.__channel_link_xpath = self.__base_xpath + "//span[@class='p-channel_sidebar__name' and @innertext='%s']"
        self.__message_textbox_xpath = self.__base_xpath + "//div[@role='main']//div[@class='ql-editor ql-blank']"

    @keyword("Select Channel")
    def select_channel(self, channel_name):
        self.ranorex.click(self.__channel_link_xpath % channel_name)
        #self.ranorex.wait_for(self.__message_textbox_xpath)

    @keyword("Write Post")
    def set_message_into_channel_chat(self, message):
        self.ranorex.key_sequence(self.__message_textbox_xpath, message)

if __name__ == "__main__":
    pass
    #x = SlackWebClient().select_channel()
    #print(x)
