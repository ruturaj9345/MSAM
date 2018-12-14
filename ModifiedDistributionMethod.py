def cal_cost(cost_matrix, arr, no_of_fac, no_of_wah):

    total_cost = 0
    
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            total_cost = total_cost + arr[i][j]*cost_matrix[i][j]
    
    return total_cost

def NWC(no_of_fac, no_of_wah, factory_production, warehouse_demand ,cost_matrix,arr):
    
    j=0
    i=0
    
    while(factory_production[i]>0 and warehouse_demand[j]>0):
        if(warehouse_demand[j] < factory_production[i]):
            arr[i][j] = warehouse_demand[i]
            factory_production[i] = factory_production[i] - warehouse_demand[i]
            warehouse_demand[i] = 0
            j+=1
        else:
            warehouse_demand[j] = warehouse_demand[j] - factory_production[i]
            arr[i][j] = factory_production[i]
            factory_production[i] = 0
            i+=1
    
    total_cost = cal_cost(cost_matrix , arr, no_of_fac, no_of_wah)
    
    return total_cost

def no_of_occupied_cells(arr,no_of_fac,no_of_wah):

    cnt = 0
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            if(arr[i][j]!=0):
                cnt +=1
    return cnt
# arr means cost in small box
#cost matrix is actual one
def MODI(arr,cost_matrix,no_of_fac, no_of_wah):
    #print(arr)
    no_of_occupied = no_of_occupied_cells(arr,no_of_fac,no_of_wah)
    #print(no_of_occupied)
    if(no_of_occupied == no_of_fac + no_of_wah -1):
        print("It is a non-denerate problem")
    else:
        print("It is a denerate problem")
        exit()
 
    u_row = [0 for x in range(0,no_of_fac+1)]
    v_col = [0 for x in range(0,no_of_wah+1)]
    
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            if(arr[i][j]!=0):
                if(i == 0):
                    v_col[j] = cost_matrix[i][j] - u_row[i]
                else:
                    if(v_col[j]!=0):
                        u_row[i] = cost_matrix[i][j] - v_col[j]
                    elif(u_row[i]!=0):
                        v_col[j] = cost_matrix[i][j] - u_row[i]

    #print(u_row)
    #print(v_col)
    
    neg_val = []
    delta = [0 for x in range(0,(no_of_fac * no_of_wah - no_of_occupied)+1)]
    k =0
    m =0
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            if(arr[i][j]==0):
                delta[k] = cost_matrix[i][j] - (u_row[i] + v_col[j])
                if(delta[k] < 0):
                    neg_val.append([i,j]) 
                    m+=1
                k+=1
            
    #print(delta)
    #print(neg_val)
    check = 0
    
    for i in range(0, ((no_of_fac * no_of_wah)-no_of_occupied)+1):
        if(delta[i]<0):
            check = 1 # not optimal
            
    if(check == 0):
        opt_cost = cal_cost(cost_matrix, arr, no_of_fac, no_of_wah)
        print("Optimal solution by MODI method is ", opt_cost)
        exit()
    else:
        print("The NWC is not optimal solution")
    
    return neg_val

def utility(parent, temp_parent, current_node,visited ,arr, cost_matrix, no_of_fac, no_of_wah, loop,check):
    
    if(current_node == parent and check == True):
        #print("loop found")
        loop.pop()
        #print(loop)
        update_loop(loop,arr)
        MODI(arr,cost_matrix,no_of_fac, no_of_wah)
        
    
    i, j = current_node
    #add right element
    if((j+1 < no_of_wah) and (visited[i][j+1] == False) and ((arr[i][j+1]>0) or [i,j+1] == parent)):
        if([i,j+1] != temp_parent):
            visited[i][j+1] = True
            #print(i,j+1)
            loop.append([i,j+1])
            utility(parent, [i,j], [i,j+1], visited ,arr, cost_matrix, no_of_fac, no_of_wah, loop,True)
    
    #add left element    
    
    if((j-1 >= 0) and (visited[i][j-1] == False) and ((arr[i][j-1]>0) or [i,j-1] == parent)):
        if([i,j-1] != temp_parent):
            visited[i][j-1] = True
            #print(i,j-1)
            loop.append([i,j-1])
            utility(parent,[i,j] ,[i,j-1], visited ,arr, cost_matrix, no_of_fac, no_of_wah, loop,True)        
    
    #add bottom element
    
    if((i+1 < no_of_fac) and (visited[i+1][j] == False) and ((arr[i+1][j]>0) or [i+1,j] == parent)):
        if([i+1,j] != temp_parent):
            visited[i+1][j] = True
            #print(i+1,j)
            loop.append([i+1,j])
            utility(parent,[i,j] ,[i+1,j], visited ,arr, cost_matrix, no_of_fac, no_of_wah,loop ,True)
    
    #add top element
    
    if((i-1 >= 0) and (visited[i-1][j] == False) and ((arr[i-1][j]>0) or [i-1,j] == parent)):
        if([i-1,j] != temp_parent):
            visited[i-1][j] = True
            #print(i-1,j)
            loop.append([i-1,j])
            utility(parent,[i,j] ,[i-1,j], visited ,arr, cost_matrix, no_of_fac, no_of_wah,loop ,True)
    if(len(loop)!=0):
        loop.pop()
    
    return 


def findCycle(neg_val, arr, cost_matrix, no_of_fac, no_of_wah):
    
    loop = []
    visited = [[False for i in range(0,no_of_fac+1)]for j in range(0,no_of_wah+1)]
    k = 0
    
    for k in neg_val :
        parent = k
        #print("Starting from",parent)
        loop.append(parent)
        utility(parent, parent, parent ,visited ,arr, cost_matrix, no_of_fac, no_of_wah,loop ,False)
        
    return 

def update_loop(loop,arr):
    #print("updating values")
    min_val = float("inf")
    for i in range(1,len(loop)):
        m,n = loop[i]
        if(arr[m][n] < min_val):
            min_val = arr[m][n]
            
    flag = True
    
    for i in range(0,len(loop)):
        m, n = loop[i]
        if(flag):
            arr[m][n] = arr[m][n]+min_val
            flag = False
        else:
            arr[m][n] = arr[m][n] - min_val
            flag = True
    
    #print(arr)
    return


if __name__ == '__main__':
    
    print("Enter no. of factories")
    no_of_fac = int(input())
    
    print("Enter no. of warehouses")
    no_of_wah = int(input())
    
    factory_production = [0 for x in range(0,no_of_fac+1)]
    warehouse_demand = [0 for x in range(0,no_of_wah+1)]
    
    for loopCounter in range(0,no_of_fac):
        print("Enter",loopCounter+1," factory's production")
        factory_production[loopCounter] = int(input())
    
    for loopCounter in range(0,no_of_wah):
        print("Enter",loopCounter+1," warehouse demand")
        warehouse_demand[loopCounter] = int(input())
    
    if (sum(factory_production) != sum(warehouse_demand)):
        print("It is an unbalanced Problem")
        exit()
    
    arr = [[0 for i in range(0,no_of_fac+1)]for j in range(0,no_of_wah+1)]
    cost_matrix = [[0 for i in range(0,no_of_fac+1)]for j in range(0,no_of_wah+1)]
    
    
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            print("enter ",i,j,"cost matrix")
            cost_matrix[i][j] = int(input())

    total_cost = NWC(no_of_fac, no_of_wah, factory_production, warehouse_demand ,cost_matrix, arr)
    print("Total cost by NWC method is ",total_cost)
    neg_val = MODI(arr,cost_matrix,no_of_fac, no_of_wah)
    findCycle(neg_val, arr, cost_matrix, no_of_fac, no_of_wah)
    