from scipy import stats

class binomial:

    def __init__(self, n, p):
        self.n = n
        self.p = p

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.binom.cdf(target, self.n, self.p)}")
    
    def pmf(self, target):
        print(f"Pr(X = {target}) = {stats.binom.pmf(target, self.n, self.p)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.binom.cdf(target, self.n, self.p)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.binom.ppf(target, self.n, self.p)}) = {target}")

    def __str__(self):
        return f"Binomial Distribution\nX: number of successes, with n = {self.n} trials and prob of success p = {self.p}" \
            + f"\nE(X) = np =  {self.n * self.p}; V(X) = np(1-p) = {self.n * self.p * (1 - self.p)}"
