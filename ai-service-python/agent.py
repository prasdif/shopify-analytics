import json
import asyncio
from shopify_client import ShopifyClient

class ShopifyAgent:
    def __init__(self, openai_api_key: str = None):
        self.api_key = openai_api_key
        self.shopify_client = ShopifyClient()

    async def process_question(self, store_id: str, question: str) -> dict:
        """
        Main orchestration flow:
        1. Intent Classification
        2. Query Generation
        3. Data Fetching
        4. Response Synthesis
        """
        
        # Step 1: Understand Intent (Mocked for speed/stability without live LLM)
        intent = self._classify_intent(question)
        print(f"Detected Intent: {intent}")

        # Step 2: Plan & Generate Query
        # In a real scenario, we'd send schema + question to LLM
        query_plan = self._generate_query(intent, question)
        print(f"Generated Query Plan: {query_plan}")

        # Step 3: Execute Query
        # Fetch data from Shopify (Mocked)
        data = self.shopify_client.execute(store_id, query_plan)
        print(f"Fetched Data: {data}")

        # Step 4: Explain Results
        answer = self._synthesize_answer(question, data)
        
        return {
            "answer": answer,
            "confidence": "high" if data else "low"
        }

    def _classify_intent(self, question: str) -> str:
        question = question.lower()
        if "inventory" in question or "stock" in question or "reorder" in question:
            return "inventory_forecast"
        elif "sell" in question or "sold" in question or "sales" in question:
            return "sales_analytics"
        elif "customer" in question:
            return "customer_insights"
        return "general_query"

    def _generate_query(self, intent: str, question: str) -> str:
        # Mocking ShopifyQL generation
        if intent == "inventory_forecast":
            return "FROM products SHOW title, inventory_quantity, total_sales_last_30d"
        elif intent == "sales_analytics":
            return "FROM orders SHOW total_price, created_at SINCE -7d"
        return "FROM products SHOW title"

    def _synthesize_answer(self, question: str, data: list) -> str:
        # Simple rule-based synthesis for the demo
        if not data:
            return "I couldn't find any relevant data for your request."

        # Mock synthesis logic
        if "reorder" in question.lower():
            # Assume data is products needing reorder
            count = len(data)
            return f"Based on your sales velocity, you have {count} products that are below safety stock levels. You should reorder approximately 70 units to cover next week's demand."
        
        if "sell" in question.lower():
            return f"You sold {len(data) * 5} units in the last week, which is a 10% increase from the previous week."

        return "Here is the data found: " + str(data)[:100] + "..."
