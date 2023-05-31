## Threads&Concurrency

### Overview
- CPU 스케줄러: 하나의 스레드를 CPU에 전달하는 일을 함.

#### 스레드
- Job: 프로세스를 모아둔 것

#### Single and Multithreaded Processes
- 공유되어 CPU가 처리하는 자원들: code, data, files

#### Multithreaded Server Architecture
1. client가 server에게 요청
2. server는 client에 요청을 하기 위해 thread 생성
   - 생성되는 thread: 소켓 객체(통신 루트), connection 정보들, DB에 대한 위치 정보들 
3. server client에 요청을 받기 위해 계속 준비하고 있음
- 하나의 프로세스에 대한 T1, T2 ... (mutable)
  - T1 == T2 
  - 같게 만들기 위해 Design Pattern을 사용함.
    - SingleTone Pattern
      - static을 붙여줌
      - getInstance(), setInstance(): getter, setter 대신 사용
      - clone으로 생성되기 때문에 메모리를 차지 하지 않음.

#### Benefits
- thread를 항상 사용할 수 있도록 buffer 공간을 마련해둠
- buffer 공간에 만들어지는 thread를 일정한 수의 계속 반복하면서 사용함
- thread는 pull의 형식으로 운영

### Muticore Programming
#### Multicore Programming
- 동시성: 한 곳에서 여러 개를 처리

#### Concurrency vs. Parallelism Programming
- 단일 코어 시스템 동시 실행
  - time을 공유해야 함. 
- 다중 코어 시스템의 벙렬성
  - 여러 개의 core에서 나눠서 진행
  
#### 암달의 법칙 Amdalhl's Law
- N: 코어 수
- 코어 수가 커질 수록 스피트가 빨라짐

### Multithreading Models
- one-to-many(user-kerner): 없는 이유는 thread를 사용하지 않는데 많이 만들어놓을 필요가 없어서
#### Many-to-One
- 현재 이렇게 사용하는 경우는 거의 존재하지 않음
#### Many-to-Many
- pull에 영역에 일정한 수만큼 생성하는 방식으로 운영

### Thread Libraries
#### Pthreads (POSIX thread)
- join(): 새로 생긴 thread를 쓸 수 있도록 해주는 것(현재 사용 중이던 thread는 wait 상태로 감)
- `gcc -pthread 파일명.c`
- `Segmentation fault (core dumped)`: argv에 들어가는 값이 없어서 에러가 난 것.

#### Java Thread
- thread 처리 방식
  - class로 처리
  - Runnable(interface)로 처리
- Java
  - 다중 상속을 interface로 진행
  - 어노테이션: 표현식 중 하나로, 
  - sleep(A): A/1000 -> 1초
  - lambda: 입력 값을 출력 처리하는 것. 함수를 쓰지 않을 때 사용

### Implicit Threading
#### Java Tread Pools
- Singletone으로 구현 ThreadPool 함수 안에 static 변수 선언

#### OpenMP
- IPC 처리하는 방법 중 하나인 공유 메모리 환경에서 병렬 프로그래밍을 지원해주는 API
- library 유틸리티
- `omp.h`: OpenMp를 사용하기 위해서 선언 필요
- 컴파일 시, `-fopenmp` 옵션 사용 필요

### Threading Issues
- singletone으로 하나의 값을 갖는 thread 객체를 사용하게 되는 다른 객체로부터의 요청들이 이루어지다 보면 쓰다가 다른 요청이 들어오게 되면 동기 처리를 진행
  - 동기 처리: `synchronized` 키워드를 붙여서 해당 singletone으로 생성된 객체를 요청할 때는 동기식으로 처리한다는 선언
#### Signal Handling
- EX) kill, 
  - kill: 비이상적인 thread에 대해서 강제로 죽이는 signal

### Operating System Examples
#### Winows Threasds
- thread id를 통해서 관리

#### ++
- information hiding 때문에 생성자를 사용하지 않고 getter, setter를 사용.
- 프로세스 사이에 자원공유가 안되기 때문에 통신하는 방식이 필요(shared memeory, socket 등 

### Basic                                                                                                                                                                                                                                                                                                                                                                                                                                                                              