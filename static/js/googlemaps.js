function initMap(iconBase) {
    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
    });

    var weddingAddress = document.getElementById('wedding-address').value;
    var partyAddress = document.getElementById('party-address').value;

    var icons = {
        church: {
            icon: iconBase + 'church-2.png'
        },
        party: {
            icon: iconBase + 'party-2.png'
        }
    };

    drawMarker(partyAddress, icons['party']);
    drawMarker(weddingAddress, icons['church']);

    function drawMarker(address, icon){
        geocoder.geocode({'address': address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                var markerPosition = results[0].geometry.location;
                var marker = new google.maps.Marker({
                    map: map,
                    position: markerPosition,
                    icon: icon.icon
                });
                map.setCenter(markerPosition);
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
}