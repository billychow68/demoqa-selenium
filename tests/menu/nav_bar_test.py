from pages.menu.nav_bar import MenuNavBar
import time


class TestMenuNavBar:

    def test_elements_menu(self, homepage):
        homepage.open_home_page()
        homepage.select_elements_option()
        menu_nav_bar = MenuNavBar(homepage.get_driver())
        # toggle expand/collapse menu
        menu_nav_bar.toggle_elements_menu()
        menu_nav_bar.toggle_elements_menu()
        # todo: assert
        menu_nav_bar.select_elements_textbox_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_checkbox_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_radiobutton_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_webtables_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_buttons_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_links_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_broken_links_images_menu_item()
        # todo: assert
        menu_nav_bar.scroll_to_bottom_of_page()
        menu_nav_bar.select_elements_upload_download_menu_item()
        # todo: assert
        menu_nav_bar.select_elements_dynamic_properties_menu_item()
        # todo: assert

    def test_forms_menu(self, homepage):
        homepage.open_home_page()
        homepage.select_forms_option()
        menu_nav_bar = MenuNavBar(homepage.get_driver())
        # toggle expand/collapse menu
        menu_nav_bar.toggle_forms_menu()
        menu_nav_bar.toggle_forms_menu()
        # todo: assert
        menu_nav_bar.select_forms_practice_form_menu_item()

    #pytest.mark.parametrize("name","email","cur_addr","perm_addr", ["Billy","test@demoqa.com","123 Main Street","456 First Street"])
    # def test_submit_textbox_form_valid(self, homepage):
    #     homepage.open_home_page()
    #     homepage.click_elements_option()
    #     menu_nav_bar = MenuNavBar(homepage.get_driver())
    #     menu_nav_bar.select_elements_textbox_menu_item()
    #     textbox_area = ElementsTextboxArea(homepage.get_driver())
    #     textbox_area.textbox_submit_form("Billy","test@demoqa.com","123 Main Street","456 First Street")
    #     assert textbox_area.validate_form_submitted_data()
