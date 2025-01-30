settings={
#module settings
    'mm_use_pregenerated_data':True,
    'mm_pregenerated_data':{
        'pd_primals':True,
        'pd_factors':True,
        'pd_constants':True
        },
#math base settings
    'mm_max_float_part':4,
    'mm_dynamic_class_changing': False,
#crypto settings
    'mm_minimum_key_value' : 2,
    'mm_maximum_key_value' : 2147483648,
    'mm_key_only_primals' : True,
    'mm_key_enable_number_repeating' : True,
    'mm_key_maximum_repeat_count' : -1,
#funcion settings
    'mm_MR_prime_max_tries' : 10,
    'mm_MR_prime_high_candidate_border': 100,
}