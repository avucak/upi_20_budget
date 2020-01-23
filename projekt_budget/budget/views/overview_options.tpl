<style>
div2 {
  resize: both;
  overflow: auto;
  background-color: #8b72be;
  padding: 50 px;
}
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #fffdd0;
  width: 310px;
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
</style>

<script>
</script>



<body>
  <div class="divFrame">
      <form action="/overview/show" method="post">
	<h2>Overview options</h2>
        <br> Start date: <input type="date" class="inputClass" name="minDate" value={{minDate}}>
        <br> End date: <input type="date" class="inputClass" name="maxDate" value={{maxDate}}>
        <p>Categories included</p>
        <label><input type="checkbox" name="checkboxAll" id="0" value="all" checked>All</label>
        % for cat in categories:
          <label><input type="checkbox" name="{{cat[1]}}" id="{{cat[0]}}" value="{{cat[0]}}" checked>{{cat[1]}}</label>
        % end
	<br><br>
        <input type="submit" class="button" style="display:inline-block;margin:0" value="Show transactions" >
        <input type="submit" class="button" style="display:inline-block" value="Create report">
      </form>
      <form action=".." method="get">
        <input type="submit" class="button" value="Discard">
      </form>
  </div>
</body>