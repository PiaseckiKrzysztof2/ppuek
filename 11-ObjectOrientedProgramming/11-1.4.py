# Zadanie 11-1.4 - Profil w mediach społecznościowych (socialmedia.py)
# Co robi: klasa SocialMediaProfile przechowuje nazwę użytkownika i listę postów.
#          Dodana metoda display_timeline wypisuje użytkownika i jego posty z numerami.
#          Program tworzy użytkownika johndoe, dodaje 3 posty i wyświetla tablicę.


class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []                      # atrybut może być listą

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):              # dodana metoda
        print(f"{self.username}'s timeline:")
        number = 1
        for post in self.posts:
            print(f'{number}. {post}')
            number += 1


def main():
    user = SocialMediaProfile('johndoe')
    user.add_post('Hello, world!')
    user.add_post('Had a great day at the park!')
    user.add_post("What's up, Natalie? How are you?")
    print()
    user.display_timeline()


if __name__ == "__main__":
    main()
