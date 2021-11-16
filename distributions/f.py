from scipy import stats

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
