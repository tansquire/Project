<?php

 if($_GET['button1']){fun1();}
 if($_GET['button2']){fun2();}
 if($_GET['button3']){fun3();}
 if($_GET['button4']){fun4();}
 
if (isset($_POST['submit']))
            {     
        include("Config.php");
        $value=$_POST['level'];
        
	$sql = "UPDATE level SET Value='$value' WHERE Device=1";
	$conn->query($sql);
        
	} 


 function fun1()
{
 include("test_opened.php");
}

function fun2()
{
 include("test_closed.php");
}
function fun3()
{
 include("test_remote.php");
}
function fun4()
{
 include("test_local.php");
}
?>

<!DOCTYPE html>

<html>

<body>
<button id="btnfun1" name="btnfun1" '>opened</button>
<button id="btnfun2" name="btnfun2" onClick='location.href="?button2=1"'>closed</button>
<button id="btnfun3" name="btnfun3" onClick='location.href="?button3=1"'>remote</button>
<button id="btnfun4" name="btnfun4" onClick='location.href="?button4=1"'>local</button>
<br></br>
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

</body>
