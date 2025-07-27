__all__ = ['Lattice2']

import NelMath
from NelMath.objects.linear_algebra.Matrix import Matrix
from NelMath.objects.linear_algebra.Vector import Vector


class Lattice2():
    def __init__(self, vectors=list|Matrix, modulo=0, init_time=0):
        from time import time
        if init_time==0:
            self.init_time=time()
        else:
            self.init_time=init_time
        self.vectors=[]
        self.modulo=modulo
        if isinstance(vectors, NelMath.objects.linear_algebra.Matrix):
            #if vectors._Matrix__flags['rows']!=vectors._Matrix__flags['columns']:
                #raise TimeoutError('Lattice2 must have R^n dimensions')
            for i in range(len(vectors.rows)):
                self.vectors.append(NelMath.objects.linear_algebra.Vector(vectors.rows[i]))
        elif type(vectors)==list and isinstance(vectors[0], NelMath.objects.linear_algebra.Vector):
            self.vectors=vectors
        elif isinstance(vectors,NelMath.objects.applied_algebra.Lattice2):
            for i in range(len(vectors.vectors)):
                self.vectors.append(vectors.vectors[i])
        self._vector_dims=len(self.vectors)

    def GSH_ort(self):
        '''
        Предоставляет процесс ортогонализации Грамма-Шмидта
        '''
        import time
        beg=time.time()
        ort_vectors=[self.vectors[0]]
        for i in range(1,len(self.vectors)):
            ort_vectors.append(self.vectors[i]-Lattice2.proj(self.vectors[i],ort_vectors, self.init_time))                    
            print(f'Программа не умерла, она усиленно считает уже {int(time.time()-self.init_time)}...[GSH_ort]                            ',end='\r')
        return Lattice2(ort_vectors,init_time=self.init_time)

    def proj(v_from, v_to, time_=0):
        '''
        Определяет оператор проекции
        '''
        import time
        beg=time.time()
        #from NelMath.objects.linear_algebra.Vector import Vector
        if isinstance(v_to, Vector) or len(v_to)==1:
            if type(v_to)==list:
                v_to=v_to[0]         
                print(f'Программа не умерла, она усиленно считает уже {int(time.time()-time_)}...[proj]                              ',end='\r')
            return v_to.vec_mul((v_from*v_to)/(v_to*v_to))
        else:
            a = sum((Lattice2.proj(v_from, v_to[i], time_) for i in range(len(v_to))), Vector([0]*len(v_from.data)))
            print(f'Программа не умерла, она усиленно считает уже {int(time.time()-time_)}...[projXproj]                             ',end='\r')
            return a

    def LLL(self, delta=0.75):
        """Алгоритм LLL для редукции решеточного базиса"""
        import time
        beg=time.time()
        A=self.copy()
        B=self.copy().GSH_ort()
        i=2  
        def update_GSH_ort(A,k):
            ort_vectors=A.vectors[0:k]
            ort_vectors+=[A.vectors[i]-Lattice2.proj(A.vectors[i],ort_vectors,self.init_time) for i in range(k,len(A.vectors))]              
            print(f'Программа не умерла, она усиленно считает уже {int(time.time()-self.init_time)}...[GSH_ort]                        ',end='\r')
            return Lattice2(ort_vectors,init_time=self.init_time)
        def calculate_mu(latt,latt_ort):
            mu=[[0] * len(latt.vectors) for _ in range(len(latt.vectors[0].data))]
            mu = [[(v_i * v_j) / (v_j * v_j) for j, v_j in enumerate(latt_ort.vectors)] for i, v_i in enumerate(latt.vectors)]      
            return mu
        def update_mu(mu, kk, latt, latt_ort, mode='k'):
            for e, f in ((e, f) for e in range(kk) for f in range(i if mode == 'k' else i+1)):
                print(f'Программа не умерла, она усиленно считает уже {int(time.time()-self.init_time)}...[mu_upd](i={e},j={f})                      ',end='\r')
                mu[e][f] = (latt.vectors[e]*latt_ort.vectors[f])/(latt_ort.vectors[f]*latt_ort.vectors[f])   
            return mu
        mu=calculate_mu(A,B)
        from NelMath.objects.linear_algebra.Vector import Vector
        while i<len(B.vectors[0].data):
            for j in range(i-1,-1,-1):
                if abs(mu[i][j])>0.5:
                    mu_=abs(mu[i][j])
                    #print(mu[i][j])
                    inverted=False if mu[i][j]>0 else True
                    if '.' in str(mu_) and int(str(mu_).split('.')[1][0])>=5:
                        mu[i][j]=-(int(mu_)+1) if inverted else int(mu_)+1
                    else:
                        mu[i][j]=-int(mu_) if inverted else int(mu_)
                    A.vectors[i]=A.vectors[i].copy()-(A.vectors[j].copy()*mu[i][j])
                    B=update_GSH_ort(A.copy(),i)                    
                    #B=A.copy().GSH_ort()
                    mu=update_mu(mu,i,A,B)
                    #mu=calculate_mu(A,B)
            if (delta-mu[i][i-1]**2)*(Vector.find_length(B.vectors[i-1])**2)<=Vector.find_length(B.vectors[i])**2:
                print(f'Программа не умерла, она усиленно считает уже {int(time.time()-self.init_time)}...[delta](i={i},j={j})                        ',end='\r')
                i=i+1
            else:                
                b=A.vectors[i].copy()
                A.vectors[i]=A.vectors[i-1].copy()
                A.vectors[i-1]=b.copy()
                del(b)
                B=update_GSH_ort(A.copy(),i-1)
                #B=A.copy().GSH_ort()
                mu=update_mu(mu,i,A,B,'k+1')
                #mu=calculate_mu(A,B)
                i=max(i-1,1)
                #i=i-1
            print(f'Программа не умерла, она усиленно считает уже {int(time.time()-self.init_time)}...[LLL-cycle](i={i})                        ',end='\r')
        print(f'                                                                                                 ',end='\r')
        return A
    

    def copy(self):
        #from NelMath.objects.linear_algebra.Matrix import Matrix
        return Lattice2(self.vectors, init_time=self.init_time)


    def zero_vector(self)->'Vector':
        from NelMath import Rational, Vector
        return Vector([Rational(0)]*self._vector_dims)

                


        

    def print(self):
        for i in range(len(self.vectors)):
            print(self.vectors[i])
