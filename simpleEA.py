import random

# EA的简单实现
class EA:
    def __init__(self,population_size=4,mutation_possibility=0.5,epoch=10) -> None:
        self.mutation_possibility=mutation_possibility
        self.epoch=epoch
        self.population_size=population_size
        self.solution=self.init()
        self.fittness=[]
        self.bestSoFarFit=0
        self.bestSoFarSolution=""
    
    def solution_encoder(self,x):
        # 将可用于计算的值映射到解空间
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

    def solution_decoder(self,x):
        # 将基因型转化为可用于计算的值
        res=0
        for i in x:
            res=(res*2+int(i))
        return res
        
    def init(self):
        # 初始化solution
        init_value = [x for x in range(32)]
        random.shuffle(init_value)
        init_solution=[self.solution_encoder(x) for x in init_value[:self.population_size]]
        return init_solution
        
    def objFunc(self,x):
        # 目标函数
        x=self.solution_decoder(x)
        return x**2
            
    def crossover(self,x1,x2):
        # 杂交方法，在随机位点对接两个solution的片段
        k=random.randint(1,3)
        # print(k)
        x=x1[:k]+x2[k:]
        return x
    
    def mutation(self,x):
        # 变异方法：以mutation_possibility概率翻转随机bit
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
        # 评估每一代solution，并更新bestSofarXX
        self.fittness= [self.objFunc(x) for x in self.solution]
        max_tmp=max(self.fittness)
        if max_tmp>self.bestSoFarFit:
            i=self.fittness.index(max_tmp)
            self.bestSoFarFit=max_tmp
            self.bestSoFarSolution=self.solution[i]

    def select(self):
        # 选择方法
        intermediat=[]
        self.evaluate()
        popu_sum=sum(self.fittness)
        for i in range(2):
            k=random.randint(0,popu_sum-1)
            tmp=0
            for j in range(len(self.fittness)):
                tmp+=self.fittness[j]
                if k<=tmp:                   
                    intermediat.append(self.solution[j])
                    break
        return intermediat
    
    def next_generation(self):
        #生成下一代的方法，包括了选择，杂交，变异
        tmp=[]
        for i in range(len(self.solution)):
            s=self.select()
            k=self.crossover(*s)
            k=self.mutation(k)
            tmp.append(k)
        self.solution=tmp
    
    def run(self):
        # 进行epoch次迭代，并输出每一代solution和bestSofarFit和bestSofarSolution
        for i in range(self.epoch):
            self.next_generation()
            print("in the %d-th generaion: the best fitness is"%i,self.bestSoFarFit,"and the best solution is ",self.bestSoFarSolution,"in ",self.solution)
            
if __name__ == '__main__':
    ea=EA()
    ea.run()
    
    