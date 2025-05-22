import Lab2.Lab2 as Lab2

def find_min_max():
    result = [5, 30]
    input_arr = [5, 12, 15, 27, 30]

    result = Lab2.calc_min_max_temperature(input_arr)

    assert (result == [5,30])

def calc_average():
    result = 17.8
    input_arr = [5, 12, 15, 27, 30]

    result = Lab2.calc_average(input_arr)

    assert (result == 17.8)

def calc_Sort_temperature():
    input_arr = [12, 5, 27, 15, 30]

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == [5, 12, 15, 27, 30])

def calc_median_temperature_odd():
    result = 15.0
    input_arr = [5, 12, 15, 27, 30]

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == 15.0)

def calc_median_temperature_even():
    input_arr = [5, 12, 27, 30]

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == 19.5)
