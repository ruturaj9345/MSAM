def row_col_reduce(arr, no_of_jobs, no_of_op):

    row_min = [0 for x in range(0,no_of_jobs+1)]
    col_min = [0 for x in range(0,no_of_op+1)]
    
    
    for i in range(0, no_of_jobs):
        min = float("inf")
        for j in range(0, no_of_op):
            if(arr[i][j]<min):
                row_min[i] = arr[i][j]
                min = arr[i][j]
                
    
    for i in range(0, no_of_jobs):
        for j in range(0, no_of_op):
            arr[i][j] = arr[i][j] - row_min[i]
    
    
    for i in range(0, no_of_jobs):
        min = float("inf")
        for j in range(0, no_of_op):
            if(arr[j][i]<min):
                col_min[i] = arr[j][i]
                min = arr[j][i]
                
    for i in range(0, no_of_jobs):
        for j in range(0, no_of_op):
            arr[j][i] = arr[j][i] - col_min[i]
               
    return arr

def find_min(arr,row_rem,col_rem,no_of_jobs,no_of_op):
    
    min_val = float("inf")
    
    
    for i in range(0, no_of_jobs):
        for j in range(0, no_of_op):
            if(arr[i][j]<min_val and row_rem[i] == False and col_rem[j] == False):
                min_val = arr[i][j]
   
    return min_val 

def remove(cost_matrix ,arr,no_of_jobs,no_of_op):
    
    row_rem = [False for x in range(0,no_of_jobs+1)]
    col_rem = [False for x in range(0,no_of_op+1)]
    
    visited = [[False for i in range(0,no_of_jobs+1)]for j in range(0,no_of_op+1)]
    
    for i in range(0, no_of_jobs):
        cnt = 0
        k = 0
        for j in range(0, no_of_op):
            if(arr[i][j] == 0 and col_rem[j] == False):
                cnt = cnt+1
                k = j
        if(cnt == 1):
            col_rem[k] = True
            visited[i][k] = True
            
        
    for i in range(0, no_of_jobs):
        cnt = 0
        k = 0
        for j in range(0, no_of_op):
            if(arr[j][i] == 0 and (col_rem[i] == False and row_rem[j] == False)):
                cnt = cnt+1
                k = j
        if(cnt == 1):
            row_rem[k] = True
            visited[k][i] = True
            
    
    #print(row_rem)
    #print(col_rem)
    
    total_cnt = 0
    for i in range(0,no_of_jobs):
        if(row_rem[i] == True):
            total_cnt = total_cnt+1

    for i in range(0,no_of_jobs):
        if(col_rem[i] == True):
            total_cnt = total_cnt+1
    
    if(total_cnt == no_of_jobs):
        print("It is optimal solution")
        total_hrs = 0
        for i in range(0, no_of_jobs):
            for j in range(0, no_of_op):
                if(visited[i][j]):
                    #print(cost_matrix[i][j])
                    total_hrs = total_hrs + cost_matrix[i][j]
        
        print("Total processing time = ",total_hrs)            
    else:
    
        min_val = find_min(arr,row_rem,col_rem,no_of_jobs,no_of_op)
        
        for i in range(0, no_of_jobs):
            for j in range(0, no_of_op):
                if(row_rem[i] == False and col_rem[j] == False):
                    arr[i][j] = arr[i][j] - min_val
                elif(row_rem[i] == True and col_rem[j] == True):
                    arr[i][j] = arr[i][j] + min_val
        
        #print(arr)
        remove(cost_matrix,arr,no_of_jobs,no_of_op)
    return 

def run():

    print("Enter no. of jobs")
    no_of_jobs = int(input())

    print("Enter no. of operators")
    no_of_op = int(input())


    arr = [[0 for i in range(0,no_of_jobs+1)]for j in range(0,no_of_op+1)]
    cost_matrix = [[0 for i in range(0,no_of_jobs+1)]for j in range(0,no_of_op+1)]


    for i in range(0, no_of_jobs):
        for j in range(0, no_of_op):
            print("enter ",i,j,"cost matrix")
            cost_matrix[i][j] = int(input())
            arr[i][j]= cost_matrix[i][j]
    
    arr = row_col_reduce(arr,no_of_jobs,no_of_op)
    
    remove(cost_matrix,arr,no_of_jobs,no_of_op)
    
    
if __name__ == '__main__':
    run()
