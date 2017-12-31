
<?php

include('session.php');
if($opened_status==1)
$image_name = 'open.png';
else
$image_name = 'close.png';
?>

<html>

<body>
<img src="<?php echo $image_name?>" style=width:40%;height:40%;">
</body>
</html>

