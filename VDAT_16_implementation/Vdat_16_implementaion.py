


import numpy as NP
from scipy import linalg as LA

def get_omega_regular_expression(reliable_states_list):
    no_of_elements = len(reliable_states_list)
    state_transition_matrix = [[[] for colindex in range(3)] for rowindex in range(no_of_elements + 1)]
    for row in range(no_of_elements + 1):
        for col in range(3):
            state_transition_matrix[row][col] = -1
    state_transition_matrix[0][1] = 0
    state_transition_matrix[0][2] = 1
    for row in range(1,no_of_elements + 1):
        for col in range(0,1):
            state_transition_matrix[row][col] = row - 1
    
    for element_count in range(0,no_of_elements):
        state = reliable_states_list[element_count]
        next_state_for_0 = state[1]+state[2]+state[3]+str(0)
        for index in range(no_of_elements):
            if next_state_for_0 == reliable_states_list[index]:
               state_transition_matrix[element_count+1][1] = index
        next_state_for_1 = state[1]+state[2]+state[3]+str(1)
        for index in range(no_of_elements):
            if next_state_for_1 == reliable_states_list[index]:
               state_transition_matrix[element_count+1][2] = index
    print(state_transition_matrix)
   
    for element_index in range(1,2):
        element = state_transition_matrix[element_index][0]
        source = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        source_top = -1 
        target = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        target_top = -1
        visit = [0,0,0,0,0,0,0,0,0,0]
        source_top = source_top + 1
        #print(source_top)
        source[source_top] = element
        target_top = target_top + 1
        target[target_top] = source[source_top]
        visit[element] = 1
        infinite = 1
        while infinite == 1: 
              current_top_element = source[source_top]
              source[source_top] = 0 - source[source_top]
              print(".....curetn elemeny")
              print(current_top_element)
              print(source)
              if state_transition_matrix[current_top_element+1][1] != -1:
                 source_top = source_top + 1
                 source[source_top] = state_transition_matrix[current_top_element+1][1]
                 print("source")
                 print(source)
              if state_transition_matrix[current_top_element+1][2] != -1:
                 source_top = source_top + 1
                 source[source_top] = state_transition_matrix[current_top_element+1][2]
                 print("source")
                 print(source) 
              target_top = target_top + 1
              target[target_top] = source[source_top]
              print("target")
              print(target)             
              #print(source)
              if visit[target[target_top]] == 1:
                 print("visit found")
                 print(target_top,",,,,,",target[target_top])
                 print(visit)
                 visit[target[target_top]] = 0
                 print("visit...")
                 print(target_top)
                 print(visit)
                 source[source_top] = 0 - source[source_top]
                 repeat_string_length = target_top
                 repeat_value = target[target_top]
                 run = 0
                 omega_regular_expression = ''
                 print ("repeat_string_length",repeat_string_length)
                 while run == 0:
                       previous_state = target[repeat_string_length]
                       repeat_string_length = repeat_string_length - 1
                       if repeat_string_length < 0:
                          break
                       next_state = target[repeat_string_length] 
                       visit[next_state] = 0                     
                       if state_transition_matrix[next_state + 1][1] == previous_state:
                          omega_regular_expression = str(0) + omega_regular_expression
                       elif state_transition_matrix[next_state + 1][2] == previous_state:
                          omega_regular_expression = str(1) + omega_regular_expression
                       #print (omega_regular_expression)
                       if repeat_value == next_state:
                                print("The omega regular expression is")
                                print (omega_regular_expression)
                                break
                 print("visit")
                 print(visit)
                 runUntil = 1
                 while runUntil == 1:
                       if source[source_top] < 0:
                          #source[source_top] = 0
                          source_top = source_top - 1
                          #target[target_top] = 0
                          target_top = target_top - 1
                          print("source")
                          print(source)
                          print("target")
                          print(target) 
                       else:
                          print("I am in else part")
                          target_top = target_top + 1
                          target[target_top] = source[source_top]
                          #print(source_top)
                          #print(target_top) 
                          break
                       if source_top == 0 : #or target_top == 0:
                          #print(source)
                          #print(target) 
                          source_top = -1
                          break 
      
              else:
                 visit[target[target_top]] = 1

              if source_top == -1 :
                 break       
              #print(source)
              #print(target)

def check_reliable_states(exponentially_statble_states_list):
    no_of_elements = len(exponentially_statble_states_list)
    reliable_states_list = []
    for element_count in range(no_of_elements):
        current_state_length= len(exponentially_statble_states_list[element_count] )
        current_state = exponentially_statble_states_list[element_count]
        reliabilyty_requirement = 1
        for current_state_length_count in range(current_state_length):
            if current_state[current_state_length_count] == '0':
               reliabilyty_requirement = reliabilyty_requirement * 1
            else:
               reliabilyty_requirement = reliabilyty_requirement * NP.exp(-0.001) * 0.996        
        print(reliabilyty_requirement)
        if reliabilyty_requirement >= 0.9845:
           reliable_states_list.append(current_state)  
    return reliable_states_list  

def check_eigenvalues(MAT):
          evals , evecs = LA.eig(MAT)
          for i in range(4):
             if evals[i] < 1 :
                print("lies in unit ball",evals[i])       


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


def check_exponential_stability(state_combination , A0, A1):
    no_of_elements = len(state_combination)    
    exponentially_statble_state_list = []
    for element_count in range(no_of_elements):
        current_state_length= len(state_combination[element_count] )
        current_state = state_combination[element_count]
        matrix_product = ([1.0, 0.0, 0.0, 0.0 ], [0.0, 1.0, 0.0,0.0], 
                                [0.0, 0.0, 1.0,0.0], [0.0, 0.0, 0.0,1.0])   
        for current_state_length_count in range(current_state_length):   
            #print (current_state_length_count)                     
            if current_state[current_state_length_count] == '0':
               matrix_product = NP.dot(matrix_product, A0)
            else:
               matrix_product = NP.dot(matrix_product, A1)            
        result = LA.norm(matrix_product)
        #print(result)
        if result < 0.5:           
           exponentially_statble_state_list.append(current_state)
    return exponentially_statble_state_list

#--------generate combination of given elements here 1 and 2---
#--------upto a certain depth,signifies the length of the control action combination

def print_combination():
    A1 = []
    A2 = []
    A3 = []
    A1 = [0, 1]
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
    A1 = ([0.268, 0.332, -0.357, -0.339], [0.332, 0.268, -0.142,-0.134],
             [0, 0.412, 0.210, -0.319],[0, 0.461, 0.291, -0.028])
    A0 = ([0.268, 0.332, -0.357, -0.339],[0.332, 0.268, -0.142, -0.134],
             [0, 0, 1, 0], [0, 0, 0, 1])
    #A0 = ([1, 0], [-1 , 1])
          #[0, -0.985, -1.017, 1.449], [0, 1.98, 0.491, -1.212])

    #A1 = ([-0.017, 1.449], [-0.491, -1.212])
          #[0, 0, 1, 0], [0, 0, 0, 1])
    check_eigenvalues(A0)
    print("-------")
    check_eigenvalues(A1)
#-----generates the combination tree and return the tree----
    state_combination = print_combination() 
    #print( state_combination)    
#----checking exponential stability and generating the resulting set----
    exponentially_statble_states_list = check_exponential_stability(state_combination, A0, A1)
    print (exponentially_statble_states_list)
    reliable_states_list = check_reliable_states(exponentially_statble_states_list)
       #=['0011', '0101', '0110', '0111', '1011', '1101', '1110']
#-----added constraint that First mode cannot appear more than two times----
    #final_result_set = result_set_based_on_constraint(exponentially_statble_states_list)
#-----------------showing the final result set---------------

    omega_regular_expression = get_omega_regular_expression(reliable_states_list)
    print (reliable_states_list)
    

    
