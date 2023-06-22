
  // Fetch user locations from the API endpoint
  fetch('/api/user-locations/')
    .then(response => response.json())
    .then(userLocations => {
      // Initialize the map
      var map = L.map('map').setView([your_latitude, your_longitude], your_zoom_level);

      // Add the tile layer (optional)
      L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=' + accessToken, {
      attribution: 'Map data &copy; <a href="https://www.mapbox.com/">Mapbox</a>',
      id: 'mapbox/streets-v11', // Replace with your desired Mapbox style
      tileSize: 512,
      zoomOffset: -1
  }).addTo(map);

      // Add markers with popups for each user location
      userLocations.forEach(function(location) {
        var marker = L.marker([location.lat, location.lng]).addTo(map);
        marker.bindPopup('<h3>' + location.name + '</h3>');
      });
    });

