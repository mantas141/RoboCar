<!DOCTYPE html>
<html>
<title> User Interface</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<head>
<?php 
if (isset($_POST['Forward']))
{
	exec('sudo python /forward.py'); #location of Forward
}
if (isset($_POST['Backward']))
{
	exec('sudo python back.py'); #location of Backward
}
if (isset($_POST['Left']))
{
	exec('sudo python left.py'); #location of Left
}
if (isset($_POST['Right']))
{
	exec('sudo python right.py'); #location of Right
}
if (isset($_POST['Stop']))
{
	exec('sudo python stop.py'); #location of Stop
}
?>
</head>
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-bar,h1,button {font-family: "Montserrat", sans-serif}
.fa-anchor,.fa-coffee {font-size:200px}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-red w3-card w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-red" href="javascript:void(0);" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
    <a href="file:///C:/Users/SAMSUNG/Desktop/RoboCarHTML/index.html" class="w3-bar-item w3-button w3-padding-large w3-white">Home</a>
    <a href="file:///C:/Users/SAMSUNG/Desktop/RoboCarHTML/Football.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">Football</a>
    <a href="file:///C:/Users/SAMSUNG/Desktop/RoboCarHTML/Follow%20the%20Line..html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">The Line</a>
    <a href="file:///C:/Users/SAMSUNG/Desktop/RoboCarHTML/User%20Interface.html" class="w3-bar-item w3-button w3-hide-small w3-padding-large w3-hover-white">User Interface</a>
  </div>
  

  <!-- Navbar on small screens -->
  <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
    <a href="#" class="w3-bar-item w3-button w3-padding-large">Football</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">The Line</a>
    <a href="#" class="w3-bar-item w3-button w3-padding-large">User Interface</a>
  </div>
</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:128px 16px">
  <h1 class="w3-margin w3-jumbo">USER INTERFACE</h1>
  <button class="w3-button w3-black w3-padding-large w3-large w3-margin-top">Take Control.</button>
</header>


<!-- Footer -->
<footer class="w3-container w3-padding-64 w3-center w3-opacity">  
  <div class="w3-xlarge w3-padding-32">
    <i class="fa fa-youtube w3-hover-opacity"></i>
 </div>
 <p>Powered by TEAM6</a></p>
</footer>

<script>
// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}


document.onkeydown = function(event) {
	var key_press = String.fromCharCode(event.keyCode);
	var key_code = event.keyCode;
	document.getElementById('kp').innerHTML = key_press;
    document.getElementById('kc').innerHTML = key_code;
	var status = document.getElementById('status');
	status.innerHTML = "DOWN Event Fired For : "+key_press;
}
document.onkeyup = function(event){
    var key_press = String.fromCharCode(event.keyCode);
	var status = document.getElementById('status');
	status.innerHTML = "UP Event Fired For : "+key_press;
}
</script>
<form method="post">
<button name="Forward">Forward</button>
<form method="post">
<button name="Backward">Backward</button>
<form method="post">
<button name="Left">Left</button>
<form method="post">
<button name="Right">Right</button>
<form method="post">
<button name="Stop">Stop</button>

</body>
</html>