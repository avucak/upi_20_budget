<style>
.divFrame {
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #fffdd0;
  width: 310px;
  padding: 50px;
}
.button {
  background-color: #69359c; 
  width: 100;
  height: 40;
  border: none;
  color: white;
  padding: 2px 2px;
  margin: 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
}
</style>


<html>
<body>
<center>
<div class="divFrame">
<h1 style="color:#322a4f"> budget.IO </h1>
<form action="transactions" method="get">
<input type="submit" class="button" name="transaction" value="Transactions">
</form>

<form action="categories" method="get">
<input type="submit" class="button" name="category" value="Categories">
</form>


<form action="overview" method="get">
<input type="submit" class="button" name="overview" value="Overview">
</form>

<input type="submit" class="button" name="exit" value="Exit">

</div>
</body>
</html>