# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:


letter_prices = {
    1: "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т",
    2: "D, G, Д, К, Л, М, П, У",
    3: "B, C, M, P, Б, Г, Ё, Ь, Я",
    4: "F, H, V, W, Y, Й, Ы",
    5: "K, Ж, З, Х, Ц, Ч",
    8: "J, X, Ш, Э, Ю",
    10: "Q, Z, Ф, Щ, Ъ",
}

word = "ноутбук"
word = word.upper()
total_score = 0

for letter in word:
    for points, letters in letter_prices.items():
        if letter in letters:
            total_score += points

print(total_score)

