# This function returns the second biggest number's value and position in a list of strings
# if there are less than two numbers, return None
def secondBiggest(s):
    res = []
    s = enumerate(s)
    for i, x in s:
        if x.isnumeric():
            res.append([int(x), i])
    res.sort(key=lambda x: x[0])
    if len(res) >= 2:
        return res[-2]
    else:
        return None

# Examples
print(secondBiggest(['a', 'b', '1', '4', '5']))
print(secondBiggest(['a', 'b', '10', 'c', '4', '5']))
print(secondBiggest(['a', 'b', '1', 'c']))




