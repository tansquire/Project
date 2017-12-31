
package oops;


public class Encapsulation 
{
    public static void main(String[] args) 
    {
        Employee Ram=new Employee();
        Ram.SetSalary(5000);
        System.out.println(Ram.GetSalary());
    }
}
 class Employee 
{
   private int Salary;  //This should be private sot that nobody can directly change it
     public  void SetSalary(int x) 
     {
         
         Salary=x;
     }
     public  int GetSalary() 
     {
         
         return(Salary);
     }
}
