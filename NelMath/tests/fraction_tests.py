from NelMath.objects.errors.Error import *
from NelMath.objects.math_constructions.Fraction import Fraction

__all__ = ['fractions_base_test']

def fractions_base_test(reportType:str='full', **kwargs):
    test_count = 0
    done_count = 0
    error_count = 0
    wrong_count = 0
    print('-----Generation tests-----')
    tests = [
        ['2',f'Fraction generation with string(only 1 number)'], 
        ['0',f'Fraction generation with string(only 1 number=0)'], 
        ['2.0',f'Fraction generation with string(number with point = 0)'], 
        ['2.3',f'Fraction generation with string(only number with point != 0)'],  
        ['2/5',f'Fraction generation with string(two numbers with \'/\' without points)'], 
        ['0/5',f'Fraction generation with string(two numbers with \'/\' without points leading 0)'], 
        ['-2/5',f'Fraction generation with string(two numbers with \'/\' without points with leading -)'], 
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
            if reportType=='full':
                print(f'{test_count}) '+test[1] + f': DONE')
    print('-----Precision tests-----')
    tests = [
        #ADD tests (different notations)
        ['2/3','3/2','+','2/3+3/2 both string notation', '13/6'],
        [['2/3'],'3/2','+','2/3+3/2 between list[1](str) and str notation', '13/6'],
        [['2', '3'],'3/2','+','2/3+3/2 between list[2](str, str) and str notation', '13/6'],
        [[2, '3'],'3/2','+','2/3+3/2 between list[2](int, str) and str notation', '13/6'],
        [['2', 3],'3/2','+','2/3+3/2 between list[2](str, int) and str notation', '13/6'],
        [[2, 3],'3/2','+','2/3+3/2 between list[2](int, int) and str notation', '13/6'],
        [[2.0,'3'],'3/2','+','2/3+3/2 between list[2](float, str) and str notation', '13/6'],
        [['2',3.0],'3/2','+','2/3+3/2 between list[2](str, float) and str notation', '13/6'],
        [[2.0,3.0],'3/2','+','2/3+3/2 between list[2](float, float) and str notation', '13/6'],
        [[2.0, 3],'3/2','+','2/3+3/2 between list[2](float, int) and str notation', '13/6'],
        [[2, 3.0],'3/2','+','2/3+3/2 between list[2](int, float) and str notation', '13/6'],
        [[2, 3.0],'0/2','+','2/3+0/2 between list[2](int, float) and str notation', '2/3'],
        [[0, 3.0],'3/2','+','0/3+3/2 between list[2](int, float) and str notation', '3/2'],
        #ADD tests (main precision part)
        [[1, 15], [1, 15],'+','Fraction+Fraction test (same denominators, result int_part=0, non_siplified)', '2/15'],
        [[2, 15], [7, 15],'+','Fraction+Fraction test (same denominators, result int_part=0, siplified)', '3/5'],
        [[1, 7], [10, 7],'+','Fraction+Fraction test (same denominators, result int_part>0, non_siplified)', '(1+4/7)'],
        [[11, 12], [5, 12],'+','Fraction+Fraction test (same denominators, result int_part>0, siplified)', '(1+1/3)'],
        [[11, 12], [13, 12],'+','Fraction+Fraction test (same denominators, result numerator==0)', '2'],
        [[1, 11], [2, 7],'+','Fraction+Fraction test (diff denominators, result int_part=0, non_siplified)', '29/77'],
        [[2, 12], [7, 15],'+','Fraction+Fraction test (diff denominators, result int_part=0, siplified)', '19/30'],
        [[7, 5], [9, 2],'+','Fraction+Fraction test (diff denominators, result int_part>0, non_siplified)', '(5+9/10)'],
        [[12, 5], [3, 4],'+','Fraction+Fraction test (diff denominators, result int_part>0, siplified)', '(3+3/20)'],
        [[3, 5], [14, 10],'+','Fraction+Fraction test (diff denominators, result numerator==0)', '2'],

        [[-1, 15], [2, 15],'+','(-Fraction)+Fraction test (same denominators, result int_part=0, non_siplified)', '1/15'],
        [[2, -15], [7, 15],'+','(-Fraction)+(-Fraction) test (same denominators, result int_part=0, siplified)', '1/3'],
        [[11, 7], [-10, 7],'+','Fraction+(-Fraction) test (same denominators, result int_part>0, non_siplified)', '1/7'],
        [[11, 12], [5, -12],'+','Fraction+(-Fraction) test (same denominators, result int_part>0, siplified)', '1/2'],
        [[-11, 12], [-13, 12],'+','(-Fraction)+(-Fraction) test (same denominators, result numerator==0)', '-2'],
        [[1, -11], [2, -7],'+','(-Fraction)+Fraction test (diff denominators, result int_part=0, non_siplified)', '-29/77'],
        [[-2, -12], [7, 15],'+','Fraction+Fraction test (diff denominators, result int_part=0, siplified)', '19/30'],
        [[7, 5], [-9, -2],'+','Fraction+Fraction test (diff denominators, result int_part>0, non_siplified)', '(5+9/10)'],
        [[-12, -5], [-3, -4],'+','Fraction+Fraction test (diff denominators, result int_part>0, siplified)', '(3+3/20)'],
        [[-3, 5], [14, -10],'+','(-Fraction)+(-Fraction) test (diff denominators, result numerator==0)', '-2'],
        #SUB tests
        [[7, 15], [6, 15],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result int_part=0, non_siplified)', '1/15'],
        [[4, 15], [11, 15],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result int_part=0, non_siplified)', '-7/15'],
        [[11, 15], [2, 15],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result int_part=0, siplified)', '3/5'],
        [[8, 15], [14, 15],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result int_part=0, siplified)', '-2/5'],
        [[12, 5], [4, 5],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result int_part>0, non_siplified)', '(1+3/5)'],
        [[3, 7], [33, 7],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result int_part>0, non_siplified)', '-(4+2/7)'],
        [[23, 4], [5, 4],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result int_part>0, siplified)', '(4+1/2)'],
        [[7, 12], [33, 12],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result int_part>0, siplified)', '-(2+1/6)'],
        [[23, 11], [12, 11],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result numerator==0)', '1'],
        [[13, 5], [23, 5],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result numerator==0)', '-2'],

        [[-7, 15], [6, 15],'-','Fraction(-a)-Fraction(b) test (a>b same denominators, result int_part=0, non_siplified)', '-13/15'],
        [[4, -15], [10, 15],'-','Fraction(-a)-Fraction(b) test (a<b same denominators, result int_part=0, non_siplified)', '-14/15'],
        [[10, 15], [-2, 15],'-','Fraction(a)-Fraction(-b) test (a>b same denominators, result int_part=0, siplified)', '4/5'],
        [[7, 15], [3, -15],'-','Fraction(a)-Fraction(-b) test (a<b same denominators, result int_part=0, siplified)', '2/3'],
        [[-12, 5], [-4, 5],'-','Fraction(-a)-Fraction(-b) test (a>b same denominators, result int_part>0, non_siplified)', '-(1+3/5)'],
        [[3, -7], [33, -7],'-','Fraction(-a)-Fraction(-b) test (a<b same denominators, result int_part>0, non_siplified)', '(4+2/7)'],
        [[-23, -4], [5, 4],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result int_part>0, siplified)', '(4+1/2)'],
        [[7, 12], [-33, -12],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result int_part>0, siplified)', '-(2+1/6)'],
        [[-23, -11], [-12, -11],'-','Fraction(a)-Fraction(b) test (a>b same denominators, result numerator==0)', '1'],
        [[-13, 5], [23, -5],'-','Fraction(a)-Fraction(b) test (a<b same denominators, result numerator==0)', '2'],
        #MUL tests
        [[2, 3], [4, 5],'*','Fraction*Fraction test', '8/15'],
        [[-2, 3], [4, 5],'*','Fraction*Fraction test', '-8/15'],
        [[2, 3], [-4, 5],'*','Fraction*Fraction test', '-8/15'],
        [[2, -3], [4, -5],'*','Fraction*Fraction test', '8/15'],
        [[7, 9], [12, 14],'*','Fraction*Fraction test', '2/3'],
        ['(1+2/3)', '(3+2/5)','*','Fraction*Fraction test', '17/3'],
        [[5,3], [12/10],'*','Fraction*Fraction test', '2'],
        #DIV tests
        [[2, 5], [2, 3],'/','Fraction/Fraction test', '3/5'],
        [[2, -5], [2, 3],'/','Fraction/Fraction test', '-3/5'],
        [[2, 5], [2, -3],'/','Fraction/Fraction test', '-3/5'],
        [[-2, 5], [-2, 3],'/','Fraction/Fraction test', '3/5'],
        [[3, 40], [5, 20],'/','Fraction/Fraction test', '3/10'],
        ['(5+2/3)', '(3+2/5)','/','Fraction/Fraction test', '(1+2/3)'],
        [[12, 4], [12, 8],'/','Fraction/Fraction test', '2'],
        ]
    last_testing=''
    for test in tests:
        test_count+=1
        testing = test[2]
        a=Fraction(test[0])
        b=Fraction(test[1])
        if last_testing != testing:
            print(f'---Test [{test[2]}] operation---')
            last_testing = testing
        match test[2]:
            case '+':                    
                try:
                    c=a+b                        
                except Exception as e:
                    error_count+=1
                    print(f' ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '-':                    
                try:
                    c=a-b                        
                except Exception as e:
                    error_count+=1
                    print(f' ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '*':                    
                try:
                    c=a*b                        
                except Exception as e:
                    error_count+=1
                    print(f' ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '/':                    
                try:
                    c=a/b                        
                except Exception as e:
                    error_count+=1
                    print(f' ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
        if c==test[-1]:
            if reportType=='full':
                print(f'{test_count}) '+test[3]+':DONE')
            done_count+=1
        else:
            print(f'{test_count}) '+test[3]+':WRONG')
            wrong_count+=1
            print(f' ->generator: {test[0]}{test[2]}{test[1]}')
            print(f'   ->expected: {test[-1]}; but get: {c}')
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