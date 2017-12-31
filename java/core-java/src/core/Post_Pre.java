
package core;


public class Post_Pre 
{
    public static void main(String[] args) 
    {
        int i,j,k,l,m;
        l=0;
        i=0;
        m=0;
        j=++i; //pre increament, i.e 1st increament, then assignment
        k=i++;
        l=l++; //post increament, i.e 1st assignment, then increment
        m=++m;
        System.out.printf("i=%d, j=%d, k=%d, l=%d, m=%d", i,j,k,l,m);
        
        
    }
    
}
