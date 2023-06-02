## FileSystem.md

### File Concept
- File: 연속적인 논리 주소 공간
- 유형
  - 데이터
    - 숫자
    - 문자
    - 바이너리
**File Attributes**
**디렉토리 구조**
- 모든 파일에 대한 정보를 포함하는 노드들의 모음
- Seconray 메모리, 디스크에 상주
**File Operations**
- Open을 하고 Injected 단계가 진행되어야 가능
- Open을 하면 반드시 Close를 해줘야 함.

## Access Methods

### Disk and Directory Structure
**일반적인 파일 시스템 구성**
**Tree-Structured Directories**
**Acyclic-Graph Directories**

### Protection
- `chmod`: change mode

### 파일과 디렉토리
- `pwd`: 현재 디렉토리 확인
- linux는 `/`를 기점으로 해서 모든 사용자에게 할당되어져 있는 구조
- `ls [-asIFR]`: 지정된 디렉터리의 내용을 나열
- `mkdir`: 폴더 생성
  - `-p`: 중간 디렉토리까지 자동 생성
- `cat`: 표준입력 내용을 모두 파일에 저장
- `touch`: 파일 크기가 0인 이름나 있는 빈 파일을 생성
**접근권한**
- ls -asl를 실행하면 파일의 권한까지 확인가능
- 권한 종류
  - r: 읽기
  - w: 쓰기
  - x: 실행
- 접근권한 표현: 8진수
  - 3가지 대상에 대하여 표현: `소유자, 그룹, 기타 사용자`
  - 777 -> rwx rwx rwx
- 접근 권한 표현: 기호
  - `사용자범위 연산자 권한`
    - 사용자범위: u g o a
    - 연산자: + - =
    - 권한: r w x

### 파일 입출력
- `readline()`: 한 줄씩 읽는 것으로 for문으로 모든 줄을 반환
  - parameter에 `a`를 사용하면 내용을 추가 가능
- `with`: open과 close 없이 에러가 생기지 않음.