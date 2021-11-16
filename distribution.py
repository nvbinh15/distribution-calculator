from distributions.binomial import binomial
from distributions.chi_square import chi_sq
from distributions.exponential import exponential
from distributions.f import f
from distributions.negative_binomial import neg_binomial
from distributions.normal import normal
from distributions.poisson import poisson
from distributions.t import t

p = f(12, 10)
print(p)
p.left_cdf(3)
p.pdf(3)
p.right_cdf(3)
p.ppf(0.05)
