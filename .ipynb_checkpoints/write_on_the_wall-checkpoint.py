from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
#import pygame
import pickle
from TxGraffiti.functions.heuristics import Theo
from TxGraffiti.functions.get_conjectures import *


__version__ = '0.0.2'

valid_invariants = {1: 'domination_number',
                    2: 'total_domination_number',
                    3: 'connected_domination_number',
                    4: 'independence_number',
                    5: 'independent_domination_number',
                    6: 'zero_forcing_number',
                    7: 'power_domination_number',
                    8: 'matching_number', 
                    9: 'min_maximal_matching_number',
                    10: 'chromatic_number',
                    11: 'clique_number',
                    12: 'triameter', 
                    13: 'atom_bond_connectivity_index'}

graph_properties = {1 : 'is_connected',
                    2 : 'is_regular',
                    3 : 'is_cubic',
                    4 : 'is_planar',
                    5 : 'is_not_K_n',
                    6 : 'is_triangle_free',
                    7 : 'is_eulerian',
                    8 : 'is_distance_regular',
                    9 : 'is_strongly_regular',
                    10: 'is_bipartite'
                    }               


def main():
    print(figlet_format('TxGRAFFITI', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2019 Randy Davila')
    print()

    print('The invariants you may conjecture against are: ')
    print('-----------------------------------------------')
    print()
    i = 1


    for x in valid_invariants:
        print(f'{i}. {valid_invariants[x]}')
        i+=1
        print()
    print('-----------------------------------------------')
    print()
    invariant = valid_invariants[int(input('Invariant: '))]
    print()

    try:
        with open(f'TxGraffiti/conjectures/{invariant}_conjectures', 'rb') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error, '. Specified database not found in conjectures directory.')
        return None

    parameter_quest = input('Would you like to specify a graph structural property to focus on? (y/n) ')
    print()
    if parameter_quest == 'y':
        for x in graph_properties:
            print(f'{x}. {graph_properties[x]}')
            print()
        parameter = graph_properties[int(input('Please specify the structural property you are interested in: '))]
        
        conjectures = get_conjectures(invariant)
        U = Theo([x for x in conjectures['upper'] if parameter in x.hyp.properties])
        L = Theo([x for x in conjectures['lower'] if parameter in x.hyp.properties])
        print()

        print('Upper Bounds')
        for i in range(15):
            print(f'Conjecture {i}. {U[i]}')
            print('')
        print()
        print('Lower Bounds')
        for i in range(15):
            print(f'Conjecture {i}. {L[i]}')
            print('')
        print()

        work = input('Remove conjectures? (y/n) ')
        while work == 'y':
            type = input('Upper or lower? (U/L) ')
            index = int(input('Conjecture label? '))
            if type == 'U':
                U.pop(index)
            else:
                L.pop(index)
            print('Upper Bounds')
            for i in range(15):
                print(f'Conjecture {i}. {U[i]}')
                print('')
            print()
            print('Lower Bounds')
            for i in range(15):
                print(f'Conjecture {i}. {L[i]}')
                print('')
            print()

            work = input('Remove conjectures? (y/n) ')

    else:
        conjectures = get_conjectures(invariant)
        U = conjectures['upper']
        L = conjectures['lower']
        print('Upper Bounds')
        for i in range(15):
            print(f'Conjecture {i}. {U[i]}')
            print('')
        print()
        print('Lower Bounds')
        for i in range(15):
            print(f'Conjecture {i}. {L[i]}')
            print('')
        print()

        work = input('Remove conjectures? (y/n) ')
        while work == 'y':
            type = input('Upper or lower? (U/L) ')
            index = int(input('Conjecture label? '))
            if type == 'U':
                U.pop(index)
            else:
                L.pop(index)
            print('Upper Bounds')
            for i in range(15):
                print(f'Conjecture {i}. {U[i]}')
                print('')
                print()
            print('Lower Bounds')
            for i in range(15):
                print(f'Conjecture {i}. {L[i]}')
                print('')
                print()

            work = input('Remove conjectures? (y/n) ')

    f = open(f'TxGraffiti/conjectures/{invariant}_conjectures', 'wb')
    conj_dict = {'upper': U, 'lower': L}
    pickle.dump(conj_dict, f)
    f.close()
    return 0



if __name__ == '__main__':
    main()
