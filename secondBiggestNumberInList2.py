# This function returns the second biggest number's value and position in a list of strings
# if there are less than two numbers, return None
# uses a heap for O(n*log(2)) time
import heapq
def secondBiggest(s):
    res = []
    s = enumerate(s)
    for i, x in s:
        if x.isnumeric():
            heapq.heappush(res, [int(x), i])
        if len(res) > 2:
            heapq.heappop(res)
    if len(res) >= 2:
        return res[0]
    else:
        return None
# Examples
print(secondBiggest(['a', 'b', '1', '4', '5']))
print(secondBiggest(['a', 'b', '10', 'c', '4', '5']))
print(secondBiggest(['a', 'b', '1', 'c']))




