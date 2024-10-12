from objects.Error import *
from objects.Matrix import Matrix

__all__ = ['matrices_base_test']

def matrices_base_test(reportType:str='full'):
    test_count = 0
    done_count = 0
    error_count = 0
    if reportType == 'full':
        print('-----Generation tests (no flags)-----')
        tests = {
            '1': f'1x1 square matrix by str(1digit) without generator symbols',
            '1,2,3,5': f'2x2 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0': f'2x2 square matrix by str(only 0) without generator symbols',
            '12,33,1.7,33': f'2x2 square matrix by str(2 digits) without generator symbols',
            '-1,2,3,-5': f'2x2 square matrix by str(negative digits) without generator symbols',
            '1,44,157,-1': f'2x2 square matrix by str(different digits) without generator symbols',
            '1,21,3,1.15,2,43,7,2.3,31': f'3x3 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0,0,0,0,0,0': f'3x3 square matrix by str(only 0) without generator symbols',
            '12,22,13,5.7,23,42,7.8,21,13': f'3x3 square matrix by str(2 digits) without generator symbols',
            '1,-2,3,5,-2,-4,7,2,-3': f'3x3 square matrix by str(negative digits) without generator symbols',
            '122,-1.2,3,53,2,47,7,-21.3,-3': f'3x3 square matrix by str(different digits) without generator symbols',
            '1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0': f'4x4 square matrix by str(only 0) without generator symbols',
            '12,23,33,5.1,23,24,31,59,68,14,1.9,56,13,23,48,50': f'4x4 square matrix by str(2 digits) without generator symbols',
            '1,-2,3,-5,2,2,3,-5,6,1,9,5,3,-2,4,-5': f'4x4 square matrix by str(negative digits) without generator symbols',
            '-122,2,31,5,23,-2,3,53,6,111,9,5,31,-44,4,115': f'4x4 square matrix by str(different digits) without generator symbols',
            'T1,2,3,5': f'2x2 square matrix by str with \'T\' generator symbol',
            'T1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'T\' generator symbol',
            'T1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'T\' generator symbol',
            'I1,2,3,5': f'2x2 square matrix by str with \'I\' generator symbol',
            'I1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'I\' generator symbol',
            'I1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'I\' generator symbol',
            'TI1,2,3,5': f'2x2 square matrix by str with \'TI\' generator symbol',
            'TI1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'TI\' generator symbol',
            'TI1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'TI\' generator symbol',
            '[sq]1,2,3,5': f'2x2 square matrix by str with \'[sq]\' generator symbol',
            '[sq]1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'[sq]\' generator symbol',
            '[sq]1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'[sq]\' generator symbol',
            '[sq]T1,2,3,5': f'2x2 square matrix by str with \'[sq]T\' generator symbol',
            '[sq]T1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'[sq]T\' generator symbol',
            '[sq]T1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'[sq]T\' generator symbol',
            '[sq]I1,2,3,5': f'2x2 square matrix by str with \'[sq]I\' generator symbol',
            '[sq]I1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'[sq]I\' generator symbol',
            '[sq]I1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'[sq]I\' generator symbol',
            '[sq]IT1,2,3,5': f'2x2 square matrix by str with \'[sq]IT\' generator symbol',
            '[sq]IT1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str with \'[sq]IT\' generator symbol',
            '[sq]IT1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str with \'[sq]IT\' generator symbol',
        }
        iterator = 0
        for key, value in tests.items():
            test_count +=1
            try:
                iterator+=1
                Matrix(key)
            except Exception as e:
                error_count+=1
                print(f'{iterator}) '+value + f': ERROR\n   ||\n   |└--->generator:{key}\n   └--->{e.__repr__()}]\n')
            else:
                done_count+=1
                print(f'{iterator}) '+value + f': DONE')

        print('-----Generation tests (with flags)-----')
        tests = [
            ['1,2,3,5',{'form':Matrix.MM_matrix_form_square}, f'2x2 square matrix by str with form flag'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with form, rows, columns flags'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with form, rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]T1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]T\' generator symbols and rows, columns flags'],
            ['1,2,3,5,1,1',{'factor':Matrix.MM_matrix_factor_diagonal}, f'generating diagonal matrix by string with no generator symbols and with factor flag'],
            [[[1,2,3],[2,3,5]],{}, f'2x3 rectangle matrix by list'],
            [[[1,2,3],[2,3,5],[3,3,1]],{}, f'3x3 square matrix by list'],
            [[[1,2,3,4,5]],{}, f'1x5 rectangle matrix by list'],
        ]
        for test in tests:
            test_count +=1
            try:
                iterator+=1
                Matrix(test[0], test[1])
            except Exception as e:
                error_count+=1
                print(f'{iterator}) '+test[2] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
            else:
                done_count+=1
                print(f'{iterator}) '+test[2] + f': DONE')

        print('-----Operation tests-----')
        tests = [
            [[Matrix('1,2,2,3'), Matrix('1,7,7,4')], '*', f'2x2 matrix multiplied by 2x2 matrix'],
            [[Matrix('1,2,2,3'), 2], '*', f'2x2 matrix multiplied by int(2)'],
            [[Matrix('1,2,2,3'), 2], '^', f'2x2 matrix powered by int(2)'],
            [[Matrix('1,2,2,3'), -1], '^', f'2x2 matrix powered by int(-1)'],
            [[Matrix('1,2,2,3'), -2], '^', f'2x2 matrix powered by int(-2)'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':3, 'columns':2}), Matrix('[rec]1,7,7,4,1,1', {'rows':2, 'columns':3})], '*', f'3x2 matrix multiplied by 2x3 matrix'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':3, 'columns':2}), 2], '*', f'3x2 matrix multiplied by int(2)'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':2, 'columns':3}), Matrix('[rec]1,7,7,4,1,1', {'rows':3, 'columns':2})], '*', f'2x3 matrix multiplied by 3x2 matrix'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':2, 'columns':3}), 2], '*', f'2x3 matrix multiplied by int(2)'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':2, 'columns':3}), Matrix([[1,7,7],[2,3,3]])], '+', f'2x3 matrix plus 2x3 matrix'],
            [[Matrix('1,2,2,3,2,1,7,3,1'), Matrix([[1,7,7],[2,3,3],[2,2,3]])], '+', f'3x3 matrix plus 3x3 matrix'],
            [[Matrix('[rec]1,2,2,3,2,1', {'rows':2, 'columns':3}), Matrix([[1,7,7],[2,3,3]])], '-', f'2x3 matrix minus 2x3 matrix'],
            [[Matrix('1,2,2,3,2,1,7,3,1'), Matrix([[1,7,7],[2,3,3],[2,2,3]])], '-', f'3x3 matrix minus 3x3 matrix'],
            [[Matrix('1,2,2,3,2,1,7,3,1'), Matrix([[1,7,7],[2,3,3],[2,2,3]])], '/', f'3x3 matrix div 3x3 matrix'],
            [[Matrix('1,2,2,3,2,1,7,3,1'), Matrix([[1,2,2],[3,2,1],[7,3,1]])], '=', f'3x3 matrix equal 3x3 matrix'],
        ]
        for test in tests:
            test_count +=1
            try:
                iterator+=1
                match test[1]:
                    case '*':
                        test[0][0]*test[0][1]
                    case '^':
                        test[0][0]**test[0][1]
                    case '+':
                        test[0][0]+test[0][1]
                    case '-':
                        test[0][0]+test[0][1]
                    case '/':
                        test[0][0]/test[0][1]
                    case '=':
                        test[0][0]==test[0][1]
            except Exception as e:
                error_count+=1
                print(f'{iterator}) '+test[2] + f': ERROR\n   ||\n   |└--->generator:{test[0][0].get_generator_attribute()}\n   └--->{e.__repr__()}]\n')
            else:
                done_count+=1
                print(f'{iterator}) '+test[2] + f': DONE')

        print('-----Matrix methods tests-----')
        tests = [
            [Matrix('1,2,2,3'), 'transpose', '', f'2x2 matrix with \'transpose()\' method'],
            [Matrix('1,2,2,3'), 'invert', '', f'2x2 matrix with \'invert()\' method'],
            [Matrix('1,2,2,3'), 'find_determinant', '', f'2x2 matrix with \'find_determinant()\' method'],
            [Matrix('1,2,2,3'), 'find_addition', (1,0), f'2x2 matrix with \'find_addition(i,j)\' method'],
            [Matrix('1,2,2,3'), 'find_minor', (0,1), f'2x2 matrix with \'find_minor(i,j)\' method'],
            [Matrix('1,2,2,3,2,3', {'form':Matrix.MM_matrix_form_rectangle, 'rows':3, 'columns':2}), 'transpose', '', f'3x2 matrix with \'transpose()\' method'],
            [Matrix('1,2,1,2,1,2,3,1,1,2,3,4,2,5,7,9'), 'transpose', '', f'4x4 matrix with \'transpose()\' method'],
            [Matrix([[1,2,1,2],[1,2,3,1],[1,2,3,4],[2,5,7,9]]), 'invert', '', f'4x4 matrix with \'invert()\' method'],
            [Matrix('1,2,1,2,1,2,3,1,1,2,3,4,2,5,7,9'), 'find_determinant', '', f'4x4 matrix with \'find_determinant()\' method'],
            [Matrix([[1,2,1,2],[1,2,3,1],[1,2,3,4],[2,5,7,9]]), 'find_addition', (3,1), f'4x4 matrix with \'find_addition(i,j)\' method'],
            [Matrix('1,2,1,2,1,2,3,1,1,2,3,4,2,5,7,9'), 'find_minor', (2,3), f'4x4 matrix with \'find_minor(i,j)\' method'],
        ]
        for test in tests:
            test_count +=1
            try:
                iterator+=1
                method = getattr(test[0], test[1])
                if test[2] == '':
                    method()
                else:
                    method(*test[2])
            except Exception as e:
                error_count+=1
                print(f'{iterator}) '+test[3] + f': ERROR\n   ||\n   |└--->generator:{test[0].generator_stroke}\n   └--->{e.__repr__()}]\n')
            else:
                done_count+=1
                print(f'{iterator}) '+test[3] + f': DONE')
        
        print('-----Error tests-----')
        tests = [
            ['generator', '2,1,1', MatrixError.MM_error_not_enough_numbers, 'test:wrong number count','expect 2x2 matrix by str but give only 3 numbers at generator'],
            ['generator', '2,1,1,3,3', MatrixError.MM_error_not_enough_numbers, 'test:wrong number count','expect 2x2 matrix by str but give only 5 numbers at generator'],
            ['generator', [[1,2,3],[3,1]], MatrixError.MM_error_not_enough_numbers, 'test:wrong number count','expect 2x3 matrix by list but give only 5 numbers at generator'],
            ['generator', [[1,2,3,2],[3,1,1]], MatrixError.MM_error_not_enough_numbers, 'test:wrong number count','expect 2x3 matrix by list but give 7 numbers at generator'],
            ['method', '2,1,2,1', MatrixError.MM_error_zero_determinant, 'test:zero determinant', 'expect to find inverted matrix for matrix with zero determinant', 'invert'],
            ['method', [[2,3,3],[1,2,7]], MatrixError.MM_error_zero_determinant, 'test:zero determinant', 'expect to find inverted matrix for matrix with \'undefined\' determinant(rectangle matrix)', 'invert'],
            ['operation', [[2,3,3],[1,2,7]], MatrixError.MM_error_wrong_line_count, 'test:wrong line count', 'expect to multiply matrices with different dimensions', '*', [[1,2],[3,4]]],
            ['operation', [[2,3,3],[1,2,7]], MatrixError.MM_error_wrong_line_count, 'test:wrong line count', 'expect to div matrices with different dimensions', '/', [[1,2],[3,4]]],
            ['operation', [[2,3,3],[1,2,7]], MatrixError.MM_error_wrong_line_count, 'test:wrong line count', 'expect to plus matrices with different dimensions', '+', [[1,2],[3,4]]],
            ['operation', [[2,3,3],[1,2,7]], MatrixError.MM_error_wrong_line_count, 'test:wrong line count', 'expect to minus matrices with different dimensions', '-', [[1,2],[3,4]]],
            ['generator', '[rec]2,1,2,1', MatrixError.MM_error_wrong_flags, 'test:wrong flags', 'expect to generate rectangle matrix with [rec]symbol but without flags rows and columns', {}],
            ['generator', '[sq]2,1,3,2,4,1', MatrixError.MM_error_wrong_flags, 'test:wrong flags', 'expect to generate square matrix with [sq]symbol but with flags rows and columns', {'rows':2, 'columns':3}],
        ]
        for test in tests:
            test_count +=1
            try:
                iterator+=1
                match test[0]:
                    case 'generator':
                        try:
                            test[5]
                        except:
                            Matrix(test[1])
                        else:
                            Matrix(test[1], test[5])
                    case 'method':
                        method = getattr(Matrix(test[1]), test[5])
                        method()
                    case 'operation':
                        match test[5]:
                            case '*':
                                Matrix(test[1])*Matrix(test[6])
                            case '/':
                                Matrix(test[1])/Matrix(test[6])
                            case '+':
                                Matrix(test[1])+Matrix(test[6])
                            case '-':
                                Matrix(test[1])-Matrix(test[6])

            except Exception as e:
                if isinstance(e, MatrixError) and e.errorCode == test[2]:
                    done_count+=1
                    print(f'{iterator}) '+test[3] + f': DONE [get an error as expected]\n   --->{test[4]}')
                else:
                    error_count+=1
                    print(f'{iterator}) '+test[3] + f': ERROR [expected one error, but get another]\n   ||\n   |└--->generator:{test[1]}\n   └--->{e.__repr__()}]\n')
            else:
                error_count+=1
                print(f'{iterator}) '+test[3] + f': WRONG [has no error]\n   ||\n   |└--->generator:{test[1]}\n   └--->There are must be an error!\n')

        print('-----Precision tests-----')
        tests = [
            [Matrix('1,2,3,5',{'form':Matrix.MM_matrix_form_square}).determinant, -1, f'2x2 square matrix by str. Find determinant', 'determinant'],
            [Matrix([[1,3],[2,5]]).determinant, -1, f'2x2 square matrix by list. Find determinant', 'determinant'],
            [Matrix('[rec]1,2,3,5,1,1', {'rows': 3, 'columns':2}).transpose().values, Matrix([[1,3,1], [2,5,1]], {'rows':2, 'columns':3}).values, f'3x2 rectangle matrix transpose test', 'transpose'],
            [Matrix('1,3,2,2,4,1,1,1,1').invert().values, Matrix([[-0.75,0.25,1.25], [0.25,0.25,-0.75], [0.5, -0.5, 0.5]]).values, f'3x3 square matrix inverse test', 'inverse'],
            [Matrix([[1,3,2,2,1], [2,4,1,2,0], [1,1,1,5,3], [1,3,1,1,1], [2,2,1,3,5]]).determinant, -42, f'5x5 square matrix determinant test', 'determinant'],
            [Matrix([[1,3,2.5,2,1], [2,4,1,2,0], [1,1,1,5,3], [1,3,1,1,1], [2.2,2,1,3,5.0]]).determinant, -73.2, f'5x5 square matrix determinant test (negative+float)', 'determinant'],            
            [(Matrix('1,2,2,3')*4).values, [[4,8],[8,12]], f'(2x2 square matrix)*4 test', 'multiply'],
            [(Matrix('1,2,2,3,3,4,1,1,1')*2).values, [[2,4,4],[6,6,8],[2,2,2]], f'(3x3 square matrix)*2 test', 'multiply'],                 
            [(Matrix('[rec]-1,2,3,-5,1,1.25', {'rows': 3, 'columns':2})*3).values, [[-3,6], [9,-15], [3, 3.75]], f'(3x2 rectangle matrix)*3 test', 'multiply'],
            [(Matrix('[rec]1,-2,3.2,5,1,1,10,-3', {'rows': 2, 'columns':4})*5).values, [[5, -10, 16, 25], [5, 5, 50, -15]], f'(2x4 rectangle matrix)*5 test', 'multiply'],
            [(Matrix('1,2,2,3')*Matrix('3,1,1,2')).values, [[5,5],[9,8]], f'(2x2 square matrix_A)*(2x2 square matrix_B) test', 'multiply'],
            [(Matrix('1,-2,1,-2,3,-1,1,-1,1')*Matrix('3,1,3,1,-2,2,3,2,1')).values, [[4,7,0],[-6,-10,-1],[5,5,2]], f'(3x3 square matrix_A)*(3x3 square matrix_B) test', 'multiply'],
            [(Matrix('1,2,2,3')**2).values, [[5,8],[8,13]], f'(2x2 square matrix_A)^2 test', 'power'],
            [(Matrix('1,-2,2,-3,3,4,1,1,-1')**3).values, [[19,-44,2],[-63,75,58],[4,13,-13]], f'(3x3 square matrix_A)^3 test', 'power'],
            [(Matrix('1,2,2,3').invert()*Matrix('1,2,2,3')).values, [[1,0],[0,1]], f'(2x2 square matrix_A.invert)*(2x2 square matrix_A) test', 'multiply'],
            [(Matrix('1,2,2,3,3,4,1,1,1').invert()*Matrix('1,2,2,3,3,4,1,1,1')).values, [[1,0,0],[0,1,0],[0,0,1]], f'(3x3 square matrix_A.invert)*(3x3 square matrix_A) test', 'multiply'],
            [(Matrix('1,2,2,3,3,4,1,1,1,3,2,3,1,1,1,1').invert()*Matrix('1,2,2,3,3,4,1,1,1,3,2,3,1,1,1,1')).values, [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], f'(4x4 square matrix_A.invert)*(4x4 square matrix_A) test', 'multiply'],
            [((Matrix('1,2,2,3')**5).invert()).values, ((Matrix('1,2,2,3').invert())**5).values, f'(2x2 matrix_A^5)^-1 == (2x2 matrix_A^-1)^5 test', 'equality'],
            [((Matrix('1,2,2,3,3,4,1,1,1')**5).invert()).values, ((Matrix('1,2,2,3,3,4,1,1,1').invert())**5).values, f'(3x3 matrix_A^5)^-1 == (3x3 matrix_A^-1)^5 test', 'equality'],
            [((Matrix('1,2,2,3,3,4,1,1,1,3,2,3,1,1,1,1')**5).invert()).values, ((Matrix('1,2,2,3,3,4,1,1,1,3,2,3,1,1,1,1').invert())**5).values, f'(4x4 matrix_A^5)^-1 == (4x4 matrix_A^-1)^5 test', 'equality'],
            [(Matrix('1,2,2,3')).find_minor(1,1), Matrix([[1]]), f'finding a minor-matrix for 2x2 matrix', 'find minor (i,j)'],
            [(Matrix('1,2,2,3,3,4,1,1,1')).find_minor(1,2), Matrix([[1,2], [1,1]]), f'finding a minor-matrix for 3x3 matrix', 'find minor (i,j)'],
            [(Matrix('1,2,2,3,3,4,1,1,1,3,2,3,1,1,1,1')).find_minor(3,2), Matrix([[1,2,3], [3,4,1], [1,3,3]]), f'finding a minor-matrix for 4x4 matrix', 'find minor (i,j)'],
        ]
        for test in tests:
            test_count +=1
            iterator+=1
            if test[0]==test[1]:
                done_count+=1
                print(f'{iterator}) '+test[2] + f': DONE')
            else:
                error_count+=1
                print(f'{iterator}) '+test[2] + f': ERROR\n   |\n   └--->{test[3]} not equal!\n')
                
        print('---------------------------------------------------------\n')
        print(f'End matrix testing with a report-mode:{reportType}\nTest count = {test_count}\nDone tests = {done_count}\nErrors = {error_count}')
        print('---------------------------------------------------------\n')