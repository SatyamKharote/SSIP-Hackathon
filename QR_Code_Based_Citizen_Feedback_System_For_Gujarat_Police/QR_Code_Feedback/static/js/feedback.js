$(document).ready(function(){
  $(".choice").on("click", function () {
    var $this = $(this);
  
    $(".reaction").removeClass("reaction-fade-in");
    $(".emoji").removeClass("emoji-selected");
    $this.find(".reaction").addClass("reaction-fade-in");
    $this.find(".emoji").addClass("emoji-selected");
  });
  
  $("#question-1 .choice").on("click", function () {
    var ranking1 = $(this).attr("data-value");
  
    $(".answer-submit").on("click", function () {
      sessionStorage.setItem("ranking1", ranking1);
      $("#question-2").removeClass("hide");
      $("#question-1").addClass("hide");
    });
  });
  
  $("#question-2 .choice").on("click", function () {
    var ranking2 = $(this).attr("data-value");
  
    $(".answer-submit").on("click", function () {
      sessionStorage.setItem("ranking2", ranking2);
      $("#question-3").removeClass("hide");
      $("#question-2").addClass("hide");
    });
  });
  
  $("#question-3 .choice").on("click", function () {
    var ranking3 = $(this).attr("data-value");
  
    $(".answer-submit").on("click", function () {
      sessionStorage.setItem("ranking3", ranking3);
      $("#question-3").addClass("hide");
      $(".summary").removeClass("hide");
  
      var total;
  
      function calculateTotal() {
        var ranking1 = sessionStorage.getItem("ranking1");
        var ranking2 = sessionStorage.getItem("ranking2");
        var ranking3 = sessionStorage.getItem("ranking3");
        var total = parseInt(ranking1) + parseInt(ranking2) + parseInt(ranking3);
  
        if (total >= 14) {
          $("#amazing").removeClass("hide");
        } else if (total < 14 && total > 10) {
          $("#good").removeClass("hide");
        } else if (total < 11 && total > 7) {
          $("#okay").removeClass("hide");
        } else if (total < 8 && total > 4) {
          $("#disappointing").removeClass("hide");
        } else {
          $("#terrible").removeClass("hide");
        }
      }
  
      // if (total > 13) {
      //   $('#amazing').removeClass('hide');
      // }
  
      calculateTotal();
    });
  });
  
});
