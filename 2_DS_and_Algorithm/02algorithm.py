'''二分查找:O(logn)'''
def binary_search(a_list:'ordered list',keyword):
    start = 0
    end = len(a_list) - 1
    while start <= end:
        mid = (start + end)//2
        if keyword == a_list[mid]:
            return mid
        elif keyword > a_list[mid]:
            start = mid +1
        else:
            end = mid - 1
    return None

'''快排,分而治之的典范:O(nlogn)'''
def quick_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less = [i for i in a_list[1:] if i < pivot]
        greater = [i for i in a_list[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    

if __name__ == '__main__':
    import random
    #print(binary_search(list(range(10)),0))
    a_list = random.sample(range(10),10)
    print(a_list)
    print(quick_sort(a_list))

            

        