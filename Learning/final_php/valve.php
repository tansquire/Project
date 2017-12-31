<?php

include('session.php');
if($opened_status==1)
$image_name = 'open.png';
if($closed_status==1)
$image_name = 'close.png';
if($closed_status==0 AND $opened_status==0)
$image_name = 'inter.png';

?>

<html>

<body>
<img src="<?php echo $image_name?>" style=width:40%;height:40%;">
</body>
</html>
