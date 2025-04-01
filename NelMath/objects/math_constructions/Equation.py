import re

class Equation():
    def __init__(self, equation:str, parameters:list, values:dict = {}):
        '''
        provides base class to work with equations
        parameters:
            :equation(str) - string representation of equation ex: 2x^3+3y-7=0
            :parameters(list) - list that contains all parameters literals of the equation ex: [x,y]
            :values(dict) - dictionary that contains all values of parameters ex:{'x':3, 'y':4}
                it must be useful for check up solutions default = {} [no values]
        methods:
            .solve() - try to solve an equation. not working for several parameters
            .generate([values]) - try to generate an equation with roots == values
        '''
        var_string = equation.translate(str.maketrans('', '', '0123456789+-^=()*/'))
        self.variables = list(set(list(var_string))).sort()
        if self.variables != parameters.sort():
            raise TimeoutError()
        equation = equation.split('=')
        for i in range(0, len(equation[1])):
            if equation[1][i] == '+':
                equation[1] = equation[1][:i]+'-'+equation[1][i+1:]
                continue
            elif equation[1][i] == '-':
                equation[1] = equation[1][:i]+'+'+equation[1][i+1:]
                continue
        if equation[1][0] != '-' and equation[1][0] != '+':
            equation[1] = '-'+equation[1]
        #print('----------')
        #print(equation)
        if equation[1] == '0' or equation[1] == 0:
            equation = equation[0]            
        else:
            equation[1] = '='+equation[1]
            equation = ''.join(equation)
        #print(equation)
        samples = re.findall(r'([\+\-]*\d*.\d*)([\+\-A-Za-z])\^(\d*)', equation) #degree calculation
        #print(samples)
        degrees = {}
        from NelMath.objects.math_base.Rational import Rational
        if samples!=[]:
            for sample in samples:
                sample=list(sample)
                sample[0]=sample[0].replace('+-','-')
                sample[0]=sample[0].replace('-+','-')
                sample[0]=sample[0].replace('--','+')
                sample[0]=sample[0].replace('++','+')
                if degrees.get(sample[1], 'none') != 'none':
                    if len(degrees[sample[1]]) >= Rational(sample[2]):
                        degrees[sample[1]][len(degrees[sample[1]])-Rational(sample[2])] =  Rational(degrees[sample[1]][len(degrees[sample[1]])-Rational(sample[2])])+Rational(sample[0])
                    else:
                        degrees[sample[1]] = [sample[0]] + [0] * (Rational(sample[2])-len(degrees[sample[1]])-1) + degrees[sample[1]]
                else:
                    degrees[sample[1]] = [sample[0]] + [0]*(int(sample[2])-1)
                equation = equation.replace(f'{sample[0]}{sample[1]}^{sample[2]}', '')
        samples = re.findall(r'([\+\-]*\d*)([A-Za-z])', equation) #^1 calculation
        #print(samples)
        if samples!=[]:
            for sample in samples:                            
                sample=list(sample)
                sample[0]=sample[0].replace('+-','-')
                sample[0]=sample[0].replace('-+','-')
                sample[0]=sample[0].replace('--','+')
                sample[0]=sample[0].replace('++','+')
                equation = equation.replace(f'{sample[0]}{sample[1]}', '')
                if sample[0] == '+':
                    sample = (1, sample[1])
                elif sample[0] == '-':
                    sample = (-1, sample[1])
                if degrees.get(sample[1], 'none') != 'none':
                    degrees[sample[1]][-1] = Rational(degrees[sample[1]][-1])+Rational(sample[0])
                else:
                    degrees[sample[1]] = [Rational(sample[0])]
                equation = equation.replace(f'{sample[0]}{sample[1]}', '')
        if equation!='':
            samples = re.findall(r'[\+\-]*\d+', equation)
            result = Rational(0)
            for sample in samples: 
                while '++' in sample or '--' in sample or '-+' in sample or '+-' in sample:
                    sample=sample.replace('++','+')
                    sample=sample.replace('--','+')
                    sample=sample.replace('-+','-')
                    sample=sample.replace('+-','-')
                result = result+Rational(sample)
            degrees['free'] = [result]
        self.degrees = degrees

    def build(self):
        equation = ''
        for key, value in self.degrees.items():
            iterator = 0
            for coef in value:                
                coef = float(coef)
                if set(list(str(coef).split('.')[1])) == {'0'}:
                    coef = int(coef)
                if coef == 0:
                    continue
                if float(coef)<0:
                    equation+=str(coef)+key
                else:
                    equation+='+'+str(coef)+key
                if len(value)-iterator > 1:
                    equation+='^'+str(len(value)-iterator)
                iterator+=1
        if self.degrees.get('free', 'none') != 'none':
            freeValue= -float(self.degrees['free'])
            equation+=f'={freeValue}'
        else:
            equation+='=0'
        if equation[0] == '+':
            equation = equation[1:]
        return equation

    def substitute(self)->'Equation':
        pass
    
    def solve(self)->dict:
        pass
        
    def get_coefficients(self)->list:
        pass

    def generate(values:list)->'Equation':
        pass

    def __rmul__(self, other):
        return self*other

    def __mul__(self, other, modulo=None)->'Equation':        
        from NelMath.objects.math_base.Rational import Rational
        if isinstance(other, Equation):
            additions = {}
            results = {}
            for key, value in self.degrees.items():
                for key2, value2 in other.degrees.items():
                    if key == 'free' and key2!='free':
                        result = [0]*len(value2)
                        for i in range(0, len(value2)):
                            result[i] = Rational(value[0])*Rational(value2[i])
                        if additions.get(key2,'none') != 'none':
                            if len(additions[key2]) > len(result):
                                result = [0]*(len(additions[key2])-len(result))+result
                            elif len(additions[key2]) < len(result):
                                additions[key2] = [0]*(len(result)-len(additions[key2]))+additions[key2]
                            for i in range(0, len(additions[key2])):
                                additions[key2][i] = additions[key2][i] + result[i]
                        else:
                            additions[key2] = result
                        continue
                    if key != 'free' and key2=='free':
                        result = [0]*len(value)
                        for i in range(0, len(value)):
                            result[i] = Rational(value[i])*Rational(value2[0])
                        if additions.get(key,'none') != 'none':
                            if len(additions[key]) > len(result):
                                result = [0]*(len(additions[key])-len(result))+result
                            elif len(additions[key]) < len(result):
                                additions[key] = [0]*(len(result)-len(additions[key]))+additions[key]
                            for i in range(0, len(additions[key])):
                                additions[key][i] = additions[key][i] + result[i]
                        else:
                            additions[key] = result
                        continue
                    if key == key2 and key == 'free':
                        results[key] = [Rational(value[0])*Rational(value2[0])]
                        continue
                    if key!=key2:
                        continue       
                    results[key] = [0]*(len(value)+len(value2))
                    for i in range(0, len(value)):
                        for j in range (0, len(value2)):
                            results[key][i+j] = results[key][i+j]+Rational(value[i])*Rational(value2[j])
            for key, value in additions.items():
                if len(additions[key]) > len(results[key]):
                    results[key] = [0]*(len(additions[key])-len(results[key]))+results[key]
                elif len(additions[key]) < len(results[key]):
                    additions[key] = [0]*(len(results[key])-len(additions[key]))+additions[key]
                for i in range(0, len(additions[key])):
                    results[key][i] = results[key][i]+additions[key][i]            
        elif isinstance(other, int) or isinstance(other, Rational):
            value=Rational(other)
            results = {}
            for key, coef in self.degrees.items():   
                results[key]=[]
                for i in range(0,len(coef)):
                    result=coef[i]*value if modulo==None else (coef[i]*value)%modulo
                    results[key].append(result)
        strEq=''
        var=[]
        for variable, degrees in results.items():                
            if var==[] and variable!='free':
                var.append(variable)
            if variable=='free':
                strEq=strEq[0:-1]
                if degrees[0].sign=='-':
                    strEq+=f"{degrees[0]}=0"
                else:
                    strEq+=f"+{degrees[0]}=0"
            else:
                for i in range(0,len(degrees)):
                    if degrees[i]==0:
                        continue
                    else:
                        strEq+=f'{degrees[i]}{variable}^{len(degrees)-i}+'
        return Equation(strEq,var)

    def get_coefficient_vector(self):
        from NelMath.objects.math_base.Rational import Rational
        from NelMath.objects.linear_algebra.Vector import Vector
        new_vector=[]
        if len(self.degrees.keys())==2:
            for variable, degrees in self.degrees.items(): 
                if variable!='free':
                    for i in range(0, len(degrees)):
                        new_vector.append(Rational(degrees[i]))
                if variable=='free':
                    new_vector.append(Rational(degrees[0]))
            return Vector(new_vector)
        else:
            raise TimeoutError()

    def copy(self):
        strEq=''
        var=[]
        for variable, degrees in self.degrees.items():                
            if var==[] and variable!='free':
                var.append(variable)
            if variable=='free':
                strEq=strEq[0:-1]
                if degrees[0].sign=='-':
                    strEq+=f"{degrees[0]}=0"
                else:
                    strEq+=f"+{degrees[0]}=0"
            else:
                for i in range(0,len(degrees)):
                    if degrees[i]==0:
                        continue
                    else:
                        strEq+=f'{degrees[i]}{variable}^{len(degrees)-i}+'
        return Equation(strEq,var)

    def __pow__(self,exponent):
        from NelMath.objects.math_base.Rational import Rational
        a=self.copy()
        if exponent==0:
            return Rational(1)
        if exponent==1:
            return a
        if exponent==2:
            return a*a
        return a*pow(self,exponent-1)


    def print(self):
        for variable, degrees in self.degrees.items():
            print(variable)
            if variable=='free':
                print(self.degrees['free'])
            else:
                for i in range(0,len(degrees)):
                    print(f'{variable}^{len(degrees)-i}:{degrees[i]}')
'''
abc=Equation('2.5x^3+2x^2=2', ['x'])
abb=Equation('1x^2+2x=-2', ['x'])
abc*abb
'''
