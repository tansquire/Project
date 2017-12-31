
package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps.

public class JDBC2 //pring first row, and single element
{
    public static void main(String[] args) throws Exception 
    {
        String url="jdbc:mysql://10.21.160.201:3306/test";//test is db name
        String user="root";
        String pass="gowsalya";
        String Query="select * from scada"; 
        Class.forName("com.mysql.jdbc.Driver"); //registration
        
        Connection con=DriverManager.getConnection(url,user,pass);//connection
        Statement st=con.createStatement();//create statement to execute query
        ResultSet rs=st.executeQuery(Query);
        rs.next();//To point the cursor towards first row by default
        //as in the query row is not selected with id=1, or, 2 or...etc
        String s=rs.getString("id")+","+rs.getString("tag")+","+rs.getString("type")
               +","+rs.getString("value");
        //Selecting the whole row with every elements after a comma
        String s1[]=s.split(","); //converting string s into an array
        System.out.println(s); //printing whole string
        System.out.println(s1[1]); //printing single array element
        for(String x:s1) //printing every Array element
            System.out.println(x);
        st.close();
        con.close();
    }
    
}
