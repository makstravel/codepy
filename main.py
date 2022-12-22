# This is study Python.
def get_lists(x):
    v_min = min(x)
    v_max = max(x)
    v_sum = sum(x)
    print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')

get_lists(list(map(int, input().split())))



