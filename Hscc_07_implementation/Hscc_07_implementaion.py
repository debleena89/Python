


import numpy as NP
from scipy import linalg as LA

def result_set_based_on_constraint(exponentially_statble_states_list):
    no_of_elements = len(exponentially_statble_states_list)
    final_result_state = []
    for element_count in range(no_of_elements):        
        current_state = exponentially_statble_states_list[element_count]
        if current_state[0] == '1' and current_state[1] == '1':
           continue
        else:
           final_result_state.append(current_state)
    return final_result_state

#--------||1121||-->this means first mtrices are to be multipled following this arrangement
#--------the norm on the resulting matrix will be calculated, Euclidean norm...
#--------this value should be lass than 1.


def check_exponential_stability(state_combination , MAT1, MAT2):
    no_of_elements = len(state_combination)    
    exponentially_statble_state_list = []
    for element_count in range(no_of_elements):
        current_state_length= len(state_combination[element_count] )
        current_state = state_combination[element_count]
        matrix_product = ([1.0, 1.0], [1.0, 1.0]) 
 
        for current_state_length_count in range(current_state_length):            
            if current_state[current_state_length_count] == '1':
               matrix_product = NP.dot(matrix_product, MAT1)
            else:
               matrix_product = NP.dot(matrix_product, MAT2)            
        result = LA.norm(matrix_product)
        if result < 1:           
           exponentially_statble_state_list.append(current_state)
    return exponentially_statble_state_list

#--------generate combination of given elements here 1 and 2---
#--------upto a certain depth,signifies the length of the control action combination

def print_combination():
    A1 = []
    A2 = []
    A3 = []
    A1 = [1, 2]
    depth = 4
    itemlen = len(A1)
    term = 2
    A3 = A1
    depth = depth - 1
    for depth_index in range(depth):
       resultlen = itemlen * pow (itemlen, depth_index)
       if term == 2 : 
          for result_set_index in range(resultlen):
             for item_set_index in range(itemlen):                
                A2.append(str(A3[result_set_index])+str(A1[item_set_index]))         
       else : 
          for result_set_index in range(resultlen):
             for item_set_index in range(itemlen):                
                A3.append(str(A2[result_set_index])+str(A1[item_set_index]))        
       if term == 2:
            A3 = []
            term = 3
       else:
            A2 = []
            term = 2 
    if term == 3:
         return A2
    else:
         return A3
      


if __name__ == "__main__":

#------The two matrices are assignede values----------------
#    MAT1 = ([0.25, 1.75], [0.26, -2.0])
#    MAT2 = ([0.25, 1.75], [0.25, -0.25])
    MAT1 = ([2.0, -1.75], [2.0, -2.0])
    MAT2 = ([0.25, 1.75], [0.25, -0.25])
#-----generates the combination tree and return the tree----
    state_combination = print_combination()     
#----checking exponential stability and generating the resulting set----
    exponentially_statble_states_list = check_exponential_stability(state_combination, MAT1, MAT2)
#-----added constraint that First mode cannot appear more than two times----
    final_result_set = result_set_based_on_constraint(exponentially_statble_states_list)
#-----------------showing the final result set---------------
    print (final_result_set)
    

    
