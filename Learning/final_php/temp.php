    <!DOCTYPE html>
    <html>
    <body>
       
                    <form method="post" name="">
                        <table bgcolor="#FFFFFF" border="0" cellpadding="3"
                        cellspacing="1" width="100%">
                           
                            <tr>
                               
                                <td width="294"><input id="username" name=
                                "username" type="text"></td>
                            </tr>
                           
                            <tr>
                               
                                <td><input name="submit" type="submit" value=
                                "Login"></td>
                            </tr>
                        </table>
                    </form>
               
    </body>
    </html>
<?php
        if (isset($_POST['submit']))
            {     
        include("config.php");
        
        $username=$_POST['username'];
        

        
	$sql = "UPDATE level SET Value='$username' WHERE Device=1";

	$conn->query($sql);
	

        ?>
