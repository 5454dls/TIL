# 0. 개요

- 최초 생성일: 22.06.28
- 최종 수정일: 22.06.29
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
- 데이터 load 또는 생성시 확인해볼 것들
  - `head()` or `tail()`
  - shape
  - describe
  - info
- 생성
  - `pd.DataFrame(data, index)`
    - data는 dict 또는 series
  - `pd.read_csv(경로, sep, header, index_col, usecols)`
- 선택
  - 기본적으로 인덱싱은 불가
  - `df[[col]]`
  - `df[ : ]`
  - `df.loc[[col], [row]]` : 임의 지정한 index 기준
  - `df.iloc[[col], [row]]` : 데이터 순서 기준
- 추가
  - `df[new_col] = data`
  - `df.insert(col위치, col명, data)`
- 삭제
  - `df.drop(대상 col or row, axis, inplace)`
  - axis 0은 row(default), 1은 col
- NaN처리
  - 확인 : `df.info()`, `df.isna()`
  - 삭제 : `df.dropna(subset = [], axis)`
  - 대체 : `df.fillna(data)`
- 그룹핑
  - group by
    - 객체 생성: `df.groupby()` : ()에는 단순히 리스트를 넣어 column명을 기준으로 하거나 Level을 명시하여 index를 기준으로 하거나 함수를 직접 넣을 수 있다.
    - 분류: `df.groups()`
    - 데이터 갯수: `df.count()`
    - 데이터 합: `df.sum()`
    - 데이터 평균: `df.mean()`
    - index를 유지한 채 groupby를 하고 싶은 경우, `df.groupby().transform()`
  - pivot
    - `df.pivot(row, col, 보고 싶은 값)`
    - index의 중복을 허락하지 않는다.
  - pivot table
    - `pd.pivot_table(df, index, columns, aggfunc)`
    - aggfunc를 통해 중복시 어떻게 할지 결정할 수 있다.
  - stack
    - `df.stack(col)`
    - col > index
  - unstack
    - `df.unstack(index)`
    - index > col
- 병합
  - concat
    - `pd.concat([df1, df2], axis, ignore_index)`
    - axis: 0은 밑으로(row), 1은 옆으로(col)
    - ignore_index: 병합된 df를 기준으로 새롭게 index 생성
    - index나 col이 다른 경우 NaN을 생성
  - merge
    - `pd.merge(df1, df2, on, how, left_index, right_index)`
    - on: index 외에 col을 기준으로 병합할 경우 입력
    - left_index, right_index: 해당 df에서 index를 기준으로 병합할 경우 입력
    - how
      - inner: 둘 다 있을 경우만 병합
      - left: df2는 없더라도 병합
      - right: df1은 없더라도 병합
      - outer: 존재 여부 상관 없이 병합

- 기타
  - 상관관계 : `df.corr()`
  - 자료형 변환: `df.astype()`
  - 같은 함수를 모든 row에 적용: `df.apply(function)`
  - one-hot : `pd.get_dummies(df, columns, drop_first)`
    - drop_first: 각 one-hot에서 첫번째 col삭제
  - 인덱스 변환: `df.set_index([col])`
  - 인덱스 초기화: `df.reset_index()`
  - 집계: `df.aggregate([원하는 통계])`
  - 정렬: `df.sort_value(by, ascending)`
