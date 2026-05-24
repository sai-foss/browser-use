from browser_use import Agent, Browser, ChatOllama
import asyncio


async def main():
    llm = ChatOllama(
        model="deepseek-v4-pro:cloud",
    )

    task = """
    1. go to google.com then search for firefox. download a mac os version. Dont bother checking or clicking on the downloaded file.

    2. in a new tab go to bing.com then search for microsoft edge. download the linux os version. Dont bother checking or clicking on the downloaded file.
    """
    browser = Browser(
        headless=False,
        executable_path="/usr/bin/google-chrome"
    )
    agent = Agent(task=task, llm=llm, browser=browser)
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())