if __name__ == '__main__':
    
    print("Enter no. of stratergies of player 1")
    no_of_stp1 = int(input())
    
    print("Enter no. of stratergies of player 2")
    no_of_stp2 = int(input())
    
    cost_matrix = [[0 for i in range(0,no_of_stp1+1)]for j in range(0,no_of_stp2+1)]
    
    
    for i in range(0, no_of_stp1):
        for j in range(0, no_of_stp2):
            print("enter ",i,j,"cost matrix")
            cost_matrix[i][j] = int(input())
            
    row_min = []
    col_max = []
    k =0
    min_val = float("inf")
    for i in range(0, no_of_stp1):
        min_val = float("inf")
        for j in range(0, no_of_stp2):
            if(cost_matrix[i][j]<min_val):
                min_val = cost_matrix[i][j]
        row_min.append(min_val)

    k =0
    max_val = 0
    for i in range(0, no_of_stp2):
        max_val = 0
        for j in range(0, no_of_stp1):
            if(cost_matrix[j][i]>max_val):
                max_val = cost_matrix[j][i]
        col_max.append(max_val)
        
                                    
    maxmin = 0
    for loopCounter in range(0,no_of_stp1):
        if(row_min[loopCounter]>maxmin):
            maxmin = row_min[loopCounter]
            p1index = loopCounter
    
    minmax = float("inf")
    
    for loopCounter in range(0,no_of_stp2):
        if(col_max[loopCounter]<minmax):
            minmax = col_max[loopCounter]
            p2index = loopCounter
    
    if(maxmin == minmax):
        print("Game Value is ",maxmin)
        print("Player 1 stratergy is", p1index+1)
        print("Player 2 stratergy is", p2index+1)
        
    p1 = [0 for x in range(0,no_of_stp1)]
    p2 = [0 for x in range(0,no_of_stp2)]
    
    p1[p1index] = 1
    p2[p2index] = 1
    
    print("Player 1:")
    print(p1)
    print("Player 2:")
    print(p2)    