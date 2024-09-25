class MatrixError(Exception):
    MM_error_wrong_line_count = 1
    MM_error_inverted_rectangle = 2
    MM_error_zero_determinant = 3
    MM_error_wrong_dimensions = 4
    MM_error_wrong_flags = 5
    MM_error_manual_disabled = 6
    MM_error_wrong_generator_keys = 7
    MM_error_not_enough_numbers = 8
    MM_error_multiply_not_allowed = 9
    def __init__(self, errorCode:int, addition = []):
        error_string = 'test error string'
        match errorCode:
            case MatrixError.MM_error_wrong_line_count: error_string = f'Wrong line count. row != column'
            case MatrixError.MM_error_inverted_rectangle: error_string = f'Error: inverted matrix is not defined for rectangle form'
            case MatrixError.MM_error_zero_determinant: error_string = f'Error: null determinant operation'
            case MatrixError.MM_error_wrong_dimensions: error_string = f'Wrong dimensions'
            case MatrixError.MM_error_wrong_flags: error_string = f'Wrong flags on matrix generation'
            case MatrixError.MM_error_manual_disabled: error_string = f'Error:generator string has a manual settings\' symbols, but manual settings disabled'
            case MatrixError.MM_error_wrong_generator_keys: error_string = f'Error: there are wrong sybols in generator-string'
            case MatrixError.MM_error_not_enough_numbers: error_string = f'Error: not enough numbers to generate matrix'
            case MatrixError.MM_error_multiply_not_allowed: error_string = f'Error: not allowed multiply between matrix and other'
            case _:
                return
        if addition != []:
            error_string += f': not expected \'{addition[0]}\''
        self.args = [error_string]
                

