
إنشاء مستخدم User 

يمكننا إنشاء مستخدم عن طريق الخطوات التالية:


- إنشاء User Schema في صفحة main.py
    ```
    class User(BaseModel):
        name: str
        email: str
        password: str
    
        class Config:  
            orm_mode = True
    ```


- إنشاء create_user API في صفحة main.py
    ```
    @app.post('/user', response_model=User)
    def create_user(user: User):
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=user.password,
        )
    
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
     ```


- إنشاء User Model في صفحة models.py
    ```
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        email = Column(String)
        password = Column(String)
     ```


- تنفيذ الأمر بداخل terminal 
    ```
    python create_db.py
    ```
- قم بالدخول على صفحة http://127.0.0.1:8000/docs ثم إضافة مستخدم جديد.


إنشاء Hash Password 

لإنشاء Hash Password لابد من تثبيت `passlib` وهي Python package تساعد بإنشاء password hashes وتدعم العديد من secure hashing algorithms وتمكننا من استخدامها.
في أمثلتنا سوف نقوم باستخدام "Bcrypt" وهي algorithm يُنصح باستخدامها لتوفير password hashes.

    
    ```
    pip install "passlib[bcrypt]"
    
    ```

في صفحة main.py

    ```
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    @app.post('/user', response_model=User)
    def create_user(user: User):
        hashed_pass = pwd_context.hash(user.password)
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=hashed_pass,
        )
    
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
        
      ```



إنشاء Show User Schema

عند إنشاء User نريد فقط استعراض name و email من دون ظهور password لذلك سوف نقوم بإنشاء Schema  جديدة (ShowUser) خاصة باستعراض معلومات المستخدم بدلا من استخدام User Schema.

في صفحة main.py

    ```
    class ShowUser(BaseModel):
        name: str
        email: str
        class Config:  # serialize our sql obj to json
            orm_mode = True
    
    @app.post('/user', response_model=ShowUser)
    def create_user(user: User):
        hashed_pass = pwd_context.hash(user.password)
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=hashed_pass,
        )
     ```

عند محاولة حذف السطر التالي سوف نحصل على خطأ، وذلك لأننا نريد إرجاع Show User Schema ك response_model  لذلك لابد من كتابة orm_mode = True والذي تساعد بتحويل sql obj إلى json .

    ```
    class Config:  # serialize our sql obj to json
        orm_mode = True
    ```
قراءة user
   
   
   ```
    @app.get('/user/{id}', response_model=ShowUser)
    def get_user(id: int):
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"User with id {id} is not Available")
        return user
    ```
    


