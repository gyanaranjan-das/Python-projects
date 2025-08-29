"""
mini_numpy.py (Phase 1, Step 1)
Starting from scratch: a barebones ndarray implementation.
"""
from typing import List, Tuple, Union

Number = Union[int, float]

def _prod(tup: Tuple[int, ...]) -> int:
    p = 1
    for x in tup:
        p *= x
    return p

class ndarray:
    """Minimal ndarray class.
    Stores:
      - flat data (list)
      - shape (tuple)
      - dtype
    """

    def __init__(self, data: List[Number], shape: Tuple[int, ...], dtype: type = float):
        # flatten input into list of dtype
        self._data: List[Number] = [dtype(x) for x in data]
        self.shape: Tuple[int, ...] = tuple(shape)
        self.dtype = dtype

        if _prod(self.shape) != len(self._data):
            raise ValueError("Data size does not match shape product")

    @property
    def size(self) -> int:
        return len(self._data)

    def tolist(self):
        """Convert flat data back into nested lists matching shape."""
        if len(self.shape) == 1:
            return list(self._data)

        def _unflat(data, shape):
            if len(shape) == 1:
                return data[: shape[0]]
            step = _prod(shape[1:])
            out = []
            for i in range(shape[0]):
                start = i * step
                out.append(_unflat(data[start : start + step], shape[1:]))
            return out

        return _unflat(self._data, self.shape)

    def __repr__(self):
        return f"ndarray(shape={self.shape}, dtype={self.dtype.__name__}, data={self.tolist()})"


# Quick test for Step 1
if __name__ == "__main__":
    a = ndarray([1, 2, 3, 4], shape=(2, 2), dtype=int)
    print(a)
    print("tolist():", a.tolist())