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
.inputClass {
margin: 5px;
}
</style>

<script>
</script>



<body>
  <div class="divFrame">
    <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>
    <div class="panel panel-default">
      % for cat in categories:
	<h4>{{cat[1]}}</h4>
      % for trans in transactions:
      % if trans[2]==cat[0]:
        <div class="panel-body" id="trans{{trans[0]}}"> {{trans[1]}}  {{trans[3]}}  {{trans[4]}} 
        </div>
      % end
      % end
      <p>Category total: Percentage: </p>
      % end
      <h3>Total:</h3>
    </div> 
  </div>
</body>