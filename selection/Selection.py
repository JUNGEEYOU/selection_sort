#-*- coding:utf-8 -*-
def find_smallest(item_list):
    """
    리스트 중 가장 작은 수의 인덱스를 리턴
    :param item_list:
    :return:
    """
    small_num = item_list[0]
    small_index = 0

    for i in range(1, len(item_list)):
        if small_num > item_list[i]:
            small_num = item_list[i]
            small_index = i
    return small_index


def selection_sort(item_list):
    """
    선택 정렬 함수
    :param item_list:
    :return: 오름차순 정렬 리턴
    """
    sort_list =list()
    for i in range(len(item_list)):
        small_num = find_smallest(item_list)
        sort_list.append(item_list.pop(small_num))
    return sort_list

my_list = [5, 2, 1, 4, 7, 10]
print (selection_sort(my_list))   # [1, 2, 4, 5, 7, 10]