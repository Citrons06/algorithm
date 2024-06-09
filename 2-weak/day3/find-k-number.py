#def quick_sort(arr):
 #   if len(arr) <= 1:
  #      return arr
   #pivot = arr[len(arr) // 2]  # 배열의 가운데 값을 피벗으로 설정
   # left = [x for x in arr if x < pivot]  # 피벗 값보다 작으면 left 배열에 삽입
   # middle = [x for x in arr if x == pivot]  # 배열의 중간 원소를 피벗으로 설정
   # right = [x for x in arr if x > pivot]  # 피벗 값보다 크면 right 배열에 삽입
   # return quick_sort(left) + middle + quick_sort(right)

#n, k = map(int, input().split())
#arr = list(map(int, input().split()))
#quick_sort(arr)
#print(arr[k])  ### 시간 초과

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 퀵 정렬 함수
def quick_sort(start, end, k):


def get_pivot(start, end):



