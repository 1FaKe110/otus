def chunkify(lst, k):
    avg = len(lst) // k  # Средняя длина чанка
    rem = len(lst) % k  # Остаток

    chunks = []
    start = 0

    # Создание чанков
    for i in range(k):
        if i < rem:
            end = start + avg + 1
        else:
            end = start + avg

        chunks.append(lst[start:end])
        start = end

    return chunks

# Пример использования
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k = 4

result = chunkify(data, k)
print(result)