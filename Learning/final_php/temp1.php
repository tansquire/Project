
<html>
   
   <head>
      <title>Welcome </title>
     <script>
$(document).ready(function() {
$("button").click(function(){
  $.ajax({
    url:"php.php", //the page containing php script
    type: "POST", //request type
    success:function(result){
    alert(result);
    }
  });
});
})
</script>

   </head>
   
   <body>
      
<h2><a href = "Logout.php">Sign Out</a></h2>
<button type="button">Click Me</button>
   </body>
   
</html>

