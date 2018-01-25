
stateMachine = []

#---------------code from cross product---------------------------------------------------------
#-----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
source_top = 0
source = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
position_matrix = [[]]
matched = 0
#------------------------------------------------------------------------------
#----------------checking emptyness of buchi automata--------------------------
#------------------------------------------------------------------------------
def is_cycle_accepting():
    global matched
    matched = 0
    run = []
    global accepting_states
    for source_idx in range(len(source)):
        if source.count(source[source_idx]) == 2:
           for source_ix in range(source_idx,len(source)):
               run.append(source[source_ix])
           break

    for run_index in range(len(run)):
        for accepting_state_index in range(len(accepting_states)):
           if run[run_index] == accepting_states[accepting_state_index]:
              print("this accepting state",run)
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
           print(to_return)
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
        #print("sourcr is ", source[index] )
        #print("the current state", current_state)
        if source[index] == current_state :
           source[source_top] = current_state
           print("cycle found", source)
           print("the matched value", matched)
           is_cycle_accepting()
           if matched == 1:
              print("the matched value", matched)
              return
           source[source_top] = 0
           source_top = source_top - 1
           print("the source is", source)
           loop_limit_nested = 1  
           while loop_limit_nested == 1:
                  position_matrix_elemenet = found_next_element()
                  if position_matrix_elemenet != 0 :                      
                          source[source_top + 1] = position_matrix_elemenet
                          #position_matrix[source_top][col] = 0
                          source_top = source_top + 1                            
                          print("the source is ",source)
                          print("")
                          print("the position_matrix is ",position_matrix)
                          check_cycle()                       
                          break
                  elif source_top == 0:
                     break
                  else:
                     source[source_top] = 0
                     source_top = source_top - 1
           return 
    source[source_top] = current_state
   

def check_emptyness_of_Buchi_automata(intersection_matrix_for_buchi_automata):
    global position_matrix
    position_matrix_length = len(intersection_matrix_for_buchi_automata)
    position_matrix_column = len(intersection_matrix_for_buchi_automata[0])
    position_matrix = [[[] for colindex in 
         range(position_matrix_column)] for rowindex in 
         range(position_matrix_length)]
    for row in  range(position_matrix_length):
        for col in range(position_matrix_column):
           position_matrix[row][col] = 0
    global source
    global source_top
    print("to ................check.....",intersection_matrix_for_buchi_automata[1][0])
    source[0] = intersection_matrix_for_buchi_automata[1][0]
    loop_limit = 1
    position_matrix_row = -1
    while loop_limit <= 50:          
          current_state = source[source_top]          
          for row_index in range(0,len(intersection_matrix_for_buchi_automata)):
              if intersection_matrix_for_buchi_automata[row_index][0] == current_state : 
                  if  intersection_matrix_for_buchi_automata[row_index][1] != '0_2' and intersection_matrix_for_buchi_automata[row_index][1] != '0_3' and intersection_matrix_for_buchi_automata[row_index][1] != '0_4' and intersection_matrix_for_buchi_automata[row_index][1] != '0_1':                
                    source_top = source_top + 1
                    source[source_top] = intersection_matrix_for_buchi_automata[row_index][1]
                    #print("Source top after insertion", source)
                    #position_matrix_row = position_matrix_row + 1 
                    colindex_p_m = 0 
                    for colindex_i_m in range(2,position_matrix_column):    
                        if intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_1' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_2' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_3':                          
                           position_matrix[source_top - 1][colindex_p_m] = intersection_matrix_for_buchi_automata[row_index][colindex_i_m]
                           colindex_p_m = colindex_p_m + 1
                  else:
                    source_top = source_top + 1
                    source[source_top] = intersection_matrix_for_buchi_automata[row_index][2]
                    #print("Source top after insertion", source)
                    #position_matrix_row = position_matrix_row + 1 
                    colindex_p_m = 0 
                    for colindex_i_m in range(3,position_matrix_column):    
                        if intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_1' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_2' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_3':                          
                           position_matrix[source_top - 1][colindex_p_m] = intersection_matrix_for_buchi_automata[row_index][colindex_i_m]
                           colindex_p_m = colindex_p_m + 1
          #print("")
          #print(position_matrix)
          #print("Now I am checking for cycle")
          check_cycle()
          if matched == 1:
             print("Is the language of this NBA empty ?? : NO")
             return
          if source_top == 0:
             break  
          loop_limit = loop_limit + 1
#-------------------------------------------------------------------------------------------
def intersection_construction_for_buchi_automata(intersection_matrix):
    print("the intersection matrix before the work", intersection_matrix )
    print("")
    number_of_states = len(stateMachine)

    intersection_matrix_len = len(intersection_matrix)
    intersection_matrix_for_buchi_automata_len = (number_of_states + 1) * intersection_matrix_len
    intersection_matrix_for_buchi_automata_col = len(intersection_matrix[0])
    intersection_matrix_for_buchi_automata = [[[] for colindex in 
         range(intersection_matrix_for_buchi_automata_col)] for rowindex in 
         range(intersection_matrix_for_buchi_automata_len)]
    track = []
    track_index = 0
    current_state = intersection_matrix[1][0]
    print("current_state is before the loop", current_state )
    splitted_string = current_state.split("_")    

    if splitted_string[0] != stateMachine[0].final_states[0] :
       for col in range(intersection_matrix_for_buchi_automata_col):
               intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_0"  )
    else:
       for col in range(intersection_matrix_for_buchi_automata_col):
               intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_1"  )

    print("after number assignment", intersection_matrix_for_buchi_automata)     
    #track_index = track_index + 1
    #track.append(intersection_matrix_for_buchi_automata[1][0])
    visit_row = 2
    for row_index in range(1, intersection_matrix_for_buchi_automata_len ):
        pass_flag = 0
        for col_index in range(1,intersection_matrix_for_buchi_automata_col):
            current_state = intersection_matrix_for_buchi_automata[row_index][col_index]
            print("current_state is, row_index", current_state,row_index)
            if visit_row == row_index:
               break
            found_track= current_state in track
            if found_track == False:
               pass_flag = 1                    
               splitted_string = current_state.split("_")
               splitted_string_length = len(splitted_string)
               #print("the found splittedd string is", splitted_string)
               
               find_string = str(splitted_string[0])
               for string_index in range(1,splitted_string_length - 1):
                   find_string = find_string + '_' + splitted_string[string_index] 
              
               for i_m_index in range(intersection_matrix_len):
                   #print("the find string is:", find_string)
                   if intersection_matrix[i_m_index][0] == find_string :
                      next_element_index = i_m_index
                      break

               intersection_matrix_for_buchi_automata[visit_row][0] = current_state
               print(intersection_matrix_for_buchi_automata)
               for index in range(0,number_of_states):
                   #if splitted_string[number_of_states] == index:
                  #print("hiiii",splitted_string[0])   
                        
                      if splitted_string[index] != stateMachine[index].final_states[0] :
                         print("if executed")
                         for col in range(1,intersection_matrix_for_buchi_automata_col):
                             intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(index)  )
                         print("result",intersection_matrix_for_buchi_automata[visit_row])
                      else:
                         print("executed else")
                         for col in range(1,intersection_matrix_for_buchi_automata_col):
                             intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(index+1)  )     
                         print("result",intersection_matrix_for_buchi_automata[visit_row])

              
                      if splitted_string[index] == index + 1:                        
                        for col in range(1,intersection_matrix_for_buchi_automata_col):
                            intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(0)  )
                      
               visit_row = visit_row + 1
               track_index = track_index + 1
              # if track_index >= len(track):
              #    print("the intersection matrix is:")
              #    print(intersection_matrix_for_buchi_automata)
              #    print("")
              #    return
               track.append(current_state)
     
        if not current_state:
                  #print("the intersection matrix is:")
                  print("Going to check cycle.......//////.....//////////....../////")
                  print(intersection_matrix_for_buchi_automata)
##-------------------------------To print the state diagram-------------------------------------- ##--------------------------------------------------------------------------------------------------
                  file = open("test_original.dot","w")
                  file.write("digraph Test{\n")
                  no_of_rows = len(intersection_matrix_for_buchi_automata)
                  no_of_cols = len(intersection_matrix_for_buchi_automata[0])
                  for row in range(1,no_of_rows):
                      for col in range(1,no_of_cols):
                          if intersection_matrix_for_buchi_automata[row][col] == []:
                             continue 
                          file.write(str(intersection_matrix_for_buchi_automata[row][0]) + ' -> ' + str(intersection_matrix_for_buchi_automata[row][col])  + '; \n')
                  file.write("}")
                  file.close() 
                  #dot -Tps test.dot -o outfile.ps
#-------------------------------------------------------------------------------------------------
                  print("")
                  print("---------------------------------------------------------------")
                  check_emptyness_of_Buchi_automata(intersection_matrix_for_buchi_automata)
                  break
           

          
#-----------------------------------------------------------------------------------

def intersection_construction(cross_Product_matrix):
    intersection_matrix_row_len = len(cross_Product_matrix)
    intersection_matrix_col_len = len(cross_Product_matrix[0])
    intersection_matrix = [[[] for colindex in range(intersection_matrix_col_len)] for rowindex in range(intersection_matrix_row_len)]
    intersection_matrix[0] = cross_Product_matrix[0]
    #intersection_matrix[0][1] = 'a'
    #intersection_matrix[0][2] = 'b'
    intersection_matrix[1] = cross_Product_matrix[1]    
    track = []
    track.append(intersection_matrix[1][0])
    true = 1
    row = 1
    visit_row = 1
    track_index = 0
    for limit in range(intersection_matrix_row_len):
          pass_flag = 0
          #print(intersection_matrix[visit_row][1],limit,row,visit_row)
          if visit_row > row:
             break
          for index in range(1,intersection_matrix_col_len):
              print("the element see", intersection_matrix[visit_row][index])
              if intersection_matrix[visit_row][index] == '0':
                 #print("the element see going to skip", intersection_matrix[visit_row][index])
                 continue
              found_track = intersection_matrix[visit_row][index] in track
              print("the element see checked in track", found_track,intersection_matrix[visit_row][index])
              if found_track == False:  
                 pass_flag = 1               
                 for find_element in range(len(cross_Product_matrix)):
                     found = intersection_matrix[visit_row][index] in cross_Product_matrix[find_element][0]
                     if found == true:
                        found = find_element
                        break
                 row = row + 1
                 intersection_matrix[row] = cross_Product_matrix[found]
                 track_index = track_index + 1
                 track.append(intersection_matrix[visit_row][index])                          
          visit_row = visit_row + 1    
          #print(intersection_matrix)
          #print("")
          #if pass_flag == 0 and row > visit_row:
           #  break
    print("the intersection matrix is",intersection_matrix)
    print("")
    print("------------------------------------------------------")
    intersection_construction_for_buchi_automata(intersection_matrix)

    print(track)
#--------generate combination of given elements here 1 and 2-------------------------------
#--------upto a certain depth,signifies the length of the control action combination-------

def product():
    
    number_of_stateMachines = len(stateMachine)
    temporary_matrix = stateMachine[0].transition_table
   
    for index in range(1,number_of_stateMachines):
        temporary_matrix_row = len(temporary_matrix)
        temporary_matrix_col = len(temporary_matrix[0])
        next_matrix_row = len(stateMachine[index].transition_table)
        cross_Product_matrix = [[[] for colindex in range(temporary_matrix_col)] for rowindex in range(temporary_matrix_row * next_matrix_row )]
        for index_first_row in range(0,temporary_matrix_col):
            cross_Product_matrix[0][index_first_row] = temporary_matrix[0][index_first_row]
        row_index = 1
        for row_temp in range(1,temporary_matrix_row):
          for row_next in range(1,next_matrix_row):
              for col in range(0,temporary_matrix_col):
                  print(stateMachine[index].transition_table[row_next][col])
                  print(temporary_matrix[row_temp][col])
                  if str(stateMachine[index].transition_table[row_next][col]) == '-' or str(temporary_matrix[row_temp][col]) == '0':
                     cross_Product_matrix[row_index][col] = str(0)
                  else :
                     cross_Product_matrix[row_index][col] = str(temporary_matrix[row_temp][col])+'_'+str(stateMachine[index].transition_table[row_next][col])
              row_index = row_index + 1
         
        temporary_matrix = cross_Product_matrix
    print("the cross product matrix is", cross_Product_matrix )
    print("-----------------------------------------------------")
    #print("")
    intersection_construction(cross_Product_matrix)


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------



class StateMachine:
      def __init__(self, name): 
          self.name = name 
          self.initial_state = None
          self.transitions = []
          self.alphabets = []
          self.state = []
          self.final_states = []
          self.transition_table = [[]]

      def get_initial_state(self):
          print("enter the initial state for this automaton")
          self.initial_state = input()
      
      def show_initial_state_value(self):
          print ("The initial state is here",self.initial_state)   

      def get_alphabets(self):
          print("how many alphabets are there:--")
          number_of_alphabets = int(input())
          self.alphabets.append('0')
          for index in range(0,number_of_alphabets):
              print("enter the alphabets")
              self.alphabets.append(input())

      def get_final_states(self):
          print("how many final states are there:--")
          number_of_final_states = int(input())
          for index in range(0,number_of_final_states):
              print("enter the final states")
              self.final_states.append(input())

      def show_final_states(self):
          print(self.final_states)    
    
      def get_states(self):
          print("how many states you want to enter")
          no_of_states = int(input())

          for state_index in range(0, no_of_states):
              try:        
                  print("enter the state")
                  state_name = input()
                  if state_name == '':
                     raise ValueError
                     break
                  self.state.append(State(state_name))        
              except ValueError:
                  print("Give some valid input")
          for state_index in  range(0,no_of_states):
              print(self.state[state_index].name)

      def get_transition_table(self):
          index = 0
          continue_while_loop = 'y'
          while continue_while_loop == 'y':
                print("enter the present state:")
                present_state = input()
               
                print("enter the condition:")
                condition = input()
                
                print("enter the next state:")
                next_state = input()

                self.transitions.append(Transitions(present_state, condition, next_state))
                
                print("Do you want to continue, press y/n:-")
                continue_while_loop = input()
                
      
      def show_transition_table(self):
          print("The transition table is shown below:->")
          transitions_length = len(self.transitions)
          for index in range(0, transitions_length):
              print(self.transitions[index].present_state,self.transitions[index].condition,self.transitions[index].next_state)


      def form_state_transition_table(self):
          transitions_length = len(self.transitions)
          number_of_states = len(self.state)
          number_of_alphabets = len(self.alphabets)
          self.transition_table = [[[] for colindex in range(number_of_alphabets)] for rowindex in range(number_of_states + 1)]

          for index in range(0,number_of_alphabets):
               self.transition_table[0][index] = self.alphabets[index]
          
          for index in range(0, number_of_states):
              self.transition_table[index + 1][0] = self.state[index].name

          for transitions_index in range(0,transitions_length):
              for state_index in range(1, number_of_states+1):
                  if self.transitions[transitions_index].present_state == self.transition_table[state_index][0]:     
                     for alphabet_index in range(1,number_of_alphabets):
                         if self.transitions[transitions_index].condition == self.alphabets[alphabet_index]:
                             self.transition_table[state_index][alphabet_index] = self.transitions[transitions_index].next_state
                           
                             break
          print(self.transition_table)
          

class State:
    def __init__(self, name): self.name = name

class Transitions:
      def __init__(self, present_state, condition, next_state):
          self.present_state = present_state
          self.condition = condition
          self.next_state = next_state  

    
if __name__== "__main__":
    print("In the main")

    print("how many states are there in the system:--")

    number_of_automata = int(input())

    for index in range(0,number_of_automata):
        stateMachine.append(StateMachine("Predict.txt"))
        stateMachine[index].get_states()
        stateMachine[index].get_initial_state()
        stateMachine[index].show_initial_state_value()
        stateMachine[index].get_alphabets()  
        stateMachine[index].get_transition_table()
        stateMachine[index].show_transition_table()
        stateMachine[index].get_final_states()
        stateMachine[index].show_final_states()
        stateMachine[index].form_state_transition_table()
        temp = stateMachine[index].transition_table
    product()

