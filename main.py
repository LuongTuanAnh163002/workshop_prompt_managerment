# agent_runner.py

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.genai.types import Part
import asyncio

async def main():
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="demo_app",
        session_service=session_service
    )

    # Tạo session
    session = await session_service.create_session(
        app_name=runner.app_name,
        user_id="user1",
        session_id="session1"
    )

    # Khởi tạo Content
    user_msg = types.Content(role="user", parts=[Part(text="Tôi muốn nghiên cứu về tác động của AI trong giáo dục.")])

    # 🔁 Gọi run_async đúng cách
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=user_msg
    ):
        if event.is_final_response():
            # In ra text phản hồi
            print(event.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(main())

