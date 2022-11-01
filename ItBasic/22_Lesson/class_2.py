class Books:
    def __init__(self, name_par, age_par, publisher_par, genre_par, author_par, price_par):
        self.name = name_par
        self.age = age_par
        self.publisher = publisher_par
        self.genre = genre_par
        self.author = author_par
        self.price = price_par
        self.reveu_list = []

    def __str__(self):
        # str_reviews = "\nReviews: ".join(map(str,self.reveu_list))
        str_reviews = ""
        for ind in range(1, len(self.reveu_list) + 1):
            str_reviews = str_reviews + f'Rewiews {ind}: {self.reveu_list[ind - 1]}\n'
        return f'{self.name}, {self.age}, {self.publisher}, {self.genre}, {self.author}, {self.price}, \n{str_reviews}'

    def change_name(self, new_name):
        self.name = new_name
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_publisher):
        self.publisher = new_publisher
        return "Saved"

    def change_genre(self, new_genre):
        self.genre = new_genre
        return "Saved"

    def change_author(self, new_author):
        self.author = new_author
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"

    def add_reveu(self, new_reveu):
        self.reveu_list.append(new_reveu)
        return "Good, well done"


class Book_reveu:
    def __init__(self, text_par):
        self.text = text_par

    def __repr__(self):
        return f"{self.text}"


metro2033 = Books("Метро 2033", "2020", "Навчальна книга - Богдан", "Фантастика", "Дмитро Ґлуховський", "449.00")
reveu = Book_reveu("Reveu 1")
reveu2 = Book_reveu("Reveu 2")

print(metro2033)
print(metro2033.add_reveu(reveu))
print(metro2033)
print(metro2033.add_reveu(reveu2))
print(metro2033)



