
var mymap = L.map('mapid').setView([12.943072,77.696665], 14);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox.streets'
}).addTo(mymap);

var closePopUp = mymap.closePopup();

L.marker([12.943072, 77.696665],13).addTo(mymap).on('mouseover', onMapOver1).on('mouseout',closePopUp);

L.marker([12.943502, 77.702943]).addTo(mymap).on('mouseover', onMapOver2).on('mouseout',closePopUp);

L.marker([12.941210, 77.696719]).addTo(mymap).on('mouseover', onMapOver3).on('mouseout',closePopUp);

L.marker([12.947763, 77.696576]).addTo(mymap).on('mouseover', onMapOver4).on('mouseout',closePopUp);

L.marker([12.939517, 77.696076]).addTo(mymap).on('mouseover', onMapOver5).on('mouseout',closePopUp);


L.circle([12.943072, 77.696665], 1000, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5
}).addTo(mymap).bindPopup("I am a circle.");


var popup = L.popup();
var name1 = "Dragon Momos";

function onMapOver1(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Dragon Momos [ Rating -6.5 ] ")
        .openOn(mymap);
}

function onMapOver2(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Pooja Tailor [rating -9.5]")
        .openOn(mymap);
}

function onMapOver3(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Sabji Ghar [Rating - 3.2]")
        .openOn(mymap);
}
function onMapOver4(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Deep Tea Stall [rating -8]")
        .openOn(mymap);
}

function onMapOver5(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Abhi da Dhaba [Rating - 7.8]")
        .openOn(mymap);
}

// mymap.on('click', onMapOver);