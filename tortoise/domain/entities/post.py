from pydantic import Field, BaseModel
from enum import Enum

class PostStatus(str, Enum):
    PUBLISHED = 'published'
    DRAFT = 'draft'

class PostDto(BaseModel):
    title: str
    content: str

class Post(PostDto):
    status: PostStatus = Field(default=PostStatus.DRAFT)