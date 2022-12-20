# Genetic-Algorithm
The genetic algorithm is comprised of 6 central features: <br />
	&nbsp;&nbsp;1. A randomized initial population (size 100)<br />
	&nbsp;&nbsp;2. A fitness function, which both prescribes a fitness score to each individual in the
	the population and orders the fitness scores in preparation for culling <br />
	&nbsp;&nbsp;3. The culling selection mechanism that eliminates the bottom half of individuals in the  
	population (culling_rate = .5)<br />
	&nbsp;&nbsp;4. A reproduction function to re-populate after each gen's culling <br />
	&nbsp;&nbsp;5. Mutation (mutation_rate = .01)<br />
	&nbsp;&nbsp;6. An Iterator, with a break point to end each generation (convergence = 200)<br />
<br />
To set up the environment, a box class was created to instantiate the 12 input boxes. The algorithm is looped over 10 times to represent 10 different generations. The four toggles for this algorithm -- mutation_rate, convergence, generation number, and initial population -- can all be found in the for loop at the bottom of python file.     
