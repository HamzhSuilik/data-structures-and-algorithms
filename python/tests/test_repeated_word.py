from repeated_word.repeated_word import repeated_word

def test_1():
    array = []
    actual = repeated_word("Python is an interpreted high-level general-purpose programming language ,PHP is a server scripting language and a powerful tool for making dynamic and interactive Web pages. , Java is a high-level class-based object-oriented programming language that is designed to have as few implementation dependencies as possible.")
    expected = 'is'
    assert actual == expected

def test_2():
    actual = repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...")
    expected = 'it'
    assert actual == expected


def test_3():
    actual = repeated_word("It was a queer, sultry summer , the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    expected = 'summer'
    assert actual == expected

# edge case
# def test_4():
#     actual = repeated_word('')
#     expected = ''
#     assert actual == expected
