__all__ = ["LinearCode"]

from NelMath.objects.linear_algebra.Matrix import Matrix

class LinearCode():
    def __init__(self, n, k, field):
        self.n=n
        self.k=k
        self.field=field
        self.C