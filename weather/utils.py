def removeDuplicates(lst):
    return [t for t in (set(tuple(i) for i in lst))]