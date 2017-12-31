 <!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
        <table bgcolor="#CCCCCC" border="0" cellpadding="0"
        cellspacing="1">
            <tr>
                <td>
                    <form method="post" name="">
                        <table bgcolor="#FFFFFF" border="0" cellpadding="3"
                        cellspacing="1" >
                            
                            <tr>
                                
                                <td ><input id="level" name=
                                "level" type="text"></td>
                            </tr>
                            
                            <tr>
                                
                                <td><input name="submit" type="submit" value=
                                "set level"> </td>
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
        $value=$_POST['level'];
        
	$sql = "UPDATE level SET Value='$value' WHERE Device=1";
	$conn->query($sql);
        echo"$value";
	}
        ?>
    </body>
    </html>
