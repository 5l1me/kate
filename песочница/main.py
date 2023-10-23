import asyncio
import logging
import openai
from datetime import datetime

logging.basicConfig(level=logging.INFO)
start = datetime.now()
async def fun1(num: int):
    num**10
    await asyncio.sleep(3)
    logging.info('первое готово')


async def fun2(num: int):
    num**10
    await asyncio.sleep(3)
    logging.info('второе готово')
    return 1

async def get_chat_gpt(message):
    user_text = message.text
    msg_for_user = await openai_message(msg_for_openai=user_text)
    await message.answer(text=msg_for_user)


async def openai_message(msg_for_openai):
    openai.api_key = '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'
    model = 'gpt-3.5-turbo'
    data_openai = [{'role': 'user', 'content': msg_for_openai}]
    responce = await openai.ChatCompletion.acreate(model=model,
                                            messages=data_openai,
                                            )
    return responce.choices[0].message.content

async def main():
    get =['кто ты', 'ыы']
    task1 = asyncio.create_task(openai_message(get[0]))
    task2 = asyncio.create_task(openai_message(get[1]))
    await task1
    await task2




if __name__ == '__main__':
    asyncio.run(main())
    print(datetime.now()-start)
