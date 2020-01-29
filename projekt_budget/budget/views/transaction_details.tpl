<html>
<style>
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
  width: 340px;
  padding: 50px;
  margin: 0 auto;
  font-size: 17px;
}

.button {
  background-color: #69359c;
  width: 100;
  height: 40;
  border: none;
  color: white;
  padding: 2px 2px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border: 1px solid black;
  border-color: #322a4f;
  font-family: "Times New Roman", Times, serif;
}


body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}

p {
  display: inline;
}
</style>



<body>
	<div class="divFrame">
		<form action="/transactions" method="get"> <input type="submit" class="button" name="go_back" value="Back">
		</form>
		<div name="details">
		<hr>
		<h2> {{transaction[1]}} </h2>
		<hr>
		<b>Category:</b> <p>{{category}}</p> 
		<br><br>
		<b>Amount:</b> <p>{{transaction[3]}}</p>
		<br><br>
		<b>Date:</b> <p>{{transaction[4]}}</p>
		<br><br>
		<b> Note: </b> 
		<br>
		<p>{{transaction[5]}}</p>
		
		</div>
	</div>
</body>

</html>