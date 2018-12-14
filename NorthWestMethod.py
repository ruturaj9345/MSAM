# code for NWR

print("Enter no. of factories")
no_of_fac = int(input())

print("Enter no. of warehouses")
no_of_wah = int(input())

factory_production = [0 for x in range(0,no_of_fac)]
warehouse_demand = [0 for x in range(0,no_of_wah)]

for loopCounter in range(0,no_of_fac):
    print("Enter",loopCounter+1," factory's production")
    factory_production[loopCounter] = int(input())

for loopCounter in range(0,no_of_wah):
    print("Enter",loopCounter+1," warehouse demand")
    warehouse_demand[loopCounter] = int(input())

if (sum(factory_production) != sum(warehouse_demand)):
    print("It is an unbalanced Problem")
    exit()

arr = [[0 for i in range(0,no_of_wah)]for j in range(0,no_of_fac)]
cost_matrix = [[0 for i in range(0,no_of_wah)]for j in range(0,no_of_fac)]

print(arr)
for i in range(0, no_of_fac):
    for j in range(0, no_of_wah):
        print("enter ",i,j,"cost matrix")
        cost_matrix[i][j] = int(input())

j=0
i=0

while(i<no_of_fac and j<no_of_wah):
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

total_cost = 0

for i in range(0, no_of_fac):
    for j in range(0, no_of_wah):
        total_cost = total_cost + arr[i][j]*cost_matrix[i][j]

print("Optimal Cost: ",total_cost)
