
# range(start, stop, step), manipulating index
# len(listobj)

# bubble sort O(n**2)
# selection sort O(n**2)


def bubble_sort(alist):
                            # 算头不算尾
    for j in range(len(alist)-1, 0, -1): 
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        

def selection_sort(alist):
    # range从零开始
    # i, j 当成index ！！！
    for j in range(len(alist) - 1, 0, -1):
        max_index = 0
        for i in range(1, j+1, 1):
            if alist[i] > alist[max_index]:
                max_index = i 
        # Stability
        if max_index != j:
            alist[j], alist[max_index] = alist[max_index], alist[j]
            
  def selection_sort(alist):
    n = len(alist) 
    for j in range(n):
        min_id = j
        for i in range(j+1, n):
            if alist[i] < alist[min_id]:
                min_id = i
        # stability
        if min_index != j:
          alist[j], alist[min_id] = alist[min_id], alist[j]
 



alist = [54,226,92,17,77,31,44,55,20]
print(selection_sort(alist))

li = [54,26,93,17,77,31,44,55,20]
selection_sort(li)
print(li)
