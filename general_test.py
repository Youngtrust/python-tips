# project_name = 'Mantis_EVT'
# project_array = project_name.split('_')
# print(project_array)
# print(project_array[0])
#
#
# test = "hahah"
#
#
# def check(is_plan):
#     if is_plan:
#         res = test
#         return res
#     return "not plan"
#
#
# print(check(1))

import bisect
import heapq  # get Max and min number
import random
# import objgraph
# import itertools
STATUS = {
    "1": "Passed",
    "2": "Blocked",
    "3": "Untested",
    "4": "Retest",
    "5": "Failed",
    "6": "Skipped",
    "7": "Performance",
    "8": "Queried",
    "9": "Parked",
    "10": "Running",
    "11": "Caution",
    "12": "Not Applicable"
}


def status_mark_check(value):
    if value not in STATUS.values():
        return False
    return True


print(status_mark_check("fail"))
print(status_mark_check("Passed"))


# def index(a, x):
#     i = bisect_left(a, x)
#     if i != len(a) and a[i] == x:
#         return i
#     raise ValueError


alist = [random.randint(0, 100) for i in range(10)]
print(alist)
# [62, 72, 18, 55, 86, 26, 88, 21, 4, 97]

heapq.heapify(alist)  # Get max/min use O(1) time

print(alist)

# [4, 21, 18, 55, 86, 26, 88, 72, 62, 97]

# x = ['a', '1', [2, 3]]
# objgraph.show_refs([x], filename="test.png")

# itertools.islice((calculate_for_value(v) for v in values), 0, 12)
