class SettingsHandler():
    __instance = None
    __created = False
    __custom_settings_file = ''
    settings=[]

    def __new__(cls, custom_settings_file_path:str=''):
        if cls.__instance is None:
            cls.__instance = super(SettingsHandler, cls).__new__(cls)
        return cls.__instance

    def __init__(self, custom_settings_file_path:str=''):
        if not self.__created:
            self.__custom_settings_file = custom_settings_file_path
            self.__created = True

    def __check_settings(self, path):
        pass

    @staticmethod
    def get_settings_file(path):
        '''
        generates settings-file on custom path to change settings manually
        '''
    def update_settings_from_file(self, path):
        '''
        updates settings from custom file. 
        --Setting present in file but not in programm will skipped
        --Setting present in programm but not in file will use default values
        ---If some setting has an error handler will use default values
        --All precision settings that present in programm both file will update if they correct
        '''