import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301030"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")

    task = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")
    )

    print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")
    try:
        await asyncio.wait_for(task, timeout=2.0)
        print(f"{ctime()} | Steak order completed successfully.")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now.")
        if not task.done():
            task.cancel()
            await asyncio.gather(task, return_exceptions=True)
            print(f"{ctime()} | Steak order task was canceled.")

if __name__ == "__main__":
    asyncio.run(main())
