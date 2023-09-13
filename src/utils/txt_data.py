import aiofiles


async def read_txt_file(path: str) -> str:
    async with aiofiles.open(path, 'r', encoding='UTF-8') as file:
        text = await file.read()
    return text


async def rewrite_txt_file(path: str, new_text: str) -> None:
    async with aiofiles.open(path, 'w', encoding='UTF-8') as file:
        await file.write(new_text)
