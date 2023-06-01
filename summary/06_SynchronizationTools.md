## Synchronization Tools

### Critical-Section Problem
#### 임계 영역 문제
- entry section: 진입 영역
- exit section
#### 임계 영역 관련 요구사항
- 진행률(deadlock 회피): 현재 사용하지 않는 것이라면 진입을 막을 이유가 없음
- 기아 회피
#### 자바 스레드에서의 경쟁 상태
- 하나의 프로세스에 대해서만 접근 가능하돌고 해야함 -> 동기화 필요
- start() -> join()
  - join():  Thread가 종료될 때까지 기다림
- p15: t1, t2는 다른 thread
  - 같은 thread로 만들기 위해 static을 이용해서 singletone을 만들었던 것
- p16: staic으로 같은 공간을 사용하고 있기 때문에 20000이 출력
  - 둘 다 race conditino 상태가 되기 때문에 `synchronized` 처리를 해주어서 값 처리하는 것이 필요함.

### Pererson's Solution
#### Algorithm for Process Pi
- flag[j] && turn ==j : 준비가 되어있는지 확인
#### Peterson 솔루션의 정확성
- 상호 배제 및 Bounded waiting 충족

#### Peterson의 솔루션과 현대 아키텍처
- 해당 알고리즘의 대안으로 시스템에서 제공해주는 알고리즘 혹은 Memory barrier으로 critical section 문제(프로세스 2개가 동시에 임계영역에 존재할 수 있음)를 해결해서 사용

#### 원자 변수(atomic variable)
- 정수, boolean, char는 기본 데이터 타입(immutable) -> 상호 배제를 보장

#### Java implemention of Peterson's solution
- count: 공유하는 공간
- entry section: peterson 처리 진행
- Producer: 값을 증가 시켜주는 thread
- Consumer: 값을 감소 시켜주는 thread

### Synchronization Hardware
#### 원자 변수 atomic variable
- waiting 상태에 있다가 풀리면 처리를 하는 방식으로 진행.

### Semaphore
#### EX with Semaphores
- 상호배제 효과를 얻음
- critical section 문제 해결

### Monitor
#### 세마포어를 사용하여 구현 모니터링

### Liveness
- 모니터의 단일 리소스를 할당하고자 하는 것

## Kubernetes scheduling (REF. 2일차 오후.pdf)
### Kubernetes 클러스터
- master node와 worker node들로 구성되어 있는 클러스트 존재
### Advanced scheduling
- `nodeSelector`라는 node를 선택해서 해당 node에 올라가도록 하는 방식을 선택함
- 

#### ++
- heap영역에 들어가면 mutable될 가능성이 높음
- remainder section는 false로 해놓고 처리를 하는 것