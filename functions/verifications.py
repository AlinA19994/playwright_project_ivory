
class Verifications:

    @staticmethod
    def verify_equals(actual, expected):
        assert actual, expected

    @staticmethod
    def compare_lists(first_list, second_list):
        if len(first_list) != len(second_list):
            return False
        assert first_list == second_list


