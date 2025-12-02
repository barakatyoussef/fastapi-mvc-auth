from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models.user import User, UserOut, UserCreate
from controllers.user_controller import verify_user, create_user
from auth.auth import create_access_token, get_current_user

router = APIRouter()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/")
async def read_root(current_user: str = Depends(get_current_user)):
    return {"message": f"❤️💙 Visca Barça, {current_user} ! (authentifié via JWT)"}

@router.get("/user/{id}")
async def get_user_by_id(id: int, current_user: str = Depends(get_current_user)):
    return {"id": id, "user": current_user}

@router.post("/users")
async def create_user_route(user: UserCreate, current_user: str = Depends(get_current_user)):
    return {
        "message": f"Utilisateur {user.name} a été créé par {current_user}",
        "données": user
    }

@router.post("/register")
async def register(user: User):
    existing = await verify_user(user.username, user.password)
    if existing:
        raise HTTPException(status_code=400, detail="Utilisateur déjà existant")
    created = await create_user(user.username, user.password)
    return {"message": f"Utilisateur {created['username']} enregistré"}


