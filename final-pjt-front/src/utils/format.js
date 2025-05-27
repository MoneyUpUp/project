export function formatDistance(distance) {
    if (distance == null) return '거리 정보 없음'
    return distance >= 1000
        ? `${(distance / 1000).toFixed(2)} km`
        : `${distance} m`
}