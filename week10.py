# Day 46: Standard binary search
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
arr = [1,3,5,7,9]
print(binary_search(arr, 5))

# Day 47: Search in rotated sorted array
def search_rotated(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            if arr[mid] < target <= arr[r]:
                l = mid+1
            else:
                r = mid-1
    return -1
arr = [4,5,6,7,0,1,2]
print(search_rotated(arr, 0))

# Day 48: 2D matrix traversal
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# Day 49: Spiral order matrix
def spiral(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral(matrix))

# Day 50: Transpose matrix
matrix = [[1,2,3],[4,5,6]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose)
