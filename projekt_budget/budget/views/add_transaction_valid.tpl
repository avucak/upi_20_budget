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

.inputClass {
margin: 5px;
}
form{ display: inline-block; }
</style>

<script>

</script>


<html>
  <body>
    <center>
    <div class="divFrame">
      <form method="post">
        Transaction name: <input type="text" name="transactionName" value={{name}}>
	<p style="color:red">{{ validation.get("name", "") }} </p>
        <br>
        Category: <select name="transactionCategory" class="inputClass" value={{category}}>
        % for cat in categories:
        <option value="{{cat[1]}}">{{cat[1]}}</option>
        % end
        </select>
	<p style="color:red">{{ validation.get("category", "") }} </p>
        <br>
        Amount: <input class="inputClass" type="number" name="transactionAmount" step="0.01" value={{amount}}>
	<p style="color:red">{{ validation.get("amount", "") }} </p>
        <br>
        Date: <input class="inputClass"  type="date" name="transactionDate" id="transactionDate" value={{date}}>
	<p style="color:red">{{ validation.get("date", "") }} </p>
        <br>
        Note: <br><textarea cols="30" rows="5" class="inputClass"  type="text" name="TransactionNote" value={{note}}></textarea>
        <br><br>
        <input type="submit" class="button" name="addTransaction" value="Add">
      </form>
      <form action="/transactions" method="get"><input type="submit" class="button" name="discardTransaction" value="Discard"></form>
    </div>
    </center>
  </body>
</html>