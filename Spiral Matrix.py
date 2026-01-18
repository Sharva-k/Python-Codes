matrix = [[1,2,3],[4,5,6],[7,8,9]]
output =[]
top = 0
bottom =len(matrix)-1
right = len(matrix)-1
left = 0

while top<=bottom and left<= right: #top boundary
    for row in range(left, right+1):
        output.append(matrix[left][row])

    top+=1
    for i in range(top,bottom+1):
        output.append(matrix[i][right])

    right-=1
    if top<=bottom:
        for i in range(right,left+1,-1):
            output.append(matrix[bottom][i])
    bottom-=1

    if left<=right:
        for i in range(bottom,top):
            output.append(matrix[i][left])
    left+=1

print(output)