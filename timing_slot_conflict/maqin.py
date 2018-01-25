if __name__ == "__main__":
    print "number of tasks"
    num_of_tasks = raw_input()
    tasks = [[]]
    #tasks = [[[] for colindex in range(2)] for rowindex in range(int(num_of_tasks))]
    for index in range(0,int(num_of_tasks)):
        print "name of the task"
        tasks[index][0] = raw_input()
        print " slot limit"
        tasks[index][1] = raw_input()
    print(tasks)    

