$(document).ready(function(){
  $(".default_option").click(function(){
    $(this).parent().toggleClass("active");
  })
  
  $(".default_option label").click(function(){
    $(".default_option").parent().toggleClass("active");
  })

  $(".sortby .select_ul label").click(function(){
    var currentsort = $(this).html();
    $(".sortby .default_option label").html(currentsort);
    $(this).parents(".sortby.select_wrap").removeClass("active");
  })
  const dropDown = document.querySelector(".sortby.select_wrap");
  $(".sortby .select_ul label").click(function(){
    var currentsort = $(this).html();
    $(".sortby .default_option li").html(currentsort);
    dropDown.classList.remove("active");
  })


});

$(function(){
  $('#todo_list').slimScroll({
    position: "right",
    size: "5px",
    height: "315px",
    color: "transparent"
  });

  $('#notifications').slimScroll({
    position: "right",
    size: "5px",
    height: "315px",
    color: "transparent"
  });
});

function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}


$(document).ready(function() {
  $('.searchname').keydown(function(event) {
      if (event.which == 13) {
          this.form.submit();
          event.preventDefault();
       }
  });
});
$(document).ready(function() { 
  document.getElementById("defaultOpen").click();
});

document.getElementById("id_image").onchange = function () {
  var reader = new FileReader();

  reader.onload = function (e) {
      // get loaded data and render thumbnail.
      document.getElementById("imageuploaded").src = e.target.result;
  };

  // read the image file as a data URL.
  reader.readAsDataURL(this.files[0]);
};