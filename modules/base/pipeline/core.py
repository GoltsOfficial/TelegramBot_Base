class Pipeline:
    def __init__(self, fetch, transform, publish):
        self.fetch = fetch
        self.transform = transform
        self.publish = publish

    async def run(self):
        raw = await self.fetch()
        processed = await self.transform(raw)
        await self.publish(processed)
