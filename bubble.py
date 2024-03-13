#버블 솔트 알고리즘

def bubble_sort(arr):
    for number in range(len(arr) -1 ,0,-1): #역순으로 인덱스를 출력
        for i in range(number): # 0부터 number까지 반복
            if arr[i] >= arr[i+1]: # 만약 arr[i]가 arr[i+1]보다 크거나 같다면
                arr[i+1],arr[i] = arr[i],arr[i+1] #두 값을 바꿔준다

    return arr

li = [4,5,2,4,5,6,7,9,4,2,3,5]

sorted_li = bubble_sort(li)
print(sorted_li)