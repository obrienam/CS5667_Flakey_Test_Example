import random
class driver:
    x=[1,2,3,4,5]
    
    def getOutput(self):
        num=random.choice(self.x)
        self.x.remove(num)
        return num
if __name__=='__main__':
    test=driver()
    for i in range(5):
        print(test.getOutput())