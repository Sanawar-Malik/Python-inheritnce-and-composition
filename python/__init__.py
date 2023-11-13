from python.admin import PayrollSystem, HourlyPolicy
from python.employees import EmployeeDatabase
from python.working import WorkingHourSystem

productivity_system = WorkingHourSystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()

employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(70)

secretary = employees[1]
secretary.payroll = HourlyPolicy(50)

sales = employees[2]
sales.payroll = HourlyPolicy(60)

factory = employees[3]
factory.payroll = HourlyPolicy(55)

productivity_system.tracking(employees, 40)
payroll_system.calculate_payroll(employees)
