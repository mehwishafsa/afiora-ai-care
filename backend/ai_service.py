import os
from typing import Optional


def gemini_available() -> bool:
    """Check if Gemini API key is available."""
    return bool(os.getenv("GEMINI_API_KEY", "").strip())


def groq_available() -> bool:
    """Check if Groq API key is available."""
    return bool(os.getenv("GROQ_API_KEY", "").strip())


def selected_provider() -> str:
    """Get the selected AI provider from environment."""
    return os.getenv("AI_PROVIDER", "auto").lower()


def call_gemini(prompt: str, language: str) -> str:
    """
    Call Gemini API.
    TODO: Implement actual Gemini API integration using google-generativeai
    """
    return "[Gemini Response Placeholder] Your query has been received and will be processed."


def call_groq(prompt: str, language: str) -> str:
    """
    Call Groq API.
    TODO: Implement actual Groq API integration using groq library
    """
    return "[Groq Response Placeholder] Your query has been received and will be processed."


def fallback_response(prompt: str, language: str, reason: Optional[str] = None) -> str:
    """
    Generate a fallback response when AI is unavailable.
    
    Args:
        prompt: The user's query
        language: Language code (e.g., 'en', 'hi')
        reason: Optional reason for fallback
        
    Returns:
        A helpful fallback message
    """
    reason_text = f" [{reason}]" if reason else ""
    
    if language.startswith("hi"):
        base_message = (
            "नमस्ते। यह एक डेमो प्रतिक्रिया है। "
            "AI सेवा अभी उपलब्ध नहीं है, लेकिन हम आपकी मदद करने की कोशिश कर रहे हैं। "
            "कृपया अपनी स्वास्थ्य सेवा आवश्यकताओं के बारे में हमें बताएं।"
        )
        return f"{base_message}{reason_text}"
    else:
        base_message = (
            "Hello. This is a demo response. "
            "AI service is currently unavailable, but we're here to help. "
            "Please share your healthcare accessibility needs and we'll do our best to assist you."
        )
        return f"{base_message}{reason_text}"


def get_ai_response(prompt: str, language: str = "en") -> str:
    """
    Main function to get AI response with automatic fallback.
    
    Args:
        prompt: User's input prompt
        language: Language code (default: 'en')
        
    Returns:
        AI response or fallback message
    """
    provider = selected_provider()
    
    if provider == "none":
        return fallback_response(prompt, language, reason="AI disabled")
    
    if provider == "gemini":
        if gemini_available():
            try:
                return call_gemini(prompt, language)
            except Exception as e:
                return fallback_response(prompt, language, reason=f"Gemini error: {str(e)}")
        else:
            return fallback_response(prompt, language, reason="Gemini key missing")
    
    if provider == "groq":
        if groq_available():
            try:
                return call_groq(prompt, language)
            except Exception as e:
                return fallback_response(prompt, language, reason=f"Groq error: {str(e)}")
        else:
            return fallback_response(prompt, language, reason="Groq key missing")
    
    if provider == "auto":
        if gemini_available():
            try:
                return call_gemini(prompt, language)
            except Exception as e:
                return fallback_response(prompt, language, reason=f"Gemini error: {str(e)}")
        elif groq_available():
            try:
                return call_groq(prompt, language)
            except Exception as e:
                return fallback_response(prompt, language, reason=f"Groq error: {str(e)}")
        else:
            return fallback_response(prompt, language, reason="No API keys configured")
    
    return fallback_response(prompt, language, reason=f"Unknown provider: {provider}")