def funnel(first_word, second_word):

    can_be_made = False

    if len(first_word) - len(second_word) == 1:
        for i in range(0, len(first_word)):
            if (first_word[:i] + first_word[i + 1:]) == second_word:
                can_be_made = True
                break

    return can_be_made


def test_funnel():

    assert funnel("leave", "eave") is True
    assert funnel("reset", "rest") is True
    assert funnel("dragoon", "dragon") is True
    assert funnel("eave", "leave") is False
    assert funnel("sleet", "lets") is False
    assert funnel("skiff", "ski") is False
