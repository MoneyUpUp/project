
let markers = []
function getDistance(lat1, lng1, lat2, lng2) {
  const R = 6371e3; // 지구 반지름 (m)
  const φ1 = lat1 * Math.PI / 180;
  const φ2 = lat2 * Math.PI / 180;
  const Δφ = (lat2 - lat1) * Math.PI / 180;
  const Δλ = (lng2 - lng1) * Math.PI / 180;

  const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
    Math.cos(φ1) * Math.cos(φ2) *
    Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return Math.round(R * c); // 단위: meter
}

export const clearMarkers = () => {
  markers.forEach(marker => marker.setMap(null))
  markers = []
}
export function searchPlace(map, keyword, myLatLng, callback) {
  const ps = new kakao.maps.services.Places();
  const markers = [];

  ps.keywordSearch(keyword, (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const results = data.map(place => {
        const position = new kakao.maps.LatLng(place.y, place.x);
        const marker = new kakao.maps.Marker({ map, position });
        markers.push(marker);

        const distance = myLatLng
          ? getDistance(myLatLng.getLat(), myLatLng.getLng(), parseFloat(place.y), parseFloat(place.x))
          : null;

        return {
          name: place.place_name,
          address: place.road_address_name || place.address_name,
          lat: place.y,
          lng: place.x,
          url: place.place_url,
          distance: distance
        };
      });

      const bounds = new kakao.maps.LatLngBounds();
      results.forEach(place =>
        bounds.extend(new kakao.maps.LatLng(place.lat, place.lng))
      );
      map.setBounds(bounds);

      callback(results);
    } else {
      callback([]);
    }
  });
}
