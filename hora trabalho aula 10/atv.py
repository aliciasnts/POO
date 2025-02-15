import random

class RandomTester:
    
    # imprime um número aleatório
    def printOneRandom(self):
        print(random.random())
    
    # imprime vários npumeros aleatórios
    def printMultiRandom(self, many):
        for _ in range(many):
            print(random.random())
    
    # simulação de um dado (retorna um número entre 1 e 6)
    def throwDice(self):
        return random.randint(1, 6)
    
    #gera um número aleatório entre 1 e max
    def randomUpTo(self, max):
        return random.randint(1, max)
    
    # gera um número aleatório entre min e max 
    def randomRange(self, min, max):
        return random.randint(min, max)
    
    # usa randomUpTo para gerar um número entre 1 e max
    def randomUpToUsingRandomRange(self, max):
        return self.randomRange(1, max)


tester = RandomTester()
tester.printOneRandom()
tester.printMultiRandom(5)
tester.throwDice()
tester.randomUpTo(10)
tester.randomRange(5, 15)
tester.randomUpToUsingRandomRange(20)