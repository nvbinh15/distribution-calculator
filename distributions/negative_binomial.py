from scipy import stats

class neg_binomial:
    
    def __init__(self, k, p):
        self.k = k
        self.p = p

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.nbinom.cdf(target - self.k, self.k, self.p)}")
    
    def pmf(self, target):
        print(f"Pr(X = {target}) = {stats.nbinom.pmf(target - self.k, self.k, self.p)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.nbinom.cdf(target - self.k, self.k, self.p)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.nbinom.ppf(target, self.k, self.p) + self.k}) >= {target}")

    def __str__(self):
        return f"X: the number of trials to produce k successes in a sequence of independent Bernoulli trials\n" \
            + "Pr(X = x) = f(x) = (x - 1)C(k - 1) * p^k * q^(x - k) for x = k, k + 1, ...\n" \
            + f"Expectation E(X) = k / p = {self.k / self.p}; Variance V(X) = (1 - p)k/p^2 = {(1 - self.p) * self.k / (self.k * self.k)}"
    