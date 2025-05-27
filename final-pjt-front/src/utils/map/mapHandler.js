
let markers = [] // 전역 마커 배열
let infowindow = null // 단일 정보창을 관리하기 위한 변수

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
  if (infowindow) {
    infowindow.close()
    infowindow = null
  }
}

export function searchPlace(map, keyword, myLatLng, callback) {
  const ps = new kakao.maps.services.Places();
  clearMarkers(); // 새로운 검색 전에 기존 마커와 정보창 제거

  ps.keywordSearch(keyword, (data, status) => {
    if (status === kakao.maps.services.Status.OK) {
      const results = data.map(place => {
        const position = new kakao.maps.LatLng(place.y, place.x);
        const marker = new kakao.maps.Marker({ map, position });
        markers.push(marker); // 전역 markers 배열에 추가

        // 마커에 클릭 이벤트 추가
        kakao.maps.event.addListener(marker, 'click', function () {
          displayPlaceInfo(map, place);
        });

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

export function displayPlaceInfo(map, place) {
  // 기존 정보창이 있다면 닫기
  if (infowindow) {
    infowindow.close();
  }

  const position = new kakao.maps.LatLng(place.y, place.x);
  let targetMarker = null;

  // 기존 markers 배열에서 해당 place의 마커를 찾습니다.
  // searchPlace 함수에서 markers.push(marker)를 통해 마커가 추가되었으므로,
  // 이 배열에서 찾을 수 있습니다.
  for (let i = 0; i < markers.length; i++) {
    const markerPosition = markers[i].getPosition();
    if (markerPosition.getLat() === position.getLat() && markerPosition.getLng() === position.getLng()) {
      targetMarker = markers[i];
      break;
    }
  }

  // 해당 마커를 찾지 못했다면 새로 생성합니다. (예: 검색 결과가 아닌 경우)
  if (!targetMarker) {
    targetMarker = new kakao.maps.Marker({ map: map, position: position });
    // 새로 생성된 마커는 markers 배열에 추가하지 않습니다.
    // 왜냐하면 이 마커는 리스트 클릭 시에만 임시로 사용될 수 있기 때문입니다.
    // 만약 이 마커도 관리해야 한다면 markers.push(targetMarker)를 추가해야 합니다.
  }

  const iwContent = `
    <div style="padding:5px;font-size:12px;">
      <b>${place.place_name}</b><br>
      ${place.road_address_name || place.address_name}<br>
      <a href="${place.place_url}" target="_blank" style="color:blue">상세보기</a>
    </div>
  `;

  infowindow = new kakao.maps.InfoWindow({
    map: map,
    position: position,
    content: iwContent,
    removable: true
  });

  map.setCenter(position); // 지도 중심 이동
  infowindow.open(map, targetMarker); // 정보창 열기
}
