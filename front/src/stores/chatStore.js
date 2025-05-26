import { ref, reactive } from 'vue'
import { defineStore } from 'pinia'
import { sendChatMessage } from '@/utils/chat'

export const useChatStore = defineStore('chat', () => {
    const isChatOpen = ref(false)
    const selectedStyle = ref(null)
    const input = ref('')
    const messages = reactive([])
    const isLoading = ref(false) // ✅ 로딩 상태

    const toggleChat = () => {
        isChatOpen.value = !isChatOpen.value
    }

    const selectStyle = (styleKey) => {
        selectedStyle.value = styleKey
        messages.splice(0)
        input.value = ''
    }

    const sendMessage = async () => {
        if (!input.value.trim()) return

        const userMsg = input.value
        messages.push({ role: 'user', content: userMsg })
        input.value = ''

        isLoading.value = true
        messages.push({ role: 'assistant', content: '...' }) // ✅ 임시 로딩 메시지

        const style = selectedStyle.value || 'default'
        const response = await sendChatMessage(style, userMsg)

        // 로딩 메시지 삭제 + 실제 응답 추가
        messages.pop()
        messages.push({ role: 'assistant', content: response.answer })

        isLoading.value = false
    }

    return {
        isChatOpen,
        selectedStyle,
        input,
        messages,
        isLoading,
        toggleChat,
        selectStyle,
        sendMessage,
    }
})
