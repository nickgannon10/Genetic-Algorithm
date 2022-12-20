import random
import numpy as np
from operator import itemgetter

#create box
class box: 
    def __init__(self, box_num, weight, value): 
        self.box_num = box_num
        self.weight = weight
        self.value = value 

    def __repr__(self): 
        return "Box Number: % s, Weight: % s, Value: % s  " % (self.box_num, self.weight, self.value)

box_array = np.array([box(1, 20, 6), box(2, 30, 5), box(3, 60, 8), box(4, 90, 7), box(5, 50, 6),
  box(6, 70, 9), box(7, 30, 4), box(8, 30, 5), box(9, 70, 4), box(10, 20, 9), box(11, 20, 2), 
  box(12, 60, 1)])

class genetic_algorithm:
    def __init__(self, convergence = 100, cull_rate = .5, mutation_rate = .01):
        self.convergence = convergence
        self.cull_rate = cull_rate
        self.mutation_rate = mutation_rate
    
    #create one instance and iterate over that to get desired pop size
    def initial_population(self, size): 
        initial_pop = []
        for n in range(size): 
            rand_ind = list(np.random.choice(a=[False, True], size=(12)))
            initial_pop.append(rand_ind)
        return initial_pop

    #for GA, I'm making fitness a function of only value, but it must account for overweight knapsacks 
    def survival_ot_fittest(self, boxes_present): 
        fitness, weight, value = 0, 0, 0
        for i in boxes_present: 
            value += i.value
            weight += i.weight
        over = max(0, weight - 250)
        fitness = value - over
        return fitness, value, weight

    #fitness function, orders population by value, largest to smallest, returns individual and value
    def fitness_heirarchy(self, initial_pop): 
        value_order = []
        for node in initial_pop: 
            fitness, value, weight = self.survival_ot_fittest(box_array[node])
            value_order.append((node, fitness, value, weight))
        final_val_order = sorted(value_order, key=itemgetter(1), reverse = True)
        init_pop = [element[0] for element in final_val_order]
        fitness = final_val_order[0][1]
        return init_pop, fitness
    
    #consolidation: includes mutations, culling, and generation iteration  
    def run(self, initial_pop): 
        iter = 0 
        fittest_ind = 0
        fittest_score = 0  
        while True:
            initial_pop, fitness = self.fitness_heirarchy(initial_pop)
            if fitness > fittest_score: 
                fittest_ind = initial_pop[0]
                fittest_score = fitness 
            #eliminate bottom half of the population
            cull = int(len(initial_pop)*.5)
            pop_next = initial_pop[:cull]
            #re-populate after the culling  
            for i in range(50):
                p_1, p_2 = random.sample(pop_next, 2)
                crosser = random.randint(1, 12)
                b_1 = p_1[:crosser] + p_2[crosser:]
                b_2 = p_2[:crosser] + p_1[crosser:]
                #switch True to False for random mutation
                if (np.random.uniform(0, 1) < self.mutation_rate): 
                    mutation = random.randint(0, len(b_1)-1)
                    b_1[mutation] = not b_1[mutation]
                pop_next.append(b_1)
            initial_pop = pop_next
            iter += 1
            #must have convergence, as improvements will reach asymtote
            if iter > self.convergence:
                break
        return fittest_ind, iter
    
#present algorithm with surrounding context 
for i in range(10): 
    gen_alg = genetic_algorithm(mutation_rate=.01, convergence=200)
    initial_pop = gen_alg.initial_population(100)
    best, iter = gen_alg.run(initial_pop)
    print("Genetic Algorithm: Generation {:2d} of 10".format(i+1, 10))
    print("Best Individual's Genotype in Population:")
    for box in box_array[best]:
        print(box)
    fitness, value, weight = gen_alg.survival_ot_fittest(box_array[best])
    print("Fitness Value: {}".format(fitness))

                




        

    









    








    




