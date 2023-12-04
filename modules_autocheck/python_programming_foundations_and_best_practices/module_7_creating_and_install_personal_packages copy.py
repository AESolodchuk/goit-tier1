def all_sub_lists(data):
    sublists = [[]]
    for start in range(len(data)):
        for end in range(start + 1, len(data) + 1):
            print(end)
            sublists.append(data[start:end])
    sublists.sort()
    return sublists


print(all_sub_lists([4, 6, 1, 3]))
