"""
mini_numpy.py
"""

from typing import List, Tuple, Union

Number = Union[int, float]

def _prod(tup: Tuple[int,...])-> int:
    p = 1
    for x in tup:
        p*=x
    return p

class ndarray:
    """Minimal ndarray class.
    Stores.
    -flat data (list)
    - shape(tuple)
    -dtype
    """
    def __init__(self, data:List[Number], shape:Tuple[int, ...], dtype:type=float):
        
        self.data:
        pass