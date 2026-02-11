__all__ = ["Random_code"]

from NelMath.objects.applied_algebra.Codes import LinearCode

class Random_code(LinearCode):
    def __init__(self, n, k, Field=2):
        