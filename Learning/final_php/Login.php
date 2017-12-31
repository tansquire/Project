<!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
        <table align="center" bgcolor="#CCCCCC" border="0" cellpadding="0"
        cellspacing="1" width="300">
            <tr>
                <td>
                    <form method="post" name="">
                        <table bgcolor="#FFFFFF" border="0" cellpadding="3"
                        cellspacing="1" width="100%">
                            <tr>
                                <td align="center" colspan="3"><strong>User
                                Login</strong></td>
                            </tr>
                            <tr>
                                <td width="78">Username</td>
                                <td width="6">:</td>
                                <td width="294"><input id="username" name=
                                "username" type="text"></td>
                            </tr>
                            <tr>
                                <td>Password</td>
                                <td>:</td>
                                <td><input id="password" name="password" type=
                                "password"></td>
                            </tr>
                            <tr>
                                <td>&nbsp;</td>
                                <td>&nbsp;</td>
                                <td><input name="submit" type="submit" value=
                                "Login"> <input name="reset" type="reset" value=
                                "reset"></td>
                            </tr>
                        </table>
                    </form>
                </td>
            </tr>
        </table>
        <?php
        if (isset($_POST['submit']))
            {     
        include("Config.php");
        session_start();
        $username=$_POST['username'];
        $password=$_POST['password'];
       // $_SESSION['login_user']=$username; 

        $sql = "SELECT * FROM Login WHERE username='$username' and password='$password'";

	$result = $conn->query($sql);
	$row = mysqli_fetch_assoc($result);

        $x=$row[password];
	//$user=$row[username];
        

	//$sql1 = "SELECT * FROM Login WHERE user_id='1'"; 

	//$result1 = $conn->query($sql1);
	//$row1 = mysqli_fetch_assoc($result1);

        //$administrator=$row1[username];

      



 // $query = mysql_query("SELECT username FROM Login WHERE username='$username' and password='$password'");
        if ($x!= 0)
        {

         $_SESSION['login_user']=$username;
         //session_register("username");
         echo "<script language='javascript' type='text/javascript'> location.href='water1.php' </script>";   
         }
          else
          {
        echo "<script type='text/javascript'>alert('User Name Or Password Invalid!')</script>";
        }
        }
        ?>
    </body>
    </html>
