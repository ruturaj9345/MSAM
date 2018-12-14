def getIndex(cost_matrix, no_of_fac, no_of_wah,warehouse_demand,factory_production ):
    
    diff_of_min = []

    for i in range(0,no_of_fac):
        min1 = float("inf")
        min2 = float("inf")
    
        for j in range(0, no_of_wah):
        
            if (cost_matrix[i][j] < min1 and (warehouse_demand[j]>0) and factory_production[i]>0):
                min2 = min1
                min1 = cost_matrix[i][j]
                
            elif(cost_matrix[i][j] < min2 and (warehouse_demand[j]>0) and factory_production[i]>0):
                min2 = cost_matrix[i][j]

        diff_of_min.append(min2-min1)
        
    for i in range(0,no_of_wah):
        min1 = float("inf")
        min2 = float("inf")
        for j in range(0, no_of_fac):
            if (cost_matrix[j][i] < min1 and (warehouse_demand[i]>0) and factory_production[j]>0):
                min2 = min1
                min1 = cost_matrix[j][i]
                
            elif(cost_matrix[j][i] < min2 and (warehouse_demand[i]>0) and factory_production[j]>0):
                min2 = cost_matrix[j][i]
        
        diff_of_min.append(min2-min1)
    
    max_val_index = 0
    max_val =0
    for i in range(0, no_of_fac+no_of_wah):
        if(diff_of_min[i]>max_val):
            max_val = diff_of_min[i]
            max_val_index = i
            
            
    check_min = float("inf")
    if(max_val_index < no_of_fac):
        for i in range(0,no_of_wah):
            if(cost_matrix[max_val_index][i]<check_min and (warehouse_demand[i]>0) and factory_production[max_val_index]>0):
                check_min = cost_matrix[max_val_index][i]
                check_min_index = i
        return max_val_index,check_min_index
    else:
        max_val_index = max_val_index - no_of_fac
        for i in range(0,no_of_fac):
            if(cost_matrix[i][max_val_index]<check_min and (warehouse_demand[max_val_index]>0) and factory_production[i]>0):
                check_min = cost_matrix[i][max_val_index]
                check_min_index = i
        return check_min_index, max_val_index
            
def run():

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

    if sum(factory_production) != sum(warehouse_demand):
        print("It is an unbalanced Problem")
        exit()

    arr = [[0 for i in range(0,no_of_fac+1)]for j in range(0,no_of_wah+1)]
    cost_matrix = [[0 for i in range(0,no_of_fac+1)]for j in range(0,no_of_wah+1)]


    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            print("enter ",i,j,"cost matrix")
            cost_matrix[i][j] = int(input())
            arr[i][j]= cost_matrix[i][j]
            
    total_cost= 0
    loopvar = 0
    while(loopvar<no_of_wah):
        
        i, j = getIndex(cost_matrix,no_of_fac,no_of_wah,warehouse_demand, factory_production)
        
        if(warehouse_demand [j] <= factory_production[i]):
            
            factory_production[i] = factory_production[i] -  warehouse_demand[j]
            total_cost += warehouse_demand[j] * arr[i][j] 
            warehouse_demand[j] = 0
            loopvar = loopvar+1
            
        
        elif(warehouse_demand [j] > factory_production[i]):
            
            warehouse_demand[j] = warehouse_demand[j] - factory_production[i]
            total_cost += factory_production[i] * arr[i][j] 
            factory_production[i] = 0
            
    print("Optimal cost is %d " %(total_cost))


if __name__ == '__main__':
    run()
