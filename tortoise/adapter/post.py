from typing import TypeVar
from pydantic import BaseModel
from domain.entities.post import Post, PostStatus

DataT = TypeVar("DataT")

class PostTortoiseAdapter(BaseModel):

    model: DataT

    async def list(self):
        return await self.model.all()
    
    async def create(self, post: Post):
        return await self.model.create(**post.model_dump())
    
    async def get(self, post_id: int):
        return await self.model.get(id=post_id)
    
    async def publish(self, post_id: int):
        post = await self.model.get(id=post_id)
        post.status = PostStatus.PUBLISHED
        await post.save()
        return post