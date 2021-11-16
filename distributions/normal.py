from scipy import stats

class normal:
    
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.norm.cdf(target, self.mu, self.sigma)}")

    def pdf(self, target):
        print(f"f({target}) = {stats.norm.pdf(target, self.mu, self.sigma)}")

    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.norm.cdf(target, self.mu, self.sigma)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.norm.ppf(target, self.mu, self.sigma)}) = {target}")

    def ppf_standard(self, target):
        print(f"Pr(Z >= {stats.norm.ppf(1 - target, 0, 1)}) = {target} where Z = (X - {self.mu}) / {self.sigma}")

    def __str__(self):
        return f"Normal Distribution\n" \
            + f"E(X) = {self.mu}; V(X) = {self.sigma * self.sigma}"
