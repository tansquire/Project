
package oops;


public class Object_Passing 
{
    public static void main(String[] args) 
    {
        paper p=new paper();
        p.settext("hello world");
        System.out.println(p.gettext());
        printer hp=new printer();
        hp.print(p);
        System.out.println(p.gettext());
        
        
    }
    
}
class paper
{
    String text;
    public void settext(String t)
    {
        text=t;
    }
    public String gettext()
    {
        return(text);
    }
}

class printer
{
    public void print(paper q)
    {
        q.settext("get lost");
    }
    
    
}
