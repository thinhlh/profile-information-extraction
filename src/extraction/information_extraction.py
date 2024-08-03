from loader import openAIClient
from loader.openai import CHAT_MODEL
class IE:
    def __init__(self,text):
        self.text = text
        
    def _build_IE_prompt(self,output_format = None, sample_output = None):
        output_format = '''
        {
            "name": "name",
            "position": "position",
            "skillset": [
                "skill1",
                "skill2"
            ],
            "certificate": [
                "certificate 1",
                "certificate 2"
            ],
            "domain": [
                "project 1 domain",
                "project 2 domain"
            ],
            "workingTimeZone": "GMT+4",
            "projects": [
                {
                "name": "project 1",
                "duration": "x weeks",
                "skills": [
                    "a",
                    "b",
                    "c"
                ],
                "contributions": "asdda",
                "project_description": "asda"
                }
            ]
        }
        ''' if output_format == None else output_format
        
        sample_output = '''
        {
            "name": "John",
            "title": "Software Engineer 1",
            "skillset": [
                "Cloud Infrastructure",
                "Google APIs",
            ],
            "certificate": [
                "AWS Cloud Solution Architect"
            ],
            "domain": [
                "Education"
            ],
            "workingTimeZone": "GMT+7",
            "projects": [
                {
                "name": "Logistic",
                "duration": "3 weeks",
                "skills": ["Android", "Google APIs"],
                "contributions": "Allow companies to initialize a logistic platform",
                "project_description": "An e2e SaaS platform for enterprise logistics"
                }
            ]
        }
        ''' if sample_output == None else sample_output
        
        prompt= f"""
            You are an AI assistant. Your task is extracting information based on the given plain text given employee profile.
            You are adhering to valid JSON output format.
            If there is no data for related field, fill it with N/A value.
            All missing data must not be generated

            Given this below colleague profile in raw text
            ```
            {self.text}
            ```

            Summary this profile and return as a JSON follow this format
            ```
            {output_format}
            ```

            Example output
            ```
            {sample_output}
            ```
            """
        return prompt
        
    def extract(self):
        chat_completion = openAIClient.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": self._build_IE_prompt(),
                }
            ],
            model=CHAT_MODEL,
        )
            
        return chat_completion.choices[0].message.content