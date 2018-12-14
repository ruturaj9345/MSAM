
def getMin(cost_matrix, warehouse_demand, no_of_fac, no_of_wah):
    min = 1000
    i_val = 0
    j_val = 0
    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            if(cost_matrix[i][j] < min):
                min = cost_matrix[i][j]
                i_val = i
                j_val = j
            elif(cost_matrix[i][j] == min):
                if(warehouse_demand[j] > warehouse_demand[j_val]):
                    i_val = i
                    j_val = j

    return i_val, j_val

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

    arr = [[0 for i in range(0,no_of_fac)]for j in range(0,no_of_wah)]
    cost_matrix = [[0 for i in range(0,no_of_fac)]for j in range(0,no_of_wah)]


    for i in range(0, no_of_fac):
        for j in range(0, no_of_wah):
            print("enter ",i,j,"cost matrix")
            cost_matrix[i][j] = int(input())

    i , j = getMin(cost_matrix, warehouse_demand, no_of_fac, no_of_wah)

    print(i)
    print(j)


if __name__ == '__main__':
    run()
