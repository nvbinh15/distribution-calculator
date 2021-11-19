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


# pmf = {0:0.05, 1:0.18, 2:0.15, 3:0.27, 4:0.19, 5:0.16}
# discrete(pmf)

p = exponential(5)
print(p)
