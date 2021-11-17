from distributions.binomial import binomial
from distributions.chi_square import chi_sq
from distributions.exponential import exponential
from distributions.f import f
from distributions.negative_binomial import neg_binomial
from distributions.normal import normal
from distributions.poisson import poisson
from distributions.t import t
from stats.sample import sample_params
from stats.discrete_random_variable import discrete_random_variable_params as discrete

p = f(12, 10)
print(p)
p.left_cdf(3)
p.pdf(3)
p.right_cdf(3)
p.ppf(0.05)
print("-------------")

samples = [10.2, 9.7, 10.1, 10.3, 10.1, 9.8, 9.9, 10.4, 10.3, 9.8]
sample_params(samples)
print("-------------")
pmf = {2:0.01, 3:0.25, 4:0.4, 5:0.3, 6:0.04}
discrete(pmf)


