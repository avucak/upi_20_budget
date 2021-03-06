<style>
.divFrame {
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
  width: 400px;
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

.inputClass {
  margin: 5px;
}

form { display: inline-block; }

.warning {
  display: none;
  color: red;
}

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>

<script>
function categoryWarning()
{
    if({{disable}}==false){
	document.getElementById("categoryWarning").style.display="none";
    }
    else {
	document.getElementById("addTransaction").disabled=true;
	document.getElementById("categoryWarning").style.display="block";
    }
		
}

</script>


<html>
  <body onload="categoryWarning()">
    <center>
    <div class="divFrame">
      <form action="/transactions/add" method="post">
        Transaction name: <input type="text" name="transactionName">
        <br>
        Category: <select name="transactionCategory" class="inputClass" >
        % for cat in categories:
        <option value="{{cat[1]}}">{{cat[1]}}</option>
        % end
        </select>
        <br>
        Amount: <input class="inputClass" type="number" name="transactionAmount" step="0.01" min="0">
        <br>
        Date: <input class="inputClass"  type="date" name="transactionDate" id="transactionDate">
        <br>
        Note: <br><textarea cols="30" rows="5" class="inputClass"  type="text" name="transactionNote"></textarea>
        <br><br>
        <input type="submit" class="button" name="addTransaction" id="addTransaction" value="Add">
	<p class="warning" id="categoryWarning">There must be at least one category to add a transaction </p>
      </form>
	  <br>
      <form action="/transactions" method="get"><input type="submit" class="button" name="discardTransaction" value="Discard"></form>
    </div>
    </center>
  </body>
</html>