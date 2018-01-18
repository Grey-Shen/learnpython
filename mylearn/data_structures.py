## list
## 当使用 sorted 排序是并不会改变原有的 list 而是会
# 生成一个新的 list
## attaction
## 使用 list 作为 stack 时是合理的，但作为 queue 使用

# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow ，
# because all of the other elements have to be shifted by one.
# 可以使用 from collections import deque
