$(document).ready(function(){
    $('#login').click(function(){
        window.location.href = '/login.html';
    })
})

/*var myModal = new bootstrap.Modal(document.getElementById('#profile-popup'), options)
console.log(myModal)*/

function myMap() {
    var mapProp= {
      center:new google.maps.LatLng(51.508742,-0.120850),
      zoom:5,
    };
    var map = new google.maps.Map(document.getElementById("google-maps"),mapProp);
}