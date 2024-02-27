# def merge_lists(list1, list2, list3, list4):
#     merged_list = list1 + list2 + list3 + list4
#     return merged_list
#
# def sort_list(lst, reverse=False):
#     return sorted(lst, reverse=reverse)
#
# def linear_search(lst, value):
#     for index, element in enumerate(lst):
#         if element == value:
#             return index
#     return -1
#
# list1 = [3, 6, 1, 9]
# list2 = [5, 2, 8, 4]
# list3 = [7, 10, 12, 11]
# list4 = [15, 13, 16, 14]
#
# merged_list = merge_lists(list1, list2, list3, list4)
# print("Объединенный список:", merged_list)
#
# choice = input("Введите 'asc' для сортировки по возрастанию или 'desc для сортировки по убыванию: ")
# if choice == 'asc':
#     sorted_list = sort_list(merged_list)
# elif choice == 'desc':
#     sorted_list = sort_list(merged_list, reverse=True)
# else:
#     print("Некорректный ввод для сортировки")
#
# print("Отсортированный список:", sorted_list)
#
# search_value = int(input("Введите значение для поиска"))
# index = linear_search(sorted_list, search_value)
# if index != -1:
#     print(f"Значение {search_value} найдено на позиции {index}")
# else:
#     print(f'Значение {search_value} не найдено в списке')


# 2


# def merge_unique_lists(list1, list2, list3, list4):
#     unique_elements = []
#
#     for element in list1:
#         if element not in list2 and element not in list3 and element not in list4:
#             unique_elements.append(element)
#
#     for element in list2:
#         if element not in list1 and element not in list3 and element not in list4:
#             unique_elements.append(element)
#
#     for element in list3:
#         if element not in list1 and element not in list2 and element not in list4:
#             unique_elements.append(element)
#
#     for element in list4:
#         if element not in list1 and element not in list2 and element not in list3:
#             unique_elements.append(element)
#
#     return unique_elements
#
#
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return - 1
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# list3 = [5, 6, 7, 8, 9]
# list4 = [7, 8, 9, 10, 11]
#
# unique_list = merge_unique_lists(list1, list2, list3, list4)
# sorted_unique_list = sorted(unique_list)
#
# print("Уникальные элементы, объединенные из всех списков:", sorted_unique_list)
#
# search_value = int(input("Введите значение для бинарного поиска:"))
# result_index = binary_search(sorted_unique_list, search_value)
#
# if result_index != -1:
#     print(f"Значение {search_value} найдено на позиции {result_index}")
# else:
#     print(f"Значение {search_value} не найдено в списке")
#
