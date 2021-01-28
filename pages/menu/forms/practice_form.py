from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class FormsPracticeFormArea(BasePage):

    def __init__(self, driver):
        super(FormsPracticeFormArea, self).__init__(driver)

    practice_form_path = "/automation-practice-form"
    name_label_loc = (By.ID, 'userName-label')
    name_fname_loc = (By.CSS_SELECTOR, '#firstName')
    name_lname_loc = (By.CSS_SELECTOR, '#lastName')
    email_label_loc = (By.CSS_SELECTOR, '#userEmail-label')
    email_loc = (By.CSS_SELECTOR, '#userEmail')
    gender_label_loc = (By.CSS_SELECTOR, '.col-md-3.col-sm-12')
    gender_male_loc = (By.XPATH, '//*/div[@id="genterWrapper"]/div[2]/div[1]/label')
    gender_female_loc = (By.XPATH, '//*/div[@id="genterWrapper"]/div[2]/div[2]/label')
    gender_other_loc = (By.XPATH, '//*/div[@id="genterWrapper"]/div[2]/div[3]/label')
    mobile_number_label_loc = (By.CSS_SELECTOR, '#userNumber-label')
    mobile_number_loc = (By.CSS_SELECTOR, '#userNumber')
    dob_label_loc = (By.CSS_SELECTOR, '#dateOfBirth-label')
    dob_loc = (By.CSS_SELECTOR, '#dateOfBirthInput')
    subjects_label_loc = (By.CSS_SELECTOR, '#subjects-label')
    subject_loc = (By.CSS_SELECTOR, '.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css-1hwfws3')
    hobbies_label_loc = (By.XPATH, '//*/div[@id="hobbiesWrapper"]/div[1]/label')
    hobbies_sports_loc = (By.XPATH, '//*/div[@id="hobbiesWrapper"]/div[2]/div[1]/label')
    hobbies_reading_loc = (By.XPATH, '//*/div[@id="hobbiesWrapper"]/div[2]/div[2]/label')
    hobbies_music_loc = (By.XPATH, '//*/div[@id="hobbiesWrapper"]/div[2]/div[3]/label')
    picture_label_loc = (By.XPATH, '//*/form[@id="userForm"]/div[8]/div[1]')
    select_picture_label_loc = (By.CSS_SELECTOR, '.form-file-label')
    choose_file_loc = (By.CSS_SELECTOR, '#uploadPicture')
    current_address_label_loc = (By.CSS_SELECTOR, '#currentAddress-label')
    current_address_loc = (By.XPATH, '//*/div[@id="currentAddress-wrapper"]/div[2]')
    state_city_label_loc = (By.ID, 'stateCity-label')
    state_loc = (By.XPATH, '//*/div[@id="stateCity-wrapper"]/div[2]/div/div/div[2]/div')
    city_loc = (By.XPATH, '//*/div[@id="stateCity-wrapper"]/div[3]')
    submit_loc = (By.ID, "submit")

    def open_practice_form_url(self):
        self.open_url(self.practice_form_path)

    def validate_page_load(self):
        assert self.is_displayed(self.name_label_loc, timeout=15) and \
           self.is_displayed(self.name_fname_loc, timeout=15) and \
           self.is_displayed(self.name_lname_loc, timeout=15) and \
           self.is_displayed(self.email_label_loc, timeout=15) and \
           self.is_displayed(self.email_loc, timeout=15) and \
           self.is_displayed(self.gender_label_loc, timeout=15) and \
           self.is_displayed(self.gender_male_loc, timeout=15) and \
           self.is_displayed(self.gender_female_loc, timeout=15) and \
           self.is_displayed(self.gender_other_loc, timeout=15) and \
           self.is_displayed(self.mobile_number_label_loc, timeout=15) and \
           self.is_displayed(self.mobile_number_loc, timeout=15) and \
           self.is_displayed(self.dob_label_loc, timeout=15) and \
           self.is_displayed(self.dob_loc, timeout=15) and \
           self.is_displayed(self.subjects_label_loc, timeout=15) and \
           self.is_displayed(self.subject_loc, timeout=15) and \
           self.is_displayed(self.hobbies_label_loc, timeout=15) and \
           self.is_displayed(self.hobbies_sports_loc, timeout=15) and \
           self.is_displayed(self.hobbies_reading_loc, timeout=15) and \
           self.is_displayed(self.hobbies_music_loc, timeout=15) and \
           self.is_displayed(self.picture_label_loc, timeout=15) and \
           self.is_displayed(self.select_picture_label_loc, timeout=15) and \
           self.is_displayed(self.choose_file_loc, timeout=15) and \
           self.is_displayed(self.current_address_label_loc, timeout=15) and \
           self.is_displayed(self.current_address_loc, timeout=15) and \
           self.is_displayed(self.state_city_label_loc, timeout=15) and \
           self.is_displayed(self.state_loc, timeout=15) and \
           self.is_displayed(self.city_loc, timeout=15) and \
           self.is_displayed(self.submit_loc, timeout=15)
