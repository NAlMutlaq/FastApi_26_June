
مفهوم ORM و Migrations

قبل البدء بكتابة Model لابد من التعرف على مفهومين أساسين وهما:

- مفهوم Object Relational Mapper(ORM)
-  مفهوم Migrations
![](https://paper-attachments.dropbox.com/s_891266F9C0268F233056BDDFA8727ABE33AA9B24618CDE2386552BF1BA469F74_1651056613934_image.png)


أولا: مفهوم Object Relational Mapper(ORM)
في معظم تطبيقات الويب نحتاج للتفاعل مع البيانات عن طريق (تخزين، عرض، تعديل، حذف) البيانات. و يقوم FastApi بتوفير طريقة سهلة للتعامل مع قواعد البيانات عن طريق ORM.

![](https://paper-attachments.dropbox.com/s_891266F9C0268F233056BDDFA8727ABE33AA9B24618CDE2386552BF1BA469F74_1651057227814_image.png)


يساعد ORM بتحويل أكواد Python إلى database schema & tables من دون الحاجة لفهم تفاصيل قواعد البيانات وهذا يساعد في تسريع Web Development لأننا نستطيع تعريف قواعد البيانات باستخدام أكواد مكتوبة بلغة Python.
 

 مكونات Object Relational Mapper(ORM)
![](https://paper-attachments.dropbox.com/s_891266F9C0268F233056BDDFA8727ABE33AA9B24618CDE2386552BF1BA469F74_1651058633959_image.png)



أولا: Model 
ويتم تمثيله عن طريق Python Class بحيث يمثل البيانات الخاصة بتطبيق معين، ونقوم بتعريف fields الخاصة بالبيانات ونوعها بداخل هذا Class.
 مثل: الاسم ورقم الطالب إذا كنا نريد بناء قاعدة بيانات خاصة بالطلاب.

----------


![](https://paper-attachments.dropbox.com/s_891266F9C0268F233056BDDFA8727ABE33AA9B24618CDE2386552BF1BA469F74_1651058659709_image.png)


 

ثانيا: Migrations
يساعد في تحديث قاعدة البيانات المكتوبة بلغة SQL بحيث تكون متوافقة مع Model الذي تم كتابته بلغة Python.






----------


![](https://paper-attachments.dropbox.com/s_891266F9C0268F233056BDDFA8727ABE33AA9B24618CDE2386552BF1BA469F74_1651058711946_image.png)


مثال توضيحي:
لو كان لدينا Model يحتوي fields خاصة بالطلاب (الاسم ورقم الطالب)، وبعد فترة زمنية أردنا تغيير Model بحيث يشمل المعدل التراكمي للطالب، في هذه الحالة سوف نقوم بإضافة المعدل بداخل Model وأيضا نحتاج لعمل نفس التغييرات على قاعدة البيانات وهنا يأتي دور Migrations التي تقوم بتحديث قواعد البيانات بحيث تكون متطابقة مع ملف Model.





أنواع SQL Database Servers

توجد أنواع مختلفة لقواعد البيانات (SQL database servers) مثل: SQLite ،PostgreSQL، MySQL  وMicrosoft SQL Server


![](https://paper-attachments.dropbox.com/s_EBA608F9DAAD1AB739955C960312010D3A72EECAACC196E674EF9D2118F1EFF6_1652169937434_image.png)

الربط مع قواعد البيانات

أولا: تثبيت SQLAlchemy

    pip install sqlalchemy

ثانيا: تثبيت db driver الخاص بقواعد بيانات PostgreSQL

    pip install psycopg2-binary

ثالثا: إنشاء قاعدة بيانات بداخل PostgreSQL.

زابعا: إنشاء ملف database.py وبداخله نقوم بالتالي:

- استدعاء SQLAlchemy
- إنشاء SQLAlchemy `engine` يحتوي database URL
- إنشاء `Base` class لإنشاء database models أو ORM models ثم عمل map لهذه models إلى tables.
- إنشاء `SessionLocal` class، وعند إنشاء instance فذلك يمثل database session.

ملف database.py

    from sqlalchemy.orm import declarative_base 
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    engine = create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
        echo=True)
    
    Base = declarative_base()
    SessionLocal=sessionmaker(bind=engine)
- يستخدم echo attribute للتأكد إذا كان تم إنشاء sql عند تنفيذ عملية معينة.
- يمكن كتابة echo=True بالشكل التالي: connect_args={"check_same_thread": False}


ملف models.py

    from database import Base
    from sqlalchemy import String, Float, Integer, Column, Text
    
    class Item(Base): # inherets from Base class
        __tablename__ = 'items'
        id = Column(Integer, primary_key=True)
        name = Column(String(255), nullable=False, unique=True)
        description = Column(Text)
        price = Column(Float, nullable=False)
        tax = Column(Float)
    
        def __repr__(self):
            return f"<Item name={self.name} price={self.price}>"
- يمكن استخدام id = Column(Integer, primary_key=True, index=True) لجعل id يكون indexable
- يتم استخدام def __repr__(self) لتمثيل Objects بطريقة يمكن فهم البيانات من خلالها، قم بحذفها ولاحظ مايحدث

لاختبار قاعدة البيانات قم بكتابة الأسطر التالية في terminal: 

    python
    from models import Item
    new_item = Item(name = "Apple", description = "It has a red color, small size.", 
    price = 3.0, tax = 5.5)
    new_item

إنشاء ملف create_db.py 

    from database import Base,engine
    from models import Item
    Base.metadata.create_all(engine)
- يتم استخدام  Base.metadata.create_all(engine) لعمل migrate ل models الخاصة بقواعد البيانات.
- ملاحظة: يمكن كتابة الأسطر السابقة (create_db.py) بداخل ملف main.py.
- لتنفيذ ملف create_db.py  قم بكتابة السطر التالي في terminal: 
    python create_db.py
- بعد تنفيذك للأمر قم بالذهاب إلى PostgreSQL (pgAdmin) سوف تلاحظ أن الجداول قد تم إضافتها.

Use our db via API inside main.py:

    from database import SessionLocal
    
    class Item(BaseModel):
        id: int
        name: str
        description: Optional[str] = None
        price: float
        tax: Optional[float] = None
    
        class Config: # serialize our sql obj to json
            orm_mode=True
    
    db=SessionLocal()







