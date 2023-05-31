## Process

### Process in Memory
- Data (main 함수 밖에서 선언되었을 경우)
  - 초기화가 되어져 있는 것이 아래 계층 할당
  - 초기화가 되어지 있지 않은 것이 위의 계층 할당
- Heap (생성된 객체가 올라가는 것이지 선언되는 것이 올라가지 않음)
  - C: 해당 영역을 최초로 사용한 언어
    - malloc: 객체 생성
    - free: 사용하지 않는 객체를 삭제
    - new: malloc -> free의 단점을 해결하는 생성하도록 사용됨.
  - python: 자료구조에서 기존의 mutable한 것이 immutable하고 immutable하던 것이 mutable함
- Stack (main 함수 안에서 선언되었을 경우)
  - 임시적으로 데이터를 저장하는 공간

### Process Concept
#### Process State
- 한 번 메모리에 적재가 된 것은 자체적인 라이프 사이클을 가지게 됨.
  - 라이프 사이클
    - 프로세스 생성 : 메모리에 적재
    - ready: new가 되어 running이 되기 전까지 있는 상태 혹은 running에서 문제가 생기면 다시 오는 상태
    - 이벤트 발생 시: running에서 waiting으로 가고 waiting에서 끝나게 되면 ready로 가게 됨.
      - EX) 저장하는 이벤트가 발생하면 running 중이던 편집 프로세스가 waiting으로 가게 됨.
    - running -> ready: 단계에서 interrupt의 system call이 발생했을 경우 (try - catch 구문으로 처리했을 경우)

#### Process Control Block(PCB)
- process id: 프로세스 식별자 (pid)

#### Thread
- thread vs process: 차이는 shared resource에 따라 구분이 된다. 
  - 프로세스는 PCB를 여러 개를 가지고 있게 됨.
  
#### Process Scheduling
- head: 처리해야할 PCB의 정보를 가지고 있음.
- CPU에서 처리되고 나면
  - I/O : wait -> ready
  - time slice expired: ready
  - chid termination wait queue -> create child process: ready
  - interrpt wait -> wait for an interrupt: ready
- file 입출력, 네트워크 프로그래밍, sql exception, 연산 처리 : try-catch 필요 
  - exit 되지 않고 wait로 갔다가 ready 상태로 갈 수 있도록 구현 가능

### Operations on Processes
#### Process Creation
-  pid > 0 -> parent process (먼저 만들어진 프로세스임으로 프로세스 id를 발급받은 것)
-  pid < 0 -> 현재 사용하지 않는 프로세스, 에러 -> 에외 처리 필요
-  pid = 0 -> child process
**C program Forking Separate Process**
- fork() : parent가 있는 상태에서 child를 만들어지는 것
  - child에 parent의 내용이 그대로 복사가 되는데 child에 다른 로직을 처리하고 싶다면 pid=0일 때, 다른 로직을 처리하도록 구현하면 가능
- execlp(A): A 명령어를 실행을 시키는 것
-> child가 생성되는 순간 parent가 wait가 되어 child가 먼저 실행이 되고 parent가 그 이후 실행이 됨. (만약 child가 안만들어지면 parent도 terminate가 됨.) -> child가 만들어지고 parent가 동작함.

#### 프로세스 종료
- parent가 wait()를 호출하지 않고 terminate가 된 경우: child 프로세스틑 orphan이 됨.
**코드 - 리턴 값으로 구분**
- `pid t_pid;` : 운영체제에서 pid에서 parent pid의 pid 값을 알아서 부여해줌
- child이 실행되는 순간 parent가 wait 상태가 된다.
**출력이 무엇인지 설명하시오**
- child와 parent가 현재는 immutable하기 때문에 값이 5/5로 나옴. (하지만 heap의 영역을 사용하게 되면 mutable하게 됨)
**초기 부모 프로세스를 포함하여 생성된 프로세스 수**
- P0 -> p0, p1 -> p0, p1, p2, p3 -> p0, p1, p2, p3 p0, p1, p2, p3
- fork()로 생성되는 횟수는 2^n개
**프로그램을 사용하여 라인 A B C D**
- getpid(): child process 값을 가져오는 함수
**출력이 무엇인지 설명하시요.**
- parent는 초기화가 되어서 원래 값인 0~4로 출력, child는 i의 제곱의 수가 반환됨.

### Interprocess Communication
#### Communications Models
- (a) shared memory: 메모리를 공유하는 방식(데이터를 다루는 방식)
- (b) Message passing: pipe를 통해서 공유(메세지를 다루는 방식)

#### 생산자 프로세스 - 공유 메모리
- in + 1 : 메모리는 0부터 사용하기 때문에 버퍼 사이즈를 계산하기 위해 추가한 + 1
- out: 제일 마지막을 의미 -> out일 떄 아무것도 하지 않음 (버퍼가 가득차있는 상태)
- buffer가 가득차있지 않을 때 buffer에 넣어주는 동작

#### 소비자 프로세스 - 공유 메모리
- buffer가 in==out이지 않을 때까지, 아무것도 존재하지 않을 때까지 소비자가 사용하는 동작

#### IPC - Message Passing
- 프로세스는 공유 변수에 의존하지 않고 서로 통신

#### Direct Communication
- P, Q 프로세스

#### Indirect Communication
- ports를 이용하는 방식: 간접 방식
- 차단: 동기식
  - resource를 점유하는 방식으로 사용하기 때문에 효율적으로 사용하는 것이 불가능
- 비 차단: 비동기
  - 다 보낼 때까지 차단을 하지 않고 계속해서 메세지를 보낼 수 있도록 함.

### Examples of IPC Systems
#### IPC 시스템의 예 - POSIX
- 통신을 하기 위해서 사용하는 규약
- shm_open() : 객체를 생성 
- ftruncate() : 객체의 크기를 설정하면서 초기화
- mmap(): 매핑 

#### POSIX Shared Memory
- 프로듀서에서 공유 메모리를 넣어놓았기 때문에 shm_customer.c 실행 시, 공유된 메모리가 있다는 출력이 존재

#### Examples of IPC Systems - Windows 
#### Window의 로컬 프로시저 호출
- port를 제공해주기 위해서 NIL 카드를 꼽아서 사용.
  - 8088 : 톰캣이 사용하는 포트
- shared memory를 사용하기는 하지만 포트를 사용하는 것이 더욱 일반적임

#### Pipes - Message passing Examples
- pipe: 하나가 끝나야 다음 단계로 넘어감.
- 
#### Ordinary pipes
- 단방향
- 부모 - 자식 관계일 경우에만 사용 (아닌 경우 Named pipes 사용)

#### Sockets in Java
- port forwarding
- 유형
  - TCP
  - UDP
  - MulticastSocket
- 

#### Remote Procedure Calls
- RPC 혹은 RMI로 통신 가능
  -  특이한 framework로 통신

#### ++
- 배열은 다른 type의 값을 저장을 하지 못 하지만, struct는 다른 type의 값을 저장 가능
  - struct는 mutable 함. -> 들어가게 되면 값을 숨겨야 함. -> 생성자대신 setter, getter를 사용함.(외부에서 접근을 못 하도록 한 것으로 캡슐한 것으로 class)
- mutable: 자료구조에 들어가면 값에 변경됨
- POSIX 컴파일 시, 옵션 주의
