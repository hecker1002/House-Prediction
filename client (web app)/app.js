
function estimate() {

    event.preventDefault()

    // Keep all the input var (coming from client web browser inside <form> tag)
    var sqft = document.getElementById("_1").value;
    var location = document.getElementById("_2").value;

    var bhk = document.getElementById("_3").value;

    var bath = document.getElementById("_4").value;
   
    var price = document.getElementById("ar");

    var url = "http://127.0.0.1:5000/predict_home_price"
  
    var data = {
        total_sqft: parseFloat(sqft),
        location: location,
        
        bhk: bhk,
        bath: bath
    };

    // this is a syntax to send request to flask server (POST) and get response and function(response) sees how to deal with response 
   $.post( url , data , function(response){

    price.innerHTML = response.estimated_price.toString() + "  Lakhs"
   })

}

