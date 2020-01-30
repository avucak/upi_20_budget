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
  width: 110;
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

.inputClass {
margin: 5px;
}

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>

<script>
function checkBoxCheckAll(){
	if (document.getElementById(0).checked){
		% for cat in categories:
			document.getElementById({{cat[0]}}).checked=true;
		% end
		}
	checkedAll=true;
	% for cat in categories:
		if (document.getElementById({{cat[0]}}).checked==false){checkedAll=false;}
	% end
	if(checkedAll && !document.getElementById(0).checked)
	{
		% for cat in categories:
			document.getElementById({{cat[0]}}).checked=false;
		% end
	}
	
}

function checkBoxChecking(){
	
	allChecked=true;
	% for cat in categories:
		if(document.getElementById({{cat[0]}}).checked==false) {allChecked = false;}
	% end
	
		
	if(allChecked) {document.getElementById(0).checked=true;}
	else {document.getElementById(0).checked=false;}
	
	if (document.getElementById(0).checked){
		% for cat in categories:
			document.getElementById({{cat[0]}}).checked=true;
		% end
		}
}
	


function checkBoxFill(){

	% for cat in categories:
		% if cat in checkedCategories:
		console.log({{cat[0]}});
			document.getElementById("{{cat[0]}}").checked=true;
		% else:
			document.getElementById("{{cat[0]}}").checked=false;
			document.getElementById("0").checked=false;
		% end
	% end	

}
</script>



<body>
  <div class="divFrame">
      <form action="/overview/show" method="post">
	<h2>Overview options</h2>
        <br> Start date: <input type="date" class="inputClass" name="minDate" value={{minDate}}>
        <br> End date: <input type="date" class="inputClass" name="maxDate" value={{maxDate}}>
        <p>Categories included</p>
        <label><input type="checkbox" name="checkboxAll" id="0" value="all" checked onclick="checkBoxCheckAll()">All</label>
        % for cat in categories:
          <label><input type="checkbox" name="{{cat[1]}}" id="{{cat[0]}}" value="{{cat[0]}}" checked onclick="checkBoxChecking()">{{cat[1]}}</label>
        % end
		<br><br>
        <input type="submit" class="button"  style="display:inline-block;margin:0" value="Show transactions" >
        <input type="submit" class="button" formaction="/overview/report" style="display:inline-block" value="Create report">
	  </form>
      
      <form action=".." method="get">
        <input type="submit" class="button" value="Discard">
      </form>
	  <p style="color: red"> File {{fileName}} was succesfully created! </p>
  </div>
</body>