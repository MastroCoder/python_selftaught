import re

text = """Today I went to the zoo. I saw a(n) __ADJECTIVE__ __NOUN__
jumping up and down in its tree. He __PAST_TENSE_VERB__ __ADVERB__
through the large tunnel that led to its __ADJECTIVE__ __NOUN__.
I got some peanuts and passed them through the cage to a gigantic gray
__NOUN__ towering above my head. Feeding that animal made
me hungry. I went to get a __ADJECTIVE__ scoop
of ice cream. It filled my stomach. Afterwards I had to
__VERB__ __ADVERB__ to catch our bus.
When I got home I __PAST_TENSE_VERB__ my
mom for a __ADJECTIVE__ day at the zoo"""

def mad_libs(text):
    hints = re.findall("__.*?__", text)
    if hints:
        for word in hints:
            a = input("Please write a {}: ".format(word))
            text = text.replace(word, a, 1)
        print("\n")
        text = text.replace("\n", " ")
        print(text)

mad_libs(text)
