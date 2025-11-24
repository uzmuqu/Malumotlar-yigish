# 1. Berilgan ro‘yxatdan takrorlanuvchi elementlarni toping  va ularni yagona set ko‘rinishida qaytaruvchi funksiya yozing.
def duplicate_elements(lst):
    return {x for x in lst if lst.count(x) > 1}


# 2. Berilgan sonlar ro‘yxatidan faqat juft raqamlarni yangi ro‘yxatga ajratadigan funksiya.
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]


# 3. Berilgan matndan har bir harf necha marta uchrashini lug‘at ko‘rinishida qaytaruvchi funksiya.
def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# 4. 1 dan n gacha bo‘lgan sonlarning kvadratlari yig‘indisini hisoblaydigan funksiya (for sikl bilan).
def sum_of_squares(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s


# 5. Ikki ro‘yxat berilgan. Ularning umumiy elementlarini toping (set intersection).
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# 6. Lug‘atda qiymati eng katta bo‘lgan elementning kalitini qaytaradigan funksiya.
def max_value_key(d):
    return max(d, key=d.get)


# 7. Ro‘yxatdagi har bir elementni 1 ga oshirib, yangi ro‘yxat qaytaruvchi funksiya (for loop bilan).
def plus_one(lst):
    new_list = []
    for x in lst:
        new_list.append(x + 1)
    return new_list


# 8. Berilgan ro‘yxat ichidagi eng uzun so‘zni topuvchi funksiya.
def longest_word(words):
    return max(words, key=len)


# 9. Ro‘yxat ichidagi faqat integer elementlarni ajratib beruvchi funksiya.
def only_integers(lst):
    return [x for x in lst if isinstance(x, int)]


# 10. Matndagi so‘zlar sonini hisoblaydigan funksiya (split yordamida).
def word_count(text):
    return len(text.split())


# 11. Fibonacci ketma-ketligining n ta birinchi elementini ro‘yxat ko‘rinishida qaytaruvchi funksiya.
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


# 12. Ro‘yxat ichidagi barcha sonlarni ko‘paytmasini hisoblaydigan funksiya.
def product_of_list(lst):
    p = 1
    for x in lst:
        p *= x
    return p

# 13. Ikki lug‘atni birlashtiradigan funksiya (update ishlatilsin).
def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result


# 14. Matndan faqat unli harflarni ajratib olib ro‘yxat qaytaruvchi funksiya.
def extract_vowels(text):
    vowels = "aeiouAEIOU"
    return [ch for ch in text if ch in vowels]


# 15. Ro‘yxatdagi elementlarni teskari tartibda for sikl orqali chiqaruvchi funksiya (reverse ishlatmasdan).
def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev


# 16. N ta tasodifiy sonlardan tashkil topgan set qaytaradigan funksiya (takrorlanmas sonlar).
import random

def random_set(n, start=1, end=100):
    result = set()
    while len(result) < n:
        result.add(random.randint(start, end))
    return result


# 17. Ro‘yxat elementlari guruhlab, takrorlanganlarni nechta ekanini qaytaruvchi lug‘at qaytaring.
def count_duplicates(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    return freq


# 18. Funksiya yozing: berilgan son bo‘lsa True, bo‘lmasa False qaytarsin.
def is_number(x):
    return isinstance(x, (int, float))

# 19. Ro'yxatdan faqat 3 ga bo'linadigan elementlarni yangi ro'yxatga ajratib beradigan funksiya yarating (filter ishlatmasdan).
def divisible_by_3(lst):
    result = []
    for x in lst:
        if x % 3 == 0:
            result.append(x)
    return result


# 20. Berilgan lug'atdagi faqat qiymati ro'yxat bo'lgan elementlarni filtrlaydigan funksiya tuzing.
def filter_list_values(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, list):
            result[key] = value
    return result

