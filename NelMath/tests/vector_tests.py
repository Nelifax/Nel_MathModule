from random import randint
from NelMath.objects.math_base.Rational import Rational

__all__ = ['number_base_test']
global test_cap
test_cap = 500
def number_base_test(reportType:str='full', **kwargs): 
    print('---Begin number testing---')
    test_count = 0
    done_count = 0
    error_count = 0
    wrong_count = 0
    print('-----Generation tests-----')
    tests = [
        [2,f'Rational generation with int(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '+'], 
        [12,f'Rational generation with int(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
        [2147483648,f'Rational generation with int(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
        [2147483649,f'Rational generation with int(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '+'], 
        [18446744073709551616,f'Rational generation with int(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
        [-2,f'Rational generation with negative int(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '-'], 
        [-12,f'Rational generation with negative int(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '-'], 
        [-2147483648,f'Rational generation with negative int(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '-'], 
        [-2147483649,f'Rational generation with negative int(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
        [-18446744073709551616,f'Rational generation with negative int(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '-'],

        ['2',f'Rational generation with str(only 1 digit)', {'integer part': '2', 'float part': '0'}, '2', '+'], 
        ['12',f'Rational generation with str(2 digits)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
        ['2147483648',f'Rational generation with str(2^31)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
        ['2147483649',f'Rational generation with str(2^31+1)', {'integer part': '2147483649', 'float part': '0'}, '2', '+'], 
        ['18446744073709551616',f'Rational generation with str(2^64)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
        ['-2',f'Rational generation with str(only 1 digit negative)', {'integer part': '2', 'float part': '0'}, '2', '-'], 
        ['-12',f'Rational generation with str(2 digits negative)', {'integer part': '12', 'float part': '0'}, '2', '-'], 
        ['-2147483648',f'Rational generation with str(2^31 negative)', {'integer part': '2147483648', 'float part': '0'}, '2', '-'], 
        ['-2147483649',f'Rational generation with str(2^31+1 negative)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
        ['-18446744073709551616',f'Rational generation with str(2^64 negative)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '-'], 

        [1.0,f'Rational generation with float(only 1 digit point 0)', {'integer part': '1', 'float part': '0'}, '2', '+'], 
        [12.0,f'Rational generation with float(2 digits point 0)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
        [2147483648.0,f'Rational generation with float(2^31 point 0)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
        [-2147483649.0,f'Rational generation with float(2^31+1 point 0)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
        [1.1,f'Rational generation with float(only 1 digit point 1 digit)', {'integer part': '1', 'float part': '1'}, '2', '+'], 
        [12.2,f'Rational generation with float(2 digits point 1 digit)', {'integer part': '12', 'float part': '2'}, '2', '+'], 
        [2147483648.3,f'Rational generation with float(2^31 point 1 digit)', {'integer part': '2147483648', 'float part': '3'}, '2', '+'], 
        [-2147483649.4,f'Rational generation with float(2^31+1 point 1 digit)', {'integer part': '2147483649', 'float part': '4'}, '2', '-'], 
        [1.12,f'Rational generation with float(only 1 digit point 2 digits)', {'integer part': '1', 'float part': '12'}, '2', '+'], 
        [12.99,f'Rational generation with float(2 digits point 2 digits)', {'integer part': '12', 'float part': '99'}, '2', '+'], 
        [2147483648.32,f'Rational generation with float(2^31 point 2 digits)', {'integer part': '2147483648', 'float part': '32'}, '2', '+'],  
        [1.1234567891,f'Rational generation with float(only 1 digit point 10 digits)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
        [12.1234567891,f'Rational generation with float(2 digits point 10 digits)', {'integer part': '12', 'float part': '1234567891'}, '2', '+'], 
        #[2147483648.1234567891,f'Rational generation with float(2^31 point 10 digits)', {'integer part': '2147483648', 'float part': '1234567891'}, '2', '+'], 
        #[-2147483649.1234567891,f'Rational generation with float(2^31+1 point 10 digits)', {'integer part': '2147483649', 'float part': '1234567891'}, '2', '-'], 
        #[1.1234567891000000000000000,f'Rational generation with float(only 1 digit point 10 digits 15 zeros)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
        #[12.1234567891234560000000000,f'Rational generation with float(2 digits point 15 digits 10 zeros)', {'integer part': '12', 'float part': '123456789123456'}, '2', '+'], 
        #[2147483648.123456789100000123456789100000,f'Rational generation with float(2^31 point 10 digits 5 zeros 5 digits 5 zeros)', {'integer part': '2147483648', 'float part': '1234567891000001234567891'}, '2', '+'], 
        #[-2147483649.0000012345678910000000000,f'Rational generation with float(2^31+1 point 5 zeros 10 digits 10 zeros)', {'integer part': '2147483649', 'float part': '000001234567891'}, '2', '-'], 

        ['1.0',f'Rational generation with str(only 1 digit point 0)', {'integer part': '1', 'float part': '0'}, '2', '+'], 
        ['12.0',f'Rational generation with str(2 digits point 0)', {'integer part': '12', 'float part': '0'}, '2', '+'], 
        ['2147483648.0',f'Rational generation with str(2^31 point 0)', {'integer part': '2147483648', 'float part': '0'}, '2', '+'], 
        ['-2147483649.0',f'Rational generation with str(2^31+1 point 0)', {'integer part': '2147483649', 'float part': '0'}, '2', '-'], 
        ['18446744073709551616.0',f'Rational generation with str(2^64 point 0)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'], 
        ['1.1',f'Rational generation with str(only 1 digit point 1 digit)', {'integer part': '1', 'float part': '1'}, '2', '+'], 
        ['12.2',f'Rational generation with str(2 digits point 1 digit)', {'integer part': '12', 'float part': '2'}, '2', '+'], 
        ['2147483648.3',f'Rational generation with str(2^31 point 1 digit)', {'integer part': '2147483648', 'float part': '3'}, '2', '+'], 
        ['-2147483649.4',f'Rational generation with str(2^31+1 point 1 digit)', {'integer part': '2147483649', 'float part': '4'}, '2', '-'], 
        ['18446744073709551616.5',f'Rational generation with str(2^64 point 1 digit)', {'integer part': '18446744073709551616', 'float part': '5'}, '2', '+'], 
        ['1.12',f'Rational generation with str(only 1 digit point 2 digits)', {'integer part': '1', 'float part': '12'}, '2', '+'], 
        ['12.99',f'Rational generation with str(2 digits point 2 digits)', {'integer part': '12', 'float part': '99'}, '2', '+'], 
        ['2147483648.32',f'Rational generation with str(2^31 point 2 digits)', {'integer part': '2147483648', 'float part': '32'}, '2', '+'], 
        ['-2147483649.41',f'Rational generation with str(2^31+1 point 2 digits)', {'integer part': '2147483649', 'float part': '41'}, '2', '-'], 
        ['18446744073709551616.78',f'Rational generation with str(2^64 point 2 digits)', {'integer part': '18446744073709551616', 'float part': '78'}, '2', '+'], 
        ['1.1234567891',f'Rational generation with str(only 1 digit point 10 digits)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
        ['12.1234567891',f'Rational generation with str(2 digits point 10 digits)', {'integer part': '12', 'float part': '1234567891'}, '2', '+'], 
        ['2147483648.1234567891',f'Rational generation with str(2^31 point 10 digits)', {'integer part': '2147483648', 'float part': '1234567891'}, '2', '+'], 
        ['-2147483649.1234567891',f'Rational generation with str(2^31+1 point 10 digits)', {'integer part': '2147483649', 'float part': '1234567891'}, '2', '-'], 
        ['18446744073709551616.1234567891',f'Rational generation with str(2^64 point 10 digits)', {'integer part': '18446744073709551616', 'float part': '1234567891'}, '2', '+'], 
        ['1.1234567891123456789198765',f'Rational generation with str(only 1 digit point 25 digits)', {'integer part': '1', 'float part': '1234567891123456789198765'}, '2', '+'], 
        ['12.1234567891123456789198765',f'Rational generation with str(2 digits point 25 digits)', {'integer part': '12', 'float part': '1234567891123456789198765'}, '2', '+'], 
        ['2147483648.1234567891123456789198765',f'Rational generation with str(2^31 point 25 digits)', {'integer part': '2147483648', 'float part': '1234567891123456789198765'}, '2', '+'], 
        ['-2147483649.1234567891123456789198765',f'Rational generation with str(2^31+1 point 25 digits)', {'integer part': '2147483649', 'float part': '1234567891123456789198765'}, '2', '-'], 
        ['18446744073709551616.1234567891123456789198765',f'Rational generation with str(2^64 point 25 digits)', {'integer part': '18446744073709551616', 'float part': '1234567891123456789198765'}, '2', '+'], 
        ['1.1234567891000000000000000',f'Rational generation with str(only 1 digit point 10 digits 15 zeros)', {'integer part': '1', 'float part': '1234567891'}, '2', '+'], 
        ['12.1234567891234560000000000',f'Rational generation with str(2 digits point 15 digits 10 zeros)', {'integer part': '12', 'float part': '123456789123456'}, '2', '+'], 
        ['2147483648.123456789100000123456789100000',f'Rational generation with str(2^31 point 10 digits 5 zeros 5 digits 5 zeros)', {'integer part': '2147483648', 'float part': '1234567891000001234567891'}, '2', '+'], 
        ['-2147483649.0000012345678910000000000',f'Rational generation with str(2^31+1 point 5 zeros 10 digits 10 zeros)', {'integer part': '2147483649', 'float part': '000001234567891'}, '2', '-'], 
        ['18446744073709551616.0000000000000000000000000',f'Rational generation with str(2^64 point 25 zeros)', {'integer part': '18446744073709551616', 'float part': '0'}, '2', '+'],
    ]
    for test in tests:
        try:
            test_count += 1
            a = Rational(test[0])
            test_str = str(test[0]).rstrip('0').lstrip('0')
            if test_str[-1]=='.':
                    test_str=test_str[:-1]
            if a.references == test[2] and a.sign == test[4] and a.value == test_str:
                if reportType=='full':
                    print(f'{test_count}) '+test[1] + f': DONE')
                done_count+=1
            else:
                print(f'{test_count}) '+test[1] + f'generator:{test[0]}-> WRONG at:')
                if a.references != test[2]:
                    print(f'-->references: expected {test[2]} but get {a.references}')
                if a.sign != test[4]:
                    print(f"-->sign: expected {test[4]} but get {a.sign}")
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
    tests = [
        #ADD tests
        ['0', '1', '+', f'0+1 in number notation', 1],
        ['1', '0', '+',f'1+0 in number notation', 1],
        ['10', '0.1', '+', f'10+0.1 in number notation', 10.1],
        ['1010', '1010', '+', f'1010+1010 in number notation', 2020],
        ['1234.4321', '9876.6789', '+', f'1234.4321+9876.6789 in number notation', 11111.111],

        [0, '1', '+', f'int(0)+1 in number notation', 1],
        [1, '0', '+', f'int(1)+0 in number notation', 1],
        [10, '0.1', '+', f'int(10)+0.1 in number notation', 10.1],
        [1010, '1010', '+', f'int(1010)+1010 in number notation', 2020],
        [1234.4321, '9876.6789', '+', f'float(1234.4321)+9876.6789 in number notation', 11111.111],
            
        ['0', 1, '+', f'0+int(1) in number notation', 1],
        ['1', 0, '+', f'1+int(0) in number notation', 1],
        ['10', 0.1, '+', f'10+float(0.1) in number notation', 10.1],
        ['1010', 1010, '+', f'1010+int(1010) in number notation', 2020],
        ['1234.4321', 9876.6789, '+', f'1234.4321+float(9876.6789) in number notation', 11111.111],

        ['0', -1, '+', f'0+int(-1) in number notation', -1],
        ['-1', 0, '+', f'-1+int(0) in number notation', -1],
        ['-10', -0.1, '+', f'-10+float(-0.1) in number notation', -10.1],
        ['1010', -1010, '+', f'-1010+int(-1010) in number notation', 0],
        ['-1234.4321', -9876.6789, '+', f'-1234.4321+float(-9876.6789) in number notation', -11111.111],
                        
        ['10', '10', '+', f'numb(summ test): ', 20],
        ['10', '-10', '+', f'numb(summ test): ', 0],
        ['-10', '10', '+', f'numb(summ test): ', 0],
        ['-10', '-10', '+', f'numb(summ test): ', -20],
                        
        ['10', '10.1', '+', f'numb(summ test): ', 20.1],
        ['1.1', '-10.1', '+', f'numb(summ test): ', -9],
        ['-1.1', '10.1', '+', f'numb(summ test): ', 9],
        ['-10.11', '-10.99', '+', f'numb(summ test): ', -21.1],
                        
        ['10.001', '10.009', '+', f'numb(summ test): ', 20.01],
        ['10.1001', '-1.0002', '+', f'numb(summ test): ', 9.0999],
        ['-10.01', '109.91', '+', f'numb(summ test): ', 99.9],
        ['-10.99999', '-89.00001', '+', f'numb(summ test): ', -100],

        #SUB tests
        ['0', '1', '-', f'0-1 in number notation', -1],
        ['1', '0', '-',f'1-0 in number notation', 1],
        ['10', '0.1', '-', f'10-0.1 in number notation', 9.9],
        ['1010', '1010', '-', f'1010-1010 in number notation', 0],
        ['1234.4321', '9876.6789', '-', f'1234.4321-9876.6789 in number notation', -8642.2468],

        [0, '1', '-', f'int(0)-1 in number notation', -1],
        [1, '0', '-', f'int(1)-0 in number notation', 1],
        [10, '0.1', '-', f'int(10)-0.1 in number notation', 9.9],
        [1010, '1010', '-', f'int(1010)-1010 in number notation', 0],
        [1234.4321, '9876.6789', '-', f'float(1234.4321)-9876.6789 in number notation', -8642.2468],
            
        ['0', 1, '-', f'0-int(1) in number notation', -1],
        ['1', 0, '-', f'1-int(0) in number notation', 1],
        ['10', 0.1, '-', f'10-float(0.1) in number notation', 9.9],
        ['1010', 1010, '-', f'1010-int(1010) in number notation', 0],
        ['1234.4321', 9876.6789, '-', f'1234.4321-float(9876.6789) in number notation', -8642.2468],

        ['0', -1, '-', f'0-int(-1) in number notation', 1],
        ['-1', 0, '-', f'-1-int(0) in number notation', -1],
        ['-10', -0.1, '-', f'-10-float(-0.1) in number notation', -9.9],
        ['1010', -1010, '-', f'-1010-int(-1010) in number notation', 2020],
        ['-1234.4321', -9876.6789, '-', f'-1234.4321-float(-9876.6789) in number notation', 8642.2468],
                        
        ['10', '10', '-', f'numb(sub test): ', 0],
        ['10', '-10', '-', f'numb(sub test): ', 20],
        ['-10', '10', '-', f'numb(sub test): ', -20],
        ['-10', '-10', '-', f'numb(sub test): ', 0],
                        
        ['10', '10.1', '-', f'numb(sub test): ', -0.1],
        ['1.1', '-10.1', '-', f'numb(sub test): ', 11.2],
        ['-1.1', '10.1', '-', f'numb(sub test): ', -11.2],
        ['-10.11', '-10.99', '-', f'numb(sub test): ', 0.88],
                        
        ['10.001', '10.009', '-', f'numb(sub test): ', -0.008],
        ['10.1001', '-1.0002', '-', f'numb(sub test): ', 11.1003],
        ['-10.01', '109.91', '-', f'numb(sub test): ', -119.92],
        ['-10.99999', '-89.00001', '-', f'numb(sub test): ', 78.00002],

        #MUL tests
        ['0', '1', '*', f'0*1 in number notation', 0],
        ['1', '0', '*',f'1*0 in number notation', 0],
        ['10', '0.1', '*', f'10*0.1 in number notation', 1],
        ['1010', '1010', '*', f'1010*1010 in number notation', 1020100],
        ['1234.4321', '9876.6789', '*', f'1234.4321*9876.6789 in number notation', 12192089.47555269],

        [0, '1', '*', f'int(0)*1 in number notation', 0],
        [1, '0', '*', f'int(1)*0 in number notation', 0],
        [10, '0.1', '*', f'int(10)*0.1 in number notation', 1],
        [1010, '1010', '*', f'int(1010)*1010 in number notation', 1020100],
        [1234.4321, '9876.6789', '*', f'float(1234.4321)*9876.6789 in number notation', 12192089.47555269],
            
        ['0', 1, '*', f'0*int(1) in number notation', 0],
        ['1', 0, '*', f'1*int(0) in number notation', 0],
        ['10', 0.1, '*', f'10*float(0.1) in number notation', 1],
        ['1010', 1010, '*', f'1010*int(1010) in number notation', 1020100],
        ['1234.4321', 9876.6789, '*', f'1234.4321*float(9876.6789) in number notation', 12192089.47555269],

        ['0', -1, '*', f'0*int(*1) in number notation', 0],
        ['-1', 0, '*', f'-1*int(0) in number notation', 0],
        ['-10', -0.1, '*', f'-10*float(-0.1) in number notation', 1],
        ['1010', -1010, '*', f'-1010*int(-1010) in number notation', -1020100],
        ['-1234.4321', -9876.6789, '*', f'-1234.4321*float(-9876.6789) in number notation', 12192089.47555269],
                        
        ['10', '10', '*', f'numb(mul test): ', 100],
        ['10', '-10', '*', f'numb(mul test): ', -100],
        ['-10', '10', '*', f'numb(mul test): ', -100],
        ['-10', '-10', '*', f'numb(mul test): ', 100],
                        
        ['10', '10.1', '*', f'numb(mul test): ', 101],
        ['1.1', '-10.1', '*', f'numb(mul test): ', -11.11],
        ['-1.1', '10.1', '*', f'numb(mul test): ', -11.11],
        ['-10.11', '-10.99', '*', f'numb(mul test): ', 111.1089],
                        
        ['10.001', '10.009', '*', f'numb(mul test): ', 100.100009],
        ['10.1001', '-1.0002', '*', f'numb(mul test): ', -10.10212002],
        ['-10.01', '109.91', '*', f'numb(mul test): ', -1100.1991],
        ['-10.99999', '-89.00001', '*', f'numb(mul test): ', 978.9992199999],

        #TRUEDIV tests
        ['0', '1', '/', f'0/1 in number notation', 0],
        ['10', '0.1', '/', f'10/0.1 in number notation', 100],
        ['1010', '1010', '/', f'1010/1010 in number notation', 1],
        ['1234.4321', '9876.6789', '/', f'1234.4321/9876.6789 in number notation', 0.124984533],

        [0, '1', '/', f'int(0)/1 in number notation', 0],
        [10, '0.1', '/', f'int(10)/0.1 in number notation', 100],
        [1010, '1010', '/', f'int(1010)/1010 in number notation', 1],
        [1234.4321, '9876.6789', '/', f'float(1234.4321)/9876.6789 in number notation', 0.124984533],
            
        ['0', 1, '/', f'0/int(1) in number notation', 0],
        ['10', 0.1, '/', f'10/float(0.1) in number notation', 100],
        ['1010', 1010, '/', f'1010/int(1010) in number notation', 1],
        ['1234.4321', 9876.6789, '/', f'1234.4321/float(9876.6789) in number notation', 0.124984533],

        ['0', -1, '/', f'0/int(1) in number notation', 0],
        ['-10', -0.1, '/', f'-10/float(-0.1) in number notation', 100],
        ['1010', -1010, '/', f'-1010/int(-1010) in number notation', -1],
        ['-1234.4321', -9876.6789, '/', f'-1234.4321/float(-9876.6789) in number notation', 0.1249845330],
                        
        ['10', '10', '/', f'numb(truediv test): ', 1],
        ['10', '-10', '/', f'numb(truediv test): ', -1],
        ['-10', '10', '/', f'numb(truediv test): ', -1],
        ['-10', '-10', '/', f'numb(truediv test): ', 1],
        ['10023006', '1002', '/', f'numb(truediv test): ', 10003],

        ['74.148222', '-74', '/', f'numb(truediv test): ', -1.002003],
        ['-0.1', '256', '/', f'numb(truediv test): ', -0.000390625],
        ['12193263111.2635269', '-1.23456789', '/', f'numb(truediv test): ', -9876543210],
        ['12193263111.2635269', '-9876543210', '/', f'numb(truediv test): ', -1.23456789],
        ['98765', '1.234', '/', f'numb(truediv test): ', 80036.4667747164],
        ['-1250000', '-500', '/', f'numb(truediv test): ', 2500],
        ['2.000200220020002', '2.00020002', '/', f'numb(truediv test): ', 1.0000001],
                        
        ['10', '10.1', '/', f'numb(truediv test): ', 0.9900990099],
        ['1.1', '-10.1', '/', f'numb(truediv test): ', -0.1089108911],
        ['-1.1', '10.1', '/', f'numb(truediv test): ', -0.1089108911],
        ['-10.11', '-10.99', '/', f'numb(truediv test): ', 0.9199272066],
                        
        ['10.001', '10.009', '/', f'numb(truediv test): ', 0.9992007194],
        ['10.1001', '-1.0002', '/', f'numb(truediv test): ', -10.0980803839],
        ['-10.01', '109.91', '/', f'numb(truediv test): ', -0.0910745155],
        ['-10.99999', '-89.00001', '/', f'numb(truediv test): ', 0.1235953794],

        #FLOORDIV tests
        ['0', '1', '//', f'0//1 in number notation', 0],
        ['10', '0.1', '//', f'10//0.1 in number notation', 100],
        ['1010', '1010', '//', f'1010//1010 in number notation', 1],
        ['1234.4321', '9876.6789', '//', f'1234.4321//9876.6789 in number notation', 0],

        [0, '1', '//', f'int(0)//1 in number notation', 0],
        [10, '0.1', '//', f'int(10)//0.1 in number notation', 100],
        [1010, '1010', '//', f'int(1010)//1010 in number notation', 1],
        [1234.4321, '9876.6789', '//', f'float(1234.4321)//9876.6789 in number notation', 0],
            
        ['0', 1, '//', f'0//int(1) in number notation', 0],
        ['10', 0.1, '//', f'10//float(0.1) in number notation', 100],
        ['1010', 1010, '//', f'1010//int(1010) in number notation', 1],
        ['1234.4321', 9876.6789, '//', f'1234.4321//float(9876.6789) in number notation', 0],

        ['0', -1, '//', f'0//int(1) in number notation', 0],
        ['-10', -0.1, '//', f'-10//float(-0.1) in number notation', 100],
        ['1010', -1010, '//', f'-1010//int(-1010) in number notation', -1],
        ['-1234.4321', -9876.6789, '//', f'-1234.4321//float(-9876.6789) in number notation', 0],
                        
        ['10', '10', '//', f'numb(floordiv test): ', 1],
        ['10', '-10', '//', f'numb(floordiv test): ', -1],
        ['-10', '10', '//', f'numb(floordiv test): ', -1],
        ['-10', '-10', '//', f'numb(floordiv test): ', 1],
        ['10023006', '1002', '//', f'numb(floordiv test): ', 10003],

        ['74.148222', '-74', '//', f'numb(floordiv test): ', -1],
        ['-0.1', '256', '//', f'numb(floordiv test): ', 0],
        ['12193263111.2635269', '-1.23456789', '//', f'numb(floordiv test): ', -9876543210],
        ['12193263111.2635269', '-9876543210', '//', f'numb(floordiv test): ', -1],
        ['98765', '1.234', '//', f'numb(floordiv test): ', 80036],
        ['-1250000', '-500', '//', f'numb(floordiv test): ', 2500],
        ['2.000200220020002', '2.00020002', '//', f'numb(floordiv test): ', 1],
                        
        ['10', '10.1', '//', f'numb(floordiv test): ', 0],
        ['1.1', '-10.1', '//', f'numb(floordiv test): ', 0],
        ['-10.11', '-10.99', '//', f'numb(floordiv test): ', 0],
                        
        ['10.001', '10.009', '//', f'numb(floordiv test): ', 0],
        ['10.1001', '-1.0002', '//', f'numb(floordiv test): ', -10],
        ['-10.01', '109.91', '//', f'numb(floordiv test): ', 0],
        ['-10.99999', '-89.00001', '//', f'numb(floordiv test): ', 0],

        #MOD tests
        ['0', '1', '%', f'0%1 in number notation', 0],
        ['10', '0.1', '%', f'10%0.1 in number notation', 0],
        ['1010', '1010', '%', f'1010%1010 in number notation', 0],
        ['1234.4321', '9876.6789', '%', f'1234.4321%9876.6789 in number notation', 1234.4321],

        [0, '1', '%', f'int(0)%1 in number notation', 0],
        [10, '0.1', '%', f'int(10)%0.1 in number notation', 0],
        [1010, '1010', '%', f'int(1010)%1010 in number notation', 0],
        [1234.4321, '9876.6789', '%', f'float(1234.4321)%9876.6789 in number notation', 1234.4321],
            
        ['0', 1, '%', f'0%int(1) in number notation', 0],
        ['10', 0.1, '%', f'10%float(0.1) in number notation', 0],
        ['1010', 1010, '%', f'1010%int(1010) in number notation', 0],
        ['1234.4321', 9876.6789, '%', f'1234.4321+float(9876.6789) in number notation', 1234.4321],

        ['0', -1, '%', f'0%int(1) in number notation', 0],
        ['-10', -0.1, '%', f'-10%float(-0.1) in number notation', 0],
        ['1010', -1010, '%', f'-1010%int(-1010) in number notation', 0],
        ['-1234.4321', -9876.6789, '%', f'-1234.4321%float(-9876.6789) in number notation', -1234.4321],
                        
        ['10', '10', '%', f'numb(module test): ', 0],
        ['10', '-10', '%', f'numb(module test): ', 0],
        ['-10', '10', '%', f'numb(module test): ', 0],
        ['-10', '-10', '%', f'numb(module test): ', 0],
        ['10023006', '1002', '%', f'numb(module test): ', 0],

        ['74.148222', '-74', '%', f'numb(module test): ', 0.148222],
        ['-0.1', '256', '%', f'numb(module test): ', -0.1],
        ['12193263111.263526', '-987654321', '%', f'numb(module test): ', 341411259.263526],
        ['98765', '1.234', '%', f'numb(module test): ', 0.576],
        ['-1250000', '-500', '%', f'numb(module test): ', 0],
                        
        ['10', '10.1', '%', f'numb(module test): ', 10],
        ['1.1', '-10.1', '%', f'numb(module test): ', 1.1],
        ['-10.11', '-10.99', '%', f'numb(module test): ', -10.11],
                        
        ['10.001', '10.009', '%', f'numb(module test): ', 10.001],
        ['10.1001', '-1.0002', '%', f'numb(module test): ', 0.0981],
        ['-10.01', '109.91', '%', f'numb(module test): ', -10.01],
        ['-10.99999', '-89.00001', '%', f'numb(module test): ', -10.99999],

        #SQRT tests
        ['1', '0', 'sqrt', f'finding a sqrt of int(1) not periodic', 1],
        ['4', '0', 'sqrt', f'finding a sqrt of int(4) not periodic', 2],
        ['9', '0', 'sqrt', f'finding a sqrt of int(9) not periodic', 3],
        ['16', '0', 'sqrt', f'finding a sqrt of int(16) not periodic', 4],
        ['25', '0', 'sqrt', f'finding a sqrt of int(25) not periodic', 5],
        ['3600', '0', 'sqrt', f'finding a sqrt of int(3600) not periodic', 60],
        ['100000000', '0', 'sqrt', f'finding a sqrt of int(100000000) not periodic', 10000],
        ['0.25', '0', 'sqrt', f'finding a sqrt of float(0.25) not periodic', 0.5],
        ['0.0001', '0', 'sqrt', f'finding a sqrt of float(0.0001) not periodic', 0.01],
        ['2.56', '0', 'sqrt', f'finding a sqrt of float(2.56) not periodic', 1.6],
        ['144.72330601', '0', 'sqrt', f'finding a sqrt of float(144.72330601) not periodic', 12.0301],
        ['100.500625', '0', 'sqrt', f'finding a sqrt of float(100.500625) not periodic', 10.025],
        ['9.01440576', '0', 'sqrt', f'finding a sqrt of float(9.01440576) not periodic', 3.0024],
        ['2', '0', 'sqrt', f'finding a sqrt of int(2) periodic', 1.4142135624],
        ['3', '0', 'sqrt', f'finding a sqrt of int(3) periodic', 1.7320508076],
        ['5', '0', 'sqrt', f'finding a sqrt of int(5) periodic', 2.2360679775],
        ['115', '0', 'sqrt', f'finding a sqrt of int(115) periodic', 10.7238052948],
        ['123456789', '0', 'sqrt', f'finding a sqrt of int(123456789) periodic', 11111.1110605556],
        ['987654321', '0', 'sqrt', f'finding a sqrt of int(987654321) periodic', 31426.9680529319],
        ['102030401', '0', 'sqrt', f'finding a sqrt of int(102030401) periodic', 10101.009900005],            
        ['101010101', '0', 'sqrt', f'finding a sqrt of int(101010101) periodic', 10050.3781520896],

        #NROOT tests
        ['1', '2', 'nroot', f'finding a nroot(2) of int(1=1^2) not periodic', 1],
        ['1', '33', 'nroot', f'finding a nroot(33) of int(1=1^33) not periodic', 1],
        ['16', '4', 'nroot', f'finding a nroot(4) of int(16=2^4) not periodic', 2],
        ['1024', '10', 'nroot', f'finding a nroot(10) of int(1024=2^10) not periodic', 2],
        ['81', '2', 'nroot', f'finding a nroot(2) of int(81=9^2) not periodic', 9],
        ['27', '3', 'nroot', f'finding a nroot(3) of int(27=3^3) not periodic', 3],
        ['625', '4', 'nroot', f'finding a nroot(4) of int(625=5^4) not periodic', 5],
        ['134217728', '27', 'nroot', f'finding a nroot(27) of int(134217728=2^27) not periodic', 2],
        ['2', '3', 'nroot', f'finding a nroot(3) of int(2) periodic', 1.2599210499],
        ['313', '5', 'nroot', f'finding a nroot(5) of int(313) periodic', 3.1557956087],
        ['5', '31', 'nroot', f'finding a nroot(31) of int(5) periodic', 1.0532886867],
            
        #POW tests
        ['1', '0', 'pow', f'finding a pow(0) of int(1):1^0', 1],
        ['1', '35', 'pow', f'finding a pow(35) of int(1):1^35', 1],
        ['2', '12', 'pow', f'finding a pow(12) of int(2):2^12', 4096],
        ['125', '15', 'pow', f'finding a pow(15) of int(125):125^15', 28421709430404007434844970703125],
        ['1.1', '3', 'pow', f'finding a pow(3) of float(1.1):1.1^3', 1.331],
        ]
    last_testing=''
    for test in tests:            
        test_count+=1
        if type(test[0])==str:
            a=Rational(test[0], {'max float part':10})
        else:
            a=test[0]
        if type(test[1])==str:
            b=Rational(test[1], {'max float part':10})
        else:
            b=test[1]
        testing = test[2]
        if last_testing != testing:
            print(f'---Test [{test[2]}] operation---')
            last_testing = testing
        match test[2]:
            case '+':                    
                try:
                    c=a+b                        
                except Exception as e:
                    error_count+=1
                    print(f'{test_count}) '+test[3]+': ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '-':
                try:
                    c=a-b                        
                except Exception as e:
                    error_count+=1
                    print(f'{test_count}) '+test[3]+': ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '*':
                try:
                    c=a*b                        
                except Exception as e:
                    error_count+=1
                    print(f'{test_count}) '+test[3]+': ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '/':
                try:
                    c=a/b   
                except Exception as e:
                    error_count+=1
                    print(f'{test_count}) '+test[3]+': ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '//':
                try:
                    c=a//b   
                except Exception as e:
                    raise e
                    error_count+=1
                    print(f'{test_count}) '+test[3]+': ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case '%':
                try:
                    c=a%b   
                except Exception as e:
                    raise e
                    error_count+=1
                    print(f'{test_count}) '+test[3]+':ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case 'sqrt':
                try:
                    c=a.sqrt()  
                except Exception as e:
                    raise e
                    error_count+=1
                    print(f'{test_count}) '+test[3]+':ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case 'nroot':
                try:
                    c=a.nroot(b)  
                except Exception as e:
                    raise e
                    error_count+=1
                    print(f'{test_count}) '+test[3]+':ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
            case 'pow':
                try:
                    c=pow(a, b)  
                except Exception as e:
                    raise e
                    error_count+=1
                    print(f'{test_count}) '+test[3]+':ERROR\n   ||\n   |└--->operation:{test[0]}{test[2]}{test[1]}\n   └--->{e.__repr__()}]\n')
        if c==test[-1]:
            if reportType=='full':
                print(f'{test_count}) '+test[3]+':DONE')
            done_count+=1
        else:
            print(f'{test_count}) '+test[3]+':WRONG')
            wrong_count+=1
            print(f' ->generator: {test[0]}{test[2]}{test[1]}')
            print(f'   ->expected: {test[-1]}; but get: {c.value}')

            
    print('---------------------------------------------------------\n')
    print(f'End Rational testing with a report-mode:{reportType}\nTest count = {test_count}\nDone tests = {done_count}\nWrong tests = {wrong_count}\nErrors = {error_count}')
    print('---------------------------------------------------------\n')
    if kwargs!={}:
        kwargs.update({
            'all_tests':kwargs['all_tests']+test_count,
            'done_tests':kwargs['done_tests']+done_count,
            'wrong_tests':kwargs['wrong_tests']+wrong_count,
            'errors':kwargs['errors']+error_count
            })
        return kwargs