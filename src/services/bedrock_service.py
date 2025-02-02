import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

class ClaudeBedrockService:
    def __init__(self):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

    async def generate_response(self, prompt: str):
        try:
            response = self.client.invoke_model(
                modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 2000,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": prompt + "\nBu soruya benzer bir soru yaratmanı istiyorum. Bir " 
                                    + "test kitabında kullanılan jargonu kullan. Sadece ama sadece soruyu yaz." 
                                    + " Başka hiçbir açıklama yapma."
                                }
                            ]
                        }
                    ]
                }),
                accept="application/json",
                contentType="application/json",
            )

            response_body = json.loads(response["body"].read().decode("utf-8"))

            if "content" in response_body and isinstance(response_body["content"], list):
                assistant_response = "\n".join(
                    item["text"] for item in response_body["content"] if item["type"] == "text"
                )
                return assistant_response

            return {"error": "Unexpected response format"}
        
        except Exception as e:
            return {"error": str(e)}

bedrock_service = ClaudeBedrockService()
