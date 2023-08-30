def main():
    workhours = int(input('Enter your work hours: 50 '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
overtime = workhours - reg_hours
   print (overtime) 
overtime_wage = overtime * ov_rate
   print (overtime_wage)
regular_wage = reg_hours * reg_rate
   print (regular_wage)
total_wage = regular_wage + overtime_wage
   print (total_wage) 
   ##################################################

    print(f"Regular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime} Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
