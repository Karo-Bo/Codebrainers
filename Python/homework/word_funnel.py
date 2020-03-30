def funnel(first_word, second_word):

    can_be_made = False

    if len(first_word) - len(second_word) == 1:
        for i in range(0, len(first_word)):
            if (first_word[:i] + first_word[i + 1:]) == second_word:
                can_be_made = True

    return can_be_made

def test_funnel():

    assert funnel("leave", "eave") == True
    assert funnel("reset", "rest") == True
    assert funnel("dragoon", "dragon") == True
    assert funnel("eave", "leave") == False
    assert funnel("sleet", "lets") == False
    assert funnel("skiff", "ski") == False