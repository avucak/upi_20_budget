<style>
.divFrame{
  resize: both;
  overflow: auto;
  text-align: center;
  background-color: #F2F7FB;
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

body {
  background-image: url("https://images.unsplash.com/photo-1496167117681-944f702be1f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1789&q=80");
  background-size: 100% 100%;
}
</style>
<head>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
var chartData={{pieChartData}};
for(var i=0; i<chartData.length; i++){
chartData[i][0]=document.getElementById("hidden".concat(chartData[i][0].toString())).value;
chartData[i][1]=chartData[i][1];
}
chartData=[["Category", "Percentage"]].concat(chartData)
var data = google.visualization.arrayToDataTable(chartData);
var options = {'title':'Budget breakdown', 'width':280, 'height':300, backgroundColor: 'transparent', 'legend':'top', chartArea:{top:40,width:"100%",height:"100%"}};


var chart = new google.visualization.PieChart(document.getElementById('piechart'));
chart.draw(data, options);

}
</script>


</head>



<body>
  <div class="divFrame">
    <form action=".." method="get"> <input type="submit" class="button" name="go_back" value="Back"></form>
	
	<br>
	<br>
	<br>
	<center><div id="piechart"></div> </center>
	
	<br><br>
    <div>
      % for cat in checkedCategories:
		<hr>
		<input type="hidden" id="hidden{{cat[0]}}" value="{{cat[1]}}">
		<h4>{{cat[1]}}</h4>
		<hr>
      % for trans in transactions:
      % if trans[2]==cat[0]:
        <div class="panel-body" id="trans{{trans[0]}}"> {{trans[1]}}  {{trans[3]}}  {{trans[4]}} 
        </div>
      % end
      % end
      <p>Category total: {{totalSum[cat[0]-1]}}</p>
	  <p>Percentage: {{'%.2f' % (totalAverage[cat[0]-1]*100)}} %</p>
      % end
	  <hr>
      <h3>Total: {{sum(totalSum)}}</h3>
    </div> 
  </div>
</body>