<html>

<style>
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
  width: 400px;
  padding: 50px;
  margin: 0 auto;
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
  font-family: "Times New Roman", Times, serif;
}

.buttonSmaller {
  background-color: #69359c; /* Purple */
  width: 50;
  height: 25;
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

td {
  text-align: center;
  padding-top: 4px;
  padding-bottom: 4px;
}

form{ display: inline-block; }
.inputClass {
margin: 5px;
}

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>

<script>
function showFilter(){
  var block=document.getElementById("divFilter");
  if(block.style.display === "none")
  { block.style.display="inline-block"; }
  else
  { block.style.display="none"; }
}

function showDiv(id){
  document.getElementById(id).style.display="block";
}

function hideDiv(id){
  document.getElementById(id).style.display="none";
}


function checkboxAndSelect(){
  if ({{sum(categoriesChecked)}}>0){
	  var i;
    for (i = 0; i < {{categoriesChecked}}.length; i++) {
		  if ({{categoriesChecked}}[i]==1) { document.getElementById(i).checked=true;}
	  }
  }
  document.getElementById("{{option}}").selected=true;
}
</script>



<body onload="checkboxAndSelect()">
  <div class="divFrame">
  <center>
    <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>
    <form action="/transactions/add" method="get"> <input type="submit" class="button" name="add_transaction" value="Add transaction"></form>
    <input type="button" class="button" name="filter_transaction" value="Filter transactions" onclick="showFilter()">
    <form action="/transactions" method="post" name="formSort">
       <input type="hidden" name="action" value="sortFilter">
       <input type="hidden" name="filtered" value="{{filtered}}">
       <input type="hidden" name="sorted" value="{{sort}}">
	     <input type="submit" class="button" name="actionButton" value="Sort">
       <select id ="sortOption" name="sortOption" value="{{option}}">
	     <option value="other" id ="other">no sort</option>
         <option value="lowest" id="lowest">Lowest amount first</option>
         <option value="highest" id="highest">Highest amount first</option>
         <option value="oldest" id="oldest">Oldest transaction first</option>
         <option value="newest" id="newest">Newest transaction first</option>
       </select>
       <div id="divFilter" style="display: none;">
	   <br>
           <label><input type="checkbox" name="checkboxAll" id="0" value="all">All</label>
           % for cat in categories:
             <label><input type="checkbox" name="{{cat[1]}}" id="{{cat[0]}}" value="{{cat[0]}}">{{cat[1]}}</label>
           % end
           <br> Min: <input type="number" class="inputClass" name="minAmount" step="0.01" value={{minAmount}}>
           <br> Max: <input type="number" class="inputClass"  name="maxAmount" step="0.01" value={{maxAmount}}>
           <br> Start date: <input type="date" class="inputClass" name="minDate" value={{minDate}}>
           <br> End date: <input type="date" class="inputClass" name="maxDate" value={{maxDate}}>
           <br> <input type="submit" class="button" name="actionButton" style="display:inline-block;margin:0" value="Apply" >
     </form>
       <form action="/transactions" method="get">
         <input type="hidden" name="optionSort" value="{{option}}">
         <input type="submit" class="button" name="removeFilter" style="display:inline-block" value="Remove">
       </form>
      </div>

    <br>
    <hr>
	<h2> Transactions </h2>
	<hr>
    <div class="panel panel-default">
      <table>
         <tr>
           <th>Name</th>
           <th>Amount</th>
           <th>Date</th>
         </tr>
       % for trans in transactions:
       <tr>
          <div class="panel-body" id="trans{{trans[0]}}">
           <td><a href="/transactions/{{trans[0]}}" style="color:#69359c;">{{trans[1]}}</a></td> 
		   <td>{{trans[3]}} </td>  
		   <td style="width:80px">{{trans[4]}}</td>

             <form action="/transactions/edit/{{trans[0]}}"  style="margin:5 !important" method="get">
                <td><input type="submit" class="buttonSmaller" value="Edit"></td>
             </form>
              <td><input type="button" class="buttonSmaller" value="Delete" onclick='showDiv("div{{trans[0]}}Delete")'></td>
         </div>
      </tr>
      <tr>
      <td colspan="5">
        <div style="display:none" id="div{{trans[0]}}Delete"> Are you sure you want to delete transaction {{trans[1]}}?
		<br>
          <form action="/transactions" method="post" >
             <input type="hidden" name="action" value="delete">
             <input type="hidden" name="transactionId" value="{{trans[0]}}">
             <input type="submit" class="button" style="width:50; height:25;"  value="Yes">
           </form>
           <input type="button" class="buttonSmaller" value="No" onclick="hideDiv('div{{trans[0]}}Delete')">
         </div>
        </td>
      </tr>
      % end
      </table>
    </div>
	</center>
  </div>
</body>

</html>