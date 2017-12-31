<?php
 include('Config.php');

   session_start();
   
         $user_check = $_SESSION['login_user'];
   
        

//Finding administrator


	$sql1 = "SELECT * FROM Login WHERE user_id='1'"; 
	$result1 = $conn->query($sql1);
	$row1 = mysqli_fetch_assoc($result1);
	$administrator=$row1[username];


//Finding current user


	$sql2 = "SELECT * FROM Login WHERE username='$user_check'";
	$result2 = $conn->query($sql2);
	$row2 = mysqli_fetch_assoc($result2);
        $login_session = $row2['username'];



        if($login_session==$administrator)
        $check=1;
	else
	$check=0;

//Finding Local/Remote status
	
	$sql3 = "SELECT * FROM command WHERE valve='1'"; 
	$result3 = $conn->query($sql3);
	$row3 = mysqli_fetch_assoc($result3);
	$remote_status=$row3[remote];


//Finding opened/closed status
	
	$sql4 = "SELECT * FROM command WHERE valve='1'"; 
	$result4 = $conn->query($sql4);
	$row4 = mysqli_fetch_assoc($result4);
	$opened_status=$row4[opened];






        if(!isset($_SESSION['login_user'])){

        echo "<script language='javascript' type='text/javascript'> location.href='welcome.php' </script>";  


   }
?>
