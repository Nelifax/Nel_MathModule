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
        if samples!=[]:
            for sample in samples:
                if degrees.get(sample[1], 'none') != 'none':
                    if len(degrees[sample[1]]) >= int(sample[2]):
                        degrees[sample[1]][len(degrees[sample[1]])-int(sample[2])] =  float(degrees[sample[1]][len(degrees[sample[1]])-int(sample[2])])+float(sample[0])
                    else:
                        degrees[sample[1]] = [sample[0]] + [0] * (int(sample[2])-len(degrees[sample[1]])-1) + degrees[sample[1]]
                else:
                    degrees[sample[1]] = [sample[0]] + [0]*(int(sample[2])-1)
                equation = equation.replace(f'{sample[0]}{sample[1]}^{sample[2]}', '')
        samples = re.findall(r'([\+\-]*\d*)([A-Za-z])', equation) #^1 calculation
        print(samples)
        if samples!=[]:
            for sample in samples:
                equation = equation.replace(f'{sample[0]}{sample[1]}', '')
                if sample[0] == '+':
                    sample = (1, sample[1])
                elif sample[0] == '-':
                    sample = (-1, sample[1])
                if degrees.get(sample[1], 'none') != 'none':
                    degrees[sample[1]][-1] = float(degrees[sample[1]][-1])+float(sample[0])
                else:
                    degrees[sample[1]] = [int(sample[0])]
                equation = equation.replace(f'{sample[0]}{sample[1]}', '')
        if equation!='':
            samples = re.findall(r'[\+\-]*\d+', equation)
            result = 0
            for sample in samples:
                result = result+float(sample)
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

    def __mul__(self, other)->'Equation':
        if isinstance(other, Equation):
            additions = {}
            results = {}
            for key, value in self.degrees.items():
                for key2, value2 in other.degrees.items():
                    if key == 'free' and key2!='free':
                        result = [0]*len(value2)
                        for i in range(0, len(value2)):
                            result[i] = float(value[0])*float(value2[i])
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
                            result[i] = float(value[i])*float(value2[0])
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
                        results[key] = [float(value[0])*float(value2[0])]
                        continue
                    if key!=key2:
                        continue       
                    results[key] = [0]*(len(value)+len(value2))
                    for i in range(0, len(value)):
                        for j in range (0, len(value2)):
                            results[key][i+j] = results[key][i+j]+float(value[i])*float(value2[j])
            for key, value in additions.items():
                if len(additions[key]) > len(results[key]):
                    results[key] = [0]*(len(additions[key])-len(results[key]))+results[key]
                elif len(additions[key]) < len(results[key]):
                    additions[key] = [0]*(len(results[key])-len(additions[key]))+additions[key]
                for i in range(0, len(additions[key])):
                    results[key][i] = results[key][i]+additions[key][i]
            print(results)




        pass

'''
abc=Equation('2.5x^3+2x^2=2', ['x'])
abb=Equation('1x^2+2x=-2', ['x'])
abc*abb
'''
