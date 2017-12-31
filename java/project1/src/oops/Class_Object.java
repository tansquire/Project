
package oops;


public class Class_Object 
{
    public static void main(String[] args) 
    {
        Student Ram=new Student();
        Ram.age=25;
        Ram.name="Ram";
        int p=Ram.add(20, 30);
        System.out.println(p);
        Student Sam=new Student(10,10);
        
    }
    
    
}
class Student
{
    int age;
    String name;
    int math;
    int phys; //this math and phys can be initialised in this class 
              //during object creation.
    public  int add(int i, int j)
            
    {

        int sum =i+j;
        return(sum);
        
    }
  
     Student() 
    {
        math=36;
        phys=87;  //phys and math get initialised if empty cons is called.
        System.out.println("empty constructor");
    }
     Student(int x, int y)  //constructor cant return
    {
       
       System.out.println(x+y);
    }
     
} 
