from bank import customer_name


def test_customer_name():
    testing_case = "dog"
    assert type(testing_case) == type(customer_name)
