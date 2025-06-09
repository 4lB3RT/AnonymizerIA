import google.generativeai as genai
from typing import Dict, Any, List
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiAIRepository:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_realistic_data(self, column_name: str, data_type: str, context: Dict[str, Any] = None) -> Any:
        """
        Generate realistic data for a given column using Gemini AI.
        
        Args:
            column_name: Name of the column
            data_type: Data type of the column
            context: Additional context about the data (e.g., table name, relationships)
        
        Returns:
            Generated data in the appropriate format
        """
        prompt = self._build_prompt(column_name, data_type, context)
        
        try:
            response = self.model.generate_content(prompt)
            return self._parse_response(response.text, data_type)
        except Exception as e:
            print(f"Error generating data with Gemini: {str(e)}")
            return self._generate_fallback_data(data_type)
    
    def _build_prompt(self, column_name: str, data_type: str, context: Dict[str, Any] = None) -> str:
        """Build a prompt for Gemini AI based on the column and context."""
        base_prompt = f"Generate a realistic {data_type} value for a database column named '{column_name}'."
        
        if context:
            if context.get('table_name'):
                base_prompt += f" This column is in the '{context['table_name']}' table."
            if context.get('is_foreign_key'):
                base_prompt += f" This is a foreign key referencing {context.get('referenced_table')}."
        
        base_prompt += " Return only the value, nothing else."
        return base_prompt
    
    def _parse_response(self, response: str, data_type: str) -> Any:
        """Parse the Gemini AI response into the appropriate data type."""
        response = response.strip()
        
        try:
            if 'int' in data_type.lower():
                return int(response)
            elif 'float' in data_type.lower() or 'double' in data_type.lower() or 'decimal' in data_type.lower():
                return float(response)
            elif 'bool' in data_type.lower() or 'boolean' in data_type.lower():
                return response.lower() in ('true', 'yes', '1')
            elif 'date' in data_type.lower():
                return response  # Assuming response is in YYYY-MM-DD format
            else:
                return response
        except ValueError:
            return self._generate_fallback_data(data_type)
    
    def _generate_fallback_data(self, data_type: str) -> Any:
        """Generate fallback data if Gemini AI fails."""
        import random
        import string
        from datetime import datetime, timedelta
        
        if 'int' in data_type.lower():
            return random.randint(1, 1000)
        elif 'float' in data_type.lower() or 'double' in data_type.lower() or 'decimal' in data_type.lower():
            return round(random.uniform(1.0, 1000.0), 2)
        elif 'varchar' in data_type.lower() or 'text' in data_type.lower() or 'char' in data_type.lower():
            return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif 'date' in data_type.lower():
            start_date = datetime(2000, 1, 1)
            end_date = datetime(2023, 12, 31)
            days_between = (end_date - start_date).days
            random_days = random.randint(0, days_between)
            return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        elif 'bool' in data_type.lower() or 'boolean' in data_type.lower():
            return random.choice([True, False])
        else:
            return None 