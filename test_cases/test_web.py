import pytest

from workflows.web_workflows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_01_verify_categories_options(self):
        WebFlows.categories_list_expect_to_have_text()
        WebFlows.search_item_small_letter()
        WebFlows.verify_filter_by_categories()

    def test_02_filter_case_sensitive_and_insensitive(self):
        WebFlows.verify_convention_write()

    def test_03_function_test_filter(self):
        WebFlows.verify_filter_to_height()
        WebFlows.verify_filter_to_lower()

    def test_04_verify_X_and_Y_positions(self):
        WebFlows.verify_coordinates_table_view()
        WebFlows.verify_coordinates_list_view()





