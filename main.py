def create_dict():
    count = 0
    d = {}
    def cr_dcttwo(s):
        nonlocal count, d
        count +=1
        d[count] = s
        return d
    return cr_dcttwo

