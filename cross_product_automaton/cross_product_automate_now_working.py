

import re
import numpy as NP
from scipy import linalg as LA
p_final_state = 'p0'
q_final_state = 'q0'
r_final_state = 'r2'
accepting_states = []
#accepting_states = ['p0_q0_3','p2_q1_3']
#accepting_states = ['f','g']
target_top = -1
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
   # intersection_matrix_for_buchi_automata = (['00','A','B','C'],['a','b','c',' s'],['b','d','e','s'],['c','b','c',''],['d','d','e',''],['e','f','g',''],['f','b','c','s'],['g','a','h',''],['h','a','h',''],['s','a','b','c'])
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
    global p_final_state
    global q_final_state
    global r_final_state
    intersection_matrix_len = len(intersection_matrix)
    intersection_matrix_for_buchi_automata_len = 4 * intersection_matrix_len
    intersection_matrix_for_buchi_automata_col = len(intersection_matrix[0])
    intersection_matrix_for_buchi_automata = [[[] for colindex in 
         range(intersection_matrix_for_buchi_automata_col)] for rowindex in 
         range(intersection_matrix_for_buchi_automata_len)]
    track = []
    track_index = 0
    current_state = intersection_matrix[1][0]
    #print("current_state is before the loop", current_state )
    splitted_string = current_state.split("_")
    if splitted_string[0] != p_final_state :
       for col in range(intersection_matrix_for_buchi_automata_col):
           intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_1"  )
    elif splitted_string[1] != q_final_state :
       for col in range(intersection_matrix_for_buchi_automata_col):
           intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_2"  ) 
    elif splitted_string[2] != r_final_state :
      for col in range(intersection_matrix_for_buchi_automata_col):
           intersection_matrix_for_buchi_automata[1][col] = str(intersection_matrix[1][col] + "_3"  ) 

      
    track_index = track_index + 1
    track.append(intersection_matrix_for_buchi_automata[1][0])
    visit_row = 2
    for row_index in range(1, intersection_matrix_for_buchi_automata_len ):
        pass_flag = 0
        for col_index in range(1,intersection_matrix_for_buchi_automata_col):
            current_state = intersection_matrix_for_buchi_automata[row_index][col_index]
            print("current_state is, row_index", current_state,row_index)
            if visit_row == row_index:
             break
            #if current_state == '0_1' or current_state == '0_2' or current_state == '0_3' or current_state == '0_4':
               #continue
            #if not current_state:
                 # break
            found_track= current_state in track
            if found_track == False:
               pass_flag = 1                    
               splitted_string = current_state.split("_")
               #print("the found splittedd string is", splitted_string)
               find_string = str(splitted_string[0] + '_' + splitted_string[1] + '_' + splitted_string[2])
              
               for i_m_index in range(intersection_matrix_len):
                   #print("the find string is:", find_string)
                   if intersection_matrix[i_m_index][0] == find_string :
                      index = i_m_index
                      break

               intersection_matrix_for_buchi_automata[visit_row][0] = current_state
               if splitted_string[3] == '1':
                  #print("hiiii",splitted_string[0])     
                  if splitted_string[0] != p_final_state :
                     for col in range(1,intersection_matrix_for_buchi_automata_col):
                         intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_1"  )
                  else:
                     #print("executed else")
                     for col in range(1,intersection_matrix_for_buchi_automata_col):
                         intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_2"  )     
                     #print("result",intersection_matrix_for_buchi_automata[visit_row])

               if splitted_string[3] == '2':
                  #print("here current state", current_state)
                  if splitted_string[1] != q_final_state :
                      for col in range(1,intersection_matrix_for_buchi_automata_col):
                          intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_2"  )
                  else:
                      #print("executed else for q2")
                      for col in range(1,intersection_matrix_for_buchi_automata_col):
                          intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_3"  ) 
                     # print("result",intersection_matrix_for_buchi_automata[visit_row])
                         # accepting_states.append(str(intersection_matrix[index][col] + "_3" ))
                         # print("the accepting states are:", accepting_states)

               if splitted_string[3] == '3':
                  #print("the splited string is ", splitted_string[1])
                  if splitted_string[2] != r_final_state :
                      for col in range(1,intersection_matrix_for_buchi_automata_col):
                          intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_3"  )
                  else:
                      for col in range(1,intersection_matrix_for_buchi_automata_col):
                          intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_4"  ) 
                          accepting_states.append(str(intersection_matrix[index][col] + "_4" ))
                         # print("the accepting states are:", accepting_states)

               if splitted_string[3] == '4':                        
                     for col in range(1,intersection_matrix_for_buchi_automata_col):
                         intersection_matrix_for_buchi_automata[visit_row][col] = str(intersection_matrix[index][col] + "_1"  )
                      
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
#--------generate combination of given elements here 1 and 2---
#--------upto a certain depth,signifies the length of the control action combination

def product(A, B, C):
    A_row = len(A)
    A_col = len(A[0])
   
    B_row = len(B)
    B_col = len(B[0])   
  
    C_row = len(C)
    C_col = len(C[0]) 
    
    product_matrix_row = ((A_row - 1) * (B_row - 1) * (C_row - 1)) + 1
    product_matrix_col = A_col     
    
    cross_Product_matrix = [[[] for colindex in range(product_matrix_col)] for rowindex in range(product_matrix_row)]
    cross_Product_matrix[0]= A[0]

    temporary_matrix_row = ((A_row - 1) * (B_row - 1)) + 1
    temporary_matrix_col = A_col
    temporary_matrix = [[[] for colindex in range(temporary_matrix_col)] for rowindex in range(temporary_matrix_row)]

    #cross_Product_matrix[0][1] = 'a'
    #cross_Product_matrix[0][2] = 'b'
    row_index = 1
    for row_p_m in range(1):
        for row_a in range(1,A_row):
          for row_b in range(1,B_row):
              for col in range(0,A_col):
                  if str(A[row_a][col]) == '-' or str(B[row_b][col]) == '-':
                     temporary_matrix[row_index][col] = str(0)
                  else :
                     temporary_matrix[row_index][col] = str(A[row_a][col])+'_'+str(B[row_b][col])
              row_index = row_index + 1
    
    #for row_p_m in range(1):
    row_index = 1
    for row_temp in range(1,temporary_matrix_row):
          for row_c in range(1,C_row):
              for col in range(0,A_col):
                  if str(C[row_c][col]) == '-' or str(temporary_matrix[row_temp][col]) == '0':
                     cross_Product_matrix[row_index][col] = str(0)
                  else :
                     cross_Product_matrix[row_index][col] = str(temporary_matrix[row_temp][col])+'_'+str(C[row_c][col])
              row_index = row_index + 1
    print("the cross product matrix is", cross_Product_matrix )
    print("-----------------------------------------------------")
    #print("")
    intersection_construction(cross_Product_matrix)

if __name__ == "__main__":

#------The two matrices are assigned values----------------
    A = (['00','a','b'],['p0','p1','p2'],['p1','p2','p1'],['p2','p0','p3'],['p3','p2','p1'])    
    #B = (['00','a','b'],['q0','q0','q1'],['q1','q0','q1'])
    B = (['00','a','b'],['q0','q1','q2'],['q1','q2','q1'],['q2','q1','q0'])
    C = (['00','a','b'],['r0','r3','r0'],['r1','r0','r2'],['r2','r3','r0'],['r3','r3','r1'])
    print(len(A[0]))
    print(A)
    print("...........")
    print(B)
    print("")
    product(A,B,C)



    
