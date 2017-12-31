<?php

 if($_GET['button1']){fun1();}
 if($_GET['button2']){fun2();}
 if($_GET['button3']){fun3();}
 if($_GET['button4']){fun4();}
 if($_GET['button5']){fun5();}
 
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
function fun5()
{
 include("test_level.php");
}
?>

<!DOCTYPE html>

<html>

<body>
<button id="btnfun1" name="btnfun1" onClick='location.href="?button1=1"'>opened</button>
<button id="btnfun2" name="btnfun2" onClick='location.href="?button2=1"'>closed</button>
<button id="btnfun3" name="btnfun3" onClick='location.href="?button3=1"'>remote</button>
<button id="btnfun4" name="btnfun4" onClick='location.href="?button4=1"'>local</button>
<button id="btnfun5" name="btnfun5" onClick='location.href="?button5=1"'>Level</button>
</body>
