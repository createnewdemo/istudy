# -*- coding: gbk -*-
d = {'a': 1, 'b': 2, 'c': 3}
# ����key
# for key in d:
# #     print(key)
# ����value
# for value in d.values():
#     print(value)
# for k,v in d.items():
#     print(k,v)
from collections.abc import Iterable

isinstance('abc', Iterable)
isinstance(123, Iterable)
