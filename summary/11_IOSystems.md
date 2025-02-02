## I/O Systems
- Output 장치
  - print, display
- 인터페이스: 한 대상과 한 대상을 연결해주는 매개체
- SAS controller: 외부의 disk를 연결해주는 컨트롤러
**일반적인 PC 버스 구조**

#### Polling
- 1인지 0인지에 대한 상태를 확인하기 위해서 계속해서 확인
#### Interrupts
- 진행이 되어지는 것을 중간에 처리가 필요한 것이 있다면 인터럽트를 통해 처리를 끊는 방식
  - 중간에 처리가 필요한데 계속 진행한다면 wait인 상태가 너무 길어질 수 있기 떄문에 (Polling)
  - 마스크 기능: 일부 인터럽트를 무시하거나 지연시킴
    **인터럽트 구동 I/O 주기**
    - 준비가 됬는지 완료가 됬는지 확인
    - 인터럽트 핸들러에 전달 
    - 반환
    - > 인턴럽트 핸들러의 역할이 가장 중요
    **직접 메모리 액세스**
    - DMA를 통해서 통신이 이루어짐
        **DMA 전송을 수행하기 위한 6단계 프로세서**

### Application I/O Interface
#### 일반적인 PC 버스 구조
- 캡슐화가 되어 있기 때문에 인터페이스를 사용 필요
**커널 I/O 구조**
- 하드웨어: device controller로 구성
- 소프트웨어: 드라이버로 구성
#### Nonblocking and Asynchronous I/O
- 비동기 처리를 위한 해석 엔진이 브라우저에 존재
- I/O 처리 방식 (사용자 영역에서 커널쪽으로 보낼 때)
  - 다이렉트로 왔다가 다이렉트로 처리

### Kernel I/O Subsystem
- Scheduling: 장치별 대기열을 통해 일부 I/O 요청 순서 지정
- 캐싱: 데이터 사본을 보관하는 더 빠른 장치
- 스풀링: 장치에 대한 출력 보류
- 장치 예약: 장치에 대한 접근을 할 때 독점

### I/O 요청을 하드웨어 작업으로 변환
- 할당 연산자(=대입 연산자)