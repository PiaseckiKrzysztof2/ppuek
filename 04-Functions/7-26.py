# Rozdziela znaki tekstu myślnikiem
def f(text):
    # join wstawia myślnik między znaki
    return '-'.join(text)


def main():
    for text in ["University", "UE", "x", ""]:
        print(f'f("{text}") returns "{f(text)}"')


if __name__ == "__main__":
    main()
