package Education_GeekBrains.ObjOrientProgram.Lesson003.HW;

import java.util.Comparator;

public class SalaryComparator implements Comparator<Employee> {


    @Override
    public int compare(Employee o1, Employee o2) {
        // -1, 0, 1

        //тернарные операции

        return Double.compare(o2.calculateSalary(), o1.calculateSalary());
        //return o1.calculateSalary() ==  o2.calculateSalary() ? 0 : (o1.calculateSalary() > o2.calculateSalary() ? 1 : -1);
        /*
         * ? - тернарный оператор((return) значит равно)
         * : - иначе (else)
         */
    }

}
