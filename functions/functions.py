
class Functions:
    @staticmethod
    def get_list_of_items_numer(item_list):
        list_to_return = []
        for i in range(item_list.count()):
            item = item_list.nth(i).inner_text()
            if len(item) == 0:
                continue
            if "," in item:
                list_to_return.append(int(item.replace(",", "")))
            else:
                list_to_return.append(int(item))
        return list_to_return

    @staticmethod
    def get_list_of_items_string(item_list):
        list_to_return = []
        for i in range(item_list.count()):
            list_to_return.append(item_list.nth(i).inner_text())
        return list_to_return

    @staticmethod
    def sorted_to_max(list_to_sorted):
        return sorted(list_to_sorted)

    @staticmethod
    def sorted_to_min(list_to_sorted):
        return sorted(list_to_sorted, reverse=True)

