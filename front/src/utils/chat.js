// utils/chat.js
import axios from 'axios'
import { useAccountStore } from '@/stores/accounts'

export const sendChatMessage = async (style, message) => {
    const account = useAccountStore()
    const token = account.token

    console.log('🔥 전송할 메시지:', message) // 👉 이거 찍어보자

    try {
        const response = await axios.post(
            `http://127.0.0.1:8000/ai/chat/${style}/`,
            { message: message },
            {
                headers: {
                    Authorization: `Token ${token}`,
                },
            }
        )
        return response.data
    } catch (error) {
        console.error('❌ 챗봇 에러:', error)
        if (error.response) {
            console.error('🔍 서버 응답:', error.response.data)
        }
        return { content: '⚠️ 챗봇 응답에 실패했어요.' }
    }
}
