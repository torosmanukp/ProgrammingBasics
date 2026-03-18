#task 1

# arr = [-12, 8, -7, 6, 12, -9, 14]
# suma = 0
# counter = 0

# for i in arr:
#     if i >=0:
#         print(i, end=" ")
#         suma += i
#         counter+=1
# print(f" \nThe sum is: {suma}")
# print(f"The avarage is: {suma / counter}")
#


# arr_positive = []
# for i in arr:
#     if i >0:
#         arr_positive.append(i)
#
# print(f" List: {arr_positive}")
# print(f" Sum: {sum(arr_positive)}")
# print(f"Average: {sum(arr_positive)/len(arr_positive)}")

#task 2

arr = [54, 43, 2, 5, 14, 17, 18, 9]
even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even: {even}")
print(f"0dd: {odd}")


#task 3

# arr = [1, 2, 2, 3, 4, 5, 5]
# unique=[]
# for i in arr:
#     for i not in unique:
#         unique.append(i)
# print(unique)
#
# #task 4
#
# for i in range(len(arr)//2):
#     arr[i], arr[len(arr) -i -1] = arr[len(arr) -i -1], arr[i]
#
# print(f"Reversed: {arr}")

#task 5

# arr=list(map(int, input().split()))
# cpp=True
# for i in range(len(arr)):
#     if arr[i] != arr[len(arr) - i -1]:
#         cpp=False
#         break
# print(cpp)

# is_sym=True
# left=0
# right=len(arr)-1
# while left<right:
#     if arr[left]!=arr[right]:
#         is_sym=False
#         break
#     left+=1
#     right-=1
# print(is_sym)

#task 6

# noisy_data=[10, 12, 30, 14, 11, 13, 12, 18]
# window=3
# smoothed_data=[]
# for i in range(len(noisy_data) -window+1):
#     values= noisy_data[i:i+window]
#     average = sum(values)/window
#     smoothed_data.append(round(average,2))
# print(f"{smoothed_data}")

#task 7
# g_forces = [0.98, 1.02, 1.85, 1.20, 0.99, 1.01, 2.10, 1.60, 0.98]
# arr=[]
# arr = [1.0] + g_forces + [1.0]
# peaks=[]
# window=3
# for i in range(1, len(arr)-1):
#     if arr[i]>arr[i-1] and arr[i]>arr[i+1] and arr[i]>1.5:
#         peaks.append(arr[i])
# print(peaks)

#task 8

# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# trans=[]
# rows=len(matrix)
# cols=len(matrix[0])
# for i in range(cols):
#     trans.append([])
#     for j in range(rows):
#         trans[i].append(matrix[j][i])
# print(trans)

#task 9
# matrix = [[1, 2], [3, 4], [5, 6]]
# vector = [10, 20]
# if len(matrix[0]) != len(vector):
#     print("Error")
# else:
#     result = []
#     for i in range(len(matrix)):
#         row_sum = 0
#         for j in range(len(matrix[0])):
#             row_sum+= matrix[i][j]*vector[j]
#         result.append(row_sum)
# tr_result = []
# for x in result:
#     tr_result.append([x])
# print(tr_result)

#eolymp 8956

# n = int(input())
# arr = list(map(int, input().split()))
# min=[]
# for i in arr:
#     if i<0:
#         min.append(i)
# if not min:
#     print("NO")
# else:
#     print(len(min))
#     print(*min[::-1])