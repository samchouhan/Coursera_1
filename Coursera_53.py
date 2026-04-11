#matrix using for nested loop
def matrix(initial_number,end_of_first_row,):
    
    n1=initial_number
    n2=end_of_first_row
    
    for row in range (n1,n2):
        
        for column in range(n1,n2):
            print(row*column,end=" ")
        print()
        
matrix(1,6)