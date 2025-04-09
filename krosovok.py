#task 1

text = input("Введіть рядок українською мовою: ")
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
vowel_count = sum(1 for char in text if char in vowels)

print(f"Кількість голосних у рядку: {vowel_count}")

#task 2

list1 = input("Введiть числа через кому для першого списку: ").split(',')
list2 = input("Введiть числа через кому для другого списку: ").split(',')

try:
    nums1 = list(map(int, list1))
    nums2 = list(map(int, list2))
    result = sorted(set(nums1 + nums2))
    print("Об'єднаний вiдсортований список без повторiв:", result)
except ValueError:
    print("Будь ласка, введiть лише цiлi числа через кому")

#task 3

from collections import Counter

text = input("Введiть текст: ")
filtered_text = ''.join(c for c in text if not c.isspace())
counts = Counter(filtered_text)

print("Статистика символiв у текстi:")
for char, count in counts.items():
    print(f"'{char}': {count} разiв")
