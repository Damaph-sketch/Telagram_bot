"""
DamaphAI - Advanced AI Module for Complex Educational Tasks
Powered by Google Gemini API
Handles: Homework help, Q&A, Explanations, Study assistance
"""

import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

# Initialize Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    logger.warning("GEMINI_API_KEY not found in environment variables")
    genai_initialized = False
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        genai_initialized = True
        logger.info("Gemini API initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Gemini API: {e}")
        genai_initialized = False


class DamaphAI:
    """
    Advanced AI assistant for Ethiopian student education
    Uses Google Gemini for intelligent responses
    """
    
    def __init__(self):
        self.model_name = "gemini-pro"
        self.initialized = genai_initialized
        
    def generate_response(self, prompt: str, subject: str = None) -> str:
        """
        Generate AI response for student queries
        
        Args:
            prompt: User question or query
            subject: Subject (Math, Science, etc.)
        
        Returns:
            AI-generated response
        """
        if not self.initialized:
            return "⚠️ AI service is currently unavailable. Please try again later."
        
        try:
            # Build context-aware prompt
            system_prompt = f"""You are DamaphAI, an intelligent study helper assistant for Ethiopian students.
Your role is to help students understand complex concepts in a simple, clear way.
Always provide explanations in both English and Amharic when possible.
Be encouraging and supportive.
"""
            
            if subject:
                system_prompt += f"\nSubject Focus: {subject}\n"
            
            full_prompt = system_prompt + f"\nStudent Question: {prompt}"
            
            # Generate response using Gemini
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(full_prompt)
            
            if response.text:
                return response.text
            else:
                return "❌ Could not generate response. Please try again."
                
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            return f"❌ Error: {str(e)[:100]}"
    
    def solve_homework(self, problem: str, subject: str, level: str = "high school") -> str:
        """
        Help solve homework problems step by step
        
        Args:
            problem: The homework problem
            subject: Subject (Math, Science, etc.)
            level: Education level
        
        Returns:
            Step-by-step solution
        """
        if not self.initialized:
            return "⚠️ AI service is unavailable."
        
        try:
            prompt = f"""You are a homework tutor for {level} students.
Subject: {subject}

Solve this problem step-by-step:
{problem}

IMPORTANT:
1. Show each step clearly
2. Explain WHY each step is done
3. Give tips for similar problems
4. Use both English and Amharic explanations
5. End with the final answer highlighted"""
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            return response.text if response.text else "Could not solve the problem."
            
        except Exception as e:
            logger.error(f"Error solving homework: {e}")
            return f"Error: {str(e)[:100]}"
    
    def explain_concept(self, concept: str, subject: str, detail_level: str = "medium") -> str:
        """
        Explain educational concepts in simple terms
        
        Args:
            concept: The concept to explain
            subject: Subject area
            detail_level: 'simple', 'medium', or 'advanced'
        
        Returns:
            Clear explanation
        """
        if not self.initialized:
            return "⚠️ AI service is unavailable."
        
        try:
            detail_map = {
                'simple': 'for beginners with simple examples',
                'medium': 'for intermediate learners with moderate detail',
                'advanced': 'for advanced learners with technical depth'
            }
            
            detail_instruction = detail_map.get(detail_level, 'for intermediate learners')
            
            prompt = f"""Explain this concept {detail_instruction}:

Concept: {concept}
Subject: {subject}

Requirements:
1. Start with a simple definition
2. Use real-world examples from Ethiopian context when possible
3. Include key points
4. Provide study tips
5. Suggest related topics
6. Use both English and Amharic"""
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            return response.text if response.text else "Could not explain the concept."
            
        except Exception as e:
            logger.error(f"Error explaining concept: {e}")
            return f"Error: {str(e)[:100]}"
    
    def generate_study_guide(self, topic: str, subject: str) -> str:
        """
        Generate comprehensive study guides
        
        Args:
            topic: Topic to study
            subject: Subject area
        
        Returns:
            Study guide
        """
        if not self.initialized:
            return "⚠️ AI service is unavailable."
        
        try:
            prompt = f"""Create a comprehensive study guide:

Topic: {topic}
Subject: {subject}

Include:
1. Key concepts (5-7 points)
2. Important definitions
3. Common misconceptions
4. Practice questions (3-5)
5. Study tips specific to this topic
6. Resources for further learning
7. Ethiopian context/examples where relevant

Format in both English and Amharic where applicable."""
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            return response.text if response.text else "Could not generate study guide."
            
        except Exception as e:
            logger.error(f"Error generating study guide: {e}")
            return f"Error: {str(e)[:100]}"
    
    def answer_question(self, question: str, subject: str) -> str:
        """
        Answer specific questions with detailed explanations
        
        Args:
            question: The question to answer
            subject: Subject area
        
        Returns:
            Detailed answer
        """
        if not self.initialized:
            return "⚠️ AI service is unavailable."
        
        try:
            prompt = f"""Answer this educational question thoroughly:

Subject: {subject}
Question: {question}

Response should include:
1. Direct answer to the question
2. Detailed explanation
3. Examples or illustrations
4. Why this answer is correct
5. Common related concepts
6. Ethiopian cultural context if applicable"""
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            return response.text if response.text else "Could not answer the question."
            
        except Exception as e:
            logger.error(f"Error answering question: {e}")
            return f"Error: {str(e)[:100]}"
    
    def check_and_improve_essay(self, essay: str, subject: str) -> str:
        """
        Review and improve student essays
        
        Args:
            essay: Student's essay
            subject: Subject area
        
        Returns:
            Feedback and suggestions
        """
        if not self.initialized:
            return "⚠️ AI service is unavailable."
        
        try:
            prompt = f"""Review and improve this student essay:

Subject: {subject}

Essay:
{essay}

Provide:
1. Grammar and spelling corrections
2. Structure improvements
3. Content feedback
4. Clarity suggestions
5. Strength highlights
6. Areas for improvement
7. Improved version (if needed)

Be encouraging and constructive."""
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(prompt)
            
            return response.text if response.text else "Could not review essay."
            
        except Exception as e:
            logger.error(f"Error reviewing essay: {e}")
            return f"Error: {str(e)[:100]}"


# Create global instance
damaph_ai = DamaphAI()


def get_ai_instance() -> DamaphAI:
    """Get the DamaphAI instance"""
    return damaph_ai
