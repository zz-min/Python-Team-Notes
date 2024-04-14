
# 백준 2884번 "알람 시계" (브론즈3)
# Q. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸기
# Input. 첫줄에 두정수 H,M(0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
# Output. 45분 앞서는 시간 출력

H, M=map(int,input().split())

if(M<45):
    H -= 1
    M += 15 # M=60+(M-45)  
else:
    M -= 45

if(H < 0):
    H += 24

print(str(H)+" "+str(M))



# 백준 2525번 "오븐 시계" (브론즈3)
# Q. 오븐시간을 요청하는 분단위 시간을 계산 후 요리가 끝나는시간 계산하기
# Input. 첫줄에 두정수 A,B(0 ≤ A ≤ 23, 0 ≤ B ≤ 59), 두 번째 줄에 요리하는데 필요한 시간 C(0 ≤ C ≤ 1,000)가 분단위로 제공
# Output. 요리끝나는 시간을 출력

A, B = map(int, input().split())
C = int(input())

B += C

if (B >= 60):
    A += B//60
    B %= 60

if (A > 23):
    A %= 24

print(str(A) + " " + str(B))


# 백준 2562번 "최댓값" (브론즈3)
# Q. 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고, 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# Input. 첫줄부터 아홉번째 줄까지 한줄에 하나의 자연수가 주어진다. (자연수<100)
# Ouput. 첫째줄에 최댓값출력, 둘째줄에 최댓값이 몇번째 수인지 출력

max=0 #최댓값
num=0 #최댓값 순서

for i in range(9):
  a=int(input())
  if(a>max):
    num=i
    max=a

print(max)
print(num+1)


# 백준 10810번 "공 넣기" (브론즈3)
# Q.
# 1번 ~ N번 바구니가 있다.1번 ~ N번이 적혀있는 공이 많이 있다.바구니당 공 1개만 넣을수 있다.
# M번 공을 넣으려고한다. (i j k => i번 바구니부터 j번 바구니까지 K번호가 적혀있는 공을 넣는다)
# Input 첫째줄에 N, M 둘째줄부터 i,j,k
# Ouput. 1 ~ N번 바구니 순서대로 공 번호 출력

N, M = map(int, input().split())

list = []  # 1~N번 바구니 (N=5, 0~4번 바구니생김)
for _ in range(N):
  list.append(0)

for _ in range(M):
  i, j, k = map(int, input().split())
  for t in range(i-1, j):
    list[t] = k

for p in list:
  print(p, end=" ")


# 백준 3052번 "나머지" (브론즈2)
# Q. 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다음 서로 다른 값이 몇개 있는지 구하라
# Input 첫째줄 ~ 열번째줄까지 수 하나씩 주어짐
# Ouput. 42로 나눈 서로다른 나머지가 몇개있는지 출력하라

list = []

for _ in range(10):
  a = int(input())
  b = a%42
  if not list.__contains__(b):
    list.append(b)

print(list.__len__())


# 백준 10811번 "바구니 뒤집기" (브론즈2)
# Q. 1~N번 바구니가 있다.
#  M번 바구니의 순서를 역순으로 변경 (i,j => i번째부터 j번째 바구니까지 역순으로 변경)
# Input 첫째줄에는 N, M, 두번째줄이상 부터는 i,j
# Ouput. 바구니 순서 출력

N, M = map(int, input().split())

list=[] #N개 바구니 생성
for p in range(N):
  list.append(p+1)

for _ in range(M):
  i,j = map(int,input().split())
  
  count = j-i+1
  temp=[]
  for _ in range(count):
    temp.append(0)
    
  for q in range(i,j+1):
    count -= 1
    temp[count]=list[q-1]
    
  for q in range(i,j+1):
    list[q-1] = temp[count]
    count += 1
  
for p in list:
  print(p,end=" ")


# 백준 1546번 "평균" (브론즈1)
# Q. 자기 점수중 최댓값을 M, 모든 점수를 점수/M*100으로 고친다
# Input 첫째줄에는 시험 본과목수N, 둘째 줄에는 성적이 주어짐
# Ouput. 정정된 평균을 출력

N = int(input())
score = list(map(int,input().split()))

M=max(score)
sum=0

for k in score:
  sum += k/M*100

print(sum/score.__len__())  