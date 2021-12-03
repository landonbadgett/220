class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.get_name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        acc = 0
        for i in self.sales:
            acc += i
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales > other.total_sales:
            return 1
        elif self. total_sales < other.total_sales:
            return -1
        else:
            return 0

    def __str__(self):
        return ("<" + self.employee_id + ">-<" + self.name + ">: <" + str(self.total_sales() + ">"))



