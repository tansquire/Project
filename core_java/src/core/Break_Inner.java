
package core;


public class Break_Inner 
{
    public static void main(String[] args) 
           
    {
         int i,j;
        for(i=0;i<5;i++)
        {
            for(j=0;j<5;j++)
            {
                if(i==2)
                    break;
                System.out.print("*");
            }
            System.out.println("");
        }
    }
    
}
