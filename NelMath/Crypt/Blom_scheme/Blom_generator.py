from NelMath.objects.math_base.Rational import Rational
from NelMath.objects.linear_algebra import Matrix
__all__=['Blom_generator']
class Blom_generator():
    def __init__(self, participants:int|Rational, min_parts:int|Rational):
        self.participants = participants
        self.min_parts = min_parts
        self.operated_cypher=''
        self.key_matrix=''
        self.keys=[]

    def initiate(self, str_to_encrypt:str):


