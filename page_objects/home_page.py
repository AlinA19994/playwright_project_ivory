from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.search_fields = self.page.locator('input[id="qSearch"]')
        self.search_button = self.page.locator('[id = "searchButton"]')
        self.list_menu = self.page.locator('ul.spriteLine.homepage-menu-list > li.menunav > span.tlt> span.actual-text')


    def search_item(self, item):
        self.search_fields.fill(item)
        self.search_button.click()


    def clear_search(self):
        self.search_fields.fill("")

    def return_all_list_menu(self):
        return self.list_menu



