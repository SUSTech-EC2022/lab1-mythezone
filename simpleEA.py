import random




def solution_encoder(x):
    s=""
    while x>0:
        tmp=x%2
        x=x//2
        s=str(tmp)+s 
    if len(s)<5:
        k=5-len(s)
        for i in range(k):
            s="0"+s
    return s

def solution_decoder(x):
    res=0
    for i in x:
        res=(res*2+int(i))
    return res

class EA:
    def __init__(self,mutation_possibility=0.5,epoch=10) -> None:
        self.mutation_possibility=mutation_possibility
        self.epoch=epoch
        self.solution=self.init()
        self.fittness=[]
        self.bestSoFarFit=0
        self.bestSoFarSolution=""
        
        
    def init(self):
        init_value = [x for x in range(32)]
        random.shuffle(init_value)
        init_solution=[solution_encoder(x) for x in init_value[:5]]
        return init_solution
        
    def objFunc(self,x):
        x=solution_decoder(x)
        return x**2
    
    def loop(self):
        for i in range(self.nGen):
            pass
            
    def crossover(self,x1,x2):
        k=random.randint(1,3)
        # print(k)
        x=x1[:k]+x2[k:]
        return x
    
    def mutation(self,x):
        res=""
        if random.random()<self.mutation_possibility:
            k=random.randint(0,4)
            xx=[i for i in x]
            if xx[k]=='1':
                xx[k]='0'
            else:
                xx[k]='1'
            for i in xx:
                res+=i
        else:
            res=x
        return res
            
    def evaluate(self):
        self.fittness= [self.objFunc(x) for x in self.solution]
        max_tmp=max(self.fittness)
        if max_tmp>self.bestSoFarFit:
            i=self.fittness.index(max_tmp)
            self.bestSoFarFit=max_tmp
            self.bestSoFarSolution=self.solution[i]

    def select(self):
        intermediat=[]
        self.evaluate()
        popu_sum=sum(self.fittness)
        # print(self.fittness)
        for i in range(2):
            k=random.randint(0,popu_sum-1)
            # print(k)
            tmp=0
            for j in range(len(self.fittness)):
                tmp+=self.fittness[j]
                if k<=tmp:
                    
                    intermediat.append(self.solution[j])
                    # print(intermediat)
                    break
        return intermediat
    
    def next_generation(self):
        tmp=[]
        for i in range(len(self.solution)):
            s=self.select()
            k=self.crossover(*s)
            k=self.mutation(k)
            tmp.append(k)
        self.solution=tmp
    
    def loop(self):
        for i in range(self.epoch):
            self.next_generation()
            
            print("in the %d-th generaion: the best fitness is"%i,self.bestSoFarFit,"and the best solution is ",self.bestSoFarSolution,"in ",self.solution)
            
            
            
            
            

if __name__ == '__main__':
    ea=EA()
    ea.loop()
    
    