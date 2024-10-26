from NelMath.objects.Error import *
from NelMath.objects.Fraction import Fraction

__all__ = ['fractions_base_test']

def fractions_base_test(reportType:str='full'):
    test_count = 0
    done_count = 0
    error_count = 0
    if reportType == 'full':
        print('-----Generation tests-----')
        tests = [
            ['2',f'Fraction generation with string(only 1 number)'], 
            ['2.0',f'Fraction generation with string(number with point = 0)'], 
            ['2.3',f'Fraction generation with string(only number with point != 0)'], 
            ['2/5',f'Fraction generation with string(two numbers with \'/\' without points)'], 
            ['2.0/3',f'Fraction generation with string(two numbers with \'/\' with zero-point on numerator)'], 
            ['2/3.0',f'Fraction generation with string(two numbers with \'/\' with zero-point on denomenator)'], 
            ['2.3/3.0',f'Fraction generation with string(two numbers with \'/\' with point on numerator and zero-point on denomenator)'], 
            ['2.0/3.1',f'Fraction generation with string(two numbers with \'/\' with zero-point on numerator and point on denomenator)'], 
            ['2.0/3.0',f'Fraction generation with string(two numbers with \'/\' with two zero-points both numerator and denomenator)'], 
            ['2.1/3.1',f'Fraction generation with string(two numbers with \'/\' with two points both numerator and denomenator)'], 
            [3,f'Fraction generation with int'], 
            [2.0,f'Fraction generation with float(1 zero-point 1 point at all)'], 
            [2.1,f'Fraction generation with float(0 zero-point 1 point at all)'], 
            [2.00,f'Fraction generation with float(2 zero-point 2 point at all)'], 
            [2.10,f'Fraction generation with float(1 zero-point 2 point at all)'], 
            [2.25,f'Fraction generation with float(0 zero-point 2 point at all)'], 
            [12.000,f'Fraction generation with float(3 zero-point 3 point at all)'], 
            [12.100,f'Fraction generation with float(2 zero-point 3 point at all)'], 
            [12.110,f'Fraction generation with float(1 zero-point 3 point at all)'], 
            [12.115,f'Fraction generation with float(0 zero-point 3 point at all)'], 

            [[2],f'Fraction generation with list(only 1 element)'], 
            [[2.0],f'Fraction generation with list(1 element with point = 0)'], 
            [[2.3],f'Fraction generation with list(1 element with point != 0)'], 
            [[2,5],f'Fraction generation with list(two elements without points)'], 
            [[2.0,3],f'Fraction generation with list(two elements with zero-point on numerator)'], 
            [[2,3.0],f'Fraction generation with list(two elements with zero-point on denomenator)'], 
            [[2.3,3.0],f'Fraction generation with list(two elements with point on numerator and zero-point on denomenator)'], 
            [[2.0,3.1],f'Fraction generation with list(two elements with zero-point on numerator and point on denomenator)'], 
            [[2.0,3.0],f'Fraction generation with list(two elements with two zero-points both numerator and denomenator)'], 
            [[2.1,3.1],f'Fraction generation with list(two elements with two points both numerator and denomenator)'],

            
            [[Fraction('3/2'),2],f'Fraction generation with list(fraction on numerator and int on denomenator)'], 
            [[Fraction('3/2'), 2.2],f'Fraction generation with list(fraction on numerator and float on denomenator)'], 
            [[2,Fraction('3/2')],f'Fraction generation with list(int on numerator fraction on denomenator)'], 
            [[2.3,Fraction('3/2')],f'Fraction generation with list(float on numerator fraction on denomenator)'], 
            [[Fraction('3/2'),Fraction('3/5')],f'Fraction generation with list(fractions both numerator and denomenator)'],
            ]
        for test in tests:
            try:
                test_count += 1
                Fraction(test[0])
            except Exception as e:
                error_count+=1
                print(f'{test_count}) '+test[1] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
            else:
                done_count+=1
                print(f'{test_count}) '+test[1] + f': DONE')
        print('---------------------------------------------------------\n')
        print(f'End fractions testing with a report-mode:{reportType}\nTest count = {test_count}\nDone tests = {done_count}\nErrors = {error_count}')
        print('---------------------------------------------------------\n')