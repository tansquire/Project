<?php
include('Config.php');



        $sql1 = "SELECT * FROM command WHERE valve='1'"; 

	$result1 = $conn->query($sql1);
	$row1 = mysqli_fetch_assoc($result1);

        $x=$row1[opened];
        echo$x;



?>
