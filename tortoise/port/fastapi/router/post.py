from typing import List

from fastapi import APIRouter, Depends, status, HTTPException, Response
from domain.entities.post import Post, PostDto
from domain.service.post import PostService

from port.factory.post import post_factory

router = APIRouter(
    prefix='/posts',
    tags=["posts"]
)

@router.get("/", response_model=List[Post])
async def list_posts(service: PostService = Depends(post_factory)):
    return await service.list()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Post)
async def create_post(body: PostDto, service: PostService = Depends(post_factory)):
    post = Post(**body.model_dump())
    return await service.create(post)

@router.get("/{post_id}", status_code=status.HTTP_200_OK, response_model=Post)
async def get_post(post_id: int, service: PostService = Depends(post_factory)):
    return await service.get(post_id)

@router.put("/{post_id}/publish", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
async def publish_post(post_id: int, service: PostService = Depends(post_factory)):
    return await service.publish(post_id)