class r:
    def __init__(self, text: str):
        self.original = text
        self.reversed = text[::-1]

    def display(self):
        print(f"Original: {self.original}")
        print(f"Reversed: {self.reversed}")

def main():
    word = input("Enter a word: ")
    rev = r(word)
    rev.display()

if __name__ == "__main__":
    main()
