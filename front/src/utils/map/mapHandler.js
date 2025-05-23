
let markers = []

export const clearMarkers = () => {
    markers.forEach(marker => marker.setMap(null))
    markers = []
}

export const searchPlace = (map, keyword) => {
    return new Promise((resolve, reject) => {
        const ps = new kakao.maps.services.Places()

        clearMarkers()

        ps.keywordSearch(keyword, (results, status) => {
            if (status !== kakao.maps.services.Status.OK) {
                reject('검색 결과가 없습니다.')
                return
            }

            const bounds = new kakao.maps.LatLngBounds()

            results.forEach((place) => {
                const coords = new kakao.maps.LatLng(place.y, place.x)
                const marker = new kakao.maps.Marker({
                    map: map,
                    position: coords
                })

                markers.push(marker)
                bounds.extend(coords)
            })

            map.setBounds(bounds)
            resolve(results)
        })
    })
} 
