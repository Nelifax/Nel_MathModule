__all__ = ['Point']

class Point():
    def __init__(self, coords:dict, modulo=None):
        for param in coords.keys():
            if type(param)!=str or len(param)>2:
                raise TimeoutError()
        self.params=coords.keys()
        for param, value in coords.items():
            exec(f'self.{param}=value')
        self.modulo=modulo

    def __mul__(self, other):
        result={}
        if isinstance(other, Point):
            if self.modulo!=None:
                for param in self.params:
                    result[param]=getattr(self, param)*getattr(other,param)%self.modulo
            else:
                for param in self.params:
                    result[param]=getattr(self, param)*getattr(other,param)
        print(result)
        return Point(result)

