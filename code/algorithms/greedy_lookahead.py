import random

def functie(n):
get options
	for i in alle opties:
		bouw de chain
		if n = 1 :
			get score
			
		else:
			functie(n-1)

def algorithm_greedy(chain):

    while len(chain.folds) < len(chain.aminocode):

        # # check previous coordinates in folds
        # options = chain.get_options()
        # while len(options) == 0:
        #     wrong_option = chain.folds[-1]
        #     chain.remove_last_point()
        #     options = chain.get_options() - {wrong_option}

        # score = 100
        # best_point = random.choice(list(options))

        # #print(best_point)
        # if len(chain.hydrophobe) != 0:

        #     list_H = chain.hydrophobe.copy()
        #     # remove current point from hydrophobe list
        #     if chain.folds[-1] in chain.hydrophobe:
        #         list_H.remove(chain.folds[-1])
            
        #     # check all options for best score
        #     index_to_check = len(chain.folds) - 1
        #     aminocode = chain.aminocode[index_to_check]
        #     if len(list_H) != 0 and aminocode != 'H':
        #         for point in options:
        #             distance = dh.distance_to_H(point, list_H)
        #             if distance < score:
        #                 best_point = point
        #                 score = distance
        
        # chain.build(best_point)

        # # add if H to list
        # if chain.aminocode[index_to_check + 1] == 'H':
        #     chain.hydrophobe.append(best_point)

    return chain