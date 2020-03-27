import random

from src.sapt5.fcOptimisGA.utils import generateNewValue


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__fitness = 0.0
        self.__repres = []
        for i in range(0, self.__problParam['noDim']):
            self.__repres.append(i+1)
        random.shuffle(self.__repres)

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        newrepres = []
        # se alege nodul al carui cluster va fi selectat
        poz = random.randint(0, len(self.__repres) - 1)
        # se gaseste cluster-ul
        cluster = self.__repres[poz]
        update = []
        # se gasesc pozitiile din cromozomul sursa care se vor modifica
        for i in range(len(self.__repres)):
            if self.__repres[i] == cluster:
                update.append(i)

        # se modifica valorile comunitatilor din cromozomul destinatie
        for j in range(0, len(self.__repres)):
            if j in update:
                newrepres.append(cluster)
            else:
                newrepres.append(c.__repres[j])

        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def binomial_crossover(self, c):
        newrepres = []
        for i in range(len(self.__repres)):
            r = generateNewValue(0, len(self.__repres))
            j = random.uniform(0.0, 1.0)
            if r == i or j <= self.__problParam['cr']:
                newrepres.append(c.__repres[i])
            else:
                newrepres.append(self.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutationNew(self):
        i = random.randint(0, len(self.__repres) - 1)
        j = random.randint(0, len(self.__repres) - 1)
        self.__repres[j] = self.__repres[i]

    def initPopulation(self):
        nrComm = 1
        noNodes = int(self.__problParam['alpha'] * self.__problParam['noDim'])
        for i in range(0, noNodes):
            nodePos = random.randint(0, self.__problParam['noDim'] - 1)
            for j in range(0, len(self.__problParam['mat'][nodePos])):
                self.__repres[nodePos] = nrComm
                if self.__problParam['mat'][nodePos][j] == 1:
                    self.__repres[j] = nrComm
            nrComm += 1

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
