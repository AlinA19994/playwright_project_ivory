from playwright.sync_api import Page, expect

from functions.functions import Functions
from utilities.common_ops import get_data


class SearchItemPage:

    def __init__(self, page: Page):
        self.page = page
        self.filter_by_categories = self.page.locator('div.row > div.col-md-auto.col-12.pr-2.pl-2.sinunLabelnewLabel'
                                                      '.d-flex > '
                                                      'label.sinunLabelnew.custom-control.custom-checkbox.hoverorange'
                                                      '.m-0 > span.sinunTitle')

        self.search_result_items_text = self.page.locator('//*[@class= "col-md-12 col-12 title_product_catalog mb-md-1 '
                                                     'main-text-area"]')
        self.search_result_items_table_view = self.page.locator('[class = "col-md-12 col-12 p-0 pt-2  image-wrapper '
                                                                'no-line-height"]')
        self.search_result_text = self.page.locator('//div[contains(text(), "Samsung")]')
        self.search_price_of_items = self.page.locator('span[class= "price "]')
        self.filter_dropdown = self.page.locator('[id= "dropdownMenuLink"]')
        self.filter_to_low = self.page.locator('//a[@data-order-by= "priceLow"]')
        self.filter_to_height = self.page.locator('//a[@data-order-by= "priceHigh"]')
        self.filter_to_newest = self.page.locator('//a[@data-order-by= "newprod"]')
        self.list_view_items = self.page.locator('[class="col-md-2 col-4"]')
        self.list_view = self.page.locator('[class = "change_mode_views_zz_controls fa fa-th-list mobile-sort-container-links-icon"]')







    def get_filter_by_categories_list(self):
        return Functions.get_list_of_items_string(self.filter_by_categories)


    def expect_filter_by_categories_list(self):
        option_list = get_data('list_of_search_categories')
        for i in range(self.filter_by_categories.count()):
            expect(self.filter_by_categories.nth(i)).to_have_text(option_list[i].strip())

    def get_result_text(self):
        return Functions.get_list_of_items_string(self.search_result_text)

    def get_text_from_items(self):
        return Functions.get_list_of_items_string(self.search_result_items_text)

    def get_price_list(self):
        return Functions.get_list_of_items_numer(self.search_price_of_items)

    def filter_from_height_to_lower(self):
        self.filter_dropdown.click()
        self.filter_to_height.click()

    def filter_from_lower_to_height(self):
        self.filter_dropdown.click()
        self.filter_to_low.click()

    def select_to_newest_filter(self):
        self.filter_dropdown.click()
        self.filter_to_newest.click()

    def select_list_view(self):
        self.list_view.click()

    def return_items(self):
        return self.list_view_items

    def return_items_table_view(self):
        return self.search_result_items_table_view



