import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301030"
    print(f"{ctime()} | --- [Task 5] Advanced Practice: Mixing concepts together ---")

    start = time()
    rice_task = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed")
    )
    noodle_task = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")
    )

    print(f"{ctime()} | Created two order tasks. Immediate status check:")
    print(f"  Rice task done={rice_task.done()}")
    print(f"  Noodle task done={noodle_task.done()}")

    try:
        rice_result = await asyncio.wait_for(rice_task, timeout=1.0)
        noodle_result = await noodle_task

        elapsed = time() - start
        print(f"{ctime()} | Success: All food served on time! Received 2 dishes.")
        print(f"{ctime()} | Rice: {rice_result['menu']}")
        print(f"{ctime()} | Noodle: {noodle_result['menu']}")
        print(f"{ctime()} | Total elapsed time: {elapsed:.2f} seconds.")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout: Chicken rice did not finish within the 1.0s deadline.")
        if not rice_task.done():
            rice_task.cancel()
        if not noodle_task.done():
            noodle_task.cancel()
        await asyncio.gather(rice_task, noodle_task, return_exceptions=True)
        print(f"{ctime()} | One or more tasks were canceled due to deadline failure.")

if __name__ == "__main__":
    asyncio.run(main())
