# 1. 코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기

[** YouTube URL ( 이코테 2021 강의 몰아보기 1 ) **](https://www.youtube.com/watch?v=m-9pAwq1o3w&t=3752s)
  


## 1. 빅오 표기법

> 좋음, 적은 시간소요 <-------------------------> 나쁨, 많은 시간소요  
> O(1) > O(logN) > O(N) > O(NlogN) > O(N^2) > O(N^3) > O(2^n)

## 2. 시간복잡도 계산
### (1) N개의 데이터의 합 
> 시간복잡도 : O(N)

    array = [3,5,1,2,4]
    summary = 0

    for x in array:
        summary += x

    print(summary)

### (2) 2중 반복문
> 시간복잡도 : O(N^2)

    array = [3,5,1,2,4]

    for i in array:
        for j in array:
            print (i*j)

## 3. Tip! "코테는 보통 시간제한 1~5초이다!"
> 연산횟수 5억번 (5* 10^8) => Python 5~15초 소요

    [예시] 
    
    O(N^3) => N의 최대가 5,000이라면!
    총 5^3*10^9 = 125,000,000,000


## 4. 문제에서 가장 먼저 확인할 사항 : 시간제한조건 (수행시간 요구사항)

    [예시] 
    
    시간제한 : 1초
    - N 최대 500 일때 : O(N^3) 가능 => 5^3*10^6 = 125,000,000
    - N 최대 2,000 일때 : O(N^2) 가능 => 2^2*10^6 = 4,000,000
    - N 최대 100,000 일때 : O(NlogN) 가능 => 10^5 *
    - N 최대 10,000,000 일때 : O(NlogN) 가능 => 10^7

## 5. 수행시간 측정 예제코드
    import time

    start_time = time.time()

    <------- 코딩 ------->

    ent_time = time.time()

    print("소요시간 : ",ent_time - start_time)

## 6. 파이썬 자료형
>정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전 등
### (1) 정수형
>양의 정수, 음의 정수, 0
### (2) 실수형
>- 소수점 아래의 데이터를 포함하는 수   
>- 양의 실수, 음의 실수  
>- 정수부가 0일 때 0 생략가능 : a = -.7 #출력시 -0.7  
>- 실수부가 0일 때 0 생략가능 : b = 5.  #출력시 5.0  
### (3) 리스트
>- 순서 O  
>- 여러 데이터 연속담을 때 (Array, LinkedList와 유사)  
>- 초기화 1 : a = [0] * 3 #출력시 [0,0,0]  
>- 초기화 2 : a = [1,2,3,4,5,6,7]  
>- 초기화 3 : a = list(range(4)) #출력시 [0,1,2,3]  
>- Indexing 인덱싱 (특정 원소에 접근)  
>   - a[2] (index 0부터니까 3번째 데이터 출력 : 3)  
>   - a[-1] (뒤에서 2번째 데이터 출력 : 6)  
>- Slicing 슬라이싱 (연속적인 위치의 원소 접근)
>   - a[1 : 3] (index 3 이전까지 2개 출력 : [2,3])
>- 컴프리헨션 (대괄호에 조건문과 반복문을 적어 리스트초기화)
>   - array = [i for i in range(4)] #출력시 [0,1,2,3]
>   - array = [i for i in range(4) if i % 2 ==1 ] #출력시 [1,3]
>   - array =[[0] * 3] #출력시 [[0,0,0]]
>   - array =[[0] * 3 for _ in range(2)] #출력시 [[0,0,0],[0,0,0]]
>- 메서드 
>   - append(삽입), sort(정렬), reerse(뒤집기), insert(삽입), count(개수),remove(제거)
### (4) 문자열 
> "" 혹은 ''     
### (5) 튜플
>- 리스트와 유사, 한 번 선언되면 수정 불가.
>- 리스트보다 상대적으로 공간 효율적
>- 순서 O
>- 튜플 : 소괄호 사용 () VS 리스트 : 대괄호 사용 []
>- 초기화 : b = (1,2,3,4)
>- Indexing 인덱싱 (특정 원소에 접근)
>   - b[2] #출력시 4  
>- Slicing 슬라이싱 (연속적인 위치의 원소 접근)
>   - b[1:3] (index 3 이전까지 2개 출력 : (2,3) )
### (6) 사전 - 딕셔더리형
>- key와 value의 쌍을 데이터로 가짐 
>- 순서 X (조회시 O(1))
>- 초기화 : d = dict(), d['ab']='ab123',d['cd']='cd123'
### (7) 집합 
>- 중복 X, 순서 X (조회시 O(1)) 
>- 리스트/문자열로 초기화 가능
>- 집합 : 중괄호 {} VS 튜플 : 소괄호 () VS 리스트 : 대괄호 []
>- 초기화1 : d1 = set([1,2,3,4,5])
>- 초기화2 : d2 = {3,4,5,6,7}
>- 연산 
>   - 합집합 d1 | d2 #출력시 {1,2,3,4,5,6,7}
>   - 교집합 d1 & d2 #출력시 {3,4,5}
>   - 차집합 d1 - d2 #출력시 {1,2}
>- 메서드
>   - add(원소1개추가), update(원소여러개추가), remove(삭제)

## 7. 지수 표현방식
> e, E 다음에 오는 수는 10이 지수부 

    [예시] 

    1e9 = 1 * 10^9 = 1,000,000,000 #출력시 1000000000.0
    75.25e1 = 75.25 * 10^1 = 752.5
    3954e-3 = 3954 * 10^-3 = 3.954

## 8. 강제 형변환
    a = 1e3
    출력시 
    print(a) : 1000.0
    print(int(a)) : 1000

## 9. 실수형 계산의 오차
>- 10진수 계산시 : 0.3 + 0.6 == 0.9
>- 2진수 계산시 : 0.3 + 0.6 != 0.9 #출력시 0.899999999
> 실수형 저장시 4byte 혹은 8byte사용하여 메모리 할당

## 10.  실수형의 반올림 round()
    - 123.456을 소수 3째자리에서 반올림 (소수점2자리만 나타내쇼)
        => round(123.456, 2) = 123.46
            round(0.3+0.6, 4) = 0.9

## 11. 사칙연산
> (1) 나누기 연산자(/) : 결과 실수형  
(2) 나머지 연산자(%)   
(3) 몫 연산자(//)  
(4) 거듭제곱 연산자(**)  
&nbsp;&nbsp;&nbsp;&nbsp;: 5 ** 3 == 5^3 == 125  
&nbsp;&nbsp;&nbsp;&nbsp;: 5 ** 0.5 == 4^0.5 == 2.2360679775

## 12. 입출력
### (1) input() : 한줄의 문자열 입력받음
        : n = int(input()) 
          print("입력된 값 : " + str(n))
### (2) map() : 리스트의 모든 원소에 각 특정함수를 적용 
        : data = list(map(int, input().split())) # 공백 기준으로 구분 
          print(data)
        : a,b,c = map(int, input().split())
### (3) readline : 빠르게 입력받기
        : import sys
            d = sys.stdin.readline().rstrip() # 입력받고 줄바꿈이 입력키
            print(d)
### (4) print() : 기본 출력 함수
        : default 줄바꿈 print("hello")
        : 줄바꿈 안할라면 print("dd",end=" ")

## 13. 조건문
### (1) if
        : if x >= 10:
            print("x>=10")
         elif x < 3:
            pass # 이 줄 무시하고 넘어감~
         else:
            print("else")
        : result = "Seccess" if score >=80 else "Fail"

### (2) in / not in
        : x in list # 리스트안에 x가 들어가면 True
        : x not in str # 문자열 안에 x가 안들어가면 True

## 14. 반복문
### (1) while
        : while i <=9:
            print(i)
        : i = 1
        while True:
            if i == 5:
                break
            print(i,end=" ") # 출력시 1 2 3 4
            i += 1
### (2) for 
        : for i in list:
            print(i)
        : for i in range(1,10):
            if i%2 == 0:
                continue
            print(i,end=" ") # 출력시 1 3 5 7 9

## 15. 함수와 람다식
### (1) 함수
    def func(a,b):
        return a-b

    print(func(4,1)) # 출력시 3
    print(func(b=1,a=8)) # 출력시 7
### (2) global 키워드
> 함수 밖에 변수를 참조  
        
    a=0
    def func():
        global a
        a +=1

    for i in range(5): func()

    print(a) # 출력시 5
### (3) 람다 lambda 표현식
    print((lambda a,b: a+b)(3,7)) 
    # 출력시 10
    
    array = [('A',50),('B',32),('C',74)]
    print(sorted(array, key=lambda x: x[1])) 
    # 출력시 [('B',32),('A',50),('C',74)]
        
## 16. 파이썬 표준 라이브러리
### (1) itertools
> 반복되는 형태 데이터 처리 (순열과 조합 라이브러리)
### (2) heapq 
> 힙(Heap) 자료구조 제공하여 우선순위 큐 기능구현
### (3) bisect
> 이진 탐색 기능 제공
### (4) collections 
> 덱(deque), 카운터(Counter) 등의 자료구조 포함
### (5) math
> 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, 파이(pi) 등  
>> sum([1,2,3]), min(7,3,5), max(7,3,5), eval("(3+5)*7")  
>> sorted([9,1,8]), sorted(array, key=lambda x: x[1],  reverse=True)

## 17. 순열과 조합
### (1) 순열
> 서로 다른 n개에서 서로다른 r개들 선택하여 일렬로 나열  
> 3개중 3개 선택한 순열 => 'abc','acb','bac','bca','cab','cba'
>> nPr = n * (n-1) * ... * (n-r+1) = 3 * 2 * 1 = 6

    from itertools import permutations
    
    data = ['a','b','c']
    print(list(permutations(data,3))) 
    # 출력시 [('a','b','c'),('a','c','b'),('b','a','c'),('b','c','a'),('c','a','b'),('c','b','a')]
### (2) 조합
> 서로 다른 n개에서 순서에 상관없이 서로다른 r개들 선택  
> 3개중 2개 선택한 조합 =>'ab','ac','bc'  
>>nCr = ( n * (n-1) * ... * (n-r+1) )/r! = (3 * 2 * 1)/(1*2) = 3

    from itertools import combinations
    
    data = ['a','b','c']
    print(list(combinations(data,2))) 
    # 출력시 [('a','b'),('a','c'),('b','c')]
### (3) 중복순열
    from itertools import product

    data = ['a','b','c']
    print(list(product(data, repeat=2)))
    # 출력시 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
### (4) 중복조합
    from itertools import combinations_with_replacement

    data = ['a','b','c']
    print(list(combinations_with_replacement(data,2)))
    # 출력시 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]

## 15. Counter
    from collections import Counter

    counter = Counter(['a','b','c','a','a','b'])
    print(counter['a']) # a 횟수 출력 3
    print(dict(counter)) # 사전 자료형으로 반환 {'a': 3, 'b': 2, 'c': 1}

## 16. 최대공약수, 최대공배수
### (1) 최대공약수 - gcd
        import math

        print(math.gcd(21,14)) # 출력시 7
### (2) 최소공배수 
        import math

        a=14, b=21
        print(a*b//math.gcd(a,b)) # 출력시 42
>  두수 곱하고 두수의 최대공약수로 나눈 몫은 최대공배수

