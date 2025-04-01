settings={
#module settings
    'mm_number_floordiv_ceiling_up': True, 
    #if True then set sage-like ceiling ex:7//-5=-2. If false then set logic ceiling ex:7//-5=-1 
#math base settings
    'mm_max_float_part':5,
    'mm_dynamic_class_changing': False,
    'mm_modulo_negative_results': True,
    #if True then set a%b operation result as -c when a>b (python-like behavior). If False then set a%b operation always positive
#crypto settings
    'mm_minimum_key_value' : 2,
    'mm_maximum_key_value' : 2147483648,
    'mm_key_only_primals' : True,
    'mm_key_enable_number_repeating' : True,
    'mm_key_maximum_repeat_count' : -1,
#funcion settings
    'mm_MR_prime_max_tries' : 10, #equivalent to (1/2)^t mistake chance
    'mm_MR_prime_high_candidate_border': 100,
}