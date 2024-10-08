# List Comprehension

## 리스트 컴프리헨션이란?

- 리스트 컴프리헨션의 기본 문법:

```python
[표현식 for 항목 in 반복가능객체 if 조건문]
```

각 부분의 의미:
1. 표현식: 각 항목에 적용할 연산
2. for 항목 in 반복가능객체: 반복할 대상
3. if 조건문: 선택적으로 사용되는 필터링 조건

예시들:

1. 기본 형태:
   ```python
   squares = [x**2 for x in range(10)]
   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```

2. 조건 포함:
   ```python
   even_squares = [x**2 for x in range(10) if x % 2 == 0]
   # [0, 4, 16, 36, 64]
   ```

3. 중첩 루프:
   ```python
   pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
   # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
   ```

## 언제 사용하는게 좋을까?

1. 문제 분석: 
   - 새 리스트를 만들어야 하는가?
   - 기존 리스트(또는 다른 반복 가능한 객체)를 순회해야 하는가?
   - 각 항목에 대해 어떤 연산을 수행해야 하는가?
   - 특정 조건을 만족하는 항목만 선택해야 하는가?

2. 구조화: 
   - 표현식: 각 항목에 수행할 연산 정의
   - for 부분: 순회할 객체 결정
   - if 부분 (선택적): 필터링 조건 추가


## Java 식으로 이해하기
```java
List<Integer> result = new ArrayList<>();
for (int num : arr) {
    if (num % divisor == 0) {
        result.add(num);
    }
}
```

## 관련 문제
- 87389. 나머지가 1이 되는 수 찾기