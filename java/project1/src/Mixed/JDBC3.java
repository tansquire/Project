
package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps.

public class JDBC3 //printing single element of 2nd row
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
        rs.next();//To point the cursor towards first row. This line is must
        rs.next();//To point the cursor towards 2nd row
        //2nd time rs.next() is applicable where id="" is not written in the query
        String s=rs.getString(1);//Selecting 1st column of the selected row
        System.out.println(s);
        st.close();
        con.close();
    }
    
}
