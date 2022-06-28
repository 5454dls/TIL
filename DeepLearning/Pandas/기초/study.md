# 0. 개요

- 최초 생성일: 22.06.28
- 최종 수정일: 22.06.28
- 내용: Pandas의 기초적인 활용법 정리



# 1. Pandas

- data 분석을 위한 여러 기능이 포함된 툴
- `import pandas as pd`



# 2. Series

- 판다스의 1차원 데이터에 해당하는 객체
- 생성
  - `s.Series(data, index, dtype)`
- 출력
  - `s.index()`
  - `s.values()`
  - `s[index]` : list를 index로 넘겨 동시 접근 가능
  - `s.tail(n)` : 하위 n개의 데이터
  - `s.head(n)` : 상위 n개의 데이터
- 삭제
  - `s.drop()` : inplace가 기본적으로 False로 설정되어 원본에 영향 없이 복사본 생성
- 확인
  - `len(s)`
  - `s.size()`
  - `s.unique()` : NaN을 포함하여 값이 한 개만 있는 것들을 출력
  - `s.count()` 
  - `s.value_counts()` : 각 값의 갯수
  - `s.통계` 
- 연산과 Boolean은 index를 기준으로 수행하며 broad cast가 적용된다.
  - index pair가 맞지 않는 경우에는 NaN을 생성
- slicing은 숫자와 문자 모두 가능
  - 숫자의 경우 index가 숫자가 아니더라도 객체의 기본 위치를 기준으로 수행
  - 문자의 경우 마지막 값을 포함하여 수행



# 3. DataFrame

- index
  - 세로 첫번째 줄
  - 고유한 값
- column
  - 세로줄
  - 개별 속성
- row
  - 가로줄
  - 개별 data
- 데이터 load 또는 생성시
  - `head()` or `tail()`
  - shape
  - describe
  - info

