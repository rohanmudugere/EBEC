from pokerOOP import Suit
from pokerOOP import Cards

def main():
    spades = Suit("Spades")
    one = Cards("6", "Spades")
    two = Cards("4", "Spades")
    three = Cards("10", "Spades")
    four = Cards("Jack", "Spades")
    five = Cards("King", "Spades")
    other1 = Cards("Ace", "Clubs")
    other2 = Cards("Queen", "Diamonds")

    result = Cards.checkStraight(one, two, three, four, five, other1, other2)
    print(f"\n{result}\n")

if __name__ == "__main__":
    main()

