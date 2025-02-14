from NelMath.objects.math_base.Fraction import Fraction
from NelMath.objects.math_base import Rational, Number

__all__ = ['type_test']

def type_test(reportType:str='full', **kwargs):
    test_count = 0
    done_count = 0
    error_count = 0
    wrong_count = 0    
    print('---Begin type changing tests---')
    print('-----Generation tests-----')    
    print('-----From Number to Rational-----')
    tests = [
        [1, f'int to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        [1.3, f'float[with integer part] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        [0.7, f'float[without integer part] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        ['1', f'str[int] to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        ['1.3', f'str[float[with integer part]] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        ['0.7', f'str[float[without integer part]] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        [[1], f'list[int] to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        [[1.3], f'list[float[with integer part]] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        [[0.7], f'list[float[without integer part]] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        [['1'], f'list[str[int]] to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        [['1.3'], f'list[str[float[with integer part]]] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        [['0.7'], f'list[str[float[without integer part]]] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        [(1), f'tuple[int] to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        [(1.3), f'tuple[float[with integer part]] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        [(0.7), f'tuple[float[without integer part]] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        [('1'), f'tuple[str[int]] to Rational through Number (changeType=False)',Rational(1), {'type changing':False}],
        [('1.3'), f'tuple[str[float[with integer part]]] to Rational through Number (changeType=False)',Rational(1.3), {'type changing':False}],
        [('0.7'), f'tuple[str[float[without integer part]]] to Rational through Number (changeType=False)',Rational(0.7), {'type changing':False}],
        ]
    for test in tests:
        try:
            test_count += 1
            a=Number(test[0], test[-1])
            if a==test[-2]:
                done_count+=1
                if reportType=='full':
                    print(f'{test_count}) '+test[1] + f': DONE')
            else:
                wrong_count+=1
                print(f'{test_count}) '+test[1] + f': WRONG\n -->Expected:{test[-2].__repr__()} but get: {a.__repr__()}]\n')
        except Exception as e:
            error_count+=1
            print(f'{test_count}) '+test[1] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
    
    print('-----From Number to Fraction-----')
    tests = [
        [[1, 2], f'list[int, int] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [[1, 2.2], f'list[int, float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [[1.2, 2], f'list[float, int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [[1.4, 2.3], f'list[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [['1', '2'], f'list[str(int), str(int)] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [['1', 2.2], f'list[str(int), float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [['1.2', 2], f'list[str(float), int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [[1, '2.2'], f'list[int, str(float)] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [[1.2, '2'], f'list[float, str(int)] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [['1.4', '2.3'], f'list[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [(1, 2), f'tuple[int, int] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [(1, 2.2), f'tuple[int, float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [(1.2, 2), f'tuple[float, int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [(1.4, 2.3), f'tuple[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [('1', '2'), f'tuple[str(int), str(int)] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [('1', 2.2), f'tuple[str(int), float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [('1.2', 2), f'tuple[str(float), int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [(1, '2.2'), f'tuple[int, str(float)] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [(1.2, '2'), f'tuple[float, str(int)] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [('1.4', '2.3'), f'tuple[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [2.3, f'float to Fraction through Number (changeType=True)',Fraction(2.3), {'type changing':True}],
        ['2.3', f'str[float] to Fraction through Number (changeType=True)',Fraction(2.3), {'type changing':True}],
        ]
    for test in tests:
        try:
            test_count += 1
            a=Number(test[0], test[-1])
            if a==test[-2]:
                done_count+=1
                if reportType=='full':
                    print(f'{test_count}) '+test[1] + f': DONE')
            else:
                wrong_count+=1
                print(f'{test_count}) '+test[1] + f': WRONG\n -->Expected:{test[-2].__repr__()} but get: {a.__repr__()}]\n')
        except Exception as e:
            error_count+=1
            print(f'{test_count}) '+test[1] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
         
    #print('-----From Number to Irrational-----')   
    print('-----From Rational to Fraction-----')
    tests = [
        [[1, 2], f'list[int, int] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [[1, 2.2], f'list[int, float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [[1.2, 2], f'list[float, int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [[1.4, 2.3], f'list[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [['1', '2'], f'list[str(int), str(int)] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [['1', 2.2], f'list[str(int), float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [['1.2', 2], f'list[str(float), int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [[1, '2.2'], f'list[int, str(float)] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [[1.2, '2'], f'list[float, str(int)] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [['1.4', '2.3'], f'list[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [(1, 2), f'tuple[int, int] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [(1, 2.2), f'tuple[int, float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [(1.2, 2), f'tuple[float, int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [(1.4, 2.3), f'tuple[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [('1', '2'), f'tuple[str(int), str(int)] to Fraction through Number (changeType=False)',Fraction([1, 2]), {'type changing':False}],
        [('1', 2.2), f'tuple[str(int), float] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [('1.2', 2), f'tuple[str(float), int] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [(1, '2.2'), f'tuple[int, str(float)] to Fraction through Number (changeType=False)',Fraction([1, 2.2]), {'type changing':False}],
        [(1.2, '2'), f'tuple[float, str(int)] to Fraction through Number (changeType=False)',Fraction([1.2, 2]), {'type changing':False}],
        [('1.4', '2.3'), f'tuple[float, float] to Fraction through Number (changeType=False)',Fraction([1.4, 2.3]), {'type changing':False}],
        [2.3, f'float to Fraction through Number (changeType=True)',Fraction(2.3), {'type changing':True}],
        ['2.3', f'str[float] to Fraction through Number (changeType=True)',Fraction(2.3), {'type changing':True}],
        ]
    for test in tests:
        try:
            test_count += 1
            a=Number(test[0], test[-1])
            if a==test[-2]:
                done_count+=1
                if reportType=='full':
                    print(f'{test_count}) '+test[1] + f': DONE')
            else:
                wrong_count+=1
                print(f'{test_count}) '+test[1] + f': WRONG\n -->Expected:{test[-2].__repr__()} but get: {a.__repr__()}]\n')
        except Exception as e:
            error_count+=1
            print(f'{test_count}) '+test[1] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
         
    print('---------------------------------------------------------\n')
    print(f'End fractions testing with a report-mode:{reportType}\nTest count = {test_count}\nDone tests = {done_count}\nWrongs tests = {wrong_count}\nErrors = {error_count}')
    print('---------------------------------------------------------\n')
    if kwargs!={}:
        kwargs.update({
            'all_tests':kwargs['all_tests']+test_count,
            'done_tests':kwargs['done_tests']+done_count,
            'wrong_tests':kwargs['wrong_tests']+wrong_count,
            'errors':kwargs['errors']+error_count
            })
        return kwargs