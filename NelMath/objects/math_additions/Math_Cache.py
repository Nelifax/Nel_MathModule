__all__=['Math_Cache']
from NelMath.properties.settings_handler import SettingsHandler
settings=SettingsHandler()

class Math_Cache():
    def __init__(self,path=settings.get('mm_math_cache_path')):
        with open(path,'w+'):
            pass
