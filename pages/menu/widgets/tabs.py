from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementsTabsArea(BasePage):

    tabs_url = "https://demoqa.com/tabs"
    what_tab_loc = (By.XPATH, "//*/a[@id='demo-tab-what']")
    origin_tab_loc = (By.XPATH, "//*/a[@id='demo-tab-origin']")
    use_tab_loc = (By.XPATH, "//*/a[@id='demo-tab-use']")

    what_text_loc = (By.XPATH, "//*/div[@id='demo-tabpane-what']/p[@class='mt-3']")
    what_text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

    origin_text_loc = (By.XPATH, "//*/div[@id='demo-tabpane-origin']/p[@class='mt-3']")
    origin_text = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'

    use_text_loc = (By.XPATH, "//*/div[@id='demo-tabpane-use']/p[@class='mt-3']")
    use_text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

    def __init__(self, driver):
        super(ElementsTabsArea, self).__init__(driver)

    def open_tabs_page(self):
        self.driver.get(self.tabs_url)

    def validate_page_load(self):
        if self.is_displayed(self.what_tab_loc, 15) and \
           self.is_displayed(self.origin_tab_loc, 15) and \
           self.is_displayed(self.use_tab_loc, 15):
                return True
        return False
    
    def select_what_tab(self):
        if self.is_displayed(self.what_tab_loc, 15):
            self.click(self.what_tab_loc)

    def validate_what_tab(self):
        if self.is_text_displayed(self.what_text_loc, self.what_text):
            return True
        return False

    def select_origin_tab(self):
        if self.is_displayed(self.origin_tab_loc, 15):
            self.click(self.origin_tab_loc)

    def validate_origin_tab(self):
        if self.is_text_displayed(self.origin_text_loc, self.origin_text):
            return True
        return False

    def select_use_tab(self):
        if self.is_displayed(self.use_tab_loc, 15):
            self.click(self.use_tab_loc)
            
    def validate_use_tab(self):
        if self.is_text_displayed(self.use_text_loc, self.use_text):
            return True
        return False
