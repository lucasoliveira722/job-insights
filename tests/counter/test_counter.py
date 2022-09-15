from src.counter import count_ocurrences


def test_counter():
    # assert (count_ocurrences('src/jobs.csv', 'New York')) == 597
    # assert (count_ocurrences('src/jobs.csv', 'Rego Park')) == 89
    # assert (count_ocurrences('src/jobs.csv', 'Williston Park')) == 89
    assert (count_ocurrences('src/jobs.csv', 'Python')) == 1639
    assert (count_ocurrences('src/jobs.csv', 'Javascript')) == 122
