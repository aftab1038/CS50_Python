import inflect

p = inflect.engine()

# METHODS:

# plural plural_noun plural_verb plural_adj singular_noun no num
# compare compare_nouns compare_nouns compare_adjs
# a an
# present_participle
# ordinal number_to_words
# join
# inflect classical gender
# defnoun defverb defadj defa defan


# UNCONDITIONALLY FORM THE PLURAL

print("The plural of ", word, " is ", p.plural(word))


# CONDITIONALLY FORM THE PLURAL

print("I saw", cat_count, p.plural("cat", cat_count))


# FORM PLURALS FOR SPECIFIC PARTS OF SPEECH

print(
    p.plural_noun("I", N1),
    p.plural_verb("saw", N1),
    p.plural_adj("my", N2),
    p.plural_noun("saw", N2),
)