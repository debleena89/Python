


import numpy as NP
from scipy import linalg as LA
p_final_state = 'p1'
q_final_state = 'q1'
#accepting_states = ['p0_q0_3','p2_q1_3']
accepting_states = ['f','g']
target_top = -1
source_top = 0
source = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
position_matrix = [[]]
matched = 0
omega_regular_expression = ''

def generate_omega_regular_expression():
    global target_top
    repeat_string_length = target_top
    repeat_value = target[target_top]
    run = 0
    global omega_regular_expression
    print ("repeat_string_length",repeat_string_length)
    while run == 0:
          previous_state = target[repeat_string_length]
          repeat_string_length = repeat_string_length - 1
          if repeat_string_length < 0:
             break
          next_state = target[repeat_string_length] 
          visit[next_state] = 0  
          global state_transition_matrix                    
          if state_transition_matrix[next_state + 1][1] == previous_state:
             omega_regular_expression = str(0) + omega_regular_expression
          elif state_transition_matrix[next_state + 1][2] == previous_state:
             omega_regular_expression = str(1) + omega_regular_expression
                       #print (omega_regular_expression)
          if repeat_value == next_state:
             print("The omega regular expression is")
             print (omega_regular_expression)
             break
       

#-------------------------------------------------------------------------------------

def is_cycle_accepting():
    global matched
    matched = 0
    global accepting_states
    for source_index in range(len(source)):
        for accepting_state_index in range(len(accepting_states)):
           if source[source_index] == accepting_states[accepting_state_index]:
              print("this accepting state",source)
              matched = 1
              break
        if matched == 1:
             break
      
def found_next_element():
    position_matrix_column = len(position_matrix[0])
    for col in range(0,position_matrix_column):
        if position_matrix[source_top][col] != 0:
           to_return = position_matrix[source_top][col]
           position_matrix[source_top][col] = 0
           #print(to_return)
           return to_return
    return 0


def check_cycle():
    global source
    global source_top
    global position_matrix
    global matched
    position_matrix_column = len(position_matrix[0])
    current_state = source[source_top]
    source[source_top] = 0
    for index in range(len(source)):
        if source[index] == current_state :
           source[source_top] = current_state
           print("cycle found", source)
           #print("the matched value", matched)
           #is_cycle_accepting()
           matched = 1
           #if matched == 1:
              #print("the matched value", matched)
              #return
           source[source_top] = 0
           source_top = source_top - 1
           #print("the source is", source)
           loop_limit_nested = 1  
           while loop_limit_nested == 1:
                  position_matrix_elemenet = found_next_element()
                  if position_matrix_elemenet != 0 :                      
                          source[source_top + 1] = position_matrix_elemenet
                          #position_matrix[source_top][col] = 0
                          source_top = source_top + 1                            
                          #print("the source is ",source)
                          #print("")
                          #print("the position_matrix is ",position_matrix)
                          check_cycle()                       
                          break
                  elif source_top == 0:
                     break
                  else:
                     source[source_top] = 0
                     source_top = source_top - 1
           return 
    source[source_top] = current_state
   

def check_emptyness_of_Buchi_automata(state_transition_matrix):
    #intersection_matrix_for_buchi_automata = (['00','A','B','C'],['a','b','c',' s'],['b','d','e','s'],['c','b','c',''],['d','d','e',''],['e','f','g',''],['f','b','c','s'],['g','a','h',''],['h','a','h',''],['s','a','b','c'])
    global position_matrix
    for row in range(1,len(state_transition_matrix)):
        for col in range(0,len(state_transition_matrix[0])):
            if state_transition_matrix[row][col] == 0:
               state_transition_matrix[row][col] = '00'
    #state_transition_matrix.replace('0','00')
    #print("")
    print("the state transition matrix is--->",state_transition_matrix )
    print("")
    if len(state_transition_matrix) == 1:
       print("only one state is stable...Empty automata")
       return
    position_matrix_length = len(state_transition_matrix)
    position_matrix_column = len(state_transition_matrix[0])
    position_matrix = [[[] for colindex in 
         range(position_matrix_column)] for rowindex in 
         range(position_matrix_length)]
    for row in  range(position_matrix_length):
        for col in range(position_matrix_column):
           position_matrix[row][col] = 0
    global source
    global source_top
    for limit in range(1, len(state_transition_matrix)):
     source[0] = state_transition_matrix[limit][0]
     loop_limit = 1
     position_matrix_row = -1
     while loop_limit <= 50:          
          current_state = source[source_top]          
          for row_index in range(0,len(state_transition_matrix)):
              if state_transition_matrix[row_index][0] == current_state :                
                    #position_matrix_row = position_matrix_row + 1 
                    colindex_p_m = 0  
                    for colindex_i_m in range(1,position_matrix_column):    
                        if state_transition_matrix[row_index][colindex_i_m] != -1 and state_transition_matrix[row_index][colindex_i_m] != current_state:   
                           source_top = source_top + 1
                           source[source_top] = state_transition_matrix[row_index][colindex_i_m] 
                           save_index = colindex_i_m
                           #print("afetr insertion", source)
                           break
                    #print("")
                    #print("the valuee of save_index",save_index) 
                    for colindex_i_m_n in range(colindex_i_m + 1,position_matrix_column):    
                        if state_transition_matrix[row_index][colindex_i_m_n] != -1 and state_transition_matrix[row_index][colindex_i_m] != current_state:   
                           position_matrix[source_top - 1][colindex_p_m] = state_transition_matrix[row_index][colindex_i_m_n]
                           colindex_p_m = colindex_p_m + 1
          #print("")
          #print(position_matrix)
          check_cycle()
          #if matched == 1:
             #print("Is the language of this NBA empty ?? : NO")
             #return
          if source_top == 0:
             break  
          loop_limit = loop_limit + 1
     
       
#------------------------------------------------------------------------------
def show_graph(exponentially_statble_states_list,state_transition_matrix):
    no_of_cols = len(state_transition_matrix[0])
    no_of_rows = len(state_transition_matrix)
    print("the matrix is ",state_transition_matrix)
    file = open("test.odt","w")
    file.write("digraph Test{\n")
    for row in range(1,no_of_rows):
        for col in range(1,no_of_cols):
            if state_transition_matrix[row][col] == -1:
               continue 
            file.write(str(exponentially_statble_states_list[state_transition_matrix[row][0]]) + '->' + str(exponentially_statble_states_list[state_transition_matrix[row][col]])  +
            ' [label = "A' + str(state_transition_matrix[0][col]) + '"]; \n')
    file.write("}")
    file.close() 
    #dot -Tps graph.dot -o graph1.ps
def check_bad_states(state_transition_matrix):
    no_of_cols = len(state_transition_matrix[0])
    no_of_rows = len(state_transition_matrix)
    #for row in range(1,len(state_transition_matrix)):  
    row = 1
    true = 1
    if no_of_rows == 1:
       print("no state found")
       return
    while true == 1:
       #print(no_of_rows)     
       for col in range(1,no_of_cols):
           if state_transition_matrix[row][0] != state_transition_matrix[row][col] and state_transition_matrix[row][col] != -1:              
              print(state_transition_matrix[row][0])
              break
           if col == no_of_cols - 1:
              print(state_transition_matrix[row][0])
              state_transition_matrix.remove(state_transition_matrix[row])  
              no_of_rows = no_of_rows - 1 
              print("no_of_rows and len(state_transition_matrix)",row,len(state_transition_matrix))
              if row >= len(state_transition_matrix):
                 #print(" rows--bye bye",row)
                 return state_transition_matrix
       row = row + 1
       if row >= len(state_transition_matrix) :                       
          return state_transition_matrix
#def check_cycle()

def get_omega_regular_expression(exponentially_statble_states_list):
    no_of_elements = len(exponentially_statble_states_list)
    global state_transition_matrix
    state_transition_matrix = [[[] for colindex in range(4)] for rowindex in range(no_of_elements + 1)]
    for row in range(no_of_elements + 1):
        for col in range(4):
            state_transition_matrix[row][col] = -1
    state_transition_matrix[0][1] = 0
    state_transition_matrix[0][2] = 1
    state_transition_matrix[0][3] = 2
    for row in range(1,no_of_elements + 1):
        for col in range(0,1):
            state_transition_matrix[row][col] = row - 1
    
    for element_count in range(0,no_of_elements):
        state = exponentially_statble_states_list[element_count]
        next_state_for_0 = state[1]+state[2]+state[3]+str(0)
        for index in range(no_of_elements):
            if next_state_for_0 == exponentially_statble_states_list[index]:
               state_transition_matrix[element_count+1][1] = index
        next_state_for_1 = state[1]+state[2]+state[3]+str(1)
        for index in range(no_of_elements):
            if next_state_for_1 == exponentially_statble_states_list[index]:
               state_transition_matrix[element_count+1][2] = index
        next_state_for_2 = state[1]+state[2]+state[3]+str(2)
        for index in range(no_of_elements):
            if next_state_for_2 == exponentially_statble_states_list[index]:
               state_transition_matrix[element_count+1][3] = index
    show_graph(exponentially_statble_states_list,state_transition_matrix)
    state_transition_matrix = check_bad_states(state_transition_matrix)
    print(state_transition_matrix)
    if state_transition_matrix == None:
       return    
    check_emptyness_of_Buchi_automata(state_transition_matrix)
    

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
          for i in range(2):
             if evals[i] < 1 :
                print("Eigen values lies in unit ball",evals[i])       


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


def check_exponential_stability(state_combination , A0, A1, A2):
    no_of_elements = len(state_combination)    
    exponentially_statble_state_list = []
    for element_count in range(no_of_elements):
        current_state_length= len(state_combination[element_count] )
        current_state = state_combination[element_count]
        #matrix_product = ([1.0, 0.0, 0.0, 0.0 ], [0.0, 1.0, 0.0,0.0], 
        #                        [0.0, 0.0, 1.0,0.0], [0.0, 0.0, 0.0,1.0])   
        matrix_product = ([1.0, 0.0],[0.0, 1.0])
        for current_state_length_count in range(current_state_length):   
            #print (current_state_length_count)                     
            if current_state[current_state_length_count] == '0':
               matrix_product = NP.dot(matrix_product, A0)
            elif current_state[current_state_length_count] == '1' :
               matrix_product = NP.dot(matrix_product, A1) 
            else:
               matrix_product = NP.dot(matrix_product, A2)            
        result = LA.norm(matrix_product)
        print(result)
        if result < 15: #0.5:           
           exponentially_statble_state_list.append(current_state)
    return exponentially_statble_state_list

#--------generate combination of given elements here 1 and 2---
#--------upto a certain depth,signifies the length of the control action combination

def print_combination():
    A1 = []
    A2 = []
    A3 = []
    A1 = [0, 1, 2]
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
    #source_top = -1
   
    target_top = -1
#------The two matrices are assignede values----------------
    #A1 = ([0.268, 0.332, -0.357, -0.339], [0.332, 0.268, -0.142,-0.134],
     #        [0, 0.412, 0.210, -0.319],[0, 0.461, 0.291, -0.028])
    #A0 = ([0.268, 0.332, -0.357, -0.339],[0.332, 0.268, -0.142, -0.134],
     #        [0, 0, 1, 0], [0, 0, 0, 1])
    #A0 =  ([2.0, -1.75], [2.0, -2.0])#([2.55, 2.75], [2.55, -2.55])#([2.0, -1.75], [2.0, -2.0])
          #[0, -0.985, -1.017, 1.449], [0, 1.98, 0.491, -1.212])
   
    #A0 = ([0.75, -2.5],[0.75, 0.75])

    #A1 = ([2.34, -0.5],[0.52, 1.22])#([0.25, 1.75], [0.25, -0.25])#([1.65, -2.5],[1.66, 1.0])#eigen value net
   
    #A1 = ([0.25, 1.75], [0.25, -0.25])#([2.0, 0.25],[0.25, -1.75])
    
    #A2 = ([0.25, -2.0],[0.25, -0.25])## eigen value permission met
  
    #A2 = ([0.45, 1.5], [0.45, -0.45])

    #A2  = ([2.0, -0.55],[0.25, -1.75])
   
    #A2 = ([0.35, 1.85], [0.35, -0.35])#([0.45, 2.05], [0.05, -0.95])#([0.25, 1.75], [0.26, -2.0])#([0.35, 1.85], [0.35, -0.35])
          #[0, 0, 1, 0], [0, 0, 0, 1])

    #A0 = ([2.34, -0.6], [0.52, 1.22])

   
    A0 = ([1.8, 1.5], [-1.5, -2])

    A1 = ([1.5, -2.6], [1.9, -2.3])

    A2 = ([-1.2, 2.4], [2.6, -1.4])

    print("---Eigen Values for A0----")
    check_eigenvalues(A0)
    print("")
    print("---Eigen Values for A1----") 
    check_eigenvalues(A1)
    print("")
    print("---Eigen Values for A2----")
    check_eigenvalues(A2)
    print("")
#-----generates the combination tree and return the tree----
    state_combination = print_combination() 
    #print( state_combination)    
#----checking exponential stability and generating the resulting set----
    exponentially_statble_states_list = check_exponential_stability(state_combination, A0, A1, A2)
    print("Exponentially stable states lists are given below-->")
    print("")
    print (exponentially_statble_states_list)
    #reliable_states_list = check_reliable_states(exponentially_statble_states_list)
       #=['0011', '0101', '0110', '0111', '1011', '1101', '1110']
#-----added constraint that First mode cannot appear more than two times----
    #final_result_set = result_set_based_on_constraint(exponentially_statble_states_list)
#-----------------showing the final result set---------------
    #print (reliable_states_list)
    omega_regular_expression = get_omega_regular_expression(exponentially_statble_states_list)
    
    

    
