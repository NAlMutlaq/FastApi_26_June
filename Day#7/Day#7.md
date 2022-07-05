
API Router

https://fastapi.tiangolo.com/tutorial/bigger-applications/

An example file structure

Let's say you have a file structure like this:

    .
    ├── app
    │   ├── __init__.py
    │   ├── main.py
    │   ├── dependencies.py
    │   └── routers
    │   │   ├── __init__.py
    │   │   ├── items.py
    │   │   └── users.py
    │   └── internal
    │       ├── __init__.py
    │       └── admin.py

There are several `__init__.py` files: one in each directory or subdirectory.
This is what allows importing code from one file into another.

For example, in `app/main.py` you could have a line like:

    from app.routers import items

To make our code more organized, we will create 
schemas.py

    from pydantic import BaseModel
    from typing import Optional, List
    
    class Item(BaseModel):
        id: int
        name: str
        description: Optional[str] = None   # required
        price: float  # int
        tax: Optional[float] = None
    
        class Config:  # serialize our sql obj to json
            orm_mode = True
    
    
    
    class User(BaseModel):
        name: str
        email: str
        password: str
    
    
    class ShowUser(BaseModel):
        name: str
        email: str
        items: List[Item] = []
        class Config:  # serialize our sql obj to json
            orm_mode = True
    
    
    class ShowItem(BaseModel):
        id: int
        name: str
        description: Optional[str] = None  # required
        price: float  # int
        tax: Optional[float] = None
        owner: ShowUser
    
        class Config:  # serialize our sql obj to json
            orm_mode = True
    

In main.py, update

    import schemas
     every response_model=schemas.ShowUser

Create a folder has the following files:

    routers
    ├── __init__.py
    ├── items.py
    └── users.py

items.py

    from fastapi import APIRouter
    router = APIRouter()

Take get_all_items() from main.py

    from typing import List
    from .. import schemas, models  
    ImportError: attempted relative import beyond top-level package
    import models, schemas, main
    
    @router.get('/items', response_model= List[schemas.Item], status_code=200, tags=["items"])
    def get_all_items():
        items = main.db.query(models.Item).all()
        return items

Go to http://127.0.0.1:8000/docs you will not find get_all_items
Go to https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies
In main.py add

    ImportError: attempted relative import with no known parent package
    from .routers import item
    from routers import item
    app.include_router(item.router)

Now, go to http://127.0.0.1:8000/docs, it will be work


Do the same for the rest routes
    from fastapi import status, HTTPException, Response
    
    @router.post('/items', response_model=schemas.Item, status_code=status.HTTP_201_CREATED, tags=["items"])
    def create_an_item(item: schemas.Item):
        db_item = main.db.query(models.Item).filter(models.Item.name == item.name).first()
        if db_item is not None:
            raise HTTPException(status_code=400, detail="Item already exists")
    
        new_item = models.Item(
            name=item.name,
            price=item.price,
            description=item.description,
            tax=item.tax,
            owner_id = 1
        )
    
        main.db.add(new_item)
        main.db.commit()
        return new_item
    
    
    @router.get('/item/{item_id}', response_model=schemas.ShowItem, status_code=status.HTTP_200_OK, tags=["items"])
    def get_an_item(item_id: int, response: Response):
        item = main.db.query(models.Item).filter(models.Item.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {item_id} is not Available")
        return item
    
    @router.put('/item/{item_id}',response_model=schemas.Item,status_code=status.HTTP_200_OK, tags=["items"])
    def update_an_item(item_id:int,item:schemas.Item):
        item_to_update=main.db.query(models.Item).filter(models.Item.id==item_id).first()
        item_to_update.name=item.name
        item_to_update.price=item.price
        item_to_update.description=item.description
        item_to_update.tax=item.tax
    
        main.db.commit()
    
        return item_to_update
    
    
    @router.delete('/item/{item_id}', tags=["items"])
    def delete_item(item_id: int):
        item_to_delete = main.db.query(models.Item).filter(models.Item.id == item_id).first()
    
        if item_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
    
        main.db.delete(item_to_delete)
        main.db.commit()
        return item_to_delete


Do the same for user
    from fastapi import APIRouter
    from passlib.context import CryptContext
    import models, main, schemas
    from fastapi import status, HTTPException
    
    
    router = APIRouter()
    
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    @router.post('/user', response_model=schemas.ShowUser, tags=["users"])
    def create_user(user: schemas.User):
        hashed_pass = pwd_context.hash(user.password)
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=hashed_pass,
        )
    
        main.db.add(new_user)
        main.db.commit()
        main.db.refresh(new_user)
        return new_user
    
    
    @router.post('/user/{id}', response_model=schemas.ShowUser, tags=["users"])
    def get_user(id: int):
        user = main.db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with id {id} is not Available")
        return user

In main.py

    from routers import item, users
    app.include_router(users.router)



API router path operators
- The main objective is to make our code is clean
- Instead of using tags=["users"] or tags=["items"]
- Go to: https://fastapi.tiangolo.com/tutorial/bigger-applications/#add-some-custom-tags-responses-and-dependencies
- Remove tags=["users"] 
- Update users.py as follows
    router = APIRouter(tags=["users"])

We can use prefix and replace all paths as follows

    router = APIRouter(
        prefix="/user",
        tags=["users"] )
    
    @router.post('/user', response_model=schemas.ShowUser)
    @router.post('/user/{id}', response_model=schemas.ShowUser)

Do the same for item.py



Login & verify Password

In schemas.py

    class Login(BaseModel):
      username: str
      password: str

In router folder create login.py

    from fastapi import APIRouter, status, HTTPException
    import schemas, main, models
    
    router = APIRouter(tags=["Auth"])
    
    @router.post("/login")
    def login(request:schemas.Login):
        user = main.db.query(models.User).filter(models.User.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invalid Credentials")
        if not hashing.Hash.verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Incorrect Password")
        return user

 In main.py

    app.include_router(login.router)

Go to: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

Create hashing.py

    from passlib.context import CryptContext
    
    pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    class Hash():
        def bcrypt(password: str):
            return pwd_cxt.hash(password)
    
        def verify(hashed_password,plain_password):
            return pwd_cxt.verify(plain_password,hashed_password)
- Try wrong username
- Try wrong password


JWT Access Token
- We need to install `python-jose` to generate and verify the JWT tokens in Python:
- Python-jose requires a cryptographic backend as an extra.
    pip install "python-jose[cryptography]"

in schemas.py

    class Token(BaseModel):
        access_token: str
        token_type: str
    
    class TokenData(BaseModel):
        email: Optional[str] = None

Create JWToken.py

```

    from datetime import datetime, timedelta
    from jose import JWTError, jwt
    import schemas
    
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

```
Update login.py as the following

    import JWToken
    
    router = APIRouter(tags=["Auth"])
    
    @router.post("/login")
    def login(request:schemas.Login):
        user = main.db.query(models.User).filter(models.User.email == request.username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invalid Credentials")
        if not hashing.Hash.verify(user.password, request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Incorrect Password")
    
        access_token = JWToken.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
- Now check login, it will return a token correctly
- We can use this token to authenticate the user to access item and user paths
Authentication Route
- Go to: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- We will use OAuth2PasswordBearer
- Create oauth2.py:

```
    from fastapi import Depends, HTTPException, status
    from fastapi.security import OAuth2PasswordBearer
    import JWToken
    
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
    
    def get_current_user(data: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
        return JWToken.verify_token(data, credentials_exception)
```

- In JWToken.py, add

```
    def verify_token(token:str,credentials_exception):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = schemas.TokenData(email=email)
        except JWTError:
            raise credentials_exception

```
- In routers/item.py, add

```
    from fastapi import APIRouter, Depends
    import oauth2
    @router.get('/', response_model= List[schemas.Item], status_code=200)
    def get_all_items(current_user:schemas.User = Depends(oauth2.get_current_user)):
        return item.get_all()
```

- Now, go to the localhost server and see that get_all_items has lock sign.
- Try to execute, you will get Not authenticated msg.


    pip install python-multipart


- In login.py

```
    from fastapi import Depends
    from fastapi.security import OAuth2PasswordRequestForm
    def login(request:OAuth2PasswordRequestForm = Depends()):
```
- Try to authorize, you will see the lock opened and you can try the function out.


- Update all functions in login.py with the dependency line.
```
    current_user:schemas.User = Depends(oauth2.get_current_user)
    
 ```
- Go to http://127.0.0.1:8000/items/ >> you will get Not authenticated






مراجع إضافية:

- go to https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
