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
        return f"Negative Binomial Distribution\nX: number of trials, with number of successes = {self.k} and prob of a success = {self.p}" \
            + f"\nE(X) = k / p = {self.k / self.p}; V(X) = (1 - p)k / p^2 = {(1 - self.p) * self.k / (self.p * self.p)}"

class poisson:
    
    def __init__(self, xlambda):
        self.xlambda = xlambda

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.poisson.cdf(target, self.xlambda)}")
    
    def pmf(self, target):
        print(f"Pr(X = {target}) = {stats.poisson.pmf(target, self.xlambda)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.poisson.cdf(target, self.xlambda)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.poisson.ppf(target, self.xlambda)}) >= {target}")

    def __str__(self):
        return f"Poisson Distribution\nX: number of successes in a Poisson experiment." \
            + f"\nE(X) = V(X) = lambda = {self.xlambda}"

class exponential:
    
    def __init__(self, alpha):
        self.xlambda = 1 / alpha

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.expon.cdf(target, 0, self.xlambda)}")
    
    def pdf(self, target):
        print(f"f({target}) = {stats.expon.pdf(target, 0, self.xlambda)}")

    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.expon.cdf(target, 0, self.xlambda)}")

    def ppf(self, target):
        print(f"Pr(X <= {stats.expon.ppf(target, 0, self.xlambda)}) = {target}")

    def __str__(self):
        return f"Exponential Distribution\n" \
            + f"E(X) = lambda = 1 / alpha = {self.xlambda}; V(X) = lambda^2 = 1 / (alpha ^2) = {self.xlambda * self.xlambda}"

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

class t:
    
    def __init__(self, dof):
        self.dof = dof

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.t.cdf(target, self.dof)}")

    def pdf(self, target):
        print(f"f({target}) = {stats.t.pdf(target, self.dof)}")
    
    def right_cdf(self, target):
        print(f"Pr(X >= {target}) = {1 - stats.t.cdf(target, self.dof)}")
    
    def ppf(self, target):
        print(f"Pr(X <= {stats.t.ppf(target, self.dof)}) = {target}")
        print(f"Pr(X >= {stats.t.ppf(1 - target, self.dof)}) = {target}")

    def __str__(self):
        return f"t-Distribution where degree of freedom  = {self.dof}"

class chi_sq:
    
    def __init__(self, dof):
        self.dof = dof
    
    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.chi2.cdf(target, self.dof)}")
    
    def pdf(self, target):
        print(f"f({target}) = {stats.chi2.pdf(target, self.dof)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.chi2.cdf(target, self.dof)}")
    
    def ppf(self, target):
        print(f"Pr(X <= {stats.chi2.ppf(target, self.dof)}) = {target}")
        print(f"Pr(X >= {stats.chi2.ppf(1 - target, self.dof)}) = {target}")

    def __str__(self):
        return f"Chi-squared Distribution where degree of freedom  = {self.dof}"

class f:
    
    def __init__(self, dof1, dof2):
        self.dof1 = dof1
        self.dof2 = dof2

    def left_cdf(self, target):
        print(f"Pr(X <= {target}) = {stats.f.cdf(target, self.dof1, self.dof2)}")
    
    def pdf(self, target):
        print(f"f({target}) = {stats.f.pdf(target, self.dof1, self.dof2)}")
    
    def right_cdf(self, target):
        print(f"Pr(X > {target}) = {1 - stats.f.cdf(target, self.dof1, self.dof2)}")
    
    def ppf(self, target):
        print(f"Pr(X <= {stats.f.ppf(target, self.dof1, self.dof2)}) = {target}")
        print(f"Pr(X >= {stats.f.ppf(1 - target, self.dof1, self.dof2)}) = {target}")

    def __str__(self):
        return f"F-Distribution where degrees of freedom are {self.dof1} and {self.dof2}"

p = f(12, 10)
print(p)
p.left_cdf(3)
p.pdf(3)
p.right_cdf(3)
p.ppf(0.05)
