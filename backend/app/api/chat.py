from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.api.auth import oauth2_scheme
from app.core.config import settings
import openai

router = APIRouter()

# Mock chat history database
chat_history = {}

class ChatMessage(BaseModel):
    content: str
    file_context: Optional[List[str]] = None

class ChatResponse(BaseModel):
    id: str
    content: str
    sender: str
    timestamp: str

class ChatHistoryResponse(BaseModel):
    messages: List[ChatResponse]

@router.post("/message", response_model=ChatResponse)
async def send_message(message: ChatMessage):
    """Send a message to the AI chat"""
    
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Prepare context
        context = "You are an AI assistant for NASA Space Apps AI Platform. You help users analyze space research documents, answer questions about space exploration, and provide insights about NASA missions and space technology."
        
        if message.file_context:
            context += f" The user has mentioned {len(message.file_context)} files in their query."
        
        # Call OpenAI API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message.content}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = completion.choices[0].message.content
        
    except Exception as e:
        print(f"OpenAI API error: {e}")
        # Fallback to diverse mock responses
        import random
        
        # Analyze the question content for more relevant responses
        content_lower = message.content.lower()
        
        if any(word in content_lower for word in ['compare', 'comparison', 'difference', 'vs', 'versus']):
            ai_response = f"Excellent question about comparing '{message.content}'! In space research, comparative analysis is crucial. Here's what I found: Different space technologies and methodologies each have unique advantages. The key is understanding the specific requirements and constraints of each mission or research objective. Would you like me to dive deeper into specific aspects of this comparison?"
        
        elif any(word in content_lower for word in ['analyze', 'analysis', 'examine', 'study']):
            ai_response = f"Great analytical question about '{message.content}'! Space research analysis involves multiple dimensions: technical feasibility, scientific value, resource requirements, and mission objectives. Based on NASA's research methodologies, here's my assessment: The data suggests several interesting patterns that could be valuable for your research. Would you like me to explore specific analytical approaches?"
        
        elif any(word in content_lower for word in ['mars', 'moon', 'planet', 'asteroid', 'comet']):
            ai_response = f"Fascinating question about '{message.content}'! Planetary exploration is a core focus of NASA's mission. Here's what I know: Each celestial body presents unique challenges and opportunities for research. The data from various missions shows interesting patterns that could inform future exploration strategies. Would you like me to discuss specific aspects of planetary science?"
        
        elif any(word in content_lower for word in ['rocket', 'engine', 'propulsion', 'fuel']):
            ai_response = f"Excellent technical question about '{message.content}'! Propulsion systems are fundamental to space exploration. Here's my analysis: Different propulsion technologies offer various trade-offs between thrust, efficiency, and complexity. NASA's research shows that the optimal choice depends on mission requirements and constraints. Would you like me to explain specific propulsion concepts?"
        
        elif any(word in content_lower for word in ['data', 'information', 'research', 'findings']):
            ai_response = f"Great question about '{message.content}'! Data analysis is crucial in space research. Here's what I found: NASA's research methodologies emphasize rigorous data collection, validation, and interpretation. The patterns in space data often reveal insights about fundamental physical processes. Would you like me to discuss specific data analysis techniques?"
        
        else:
            fallback_responses = [
                f"Great question about '{message.content}'! This relates to space exploration and NASA research. Let me analyze this for you...",
                f"Interesting query regarding '{message.content}'. Based on space research data, here's what I found...",
                f"Your question about '{message.content}' touches on important space technology concepts. Here's my analysis...",
                f"Fascinating topic '{message.content}'! This connects to NASA's mission objectives. Let me break it down...",
                f"Excellent question about '{message.content}'! This involves space science and exploration technology. Here's what I discovered...",
                f"Your inquiry about '{message.content}' relates to space research methodologies. Here's my assessment...",
                f"Interesting perspective on '{message.content}'! This aligns with space exploration goals. Let me explain...",
                f"Great question '{message.content}'! This involves space technology and research. Here's my analysis..."
            ]
            ai_response = random.choice(fallback_responses)
    
    response = ChatResponse(
        id=str(len(chat_history) + 1),
        content=ai_response,
        sender="ai",
        timestamp=datetime.now().isoformat()
    )
    
    # Store in history
    user_id = "current_user"  # Get from token in production
    if user_id not in chat_history:
        chat_history[user_id] = []
    
    chat_history[user_id].append({
        "id": str(len(chat_history[user_id]) + 1),
        "content": message.content,
        "sender": "user",
        "timestamp": datetime.now().isoformat()
    })
    
    chat_history[user_id].append(response.dict())
    
    return response

@router.get("/history", response_model=ChatHistoryResponse)
async def get_chat_history(token: str = Depends(oauth2_scheme)):
    """Get chat history for the current user"""
    user_id = "current_user"  # Get from token in production
    
    if user_id not in chat_history:
        return ChatHistoryResponse(messages=[])
    
    return ChatHistoryResponse(messages=chat_history[user_id])

@router.delete("/history")
async def clear_chat_history(token: str = Depends(oauth2_scheme)):
    """Clear chat history"""
    user_id = "current_user"  # Get from token in production
    
    if user_id in chat_history:
        chat_history[user_id] = []
    
    return {"message": "Chat history cleared"}

@router.post("/analyze")
async def analyze_with_ai(
    file_ids: List[str],
    query: str,
    token: str = Depends(oauth2_scheme)
):
    """Analyze multiple files with a specific query"""
    
    # TODO: Implement actual AI analysis with LangChain/OpenAI
    return {
        "query": query,
        "files_analyzed": len(file_ids),
        "insights": [
            "Common themes across documents identified",
            "Key data patterns extracted",
            "Recommendations generated based on analysis"
        ],
        "summary": "This is a mock analysis. Implement with actual AI integration."
    }

