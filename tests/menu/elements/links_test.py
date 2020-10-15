from pages.menu.elements.links import ElementsLinksArea
import pytest


class TestElementsLinksArea:

    def test_page_load(self, driver):
        links_area = ElementsLinksArea(driver)
        links_area.open_links_page()
        assert links_area.validate_page_load()

    def test_select_home_link(self, driver):
        links_area = ElementsLinksArea(driver)
        links_area.open_links_page()
        links_area.select_home_link()
        assert links_area.validate_select_home_link()

    def test_select_homenouoh_link(self, driver):
        links_area = ElementsLinksArea(driver)
        links_area.open_links_page()
        links_area.select_homenouoh_link()
        assert links_area.validate_select_home_link()

    def test_select_created_link(self, driver):
        links_area = ElementsLinksArea(driver)
        links_area.open_links_page()
        links_area.select_created_link()
        assert links_area.validate_select_created_link()


