
تنفيذ عمليات CRUD على قواعد البيانات

مصطلح CRUD يعتبر اختصار للعمليات (Create, Read, Update, Delete) وهي تشمل:

- عملية الإنشاء (Create) ونستخدم معها `POST` لإضافة البيانات.
- عملية القراءة (Read) ونستخدم معها `GET` لقراءة البيانات.
- عملية التحديث (Update) ونستخدم معها `PUT` لتحديث البيانات.
- عملية الحذف (Delete) ونستخدم معها `DELETE` لحذف البيانات.
أولا: عملية الإنشاء (Create).

لإضافة item إلى قاعدة البيانات يمكننا ذلك عن طريق كتابة db.add(new_item)

    from fastapi import FastAPI
    from database import SessionLocal
    import models
    
    @app.post('/items', response_model=Item)
    def create_an_item(item: Item):
        new_item = models.Item(
            name=item.name,
            price=item.price,
            description=item.description,
            tax=item.tax)
    
        db.add(new_item)
        db.commit()
        return new_item
- قم بالدخول على http://127.0.0.1:8000/docs ثم إضافة item.
- قم بالدخول على http://127.0.0.1:8000/items سوف تحصل على response عبارة عن item list.
- قم بالتحقق من إضافة items بداخل PostgreSQL.


ثانيا: عملية القراءة (Read).

في عملية القراءة يمكننا قراءة عنصر محدد أو قراءة جميع العناصر.


- قراءة عنصر محدد

لاسترجاع item معين، يمكننا ذلك باستخدام الدالة first() .

    @app.get('/item/{item_id}', response_model=Item)
    def get_an_item(item_id:int):
        item = db.query(models.Item).filter(models.Item.id==item_id).first()
        return item
- قم بالدخول على http://127.0.0.1:8000/item/1 سوف تحصل على البيانات الخاصة بالعنصر الذي id = 1
- قم بالدخول على http://127.0.0.1:8000/item/10 سوف تحصل على null.


- قراءة جميع العناصر 

لاسترجاع جميع items التي قمنا بإنشائها يمكننا ذلك باستخدام الدالة all() .

    from typing import Optional,List
    
    @app.get('/items', response_model=List[Item])
    def get_all_items():
        items = db.query(models.Item).all()
        return items
- عند محاولتك الدخول على http://127.0.0.1:8000/items سوف تحصل جميع العناصر المضافة.


ثالثا: عملية التحديث (Update).
    
    
    @app.put('/item/{item_id}',response_model=Item)
    def update_an_item(item_id:int,item:Item):
        item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
        item_to_update.name=item.name
        item_to_update.price=item.price
        item_to_update.description=item.description
        item_to_update.tax=item.tax
        db.commit()
        return item_to_update
- قم بالدخول على http://127.0.0.1:8000/docs وتحديث أحد العناصر.
- قم التحقق من تحديث العنصر بداخل PostgreSQL. 


رابعا: عملية الحذف (Delete).
    
    
    @app.delete('/item/{item_id}')
    def delete_item(item_id:int):
        item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()
        db.delete(item_to_delete)
        db.commit()
        return item_to_delete
- قم بالدخول على http://127.0.0.1:8000/docs وحذف أحد العناصر.
- قم التحقق من حذف العنصر بداخل PostgreSQL. 
- قم التحقق من حذف العنصر عن طريق http://127.0.0.1:8000/items .



إضافة HTTPException

في الأمثلة التالية، سوف نقوم بتحسين Apis التي قمنا بإنشائها عن طريق إضافة HTTPException.

أولا: عملية الإنشاء (Create).
    
    
    from fastapi import FastAPI,status, HTTPException
    @app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
    def create_an_item(item: Item):
        db_item = db.query(models.Item).filter(models.Item.name == item.name).first()
        if db_item is not None:
            raise HTTPException(status_code=400, detail="Item already exists")
    
        new_item = models.Item(
            name=item.name,
            price=item.price,
            description=item.description,
            tax=item.tax)
    
        db.add(new_item)
        db.commit()
        return new_item
- قم بالتحقق من إضافة item موجود مسبقا، سوف تحصل على Bad Request error.


ثانيا: عملية القراءة (Read).


- قراءة عنصر محدد.
    
    
    ```
    from fastapi import FastAPI, status, HTTPException
    @app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
    def get_an_item(item_id: int):
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id {item_id} is not Available")
        return item
     ```
        
        
- الآن عند محاولتك دخول http://127.0.0.1:8000/item/10 سوف تحصل على الرسالة التالية: 

`Error: Not Found in docs and {"detail":"Item with id 2 is not Available"}`


أيضا، يمكن استبدال null عن طريق status code ولكن الأفضل استخدام HTTPException.

    
    from fastapi import FastAPI, status, HTTPException, Response
    @app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
    def get_an_item(item_id: int, response: Response):
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if not item:
            response.status_code = status.HTTP_404_NOT_FOUND
        return item




- قراءة جميع العناصر.
    
   
    ```
    @app.get('/items', response_model=List[Item], status_code=200)
    def get_all_items():
        items = db.query(models.Item).all()
        return items
    ```
        
        


ثالثا: عملية التحديث (Update).
    
    
    @app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
    def update_an_item(item_id:int,item:Item):
        item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
        item_to_update.name=item.name
        item_to_update.price=item.price
        item_to_update.description=item.description
        item_to_update.tax=item.tax
        db.commit()
        return item_to_update
        


رابعا: عملية الحذف (Delete).
    
    @app.delete('/item/{item_id}')
    def delete_item(item_id:int):
        item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()
        if item_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
        db.delete(item_to_delete)
        db.commit()
        return item_to_delete


مصادر إضافية:
- عمليات filter: 

https://docs.sqlalchemy.org/en/14/orm/tutorial.html#common-filter-operators

- https://fastapi.tiangolo.com/tutorial/response-status-code/
- https://docs.python.org/3/library/http.html#http.HTTPStatus
