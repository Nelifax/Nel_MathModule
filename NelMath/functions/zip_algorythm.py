__all__ = ['build_fraction','get_continued_fraction_denominators']
from NelMath.objects.math_base.Fraction import Fraction

def build_fraction(denominator_list:list)->'Fraction':
    result = Fraction([0,1])
    for d in denominator_list:
        result.improper_view()
        result = Fraction([1, d + result])
    return result

def get_continued_fraction_denominators(frac:Fraction, max_terms=10):
    """Восстанавливает знаменатели из цепной дроби"""
    denominators = []
    x = frac
    for _ in range(max_terms+1):
        term = x.references['integer part']
        denominators.append(term)
        x = x - term
        if x != 0:
            x = 1 / x
    return denominators
