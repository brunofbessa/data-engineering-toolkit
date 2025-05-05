# generate fake data

from faker import Faker
fake = Faker(locale='pt_BR')
fake.random.seed(4321)  

def create_employee(num_rows):
    _list = []
    for i in range(1, num_rows):
        row = {}
        row['id'] = i
        row['first_name'] = fake.first_name()
        row['last_name'] = fake.last_name()
        row['department'] = fake.random_element(elements=('ti', 'consultoria', 'rh', 'financeiro'))
        row['position_type'] = fake.random_element(elements=('analista', 'consultor', 'trainee', 'gerente'))
        row['salary'] = fake.random_int(min=3000, max=20000, step=500)
        row['date_of_birth'] = fake.date_of_birth(minimum_age=18, maximum_age=60)
        row['date_of_hire'] = fake.date_of_birth(minimum_age=0, maximum_age=10)
        row['email'] = fake.email()
        
        _list.append(row)

    return pd.DataFrame(_list)


def create_client(num_rows):
    _list = []
    for i in range(1, num_rows):
        row = {}
        row['id'] = i
        row['name'] = fake.company() + ' ' + fake.company_suffix()
        row['sector'] = fake.random_element(elements=('farma', 'energia', 'governo'))
        row['last_revenue_million'] = fake.random_int(min=10, max=400, step=10)
        row['email'] = fake.email()
        
        _list.append(row)

    return pd.DataFrame(_list)

def create_sale(num_rows):
    _list = []
    for i in range(1, num_rows):
        row = {}
        row['id'] = i
        row['client_id_fk'] = fake.random_int(min=1, max=50, step=1)
        row['employee_responsible_id_fk'] = fake.unique.random_int(min=1, max=400, step=1)
        row['date_of_start'] = fake.date_of_birth(minimum_age=0, maximum_age=5)
        _list.append(row)

    return pd.DataFrame(_list)


def create_project_allocation(num_rows):
    _list = []
    for i in range(1, num_rows):
        row = {}
        row['id'] = i
        row['sale_id_fk'] = fake.random_int(min=1, max=50, step=1)
        row['employee_id_fk'] = fake.unique.random_int(min=1, max=400, step=1)

        _list.append(row)

    return pd.DataFrame(_list)
