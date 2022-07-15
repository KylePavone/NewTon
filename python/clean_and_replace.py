"""
    Написать функцию, заменяющую синонимы и убирающую лишние пробелы. Пример:

    clean_and_replace(“   I love buns  with strawberry jam  ”, “jam”, “filling”)
    =>
    “I love buns with strawberry filling”

"""

def clean_and_replace(sentence: str, rep_word: str, syn_word: str):
    return " ".join(sentence.replace(rep_word, syn_word).split())

print(clean_and_replace("   I love buns  with strawberry jam  ", "jam", "filling"))
