import time
from playwright.sync_api import expect
from functions.functions import Functions
from utilities import manage_page as page
from utilities.common_ops import get_data
from functions.verifications import Verifications

path = '../report'


class WebFlows:
    @staticmethod
    def search_item_small_letter():
        page.home_page.search_item("samsung")

    @staticmethod
    def verify_filter_by_categories():
        time.sleep(2)
        actual = page.search_item_page.get_filter_by_categories_list()
        Verifications.verify_equals(actual, get_data('list_of_search_categories'))

    @staticmethod
    def verify_convention_write():
        # Small letter
        page.home_page.search_item("samsung")
        time.sleep(2)
        list_include_search_name = page.search_item_page.get_result_text()
        items_found = page.search_item_page.get_text_from_items()
        Verifications.verify_equals(items_found, list_include_search_name)
        # Camel Case
        page.home_page.clear_search()
        page.home_page.search_item("SamSunG")
        time.sleep(2)
        items_found = page.search_item_page.get_text_from_items()
        Verifications.verify_equals(items_found, list_include_search_name)
        # BIG LETTER
        page.home_page.clear_search()
        page.home_page.search_item("SAMSUNG")
        time.sleep(3)
        items_found = page.search_item_page.get_text_from_items()
        Verifications.verify_equals(items_found, list_include_search_name)

    @staticmethod
    def verify_filter_to_height():
        page.home_page.search_item('headphones')
        time.sleep(1)
        page.search_item_page.filter_from_lower_to_height()
        sorted_list = Functions.sorted_to_max(page.search_item_page.get_price_list())
        list_without_sorted = page.search_item_page.get_price_list()
        Verifications.compare_lists(sorted_list, list_without_sorted)

    @staticmethod
    def verify_filter_to_lower():
        page.home_page.search_item('headphones')
        time.sleep(1)
        page.search_item_page.filter_from_height_to_lower()
        sorted_list = Functions.sorted_to_min(page.search_item_page.get_price_list())
        list_without_sorted = page.search_item_page.get_price_list()
        Verifications.compare_lists(sorted_list, list_without_sorted)

    @staticmethod
    def verify_coordinates_list_view():
        page.home_page.search_item('play station')
        time.sleep(1)
        page.search_item_page.select_list_view()
        items = page.search_item_page.return_items()
        data = []
        time.sleep(1)
        for i in range(items.count()):
            item = items.nth(i).bounding_box()
            data.append(item)
        x_point = data[0]['x']
        if not all(x['x'] == x_point for x in data):
            raise AssertionError("Not all elements have the same x-coordinate.")
        print("All elements have the same x-coordinate:", x_point)

    @staticmethod
    def verify_coordinates_table_view():
        page.home_page.search_item('play station')
        time.sleep(1)
        items = page.search_item_page.return_items_table_view()
        data = []
        for i in range(items.count()):
            item = items.nth(i).bounding_box()
            data.append(item)
        for i in range(0, len(data) - 1, 6):
            start = i
            end = i + 6
            y_point = data[i]['y']
            if not all(data[y]['y'] == y_point for y in range(start, end)):
                raise AssertionError("Not all elements have the same y-coordinate.", {y_point})

    @staticmethod
    def categories_list_expect_to_have_text():
        expect(page.home_page.return_all_list_menu()).to_have_text(
            ['מחשבים נייחים ומסכי מחשב', 'מחשבים ניידים ואביזרים', 'סמארטפונים ואביזרים', 'טאבלטים, אייפדים ואביזרים',
             'שעונים', 'מוצרי גיימינג', 'מבצעים ומציאון', 'טלוויזיות, מקרנים וסטרימרים', 'אוזניות, רמקולים ושמע',
             'מדפסות, ראשי דיו ומגרסות', 'תקשורת ומוצרי רשת', 'חומרה למחשב ותוכנות', 'קונסולות, משחקים ואביזרים',
             'מקלדות ועכברים', 'כבלים, מתאמים ומפצלים', 'אחסון נתונים', 'תאורה, בית חכם ואל פסק',
             'מוצרי חשמל קטנים למטבח', 'מוצרי חשמל לבית', 'ריהוט וכלי עבודה', 'בשמים, טיפוח, תספורת ופארם',
             'מצלמות צילום ואבטחה', 'ספורט, טיולים ופנאי', 'קניה לפי מותג']
            )
