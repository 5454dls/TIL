import numpy as np

total = int(1e7)
points = np.random.rand(total, 2) # (total, 2) 벡터 생성

# pi / 4 : 1 = 사분원 안의 점 : 전체 점
4 * np.sum(np.sum(points ** 2, axis=1) < 1) / total # broad cast로 각 값을 제곱하고, 더해서 (total, )를 만든다. 이후 broad cast로 boolean mask를 만든 뒤 합하여 전체 갯수를 구할 수 있다.