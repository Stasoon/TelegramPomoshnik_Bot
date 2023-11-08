import aiofiles
import json


class Json:
    def __init__(self, file_path: str):
        self.file_path = file_path

    async def _read_data(self):
        async with aiofiles.open(self.file_path, 'r', encoding='UTF-8') as file:
            return await file.read()

    async def _write_data(self, data):
        async with aiofiles.open(self.file_path, 'w', encoding='UTF-8') as file:
            await file.write(json.dumps(data, indent=4))

    async def update_data(self, key: str, value: str):
        data = await self._read_data()
        data = json.loads(data)
        data[key] = value
        await self._write_data(data)

    async def get_data(self, key: any) -> any:
        data = await self._read_data()
        data = json.loads(data)
        return data.get(key)

    async def get_keys(self):
        data = await self._read_data()
        data = json.loads(data)
        return data.keys()