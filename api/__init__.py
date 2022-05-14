from fastapi import APIRouter, status

router = APIRouter(
    tags=["healthcheck"],

    responses={404: {"description": "not found"}},
)
@router.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    return {'healthcheck': 'Everything OK!'}