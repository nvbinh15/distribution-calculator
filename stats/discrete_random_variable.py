def discrete_random_variable_params(pmf):
    expectation = 0
    second_moment = 0
    total_probability = sum(pmf[x] for x in pmf)
    if (total_probability - 1 >= 0.01):
        print(f"The total probability is not 1. ({total_probability})")
        return
    print(f"Probability: {total_probability}")
    for sample_point in pmf:
        expectation += sample_point * pmf[sample_point]
        second_moment += pmf[sample_point] * sample_point * sample_point
    variance = second_moment - expectation ** 2
    print(f"Expectation E(X) = mu = {expectation}")
    print(f"Second moment E(X^2) = {second_moment}")
    print(f"Variance V(X) = {variance}")
