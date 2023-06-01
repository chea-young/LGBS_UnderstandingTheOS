## Deadlocks

### Deadlock Characterization
- 상호배제
- 보류 및 대기
- 선점 없음: 자발적으로 해제할 수 있는 경우
- Circular wait

#### 리소스 할당 그래프
- 그래프 주기가 없는 경우 -> 데드락 X
- 그래프 주기가 포함된 경우
  - 하나의 인스턴스만 있는 경우 교착 상태
  - 유형당 여러 개의 경우 교착 상태 가능성 존재
**사이클이 있지만 교착 상태가 없는 그래프**
- 점유 및 요청을 해나가고 있지만 Deadlock이 발생하지 않음
- 주기가 없어서

### Methods for Handing Deasdlocks
- 교착 상태로 빠지지 않도록 하는 방안
  - 교착 상태 방지: 일어나기 전에 대비
  - 교착 상태 회피: 교착 상태가 일어났을 때 대처하는 것

### Deadlock Prevention
- Deadlock이 발생할 수 있는 조건 중 하나를 무효화 시킴
  - 상호 배제
  - Hold and Wait: 리소스를 요청할 때 다른 리소스를 가지고 있지 않도록 보장
  - 선점 없음: 다른 리소스를 요청했을 때 현재 보유하고 있는 리소스를 강제 해제
  - 순환 대기: 총 순서를 지정하여 해당 순서대로 리소스를 요청하도록 요구

### Deadlock Avoidance
**Safe, Unsafe, Deadlock State**
- 안전하다 == Deadlock이 없음
- safe 영역이 아닌 곳에 들어가지 않도록 하는 것

#### Banker's Algorithm
- 리소를 요청하면 대기를 해야하는데 대기 조건이 존재
- i가 없으면 = 필요로 하는 것이 없으면

#### Process  Ti를위한리소스요청알고리즘
- T4가(3,3,0)에대한요청을승인할수있을까?
    - Request가 Available보다 작거나 같은가를 확인하는 것이 필요, -> 승인이 안됨
- T0의(0,2,0) 요청을승인할수있을까?
  - (0, 2, 0)은 (2, 3, 0)보다 작아서 승인이 된다.

### Deadlock Detection
**리소스 할당 그래프 및 대기 그래프**
- Dependency가 있는 것을 제외하고 나머지만 탐색

### Recovery from Deadlock
**자원 선점**
- 롤백: DB 관리 시스템에서 실행한 내용들이 복귀를 하게 된 것
- 기아