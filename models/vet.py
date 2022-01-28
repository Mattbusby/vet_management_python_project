class Vet:
    
    def __init__(self, first_name, last_name, grad_date, fun_fact, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.grad_date = grad_date
        self.fun_fact = fun_fact
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"