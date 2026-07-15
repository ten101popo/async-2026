import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301030"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")

    start = time()
    tasks = [
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Mixed")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")),
    ]

    print(f"{ctime()} | [Pickup] All orders queued. Waiting for all dishes to finish...")
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"{ctime()} | [Pickup] Shop: {result['shop']} | Menu: {result['menu']} is ready!")

    elapsed = time() - start
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds (Equals the slowest dish).")

if __name__ == "__main__":
    asyncio.run(main())
