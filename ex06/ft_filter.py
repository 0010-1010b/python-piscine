def ft_filter(function, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """

    result = [i for i in iterable if function(i)]
    return result


def is_adult(age):
    return age >= 18


def main():
    print(ft_filter.__doc__)
    print(filter.__doc__)
    # ages = [12, 17, 21, 30, 15]

    # adults_iterator = ft_filter(is_adult, ages)

    # print(adults_iterator)
    # adults_list = list(adults_iterator)
    # print(adults_list)


if __name__ == "__main__":
    main()
