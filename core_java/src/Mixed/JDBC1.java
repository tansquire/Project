
package Mixed;
import java.sql.*;
//For netbeans, right click on library->add library->mysql jdbc driver->add
//For eclips, you have to download the library(jar file) first
//and then follow the abobe steps(master) added in temp

public class JDBC1 //printing single element of any row
{
    public static void main(String[] args) throws Exception 
    {
        String url="jdbc:mysql://10.21.160.201:3306/test";//test is db name
        String user="root";
        String pass="gowsalya";
        String Query="select * from scada where id=2";
        Class.forName("com.mysql.jdbc.Driver"); //registration
        
        Connection con=DriverManager.getConnection(url,user,pass);//connection
        Statement st=con.createStatement();//create statement to execute query
        ResultSet rs=st.executeQuery(Query);
        rs.next();//To point the cursor towards first row where id=2
        String s=rs.getString("id");//Selecting id column of the selected row
        System.out.println(s);
        st.close();
        con.close();
    }
    
}
