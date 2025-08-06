
import copy

# 원본 딕셔너리 (내부에 리스트를 포함)
original_dict = {
    "name": "Alice",
    "level": 25,
    "items": ["sword", "potion"]
}

print("--- 원본 데이터 ---")
print(f"원본 딕셔너리: {original_dict}")
print(f"원본 ID: {id(original_dict)}")
print(f"원본 items 리스트 ID: {id(original_dict['items'])}", '\n')

# --- 1. 얕은 복사 (Shallow Copy) 예제 ---
print("--- 1. 얕은 복사 (Shallow Copy) ---")

# 방법 1: .copy() 메서드 사용
shallow_copied_dict = original_dict.copy()

# 방법 2: dict() 생성자 사용 (동일한 결과)
# shallow_copied_dict = dict(original_dict)

print(f"얕은 복사된 딕셔너리: {shallow_copied_dict}")
print(f"얕은 복사본 ID: {id(shallow_copied_dict)} (원본과 다름)")
print(f"얕은 복사본 items 리스트 ID: {id(shallow_copied_dict['items'])} (원본과 같음!)", '\n')

# 얕은 복사된 딕셔너리의 내부 리스트를 변경해보기
print(">>> 얕은 복사본의 items 리스트에 'shield' 추가...")
shallow_copied_dict["items"].append("shield")

print(f"변경 후 얕은 복사본: {shallow_copied_dict}")
print(f"변경 후 원본 딕셔너리: {original_dict} (같이 변경됨!)", '\n')


# --- 2. 깊은 복사 (Deep Copy) 예제 ---
print("--- 2. 깊은 복사 (Deep Copy) ---")

# 깊은 복사를 위해 원본 딕셔너리를 초기 상태로 되돌립니다.
original_dict["items"].pop() # "shield" 제거

print(f"초기화된 원본 딕셔너리: {original_dict}", '\n')

# copy 모듈의 deepcopy() 함수 사용
deep_copied_dict = copy.deepcopy(original_dict)

print(f"깊은 복사된 딕셔너리: {deep_copied_dict}")
print(f"깊은 복사본 ID: {id(deep_copied_dict)} (원본과 다름)")
print(f"깊은 복사본 items 리스트 ID: {id(deep_copied_dict['items'])} (원본과 다름!)", '\n')

# 깊은 복사된 딕셔너리의 내부 리스트를 변경해보기
print(">>> 깊은 복사본의 items 리스트에 'helmet' 추가...")
deep_copied_dict["items"].append("helmet")

print(f"변경 후 깊은 복사본: {deep_copied_dict}")
print(f"변경 후 원본 딕셔너리: {original_dict} (영향 없음!)", '\n')


# --- 요약 ---
print("--- 요약 ---")
print("얕은 복사: 딕셔너리 자체는 새로 만들지만, 내부의 복잡한 객체(리스트, 딕셔너리 등)는 주소만 공유합니다.")
print("깊은 복사: 딕셔너리 내부의 모든 객체까지 완전히 복제하여 완전히 독립적인 사본을 만듭니다.")
