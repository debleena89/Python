#------------------------------------------------------------------------------
#------emptyness checking of buchi automata------------------------------------
#------------------------------------------------------------------------------
def clean_source_target(target,source):
    global source_top
    global target_top
    source[source_top] = 0
    source_top = source_top - 1
    target[target_top] = 0
    target_top = target_top - 1
    loop_limit = 1
    while loop_limit == 1:
          visited = "visit" in source[source_top]
          if visited == False:
                 break
          source[source_top] = 0
          source_top = source_top - 1
          target[target_top] = 0
          target_top = target_top - 1
    print("after clean up..........................................")
    print("source = ", source)
    print("")
    print("target = ", target)


def check_cycle(target,source):
    global target_top
    target_top_element = target[target_top]
    target[target_top] = 0
    for in_tar in range(len(target)):
         if target_top_element == target[in_tar]:
           print("cycle found",target_top_element,target[in_tar])
           target[target_top] = target_top_element
           print("target=",target)
       #print("")
       #print("source = ", source)
           print("....................before clean up....................")
           print("source = ", source)
           print("")
           print("target = ", target)
           print("")
           clean_source_target(target,source)
           return 1
    target[target_top] = target_top_element
    return 0

def insert_to_target(element,target):
    global target_top
    target_top = target_top + 1
    target[target_top] = element

def check_emptyness_of_Buchi_automata(intersection_matrix_for_buchi_automata):
    global source_top
    global target_top
    source = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    target = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    source[0] = intersection_matrix_for_buchi_automata[1][0]
    #source_top = 0    
    loop_limit = 1
    while loop_limit == 1:
          current_state = source[source_top]
          #print("curresnt_state is ", current_state)
          insert_to_target(current_state,target)
          #print("target=",target)
          is_cycle_checked = check_cycle(target,source)
          if is_cycle_checked == 1:
             current_state = source[source_top] 
          source[source_top] = str("visit_" + source[source_top])
          for row_index in range(0,len(intersection_matrix_for_buchi_automata)):
              if intersection_matrix_for_buchi_automata[row_index][0] == current_state :
                 #print("row_index===", row_index)
                 if intersection_matrix_for_buchi_automata[row_index][1] != current_state :
                    source_top = source_top + 1
                    source[source_top] = intersection_matrix_for_buchi_automata[row_index][1]
                 if intersection_matrix_for_buchi_automata[row_index][2] != current_state :
                    source_top = source_top + 1
                    source[source_top] = intersection_matrix_for_buchi_automata[row_index][2]
                 #print("source=", source)      

