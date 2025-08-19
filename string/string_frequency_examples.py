# Character Frequency Cheat Sheet in Python

from collections import Counter

s = "geeksforgeeks"
freq = Counter(s)
print("1. Frequency of each char:", freq)

# 2. Maximum frequency character
print("2. Max freq char:", max(freq.items(), key=lambda x: x[1]))

# 3. Minimum frequency character
print("3. Min freq char:", min(freq.items(), key=lambda x: x[1]))

# 4. Odd frequency characters
print("4. Odd freq chars:", [ch for ch, cnt in freq.items() if cnt % 2 == 1])

# 5. Even frequency characters
print("5. Even freq chars:", [ch for ch, cnt in freq.items() if cnt % 2 == 0])

# 6. Frequency of a specific character
print("6. Frequency of 'e':", freq['e'])

# 7. Top 2 most common chars
print("7. Most common 2:", freq.most_common(2))

# 8. All duplicate characters
print("8. Duplicates:", [ch for ch, cnt in freq.items() if cnt > 1])

# 9. Remove duplicates keeping order
print("9. Remove duplicates:", "".join(dict.fromkeys(s)))

# 10. Count vowels frequency
vowels = {ch: freq[ch] for ch in "aeiou" if ch in freq}
print("10. Vowel frequency:", vowels)

# 11. Sorted by frequency (desc)
print("11. Sorted by frequency:", sorted(freq.items(), key=lambda x: x[1], reverse=True))

# 12. Check if two strings are anagrams
s1, s2 = "listen", "silent"
print("12. Anagrams?", Counter(s1) == Counter(s2))

# 13. First non-repeating character
non_rep = next((ch for ch in s if freq[ch] == 1), None)
print("13. First non-repeating:", non_rep)

# 14. First repeating character
rep = next((ch for ch in s if freq[ch] > 1), None)
print("14. First repeating:", rep)

# 15. Check if all char frequencies same
print("15. All freq same?", len(set(freq.values())) == 1)

# 16. Character closest to k frequency
k = 3
closest = min(freq.items(), key=lambda x: abs(x[1]-k))
print("16. Char closest to freq 3:", closest)

# 17. Remove least frequent chars
min_count = min(freq.values())
print("17. Remove least frequent:", "".join(ch for ch in s if freq[ch] > min_count))

# 18. Remove most frequent chars
max_count = max(freq.values())
print("18. Remove most frequent:", "".join(ch for ch in s if freq[ch] < max_count))

# 19. Find k-th most frequent char
k = 2
print("19. 2nd most frequent:", sorted(freq.items(), key=lambda x: x[1], reverse=True)[k-1])

# 20. Characters grouped by frequency
grouped = {cnt: [ch for ch, v in freq.items() if v == cnt] for cnt in set(freq.values())}
print("20. Grouped by frequency:", grouped)

# 21. Frequency difference between strings
s1, s2 = "geeks", "seek"
print("21. Difference (s1-s2):", Counter(s1) - Counter(s2))
