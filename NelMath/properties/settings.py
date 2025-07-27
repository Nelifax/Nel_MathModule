settings={
#module settings
    'mm_number_floordiv_ceiling_up': True, 
    #if True then set sage-like ceiling ex:7//-5=-2. If False then set logic ceiling ex:7//-5=-1 
#math base settings
    'mm_max_float_part':10,
    'mm_dynamic_class_changing': False,
    'mm_modulo_negative_results': True,
    #if True then set a%b operation result as -c when a>b (python-like behavior). If False then set a%b operation always positive
#linear_algebra settings
    'mm_vector_auto_calculations': False,
    'mm_vector_auto_calculated_values':[
                                        ],
    'mm_matrix_auto_calculations': False,
    'mm_matrix_auto_calculated_values':['determinant' #some combination of [determinant, rank]
                                        'rank'
                                        ],
#crypto settings
    'mm_minimum_key_value' : 2,
    'mm_maximum_key_value' : 2147483648,
    'mm_key_only_primals' : True,
    'mm_key_enable_number_repeating' : True,
    'mm_key_maximum_repeat_count' : -1,
#funcion settings
    'mm_MR_prime_max_tries' : 10, #equivalent to (1/2)^t mistake chance
    'mm_MR_prime_high_candidate_border': 100,
#factorization settings
    'mm_prefered_factorization_algorythm': 'squfof', #can be squfof (square form factorization) or LPS (Lenstra–Pomerance–Schnorr lattice-based factorization)
    'mm_LPS_max_trials': 10,
    'mm_ECM_B_border': 0,  #if 0 then B calculated automatically else set B-border
    'mm_ECM_curve_trials': 20, #defines curve-factorization trials
#math cache settings
    'mm_use_operation_cache': True,
    'mm_cached_operations': [],
    'mm_math_cache_path' : 'math_cache.txt',
    'mm_is_cache_expiring' : False,
    #if True then cache will have expiring time
    'mm_cache_expiring_time': None,
    #set cache expiring time in minutes. None - make cache never-expiring
    'mm_cache_expired_tries': None,
    #set cache expiring time in program launches. None - make cache never-expiring
}