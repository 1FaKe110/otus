import json
import csv
from munch import DefaultMunch

from src.repo.book import Book
from src.repo.user import User

BOOKS_PATH = './input/books.csv'
USERS_PATH = './input/users.json'
REFERENCE_PATH = './output/reference.json'
as_class = DefaultMunch.fromDict


def read_data():
    with open(BOOKS_PATH, 'r') as f:
        books = [Book(**row) for row in list(csv.DictReader(f))]

    with open(USERS_PATH, 'r') as f:
        users = [User(**r) for r in json.loads(f.read()) if r['isActive']]

    return books, users


def save(data):
    with open(REFERENCE_PATH, 'w', encoding='utf-8') as f:
        f.write(json.dumps(
            [user.as_dict() for user in data],
            indent=2,
            ensure_ascii=False))


def main():
    books, users = read_data()

    k = len(users)
    avg = len(books) // k  # Средняя длина чанка
    rem = len(books) % k  # Остаток

    chunks = []
    start = 0

    # Создание чанков
    for i in range(k):
        if i < rem:
            end = start + avg + 1
        else:
            end = start + avg

        chunks.append(books[start:end])
        start = end

    # Добавление пользователю книг из чанка
    for c in range(len(chunks)):
        for book in chunks[c]:
            users[c].add_book(book)

    save(users)


if __name__ == '__main__':
    main()
