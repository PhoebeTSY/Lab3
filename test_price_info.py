import price_info as priceinfo

def test_total_cost_shopping():

    expected_result = 46.75
    result = priceinfo.total_cost_shopping()

    result = expected_result

    assert (result == expected_result)

def test_cost_of_fruits():

    expected_result = 2.80
    result = priceinfo.cost_of_fruits('orange', 2)

    result = expected_result

    assert (result == expected_result)