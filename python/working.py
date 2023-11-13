class WorkingHourSystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def tracking(self, employees, hours):
        print('Tracking Employee WorkingHour')
        print('==============================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')

# -------------------------------------ManagerRole Class---------------------------------


class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'

# -------------------------------------SecretaryRole Class---------------------------------


class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'

# -------------------------------------SalesRole Class---------------------------------


class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'

# -------------------------------------FactoryRole Class---------------------------------


class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'
