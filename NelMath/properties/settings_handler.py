class SettingsHandler():
    __instance = None
    __created = False
    __custom_settings_file = ''
    __settings={}


    def __new__(cls, custom_settings_file_path:str=''):
        if cls.__instance is None:
            cls.__instance = super(SettingsHandler, cls).__new__(cls)
        return cls.__instance

    def __init__(self, custom_settings_file_path:str=''):
        if not self.__created:
            self.__custom_settings_file = custom_settings_file_path
            self.__created = True            
            if SettingsHandler.__settings=={}:
                from .settings import settings
                SettingsHandler.__settings=settings

    def __check_settings(self, path=''):
        pass

    @staticmethod
    def save_working_settings():
        SettingsHandler.__instance.__working=SettingsHandler.__instance.__settings

    @staticmethod
    def release_working_settings():
        if SettingsHandler.__instance.__working:
            SettingsHandler.__instance.__settings=SettingsHandler.__instance.__working
            del(SettingsHandler.__instance.__working)
    
    @staticmethod
    def release_settings_file(path):
        '''
        generates settings-file on custom path to change settings manually
        '''
        pass
        
    def update_settings_from_file(self, path):
        '''
        updates settings from custom file. 
        --Setting present in file but not in programm will skipped
        --Setting present in programm but not in file will use default values
        ---If some setting has an error handler will use default values
        --All precision settings that present in programm both file will update if they correct
        '''
        pass
    
    @staticmethod
    def get(key):
        '''
        returns setting by it's key or None if setting isn't present in handler
        '''
        if key in SettingsHandler.__instance.__settings.keys():
            return SettingsHandler.__instance.__settings[key]
        return None

    def set_defaults(self)->None:
        '''
        set settings to a default values for a working space
        '''
        default_settings={
                'mm_number_floordiv_ceiling_up': False,
                'mm_max_float_part':10,
                'mm_dynamic_class_changing': False,
                'mm_minimum_key_value' : 2,
                'mm_maximum_key_value' : 2147483648,
                'mm_key_only_primals' : True,
                'mm_key_enable_number_repeating' : True,
                'mm_key_maximum_repeat_count' : -1,                
                'mm_MR_prime_max_tries' : 10,
                'mm_MR_prime_high_candidate_border': 100,
            }
        self.__settings=default_settings

    def change_setting(self, key:str, value:any)->None:
        '''
        changes a setting not applied this to a setting file. Useful for testing or for some situations
        '''
        if key in self.__settings.keys():
            self.__settings[key]=value