
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out
from code.algorithms import depth_first as df
from code.algorithms import random as rnd
from code.algorithms import greedy_distance as gd
from code.algorithms import greedy_gravity as gg
from code.algorithms import hill_climber as hc

def main():    
    # Ask user for input chain
    print("Welcome to Protein Po(w)der, fill in the following variables to get solutions")
    aminocode = input("Chain: ").upper()

    # Ask for algorithm
    algoritm = int(input("Pick a number to choose an algoritm: (1) Random, (2) Depth First, (3) Greedy Distance, (4) Greedy Gravity, (5) Hill Climber \n"))

    # Ask for amount of dimensions
    dimensions = int(input("How many dimensions can the chain occupy (choose between 2 and 3)?\n"))

    # Build protein chain
    chain = ch.Chain(aminocode, dimensions)

    # Perform choosen algoritm
    if algoritm == 1:
        #---------------------------------- Random -------------------------------------------
        chain_result = rnd.algorithm_random(chain)

    elif algoritm == 2:
        #--------------------------------- Depth First ----------------------------------------
        depth_first = df.DepthFirst(chain)
        depth_first.run()
        chain_result = depth_first.chain

    elif algoritm == 3:
        #-------------------------------- Greedy Distance --------------------------------------
        greedy_distance = gd.GreedyDistance(chain)
        greedy_distance.run()
        chain_result = greedy_distance.chain

    elif algoritm == 4:
        #--------------------------------- Greedy Gravity ---------------------------------------
        greedy_gravity = gg.GreedyGravity(chain)
        greedy_gravity.run()
        chain_result = greedy_gravity.chain

    else:
        #--------------------------------- Hill Climber -----------------------------------------
        hillclimber = hc.HillClimber(chain, 7, 200)
        hillclimber.run()
        chain_result = hillclimber.chain

    # visualize protein chain
    vis.visualisation(chain_result)

    # store protein data into csv
    out.outputwriter(chain_result.folds, aminocode, chain_result)

if __name__ == "__main__":
    main()

"""
HHPHHHPHPHHHPH
HPHPPHHPHPPHPHHPPHPH
PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP
HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH
"""

"""
PPCHHPPCHPPPPCHHHHCHHPPHHPPPPHHPPHPP
CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC
HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH
HCPHPHPHCHHHHPCCPPHPPPHPPPPCPPPHPPPHPHHHHCHPHPHPHH
"""
