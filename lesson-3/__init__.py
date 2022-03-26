def say_the_word_1(word):
    print("Hello" + word)


def say_the_word_2(*froods):
    print("the first frood is: " + froods[0])
    print("the second frood is: " + froods[1])
    print("the third frood is: " + froods[2])


def say_the_word_3(child3, child2, child1):
    print("The youngest child is " + child3)
    print("The second youngest child is " + child2)
    print("The oldest child is " + child1)


def say_the_word_4(**kids):
    print("The youngest child is " + kids["child3"])
    print("The second youngest child is " + kids["child2"])
    print("The oldest child is " + kids["child1"])


def calculate_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def print_christmas_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (i * 2 + 1))


if __name__ == '__main__':
    # say_the_word_1()
    # say_the_word_2("banana", "apple", "orange")
    # say_the_word_3(child1="Emil", child2="Tobias", child3="Linus")
    # say_the_word_4(child1="Emil", child2="Tobias", child3="Linus")
    # calculate_prime()
    print_christmas_tree(5)
