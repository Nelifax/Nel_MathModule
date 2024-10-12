from random import randint
from objects.Number import Number

__all__ = ['number_base_test']
global test_cap
test_cap = 500
def number_base_test(reportType:str='full'):
    test_count = 0
    done_count = 0
    error_count = 0
    wrong_count = 0
    if reportType == 'full':
        print('-----Generation tests-----')
        tests = [
            [2,f'Number generation with int(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '+'], 
            [12,f'Number generation with int(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
            [2147483648,f'Number generation with int(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
            [2147483649,f'Number generation with int(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '+'], 
            [18446744073709551616,f'Number generation with int(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
            [-2,f'Number generation with negative int(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '-'], 
            [-12,f'Number generation with negative int(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '-'], 
            [-2147483648,f'Number generation with negative int(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '-'], 
            [-2147483649,f'Number generation with negative int(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
            [-18446744073709551616,f'Number generation with negative int(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '-'],

            ['2',f'Number generation with str(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '+'], 
            ['12',f'Number generation with str(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
            ['2147483648',f'Number generation with str(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
            ['2147483649',f'Number generation with str(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '+'], 
            ['18446744073709551616',f'Number generation with str(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
            ['-2',f'Number generation with str(only 1 digit negative)', {'integer part': '2', 'float part': '0'}, '2', '-'], 
            ['-12',f'Number generation with str(2 digits negative)', {'integer part': '12', 'float part': '0'}, '2', '-'], 
            ['-2147483648',f'Number generation with str(2^31 negative)', {'integer part': '2147483648', 'float part': '0'}, '2', '-'], 
            ['-2147483649',f'Number generation with str(2^31+1 negative)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
            ['-18446744073709551616',f'Number generation with str(2^64 negative)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '-'], 

            [1.0,f'Number generation with float(only 1 digit point 0)', {'integer part': '1', 'float part': '0'}, '2', '+'], 
            [12.0,f'Number generation with float(2 digits point 0)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
            [2147483648.0,f'Number generation with float(2^31 point 0)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
            [-2147483649.0,f'Number generation with float(2^31+1 point 0)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
            [1.1,f'Number generation with float(only 1 digit point 1 digit)', {'integer part': '1', 'float part': '1'}, '2', '+'], 
            [12.2,f'Number generation with float(2 digits point 1 digit)', {'integer part': '12', 'float part': '2'}, '2', '+'], 
            [2147483648.3,f'Number generation with float(2^31 point 1 digit)', {'integer part': '2147483648', 'float part': '3'}, '2', '+'], 
            [-2147483649.4,f'Number generation with float(2^31+1 point 1 digit)', {'integer part': '2147483649', 'float part': '4'}, '2', '-'], 
            [1.12,f'Number generation with float(only 1 digit point 2 digits)', {'integer part': '1', 'float part': '12'}, '2', '+'], 
            [12.99,f'Number generation with float(2 digits point 2 digits)', {'integer part': '12', 'float part': '99'}, '2', '+'], 
            [2147483648.32,f'Number generation with float(2^31 point 2 digits)', {'integer part': '2147483648', 'float part': '32'}, '2', '+'],  
            [1.1234567891,f'Number generation with float(only 1 digit point 10 digits)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
            [12.1234567891,f'Number generation with float(2 digits point 10 digits)', {'integer part': '12', 'float part': '1234567891'}, '2', '+'], 
            #[2147483648.1234567891,f'Number generation with float(2^31 point 10 digits)', {'integer part': '2147483648', 'float part': '1234567891'}, '2', '+'], 
            #[-2147483649.1234567891,f'Number generation with float(2^31+1 point 10 digits)', {'integer part': '2147483649', 'float part': '1234567891'}, '2', '-'], 
            #[1.1234567891000000000000000,f'Number generation with float(only 1 digit point 10 digits 15 zeros)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
            #[12.1234567891234560000000000,f'Number generation with float(2 digits point 15 digits 10 zeros)', {'integer part': '12', 'float part': '123456789123456'}, '2', '+'], 
            #[2147483648.123456789100000123456789100000,f'Number generation with float(2^31 point 10 digits 5 zeros 5 digits 5 zeros)', {'integer part': '2147483648', 'float part': '1234567891000001234567891'}, '2', '+'], 
            #[-2147483649.0000012345678910000000000,f'Number generation with float(2^31+1 point 5 zeros 10 digits 10 zeros)', {'integer part': '2147483649', 'float part': '000001234567891'}, '2', '-'], 

            ['1.0',f'Number generation with str(only 1 digit point 0)', {'integer part': '1', 'float part': '0'}, '2', '+'], 
            ['12.0',f'Number generation with str(2 digits point 0)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
            ['2147483648.0',f'Number generation with str(2^31 point 0)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
            ['-2147483649.0',f'Number generation with str(2^31+1 point 0)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
            ['18446744073709551616.0',f'Number generation with str(2^64 point 0)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'], 
            ['1.1',f'Number generation with str(only 1 digit point 1 digit)', {'integer part': '1', 'float part': '1'}, '2', '+'], 
            ['12.2',f'Number generation with str(2 digits point 1 digit)', {'integer part': '12', 'float part': '2'}, '2', '+'], 
            ['2147483648.3',f'Number generation with str(2^31 point 1 digit)', {'integer part': '2147483648', 'float part': '3'}, '2', '+'], 
            ['-2147483649.4',f'Number generation with str(2^31+1 point 1 digit)', {'integer part': '2147483649', 'float part': '4'}, '2', '-'], 
            ['18446744073709551616.5',f'Number generation with str(2^64 point 1 digit)', {'integer part': '18446744073709551616', 'float part': '5'}, '2', '+'], 
            ['1.12',f'Number generation with str(only 1 digit point 2 digits)', {'integer part': '1', 'float part': '12'}, '2', '+'], 
            ['12.99',f'Number generation with str(2 digits point 2 digits)', {'integer part': '12', 'float part': '99'}, '2', '+'], 
            ['2147483648.32',f'Number generation with str(2^31 point 2 digits)', {'integer part': '2147483648', 'float part': '32'}, '2', '+'], 
            ['-2147483649.41',f'Number generation with str(2^31+1 point 2 digits)', {'integer part': '2147483649', 'float part': '41'}, '2', '-'], 
            ['18446744073709551616.78',f'Number generation with str(2^64 point 2 digits)', {'integer part': '18446744073709551616', 'float part': '78'}, '2', '+'], 
            ['1.1234567891',f'Number generation with str(only 1 digit point 10 digits)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
            ['12.1234567891',f'Number generation with str(2 digits point 10 digits)', {'integer part': '12', 'float part': '1234567891'}, '2', '+'], 
            ['2147483648.1234567891',f'Number generation with str(2^31 point 10 digits)', {'integer part': '2147483648', 'float part': '1234567891'}, '2', '+'], 
            ['-2147483649.1234567891',f'Number generation with str(2^31+1 point 10 digits)', {'integer part': '2147483649', 'float part': '1234567891'}, '2', '-'], 
            ['18446744073709551616.1234567891',f'Number generation with str(2^64 point 10 digits)', {'integer part': '18446744073709551616', 'float part': '1234567891'}, '2', '+'], 
            ['1.1234567891123456789198765',f'Number generation with str(only 1 digit point 25 digits)', {'integer part': '1', 'float part': '1234567891123456789198765'}, '2', '+'], 
            ['12.1234567891123456789198765',f'Number generation with str(2 digits point 25 digits)', {'integer part': '12', 'float part': '1234567891123456789198765'}, '2', '+'], 
            ['2147483648.1234567891123456789198765',f'Number generation with str(2^31 point 25 digits)', {'integer part': '2147483648', 'float part': '1234567891123456789198765'}, '2', '+'], 
            ['-2147483649.1234567891123456789198765',f'Number generation with str(2^31+1 point 25 digits)', {'integer part': '2147483649', 'float part': '1234567891123456789198765'}, '2', '-'], 
            ['18446744073709551616.1234567891123456789198765',f'Number generation with str(2^64 point 25 digits)', {'integer part': '18446744073709551616', 'float part': '1234567891123456789198765'}, '2', '+'], 
            ['1.1234567891000000000000000',f'Number generation with str(only 1 digit point 10 digits 15 zeros)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
            ['12.1234567891234560000000000',f'Number generation with str(2 digits point 15 digits 10 zeros)', {'integer part': '12', 'float part': '123456789123456'}, '2', '+'], 
            ['2147483648.123456789100000123456789100000',f'Number generation with str(2^31 point 10 digits 5 zeros 5 digits 5 zeros)', {'integer part': '2147483648', 'float part': '1234567891000001234567891'}, '2', '+'], 
            ['-2147483649.0000012345678910000000000',f'Number generation with str(2^31+1 point 5 zeros 10 digits 10 zeros)', {'integer part': '2147483649', 'float part': '000001234567891'}, '2', '-'], 
            ['18446744073709551616.0000000000000000000000000',f'Number generation with str(2^64 point 25 zeros)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
        ]
        for test in tests:
            try:
                test_count += 1
                a = Number(test[0])
                test_str = str(test[0]).rstrip('0').lstrip('0')
                if test_str[-1]=='.':
                        test_str=test_str[:-1]
                if a.references == test[2] and a.get_sign() == test[4] and a.value == test_str:
                    print(f'{test_count}) '+test[1] + f': DONE')
                    done_count+=1
                else:
                    print(f'{test_count}) '+test[1] + f'generator:{test[0]}-> WRONG at:')
                    if a.references != test[2]:
                        print(f'-->references: expected {test[2]} but get {a.references}')
                    if a.get_sign() != test[4]:
                        print(f"-->sign: expected {test[4]} but get {a.get_sign()}")
                    if a.value !=  test_str:
                        print(f"-->value: expected {test_str} but get {a.value}")
                    wrong_count+=1
            except Exception as e:
                error_count+=1
                print(f'{test_count}) '+test[1] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
            else:
                pass
                #done_count+=1
                #print(f'{test_count}) '+test[1] + f': DONE')
        print('-----Precision tests-----')
        tests=['add(+)', 'sub(-)', 'lt(<)', 'gt(>)', 'le(<=)', 'ge(>=)', 'eq(==)', 'mul(*)', 'div(/)', 'pow(^)']
        for test in tests:            
            print(f'---Precision test block[{test}]. Start {2*test_cap}[{test_cap}int/{test_cap}float] tests---')
            match test:
                case 'add(+)':
                    for i in range(0,test_cap):
                        try:
                            test_count+=1
                            a=randint(-99999999, 99999999)
                            b=randint(-99999999, 99999999)
                            if (Number(a)+Number(b)).value == str(a+b):
                                print(f'{test_count})({a})+({b}): DONE')
                                done_count+=1
                            else:
                                wrong_count+=1
                                print(f'{test_count})({a})+({b}): WRONG\nExpected [{a+b}] but get [{(Number(a)+Number(b)).value}]')
                        except Exception as e:
                            error_count+=1
                            print(f'{test_count}: ERROR\n   ||\n   |└--->generator:{test}[{a},{b}]\n   └--->{e.__repr__()}]\n')
                    for i in range(0,test_cap):
                        try:
                            test_count+=1
                            a=randint(-99999999, 99999999)+float('0.'+str(randint(0, 99999)))
                            b=randint(-99999999, 99999999)+float('0.'+str(randint(0, 99999)))
                            if (Number(a)+Number(b)).value == str(a+b):
                                print(f'{test_count})({a})+({b}): DONE')
                                done_count+=1
                            else:
                                wrong_count+=1
                                print(f'{test_count})({a})+({b}): WRONG\nExpected [{a+b}] but get [{(Number(a)+Number(b)).value}]')
                        except Exception as e:
                            error_count+=1
                            print(f'{test_count}: ERROR\n   ||\n   |└--->generator:{test}[{a},{b}]\n   └--->{e.__repr__()}]\n')
                case 'sub(-)':
                    for i in range(0,test_cap):
                        try:
                            test_count+=1
                            a=randint(-99999999, 99999999)
                            b=randint(-99999999, 99999999)
                            if (Number(a)-Number(b)).value == str(a-b):
                                print(f'{test_count})({a})-({b}): DONE')
                                done_count+=1
                            else:
                                wrong_count+=1
                                print(f'{test_count})({a})-({b}): WRONG\nExpected [{a-b}.str] but get [{(Number(a)-Number(b)).value}]')
                        except Exception as e:
                            error_count+=1
                            print(f'{test_count}: ERROR\n   ||\n   |└--->generator:{test}[{a},{b}]\n   └--->{e.__repr__()}]\n')
                    for i in range(0,test_cap):
                        try:
                            test_count+=1
                            a=randint(-99999999, 99999999)+float('0.'+str(randint(0, 99999)))
                            b=randint(-99999999, 99999999)+float('0.'+str(randint(0, 99999)))
                            if (Number(a)-Number(b)).value == str(a-b):
                                print(f'{test_count})({a})-({b}): DONE')
                                done_count+=1
                            else:
                                wrong_count+=1
                                print(f'{test_count})({a})-({b}): WRONG\nExpected [{a-b}] but get [{(Number(a)-Number(b)).value}]')
                        except Exception as e:
                            error_count+=1
                            print(f'{test_count}: ERROR\n   ||\n   |└--->generator:{test}[{a},{b}]\n   └--->{e.__repr__()}]\n')
            
        print('---------------------------------------------------------\n')
        print(f'End Number testing with a report-mode:{reportType}\nTest count = {test_count}\nDone tests = {done_count}\nWrong tests = {wrong_count}\nErrors = {error_count}')
        print('---------------------------------------------------------\n')