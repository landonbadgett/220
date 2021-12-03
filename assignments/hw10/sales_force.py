from sales_person import SalesPerson

class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        file.readline()
        for line in file:
            variables = line.split(", ")
            employee = SalesPerson(variables[0], variables[1])
            for i in variables[2].split(" "):
                employee.enter_sale(float(i))
            return self.sales_people.append(employee)

    def quota_report(self, quota):
        list = []
        for i in self.sales_people:
            data = [i.get_id(), i.get_name(), i.total_sales(), i.met_quota(quota)]
            list.append(data)
            return data

    def top_seller(self):
        top_seller = []
        for i in range(len(self.sales_people)):
            for j in range(i + 1, len(self.sales_people)):
                if self.sales_people[j].compare_to(self.sales_people[i]) > 0:
                    self.sales_people[i], self.sales_people[j] = \
                        self.sales_people[j], self.sales_people[i]
        top_seller.append(self.sales_people[0])
        for i in range(1, len(self.sales_people)):
            if self.sales_people[i] >= top_seller[0].total_sales():
                top_seller.append(self.sales_people[i])
            else:
                break
        return top_seller

    def individual_sales(self, id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i] == id:
                return self.sales_people[i]
        return None




