import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301030"
    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED) ---")

    start = time()
    tasks = {
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Thigh")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")),
    }

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    fastest = next(iter(done)).result()

    elapsed = time() - start
    print(f"{ctime()} | Winner served dish: Shop: {fastest['shop']} | Menu: {fastest['menu']}")
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    print(f"{ctime()} | Total waiting time for the first dish: {elapsed:.2f} seconds.")

    for pending_task in pending:
        pending_task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
