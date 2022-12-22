# This is study Python.
def info_kwargs(**kwargs):
    [print(f'{k} = {v}') for k, v in sorted(kwargs.items())]

