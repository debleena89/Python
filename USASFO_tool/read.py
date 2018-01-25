if __name__== "__main__":
   
   filepointer = open('stateMachine_1.txt', 'r')
   for line in filepointer:
       print(line)
       print("next")
   filepointer.close()
    
