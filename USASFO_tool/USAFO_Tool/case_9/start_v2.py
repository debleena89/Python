
from tkinter import *
import os 
import time
import tkinter as tk
from tkinter import filedialog
#from memory_profiler import memory_usage

master = Tk()
#---------------------global variables-----------------------
no_of_state_counter = 0
no_of_final_state_counter = 0
no_of_alphabets_counter = 0
filepointer = ''
stateMachine = []
set_of_accepting_states = []
#---------------------------------------------------------------------
#----------------------------------------------------------------------
#-----------------------Background Code--------------------------------
#----------------------------------------------------------------------

source_top = 0
source = []
position_matrix = [[]]
matched = 0
#------------------------------------------------------------------------------
#----------------checking emptyness of buchi automata--------------------------
#------------------------------------------------------------------------------


def draw_image(run):
    file = open("test_original.dot","w")
    file.write("digraph Test{\n")
    no_of_rows = len(run)
    #no_of_cols = len(intersection_matrix_for_buchi_automata[0])
    for row in range(0,no_of_rows-1):
        #for col in range(1,no_of_cols):
         #   if intersection_matrix_for_buchi_automata[row][col] == []:
          #     continue 
           file.write(run[row] + " -> ")

    file.write(run[no_of_rows-1] + ";")
    file.write("}")
    file.close() 

#def get_accepting_states():
    


def found_next_element():
    position_matrix_column = len(position_matrix[0])
    for col in range(0,position_matrix_column):
        if position_matrix[source_top][col] != 0:
           to_return = position_matrix[source_top][col]
           position_matrix[source_top][col] = 0
           return to_return
    return 0


def check_cycle():
    global source
    global source_top
    global position_matrix
    global matched
 
    position_matrix_column = len(position_matrix[0])
    current_state = source[source_top]
    
    if current_state == source[0]:
       #print("accepted string found", source)
       
       matched = 1
       return
    source[source_top] = 0
    for index in range(len(source)-1):
        if source[index] == current_state :
           source[source_top] = current_state     
           source[source_top] = 0
           source_top = source_top - 1
           loop_limit_nested = 1  
           while loop_limit_nested == 1:
                  position_matrix_elemenet = found_next_element()
                  if position_matrix_elemenet != 0 :                      
                          source[source_top + 1] = position_matrix_elemenet
                          source_top = source_top + 1
                          check_cycle()                       
                          break
                  elif source_top == 0:
                     break
                  else:
                     source[source_top] = 0
                     source_top = source_top - 1
                     
           return 
    source[source_top]=current_state
   

def check_emptyness_of_Buchi_automata(intersection_matrix_for_buchi_automata):
    global position_matrix
    global source
    position_matrix_length = len(intersection_matrix_for_buchi_automata)
    position_matrix_column = len(intersection_matrix_for_buchi_automata[0])

    source_length = len(intersection_matrix_for_buchi_automata)
      

    source = [ rowindex for rowindex in 
         range(source_length)]
    for row in  range(0,source_length):
        source[row] = 0

    position_matrix = [[[] for colindex in 
         range(position_matrix_column)] for rowindex in 
         range(position_matrix_length)]
    for row in  range(position_matrix_length):
        for col in range(position_matrix_column):
           position_matrix[row][col] = 0
    
    global source_top
    
    #get_accepting_states()
    
    source[0] = set_of_accepting_states[0]
    loop_limit = 1
    position_matrix_row = -1
    while loop_limit <= source_length:          
          current_state = source[source_top]
                    
          for row_index in range(0,len(intersection_matrix_for_buchi_automata)):
              if intersection_matrix_for_buchi_automata[row_index][0] == current_state :
                                  
                    source_top = source_top + 1
                    source[source_top] = (intersection_matrix_for_buchi_automata[row_index][1])
                    colindex_p_m = 0 
                    for colindex_i_m in range(2,position_matrix_column):    
                        if intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_1' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_2' and intersection_matrix_for_buchi_automata[row_index][colindex_i_m] != '0_3':                          
                           position_matrix[source_top - 1][colindex_p_m] = intersection_matrix_for_buchi_automata[row_index][colindex_i_m]
                           colindex_p_m = colindex_p_m + 1
                            
          check_cycle()
          if matched == 1:
             print("Is the language of this NBA empty ?? : NO")
             return
          if source_top == 0:
             break  
          loop_limit = loop_limit + 1
    print("Is the language of this NBA empty ?? : YES")
#-------------------------------------------------------------------------------------------
def intersection_construction_for_buchi_automata(intersection_matrix):
    #print("the obtained intersection matrix is")
    #print(intersection_matrix)
    number_of_states = len(stateMachine)

    intersection_matrix_len = len(intersection_matrix)
    intersection_matrix_for_buchi_automata_len = (number_of_states + 1) * (intersection_matrix_len-1) +1
    #print("intersection_matrix_for_buchi_automata_len",intersection_matrix_for_buchi_automata_len)
    intersection_matrix_for_buchi_automata_col = len(intersection_matrix[0])
    intersection_matrix_for_buchi_automata = [[[] for colindex in 
         range(intersection_matrix_for_buchi_automata_col)] for rowindex in 
         range(intersection_matrix_for_buchi_automata_len)]
    intersection_matrix_for_buchi_automata[0] = intersection_matrix[0]
    track = []
    track = [row_index for row_index in range(0, intersection_matrix_for_buchi_automata_len-1)]
    
    for index in range(0,intersection_matrix_for_buchi_automata_len-1):
        track[index] = 0

    track_index = 0
    current_state = intersection_matrix[1][0]
    
    splitted_string = current_state.split("_")    
    
    intersection_matrix_for_buchi_automata[1][0] = str(current_state + "_0")
    track[track_index] = intersection_matrix_for_buchi_automata[1][0]
    #print("the track is", track)
     
    final_state_present =  splitted_string[0] in stateMachine[0].final_states
    if final_state_present == False :
       for col in range(1,intersection_matrix_for_buchi_automata_col):
               intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_0"  )
    else:
       for col in range(1,intersection_matrix_for_buchi_automata_col):
               intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_1"  )

    print("len is", intersection_matrix_for_buchi_automata_len)
    visit_row = 2
    for row_index in range(1, intersection_matrix_for_buchi_automata_len ):
        pass_flag = 0
        for col_index in range(1,intersection_matrix_for_buchi_automata_col):
            current_state = intersection_matrix_for_buchi_automata[row_index][col_index]

            if visit_row == row_index:
               break
            found_track= current_state in track
            #print("")
            #print("current state found in track", current_state, found_track, track)
            if found_track == False:
               pass_flag = 1                    
               splitted_string = current_state.split("_")
               splitted_string_length = len(splitted_string)
               
               find_string = str(splitted_string[0])
               for string_index in range(1,splitted_string_length - 1):
                   find_string = find_string + '_' + splitted_string[string_index] 
              
               for i_m_index in range(intersection_matrix_len):
                   if intersection_matrix[i_m_index][0] == find_string :
                      next_element_index = i_m_index
                      break
               #print(intersection_matrix_for_buchi_automata)
               intersection_matrix_for_buchi_automata[visit_row][0] = current_state
               if int(splitted_string[number_of_states]) == number_of_states:
                  for col in range(1,intersection_matrix_for_buchi_automata_col):   
                            intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(0)  )
                            #set_of_accepting_states.append(intersection_matrix_for_buchi_automata[visit_row][col])
                            #print(set_of_accepting_states)
               else:

                      index = int(splitted_string[number_of_states])
                  
                 #for index in range(0,number_of_states):
                        
                      #print("seeeee", splitted_string[index],stateMachine[index].final_states[0],index) 
                      final_state_present =  splitted_string[index] in stateMachine[index].final_states
                      if final_state_present == False :
                         
                         for col in range(1,intersection_matrix_for_buchi_automata_col):
                             intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(index)  )
                        
                      else:
                         
                         for col in range(1,intersection_matrix_for_buchi_automata_col):
                             #print("the index value here is", index,intersection_matrix[next_element_index][col])
                             intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[next_element_index][col] + "_" + str(index+1)  )     
                             if index+1 == number_of_states:
                                set_of_accepting_states.append(str(intersection_matrix[next_element_index][col] + "_" + str(index+1))) 
                                #print("list....",set_of_accepting_states)

              
                 
                      
               visit_row = visit_row + 1
               track_index = track_index + 1
               if track_index < intersection_matrix_for_buchi_automata_len:
                  track[track_index] = current_state
     
        if current_state == []:
                  
##-------------------------------To print the state diagram-------------------------------------- ##--------------------------------------------------------------------------------------------------
                  
                  #dot -Tps test.dot -o outfile.ps
#-------------------------------------------------------------------------------------------------
                  print("")
                  print("---------------------------------------------------------------")
                  #print("intersection_matrix_for_buchi_automata",intersection_matrix_for_buchi_automata)
                  count = 0 
                  for index in range(len(intersection_matrix_for_buchi_automata)):
                      if (intersection_matrix_for_buchi_automata[index][0] != [] ):        
                         count = count + 1
                      else:
                          break
                  print("Number of states in intersection automata", count)
                  #print(intersection_matrix_for_buchi_automata)
                  return intersection_matrix_for_buchi_automata
           

          
#-----------------------------------------------------------------------------------


 
   
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------


def new_product():
    number_of_stateMachines = len(stateMachine)
    temporary_matrix = stateMachine[0].transition_table
    temporary_matrix_initial_state = stateMachine[0].initial_state
    
    temporary_matrix_dict = stateMachine[0].state_index_pair
    
    for index in range(1,number_of_stateMachines):
        row_next = 1
        temporary_matrix_row = len(temporary_matrix)
        temporary_matrix_col = len(temporary_matrix[0])
        next_matrix_row = len(stateMachine[index].transition_table)
        cross_Product_matrix = [[[] for colindex in range(temporary_matrix_col)] for rowindex in range(((temporary_matrix_row-1) * (next_matrix_row - 1 ) + 1))]
        cross_product_dict = {}

        for index_first_row in range(0,temporary_matrix_col):
            cross_Product_matrix[0][index_first_row] = temporary_matrix[0][index_first_row]
        cross_Product_matrix[1][0] = str(temporary_matrix_initial_state) + '_' + str(stateMachine[index].initial_state)        
        cross_product_dict[str(temporary_matrix_initial_state) + '_' + str(stateMachine[index].initial_state)] = 1
        
        temp_mat_row = temporary_matrix_dict[temporary_matrix_initial_state]
        next_mat_row = stateMachine[index].state_index_pair[stateMachine[index].initial_state]
        temporary_matrix_initial_state = cross_Product_matrix[1][0]

        #print("before operation the temo matrix is")
        #print(temporary_matrix)

        for col_index in range(1,temporary_matrix_col):
            cross_Product_matrix[1][col_index] = str(temporary_matrix[temp_mat_row][col_index]) + '_' + str(stateMachine[index].transition_table[next_mat_row][col_index])
        #print(stateMachine[0].transition_table,stateMachine[1].transition_table)
        #print("")
        #print(cross_Product_matrix)
        number_of_row_in_cpm = 3
        for row_index in range(1, len(cross_Product_matrix)):     
            current_state = cross_Product_matrix[row_index][0]
            #print("the current state is", current_state)
            if current_state == []:
               break
            for col_index in range(1, temporary_matrix_col):
                current_state = cross_Product_matrix[row_index][col_index]                 
                if current_state not in cross_product_dict:
                   row_next = row_next + 1
                   cross_Product_matrix[row_next][0] = current_state  
                   cross_product_dict[current_state] = row_next                 
                   number_of_row_in_cpm = number_of_row_in_cpm + 1
                   
                   split_string = current_state.split("_")
                   for col_index_temp in range(1, temporary_matrix_col):
                       temporary_matrix_find_string = split_string[0]
                       for concat_index in range(1,index):
                           temporary_matrix_find_string = str(temporary_matrix_find_string) + '_' + str(split_string[concat_index])
                       cross_Product_matrix[row_next][col_index_temp] = str(temporary_matrix[temporary_matrix_dict[temporary_matrix_find_string]][col_index_temp]) +'_' + str(stateMachine[index].transition_table[stateMachine[index].state_index_pair[split_string[index]]][col_index_temp])
        temporary_matrix = cross_Product_matrix  
        temporary_matrix_dict = cross_product_dict

        #print("Now it will print the final temporary product matrix")
        #print(cross_Product_matrix)
    

    print("length of cross_Product_matrix",len(cross_Product_matrix))
    #intersection_construction(cross_Product_matrix)

    count = 0
    for count_index in range(len(cross_Product_matrix)):
        if (cross_Product_matrix[count_index][0] != [] ):        
            count = count + 1
            print(count)
        else:
            break
    intersection_matrix = [[[] for colindex in range(temporary_matrix_col)] for rowindex in range(count)]
    for row in range(0,count):        
            intersection_matrix[row]= cross_Product_matrix[row]
 

    start_time = time.time()
    
    intersection_matrix_for_buchi_automata = intersection_construction_for_buchi_automata(intersection_matrix) 
    print("---Time taken for product construction %s seconds ---" % (time.time() - start_time))
    
    #print(intersection_matrix_for_buchi_automata)
    
    start_time = time.time()        
    check_emptyness_of_Buchi_automata(intersection_matrix_for_buchi_automata)
    print("---Time taken for cycle construction %s seconds ---" % (time.time() - start_time))




class StateMachine:
      def __init__(self, name): 
          self.name = name 
          self.initial_state = None
          self.transitions = []
          self.alphabets = []
          self.state = []
          self.final_states = []
          self.transition_table = [[]]
          self.state_index_pair = {}
          self.alphabets.append('0')
      def get_initial_state(self,initial_state):          
          self.initial_state = initial_state

      def get_alphabets(self,alphabet_name):
          self.alphabets.append(alphabet_name)

      def get_final_states(self,Final_state_name):
          self.final_states.append(Final_state_name)
    
      def get_states(self, state_name):
          self.state.append(State(state_name))        


      def get_transition_table(self,one_transition):
          one_transition_temp = one_transition.split("(")
          transition_words = one_transition_temp[1].split(",")
               
          present_state = transition_words[0]

          condition = transition_words[1]
              
          next_state = transition_words[2]
          self.transitions.append(Transitions(present_state, condition, next_state))

      def form_state_transition_table(self):
          transitions_length = len(self.transitions)
          number_of_states = len(self.state)
          number_of_alphabets = len(self.alphabets)
          self.transition_table = [[[] for colindex in range(number_of_alphabets)] for rowindex in range(number_of_states + 1)]

          for index in range(0,number_of_alphabets):
               self.transition_table[0][index] = self.alphabets[index]
          
          for index in range(0, number_of_states):
              self.transition_table[index + 1][0] = self.state[index].name
              self.state_index_pair[self.state[index].name] = index + 1

          for transitions_index in range(0,transitions_length):
              for state_index in range(1, number_of_states+1):
                  if self.transitions[transitions_index].present_state == self.transition_table[state_index][0]: 
                     for alphabet_index in range(1,number_of_alphabets):
                         
                         if self.transitions[transitions_index].condition == self.alphabets[alphabet_index]:
                             
                             self.transition_table[state_index][alphabet_index] = self.transitions[transitions_index].next_state
                             
                             break
           
          
class State:
    def __init__(self, name): self.name = name

class Transitions:
      def __init__(self, present_state, condition, next_state):
          self.present_state = present_state
          self.condition = condition
          self.next_state = next_state  

def create_window():
    slave = Toplevel(master)

#---------------------Input StateMachine name-----------------
#-------------------------------------------------------------
def statemachine_save():
    global filepointer
    filename = entry_statemachine_name.get() + ".txt"
    filepointer =open(filename,'w')


Label(master, text = "Enter Statemachine Name:").grid(row = 0)

entry_statemachine_name = Entry(master)

entry_statemachine_name.grid(row = 0, column = 1)

button_save_statemachine_name = Button(master, text = 'Save', command = statemachine_save)
button_save_statemachine_name.grid(row = 0,column = 2)
#-------------------------------------------------------------
#--------------------------------------------------------------

#---------------------Input states-----------------------------
#--------------------------------------------------------------
def enable_entry():
    global no_of_state_counter
    global filepointer
    
    no_of_state_counter = int(entry_no_of_states.get())
    filepointer.write("number_of_state:"+ str(no_of_state_counter ) + "\n\n")
    filepointer.write("States:")
    entry_state.configure(state = 'normal')

def next_entry_state():
    global no_of_state_counter
    no_of_state_counter = no_of_state_counter-1
    if no_of_state_counter == 0:
       filepointer.write(entry_state.get()+ "\n\n")
       entry_state.delete(0, 'end')
       entry_state.configure(state = 'disabled') 
    else:
       filepointer.write(entry_state.get()+"," ) 
    entry_state.delete(0,'end')

Label(master, text = "Enter number of states").grid(row = 1)
Label(master, text = "Enter State:").grid(row = 2)

entry_no_of_states = Entry(master)
entry_state = Entry(master)

entry_state.configure(state = 'disabled')

entry_no_of_states.grid(row = 1, column = 1)
entry_state.grid(row = 2, column = 1)

button5 = Button(master, text = 'Save', command = enable_entry)
button5.grid(row = 1,column = 2)

button3 = Button(master,text = 'Next state',command = next_entry_state)
button3.grid(row = 2,column = 2)

#---------------------------------------------------------------
#---------------------------------------------------------------

#----------------------Input Initial state----------------------
#---------------------------------------------------------------

def Initial_state_save():
    global filepointer
    
    filepointer.write("Initial State:" + entry_initial_state.get() + "\n\n")    


Label(master, text = "Enter Initial State:").grid(row = 3)

entry_initial_state = Entry(master)

entry_initial_state.grid(row = 3, column = 1)

button6 = Button(master, text = 'Save',command = Initial_state_save)
button6.grid(row = 3,column = 2)

#---------------------------------------------------------------
#--------------------------------------------------------------

#----------------------Input Final state----------------------
#---------------------------------------------------------------

def final_states_save():
    global no_of_final_state_counter
    no_of_final_state_counter = int(entry_number_of_final_states.get())
    filepointer.write("number_of_final_states:" + entry_number_of_final_states.get() + "\n\n")
    filepointer.write("Final_states:")
    entry_final_state.configure(state = 'normal')

def next_entry_final_state():
    global no_of_final_state_counter
    no_of_final_state_counter = no_of_final_state_counter-1
    if no_of_final_state_counter == 0:
       filepointer.write(entry_final_state.get() + "\n\n")
       entry_final_state.delete(0, 'end')
       entry_final_state.configure(state = 'disabled')  
    else:
       filepointer.write(entry_final_state.get() + ",")
    entry_final_state.delete(0,'end')

Label(master, text = "Enter number of final states").grid(row = 4)
Label(master, text = "Enter Final State:").grid(row = 5)

entry_number_of_final_states = Entry(master)
entry_final_state = Entry(master)

entry_final_state.configure(state = 'disabled')

entry_number_of_final_states.grid(row = 4, column = 1)
entry_final_state.grid(row = 5,column = 1)

button5 = Button(master, text = 'Save',command = final_states_save)
button5.grid(row = 4,column = 2)

button7 = Button(master, text = 'Next Final state', command = next_entry_final_state)
button7.grid(row = 5,column = 2)


#---------------------------------------------------------------
#--------------------------------------------------------------

#----------------------Input alphabets-------------------------
#---------------------------------------------------------------

def alphabets_save():
    global no_of_alphabets_counter
    no_of_alphabets_counter = int(entry_number_of_alphabets.get())
    filepointer.write("number_of_alphabets:" + entry_number_of_alphabets.get() + "\n\n")
    filepointer.write("alphabets:")
    entry_alphabets.configure(state = 'normal')

def next_entry_alphabets():
    global no_of_alphabets_counter
    no_of_alphabets_counter = no_of_alphabets_counter-1 
    if no_of_alphabets_counter == 0:
       filepointer.write(entry_alphabets.get() + "\n\n" + "Transitions:")
       entry_alphabets.delete(0, 'end')
       entry_alphabets.configure(state = 'disabled')  
    else:
       filepointer.write(entry_alphabets.get() + ",")
    entry_alphabets.delete(0,'end')

Label(master, text = "Enter number of alphabets").grid(row = 6)
Label(master, text = "Enter alphabets:").grid(row = 7)

entry_number_of_alphabets = Entry(master)
entry_alphabets = Entry(master)

entry_alphabets.configure(state = 'disabled')

entry_number_of_alphabets.grid(row = 6, column = 1)
entry_alphabets.grid(row = 7,column = 1)

button5 = Button(master, text = 'Save', command = alphabets_save)
button5.grid(row = 6,column = 2)

button7 = Button(master, text = 'Next alphabets', command = next_entry_alphabets)
button7.grid(row = 7,column = 2)

#---------------------------------------------------------------
#--------------------------------------------------------------

#--------------------Input Transitions--------------------------
#---------------------------------------------------------------

def transitions_save_and_next():
    filepointer.write("("+ entry_Present_state.get() + "," + entry_Condition.get() + "," +entry_Next_state.get() + "),")
    entry_Present_state.delete(0,'end')
    entry_Condition.delete(0,'end')
    entry_Next_state.delete(0,'end')


def transitions_done():
    filepointer.write("("+ entry_Present_state.get() + "," + entry_Condition.get() + "," +entry_Next_state.get() + ")")
    entry_Present_state.delete(0,'end')
    entry_Condition.delete(0,'end')
    entry_Next_state.delete(0,'end')
    filepointer.close()
    #entry_Present_state.configure(state = 'disabled')
    #entry_Condition.configure(state = 'disabled')
    #entry_Next_state.configure(state = 'disabled')

Label(master, text = "Enter State Machine Transitions").grid(row = 9, column = 1)
Label(master, text = "Present state").grid(row = 11, column = 0)
Label(master, text = "Condition").grid(row = 11, column = 1)
Label(master, text = "Next state").grid(row = 11, column = 2)

entry_Present_state = Entry(master)
entry_Condition = Entry(master)
entry_Next_state = Entry(master)

entry_alphabets.configure(state = 'disabled')

entry_Present_state.grid(row = 12, column = 0)
entry_Condition.grid(row = 12, column = 1)
entry_Next_state.grid(row = 12, column = 2)

button5 = Button(master, text = 'Save & Next', command = transitions_save_and_next)
button5.grid(row = 13,column = 1)

button7 = Button(master, text = 'Done', command = transitions_done)
button7.grid(row = 13,column = 2)
#---------------------------------------------------------------
#---------------------------------------------------------------
def quit():
    master.destroy()


#------------------General Buttons--------------------------------
#-----------------------------------------------------------------
def Entry_Reset():
    entry_statemachine_name.delete(0, 'end')
    entry_no_of_states.delete(0, 'end')    
    entry_state.configure(state = 'disabled')
    entry_initial_state.delete(0, 'end')
    entry_number_of_final_states.delete(0, 'end')
    entry_final_state.delete(0, 'end')
    entry_final_state.configure(state = 'disabled')
    entry_number_of_alphabets.delete(0, 'end')    
    entry_alphabets.configure(state = 'disabled')
    entry_Present_state.delete(0, 'end')
    entry_Condition.delete(0, 'end')
    entry_Next_state.delete(0, 'end')

button4 = Button(master,text = 'Quit',command = quit)
button4.grid(row = 15, column = 2)

button_Reset = Button(master, text = 'Reset', command = Entry_Reset)
button_Reset.grid(row = 15, column = 3)
#------------------------Browse options--------------------------------
#----------------------------------------------------------------------
class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid() 
        self.browse_file()
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [("All files", "*.*")]

        options['parent'] = self
        options['title'] = 'This is a title'

    def browse_file(self):
        self.browseButton = tk.Button(self, text='Browse', command=self.askopenfile)
        self.browseButton.grid()
    def askopenfile(self):
        filename = filedialog.askopenfile(**self.file_opt )
        print(os.path.split(filename.name)[1])
        stateMachine.append(StateMachine(os.path.split(filename.name)[1]))

app = Application()                       
app.master.title('Sample application')  

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#--------------------Function of Check Schedule button---------------------------
#-------------------------------------------------------------------------------

def start_automata_intersection_procedure():
    number_of_stateMachines = len(stateMachine)
    for index in range(0,number_of_stateMachines):
        file_to_read = open(stateMachine[index].name,'r')
        for line in file_to_read:
            left = line.split(":")
            if left[0] == 'States':
               each_state_temp = left[1].split("\n")
               each_state = each_state_temp[0].split(",")
               no_of_states = len(each_state)
               for state_index in range(0, no_of_states):
                   stateMachine[index].get_states(each_state[state_index])
            elif left[0] == 'Final_states':
               each_Final_state_temp = left[1].split("\n")
               each_Final_state = each_Final_state_temp[0].split(",")
               no_of_Final_states = len(each_Final_state)
               for final_state_index in range(0, no_of_Final_states):
                   stateMachine[index].get_final_states(each_Final_state[final_state_index])  
            elif left[0] == 'Initial State':
               each_Initial_state_temp = left[1].split("\n")
               each_Initial_state = each_Initial_state_temp[0].split(",")
               
               print(" each_Initial_state is",each_Initial_state) 
               no_of_Initial_states = len(each_Initial_state)              
               for initial_state_index in range(0, no_of_Initial_states):
                   stateMachine[index].get_initial_state(each_Initial_state[initial_state_index])  
            elif left[0] == 'alphabets':
               each_alphabet_temp = left[1].split("\n")
               each_alphabet = each_alphabet_temp[0].split(",")
               no_of_alphabet = len(each_alphabet)
               for alphabet_index in range(0, no_of_alphabet):
                   stateMachine[index].get_alphabets(each_alphabet[alphabet_index])          
            elif left[0] == 'Transitions':
               left_string_temp = left[1]
              
               left_string = str("," + left_string_temp)
               each_Transitions = left_string.split(")")
               
               
               no_of_Transitions = len(each_Transitions)
               no_of_Transitions = no_of_Transitions - 1
               
               for Transitions_index in range(0, no_of_Transitions):
                   stateMachine[index].get_transition_table(each_Transitions[Transitions_index])
        
            stateMachine[index].form_state_transition_table()
            #stateMachine[index].show_transition_table()
    start_time = time.time()
    print("goint to perform product")
    new_product()  
    print("--- Total Time taken for schedulability analisys %s seconds ---" % (time.time() - start_time))
              
        
    #mem = max(memory_usage(proc=product))

    #print("Maximum memory used: {0} MiB".format(str(mem)))

button_check_schedule = Button(master,text = 'Check Schedule',command = start_automata_intersection_procedure)
button_check_schedule.grid(row = 15, column = 0)

#----------------------------------------------showing the cycle image-------------------------------

def show_cycle_image():
    os.system("dot -Tps test_original.dot -o graph_original.pdf")

button2 = Button(master, text = 'Show Cycle Image', command = show_cycle_image)
button2.grid(row = 15, column = 1)

#start_time = time.time()
mainloop()
#print("--- %s seconds ---" % (time.time() - start_time))

