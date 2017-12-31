package oops;


public class Interface_LambdaExpression  //new java 8 feature
{
    public static void main(String[] args) 
    {
//        II obj=()-> //Taking help of annynomous inner class
//           {
//               System.out.println("HI");  //For multiple expression
                 //this is method defination
//           };
        
        II obj=()->System.out.println("HI");   //For single expression
        
        obj.show();
        
       }
        
        
    }
    

interface II
{
    void show();
}