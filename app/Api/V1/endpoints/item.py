from fastapi import APIRouter, HTTPException

router = APIRouter()

fake_items = [
    {
        "id": 1,
        "title": "Foo"
    },
    {
        "id": 2,
        "title": "Bar"
    },
]


@router.get("/")
async def read_items():
    return fake_items


@router.get("/{id}")
async def read_item(id: str):
    for item in fake_items:
        if item["id"] == id:
            return item
    return None


@router.put("/{item_id}", responses={403: {"description": "Operation forbidden"}})
async def update_item(item_id: str):
    if item_id != "1":
        raise HTTPException(
            status_code=403,
            detail="You can only update the item: foo"
        )
    return {"item_id": item_id, "name": "The Fighters"}
