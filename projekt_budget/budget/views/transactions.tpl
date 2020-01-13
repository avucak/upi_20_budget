<style>
div {
  resize: both;
  overflow: auto;
  background-color: #8b72be;
  padding: 50 px;
}
.button {
  background-color: #69359c; /* Purple */
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
}
form{ display: inline-block; }
</style>

<script>
function showFilter(){
var block=document.getElementById("divFilter");
if(block.style.display ==="none")
{block.style.display="block";}
else
{block.style.display="none";}
}
</script>



<body bgcolor="#fffdd0">
<form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>

<form action="/addtransaction" method="get"> <input type="submit" class="button" name="add_transaction" value="Add transaction"></form>
<input type="submit" class="button" name="filter_transaction" value="Filter transactions" onclick="showFilter()">


<br>
<form action="/sorttransactions" method="get"> <input type="submit" class="button" name="sort_transaction" value="Sort transactions"></form>
<select>
  <option value="volvo">Lowest amount first</option>
  <option value="saab">Highest amount first</option>
  <option value="mercedes">Oldest transaction first</option>
  <option value="audi">Newest transaction first</option>
</select>

<div id="divFilter" style="display: none;">
<input type="checkbox" name="food">All<input type="checkbox" name="food">Food <input type="checkbox" name="food">Rent <input type="checkbox" name="food">Clothes
<br> Min:<input type="text">   Max:<input type="text">
<br>Start date: <input type="date" value="2018-12-01">   End date:<input type="date" value="2018-12-31">
<input type="submit" class="button" name="applyFilter" value="Apply">
<input type="submit" class="button" name="removeFilter" value="Remove">
</div>


<br>
<hr>
<br>
<input type="month" value="2019-12">


<div class="panel panel-default">
% for i in range(5):
<div class="panel-body" id="trans{{i}}">Transakcija {{i}} <button class="button" style="width:50; height:25;">Edit</button> <button class="button" style="width:50; height:25;">Delete</button> </div>
<br>
% end
</div> 
</body>