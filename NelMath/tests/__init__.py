from .matrix_tests import *
from .fraction_tests import *
from .number_tests import *
from .type_tests import *
from NelMath.properties.settings_handler import SettingsHandler

__all__=['full_test', 'solo_test']

def full_test(report_mode:str='full')->None:
    '''
    start full test of module classes with report_mode
    allowed report_mode:
        full (default) - prints both wrong and correct tests
        short - prints only wrong tests
    '''
    settings=SettingsHandler()
    settings.save_working_settings()
    settings.set_defaults()
    if report_mode not in ['full', 'short']: report_mode='full'
    test_results={
        'all_tests':0,
        'done_tests':0,
        'wrong_tests':0,
        'errors':0
        }
    test_results=matrices_base_test(report_mode,**test_results)
    test_results=fractions_base_test(report_mode,**test_results)
    test_results=number_base_test(report_mode,**test_results)
    test_results=type_test(report_mode,**test_results)
    print(f'-------------------Full test results-------------------')
    print(f'There are {test_results["all_tests"]} tests, with:')
    print(f'    --->{test_results["done_tests"]} "DONE" tests')
    print(f'        --->{test_results["wrong_tests"]} "WRONG" tests')
    print(f'            --->{test_results["errors"]} "ERRORS"')
    print(f'-------------------------------------------------------')    
    settings.release_working_settings()

def solo_test(test_name:str='Rational', report_mode:str='full')->None:
    '''
    start a test for 'class_name' class with report_mode
    allowed tests:
        Rational (default)
        Fraction
        Matrix
    allowed report_mode:
        full (default) - prints both wrong and correct tests
        short - prints only wrong tests
    '''    
    settings=SettingsHandler()
    settings.save_working_settings()
    settings.set_defaults()
    print(settings.get('mm_dynamic_class_changing'))
    if report_mode not in ['full', 'short']: report_mode='full'
    print(f'Starting a test for {test_name} class with report_mode:{report_mode}')
    print('------------------------------------')
    match(test_name):
        case 'Fraction':
            fractions_base_test(report_mode)
        case 'Matrix':
            matrices_base_test(report_mode)
        case 'Number':
            number_base_test(report_mode)
        case 'Type':
            type_test(report_mode)
        case _:
            print(f'No such test: {test_name} found')
    settings.release_working_settings()