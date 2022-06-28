
ماهو FastApi Framework؟

هو إطار عمل حديث يُستخدم لبناء web APIs يتميز بسرعته وأداؤه العالي ويتوافق مع إصدار Python 3.6+.

مميزاته:
- أداؤه العالي وذلك بسبب استخدامه Starlette و Pydantic.
- سرعة عملية التطوير باستخدام FastApi حيث تكون أسرع 200% إلى 300% .
- قلة الأخطاء حيث يساعد بتقليل الأخطاء البشرية بنسبة 40%.
- سهل التعلم والاستخدام.
- تقليل الأكواد البرمجية.
- يتميز بوجود automatic interactive documentation.


مقارنة بين FastAPI و Flask و Django:
- ا Django يعتبر web framework بينما Flask و FastAPI عبارة عن micro web frameworks.
- يتم استخدام Django لبناء full-stack أو web App أو REST API’s.
- يتم استخدام Flask لبناء minimalist web App و REST API’s.
- يتم استخدام FastAPI لبناء fast web App و REST API’s.
- ا Django يدعم WSGI و ASGI بينما Flask يدعم WSGI أما FastAPI فهو يدعم ASGI.
![FastAPI python development company — Quintagroup](https://quintagroup.com/services/service-images/fastapi-vs-flask-and-django.jpg)

أنواع Web Servers
- أولا: WSGI وهو اختصار Web Server Gateway Interface.
- ثانيا: ASGI وهو اختصار Asynchronous Server Gateway interface. 

كلا النوعين يستخدم كوسيط بين web server و Python web application  أو framework.

![wsgi vs. asgi interface](https://learn.vonage.com/content/blog/how-pythons-wsgi-vs-asgi-is-like-baking-a-cake/wsgi-vs.-asgi.png)

مثال على WSGI:
![](https://paper-attachments.dropbox.com/s_DB0F2E35FD8CC02D881033F9C84F6548FEC16E37F57F487E9A274035F265B69D_1645910062650_Screen+Shot+1443-07-26+at+12.14.03+AM.png)



مثال على ASGI:
![](https://paper-attachments.dropbox.com/s_DB0F2E35FD8CC02D881033F9C84F6548FEC16E37F57F487E9A274035F265B69D_1645909947148_Screen+Shot+1443-07-26+at+12.11.26+AM.png)





إنشاء Api عن طريق FastAPI

في المثال التالي سوف نقوم بإنشاء Api بسيطة تقوم بطباعة Hello World عن طريق الخطوات التالية:


- تثبيت fastapi.
    pip3 install fastapi
- تثبيت uvicorn.
    pip3 install uvicorn
    uvicorn --version


- إنشاء ملف `main.py`
    from fastapi import FastAPI  
    
    app = FastAPI() # create instance from fastapi
    
    # to give the function a path
    @app.get("/") # localhoat path
    def root():
        return {"message": "Hello World"}

في المثال السابق قمنا بالتالي:

- استيراد `FastAPI` وهو Python class يوفر جميع الوظائف اللازمة لإنشاء API.
- إنشاء `FastAPI` instance
- إنشاء path operation حيث أن `Path` يشير إلى الجزء الأخير من  URL بداية من عند أول `/` و يسمى "path"  ب "endpoint" أو "route".

على سبيل المثال:
لو كان لدينا URL كالتالي:

    https://example.com/items/foo

سوف يكون path كالتالي:

    /items/foo


العمليات(path operations)

نقصد بالعمليات أي عملية من عمليات HTTP methods وهي:

- عملية `POST` لإضافة البيانات.
- عملية `GET` لقراءة البيانات.
- عملية `PUT` لتحديث البيانات.
- عملية `DELETE` لحذف البيانات.

يشير الرمز @ إلى decorator في لغة Python حيث يتم وضعه بأعلى function بحيث يقوم 
بإخبار FastAPI بأن function في الأسفل هي تابعة إلى path `/` ويتم تنفيذ عملية `get` عليها.

يمكن إرجاع قيم مختلفة مثل `dict`, `list`, `str`, `int` أو إرجاع Pydantic models والذي سنتعرف عليه لاحقا.

لتشغيل البرنامج نقوم بكتابة:

    uvicorn main:app --reload
- حيث يشير app إلى اسم FastAPI instance.
- أما main فهو يشير لملف `main.py`.
- أما `--reload` تساعد server بإعادة التشغيل عند القيام بتغييرات داخل الأكواد.

أخيرا سوف تجد برنامجك على الرابط http://127.0.0.1:8000 مع JSON response
لإيقاف البرنامج يمكنك ذلك عن طريق CTRL+C .

يمكن تغيير router عن طريق كتابة:

    @app.get("/home")

يمكن تكرار اسم function مثل:

    @app.get("/")
    def root():
        return {"Hello World"}
    
    @app.get("/students")
    def root():
        return {"Student1": {"Name":"Sara", "ID":"123456"},
                "Student2": {"Name":"Amal", "ID":"324567"}}


لاختبار API، يمكنك ذلك عن طريق:

الطريقة الأولى : http://127.0.0.1:8000/docs
الطريقة الثانية: http://127.0.0.1:8000/redoc



مفهوم Path Parameters

يمكن تعريف path parameters أو variables بنفس طريقة تعريف Python format strings


    @app.get("/items/{item_id}")
    def read_item(item_id):
        return {"item_id": item_id}

نقوم باستخدام {} مع dynamic router على سبيل المثال: http://127.0.0.1:8000/items/foo



تعريف Path parameters مع استخدام types.

مثال:

    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}


التحقق من صحة البيانات (Data validation)

عند محاولة الدخول على http://127.0.0.1:8000/items/foo سوف نحصل على HTTP error.

- عند كتابة (item_id: int) ثم تجربة string بدلا من integer سوف نحصل على error.
- عند كتابة (item_id: str) ثم تجربة integer بدلا من string لن نحصل على error.


ترتيب paths

عندما يكون لدينا paths متشابهة (fixed and dynamic path)، لابد من وضع dynamic في الأسفل وذلك بسبب أن path operations يتم اختباره بالترتيب، لذا لابد من التأكد بأن يتم تعريف `/items/home` قبل `/items/{item_id}` و إلا سوف يكون `/items/{item_id}` مطابق `/items/home` ولن نتمكن من الوصول إلى `/items/home`.


    @app.get("/items/home")
    def read_item():
        return {"items home"}
    
    @app.get("/items/{item_id}")
    def read_item(item_id: str):
        return {"item_id": item_id}


مفهوم Query Parameters

يمكن تعريف query parameters بأنها function parameters الأخرى والتي ليست جزء من path parameters.
مثال:

    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    @app.get("/items/")
    def read_item(skip: int = 0, limit: int = 10):
        return fake_items_db[skip : skip + limit]
- قم بالدخول على http://127.0.0.1:8000/items/?skip=0&limit=10
- القيم الافتراضية هي `skip=0` و `limit=10`


تعريف Optional parameters

يمكن تعريف optional query parameters عن طريق وضع القيم الافتراضية = `None`

    from typing import Optional
    @app.get("/items/{item_id}")
    def read_item(item_id: str, q: Optional[str] = None):
        if q:
            return {"item_id": item_id, "q": q}
        return {"item_id": item_id}
- قم بالدخول على http://127.0.0.1:8000/items/?item_id=2&q=4
- قم بالدخول على http://127.0.0.1:8000/items/2?q=4

 لاحظ أن  FastAPI يمكنه التمييز بين path parameter وهو  `item_id` وبين query parameter وهو `q`.


مفهوم Query parameter type conversion


    @app.get("/items/{item_id}")
    def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
        item = {"item_id": item_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item


- قم بالدخول على http://127.0.0.1:8000/items/foo?short=1
- قم بالدخول على http://127.0.0.1:8000/items/foo?short=True
- قم بالدخول على http://127.0.0.1:8000/items/foo?short=true
- قم بالدخول على http://127.0.0.1:8000/items/foo?short=on
- قم بالدخول على http://127.0.0.1:8000/items/foo?short=yes
