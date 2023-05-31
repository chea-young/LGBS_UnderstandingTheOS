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

### Scheduling Criteria
#### 스케줄링 알고리즘 최적화 기준
- 대기시간: 
- 실행시간: 
- 반환시간: 요청을 하서 완료가 된 것