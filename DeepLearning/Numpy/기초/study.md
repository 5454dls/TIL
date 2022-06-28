# 0. 개요

- 최초 생성일: 22.06.16
- 최종 수정일: 22.06.21
- 내용: Numpy의 기초적인 활용법 정리



# 1. Numpy의 사용 이유

- 빠른 속도
- 적은 메모리 사용
- 선형대수, 통계 등 다양한 기능 제공



# 2. Numpy의 기초적인 사용법

- 설치
  - `import numpy as np`
- 생성
  - `np.array()` : 직접 생성
  - `np.arange()` : range랑 같은 기능
  - `np.ones((행, 열))`: 모두 1로 된 ndarray 생성
  -  `np.zeros((행, 열))`: 모두 0으로 된 ndarray 생성
  - `np.empty((행, 열))`: 초기화 된 ndarray 생성
  - `np.full((행, 열), value)`: 특정 값으로 이뤄진 ndarray 생성
  - `np.eye()`: 단위 행렬 생성
  - `np.linspace(start, end, 구간)`: start부터 end까지 같은 간격으로 구간 수만큼 나눠서 생성
- 차원변경
  - `reshape()`
    - 원소의 수가 같아야 함
    - -1은 자동 채우기
  - `ravel()` / `flatten()` : 1차원으로 변경
    - ravel은 원본을 변경하고 flatten은 사본을 생성
    - order을 'C'로 주면 행 우선(default), 'F'로 주면 열 우선
  - `ndim()`: 차원 확인
- random
  - `random.seed(정수)` : 정수를 seed로 하는 특정 random 값으로 고정
  - `random.rand()`: 0~1로 샘플링하여 ndarray 생성
  - `random.randn()`: 정규분포로 샘플링하여 ndarray 생성
    - `random.normal()`과 동일
  - `random.randint(start, end, size)` : start ~ end 사이의 정수로 샘플링하여 ndarray 생성
    - replace를 False로 주면 중복 X
    - `random.uniform()`과 동일
- 인덱싱 / 슬라이싱
  - 인덱싱: `[행, 열]`
    - 차원 축소
  - 슬라이싱: `[:, :]`
    - 차원 유지
- 논리 / 연산
  - 연산
    - `add`(`+`), `substract`(`-`), `multiply`(`*`), `divide`(`/`): shape가 같은 경우 같은 위치의 값끼리 연산
  - 통계
    - `mean()`, `max()`, `argmax()`, `sum()`, `cusum()` 등 다양한 통계 제공
    - 공식문서 참고
  - 논리
    - `np.any(조건)`
    - `np.all(조건)`
    - `np.where(조건, 참인 경우, 거짓인 경우)`

- axis
  - None : 전체 대상
  - None이 아닌 경우 : 해당 인덱스를 기준으로 압축
- broad cast
  - shape이 다른 경우 정해진 규칙에 따라서 연산
  - 뒤 부터 비교하여 1 or 같은 경우는 그 값을 broad하게 적용
- boolean mask
  - 해당 인덱스가 True인 경우 그 값을 추출
  - True와 False는 암묵적 형변환 적용



# 3. 기타 모듈

- lialg
  - 선형대수를 위한 모듈
  - `np.linalg.inv` : 역행렬
  - `np.linalg.solve` : 간단한 선형대수 해
- matplotlib
  - 시각화를 위한 모듈
  - 그래프 생성 : plot, scatter, hist > 색상, 스타일 등 명시 가능
  - 축 : xlabel, ylabel, title
  - 격자: grid, xlim, ylim
  - 여러개 그리기: subplot
