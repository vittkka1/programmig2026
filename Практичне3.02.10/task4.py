def find_longest(*words):
    longest=" "
    for w in words:
        if len(w)>len(longest):
            longest=w
    return longest