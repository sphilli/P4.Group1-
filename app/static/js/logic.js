$(document).ready(function() {
  console.log("Page Loaded");

  $("#filter").click(function() {
      // alert("button clicked!");
      makePredictions();
  });
});


// call Flask API endpoint
function makePredictions() {
  var gender = $("#Gender").val();
  var own_car = $("#Own_car").val();
  var own_property = $("#Own_property").val();
  var unemployed = $("#Unemployed").val();
  var family_status = $("#Family_status").val();
  var education_type = $("#Education_type").val();
  var housing_type = $("#Housing_type").val();
  var income_type = $("#Income_type").val();
  var occupation_type = $("#Occupation_type").val();
  var age = $("#Age").val();
  var num_children = $("#Num_children").val();
  var num_family = $("#Num_family").val();
  var account_length = $("#Account_length").val();
  var total_income = $("#Total_income").val();
  var years_employed = $("#Years_employed").val();

  // check if inputs are valid

  // create the payload
  var payload = {
      "gender": gender,
      "own_car": own_car,
      "own_property": own_property,
      "unemployed": unemployed,
      "family_status": family_status,
      "education_type": education_type,
      "housing_type": housing_type,
      "income_type": income_type,
      "occupation_type": occupation_type,
      "age": age,
      "num_children": num_children,
      "num_family": num_family,
      "account_length": account_length,
      "total_income": total_income,
      "years_employed": years_employed
  }

  // Perform a POST request to the query URL
  $.ajax({
      type: "POST",
      url: "/makePredictions",
      contentType: 'application/json;charset=UTF-8',
      data: JSON.stringify({ "data": payload }),
      success: function(returnedData) {
          // print it
          console.log(returnedData);
          let pred = returnedData["prediction"]

          if (pred["loan_pred"] === "high_risk") {
              $("#output").text(`Sorry, you have not been approved at this time with a probability of ${(pred["prob_high_risk"]*100).toFixed(2)}%.`);
          } else {
              $("#output").text(`Congratulations! You have been conditionally approved with a probability of ${(pred["prob_low_risk"]*100).toFixed(2)}%.`);
          }

      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
          alert("Status: " + textStatus);
          alert("Error: " + errorThrown);
        }
    });

    }
