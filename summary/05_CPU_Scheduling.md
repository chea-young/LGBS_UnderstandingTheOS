## CPU Scheduling

### Basic Concepts
#### CPU Scheduler
- running을 할 떄는 안일어남
- waiting,  ready 일 때 일어남

#### 선점형 및 비선점형 스케줄링
- 선점형: 뻇어서 강제로 바꿀 수 있는 것. 실행이 안되게끔 가능
- 비선점형: 뻇어서 강제로 할 수 없는 것

#### Dispatcher
- P0 -> P1로 전환되는 순간 상태가 save가 되어지고 PCB1가 복구되면서 전환: 대기 시간
- `cat /proc/1/status | grep ctxt`: ctxt에 대한 내용한 조회를 하겠다는 명령어
  - ctxt: content
  - grep: 조회를 하는 명령어
- voluntary: 비선점형
- nonvoluntary: 선점형

### Scheduling Algorithm
#### 스케줄링 알고리즘 최적화 기준
- 대기시간: 
  - P1: 대기시간 0
- 실행시간(Burst Time): 
- 반환시간: 요청을 하서 완료가 된 것

#### First-Come, First-Served (FCFS) Scheduling
- Convoy effect를 많이 받기 때문에 좋은 효과를 보기가 어려움
- 비선점

#### Shortest-Job-First (SJF) Scheduling
- 가장 짧게 처리를 할 수 있는 프로세스를 먼저 처리
- 실질적으로 짧게 처리하는 시간 처리하기 위해 CPU 버스트 시간 계산
- 먼저 도착한 것에 대한 benefit이 존재하지 않음.

#### 최단 남은 시간 우선 스케줄링(Shortest-remaining-time-first Scheduling)
- 도착을 한 것도 먼저 도착한 것에 대한 benefit을 주는 것.
  - 실제 process는 먼저 도착한 것에 정보도 중요

#### Round Robin (RR)
- time quantum: CPU 시간을 쪼개서 10-100밀리초
- 프로세스를 time quantum으로 나눔 -> 청크
- RR에서 q를 작게 가져가는 것이 좋은데 컨텍스트 스위치가 자주 발생할 수가 있는데 이때 오버헤드가 놓아질 수 있어 컨텍스트 스위치와 관련해서는 q가 어느정도는 커야 함
- 먼저 도착한 것에 대한 benefit이 존재
- q보다 burst time보다 작으면 쪼개지 않고 다 처리를 함
- 장점
  - 모든 프로세스에 대해서 응답 속도가 가장 빠름

#### Priority Scheduling
- RR과 함께 리눅스에서 사용하는 알고리즘
**Example of Priority Scheduling**
- 우선 순위가 가장 높은 프로세스 안에서 RR로 실행
**다단계 피드백 대기열 (Mutilevel Feddback Queue)**
- Q 자체에도 q를 지정
- 여러 개를 형평성있도록 처리

### Thread Scheduling
#### Pthread Scheduling
- thread scheduling은 허용이 되는 곳에서만 사용가능

#### Multiprocess architectures
- SMP: 코어 마다 각각의 자원을 할당해서 처리해나가는 방식

#### 다중 프로세서 스케줄링
- Affinity: 선호도

### Real-Time CPU Scheduling