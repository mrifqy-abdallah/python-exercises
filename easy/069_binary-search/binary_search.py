def find(search_list: 'list[int]', value: int) -> int:
    if not search_list:
        raise ValueError("List cannot be empty.")

    if not all(map(lambda x: type(x) is int, search_list)):
        raise ValueError("All input must be integer.")

    if value not in search_list:
        raise ValueError("Searched value must be part of the list's element.")

    return binary_search(sorted(search_list), value)


def binary_search(a_list: list, element: int, start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(a_list)

    mid = (start + end) // 2

    if a_list[mid] == element:
        return mid
    if a_list[mid] > element:
        return binary_search(a_list, element, start, mid-1)
    elif a_list[mid] < element:
        return binary_search(a_list, element, mid+1, end)
