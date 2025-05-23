
const appkey = import.meta.env.VITE_MAP_JS_API_KEY

export const loadKakaoMap = () => {
    return new Promise((resolve, reject) => {
        if (window.kakao && window.kakao.maps) {
            resolve()
            return
        }

        const existingScript = document.querySelector('script[src*="kakao.com"]')
        if (existingScript) {
            existingScript.onload = resolve
            return
        }

        const script = document.createElement('script')
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${appkey}&libraries=services&autoload=false`
        script.onload = () => {
            window.kakao.maps.load(resolve)
        }
        script.onerror = reject
        document.head.appendChild(script)
    })
}
