from book import Book

library = [
    Book('Кортик', "Анатолий Рыбаков"),
    Book('Эммануэль', 'Эммануэль Арсан'),
    Book('Преступление и наказание ', 'Федор Достоевский')]

for book in library:
    print({book.name} - {book.author})
