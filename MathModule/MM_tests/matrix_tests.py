from MM_objects.Error import *
from MM_objects.Matrix import Matrix

def matrix_test(reportType:str='full'):
    if reportType == 'full':
        print('-----Generation tests (no flags)-----')
        tests = {
            '1': f'1x1 square matrix by str(1digit) without generator symbols',
            '1,2,3,5': f'2x2 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0': f'2x2 square matrix by str(only 0) without generator symbols',
            '12,33,17,33': f'2x2 square matrix by str(2 digits) without generator symbols',
            '-1,2,3,-5': f'2x2 square matrix by str(negative digits) without generator symbols',
            '1,44,157,-1': f'2x2 square matrix by str(different digits) without generator symbols',
            '1,2,3,5,2,4,7,2,3': f'3x3 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0,0,0,0,0,0': f'3x3 square matrix by str(only 0) without generator symbols',
            '12,22,13,57,23,42,78,21,13': f'3x3 square matrix by str(2 digits) without generator symbols',
            '1,-2,3,5,-2,-4,7,2,-3': f'3x3 square matrix by str(negative digits) without generator symbols',
            '122,-12,3,53,2,47,7,-213,-3': f'3x3 square matrix by str(different digits) without generator symbols',
            '1,2,3,5,2,2,3,5,6,1,9,5,3,2,4,5': f'4x4 square matrix by str(different 1digit) without generator symbols',
            '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0': f'4x4 square matrix by str(only 0) without generator symbols',
            '12,23,33,51,23,24,31,59,68,14,19,56,13,23,48,50': f'4x4 square matrix by str(2 digits) without generator symbols',
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
            try:
                iterator+=1
                Matrix(key)
            except Exception as e:
                print(f'{iterator}) '+value + f': ERROR\n   ||\n   |└--->generator:{key}\n   └--->{e.__repr__()}]\n')
            else:
                print(f'{iterator}) '+value + f': DONE')
        print('-----Generation tests (with flags)-----')
        tests = [
            ['1,2,3,5',{'form':Matrix.MM_matrix_form_square}, f'2x2 square matrix by str with form flag'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with form, rows, columns flags'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with form, rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]T1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]T\' generator symbols and rows, columns flags'],
            [[[1,2,3],[2,3,5]],{}, f'2x3 rectangle matrix by list'],
            [[[1,2,3],[2,3,5],[3,3,1]],{}, f'3x3 square matrix by list'],
            [[[1,2,3,4,5]],{}, f'1x5 square matrix by list'],
        ]
        for test in tests:
            try:
                iterator+=1
                Matrix(test[0], test[1])
            except Exception as e:
                print(f'{iterator}) '+test[2] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
            else:
                print(f'{iterator}) '+test[2] + f': DONE')
        print('-----Operation tests-----')
        tests = [
            ['1,2,3,5',{'form':Matrix.MM_matrix_form_square}, f'2x2 square matrix by str with form flag'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with form, rows, columns flags'],
            ['1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with form, rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 2, 'columns':3}, f'2x3 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]\' generator symbols and rows, columns flags'],
            ['[rec]T1,2,3,5,1,1',{'form':Matrix.MM_matrix_form_rectangle, 'rows': 3, 'columns':2}, f'3x2 rectangle matrix by str with \'[rec]T\' generator symbols and rows, columns flags'],
            [[[1,2,3],[2,3,5]],{}, f'2x3 rectangle matrix by list'],
            [[[1,2,3],[2,3,5],[3,3,1]],{}, f'3x3 square matrix by list'],
            [[[1,2,3,4,5]],{}, f'1x5 square matrix by list'],
        ]
        for test in tests:
            try:
                iterator+=1
                Matrix(test[0], test[1])
            except Exception as e:
                print(f'{iterator}) '+test[2] + f': ERROR\n   ||\n   |└--->generator:{test[0]}\n   └--->{e.__repr__()}]\n')
            else:
                print(f'{iterator}) '+test[2] + f': DONE')