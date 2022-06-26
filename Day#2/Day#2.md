
كيف يعمل Internet

لنفترض أنك تريد الوصول لبيانات معينة من خلال Laptop أو Smart Phone موصول بشبكة الانترنت من خلال wifi. والبيانات التي تريد الوصول لها مثلاً عبارة عن مقطع Youtube مخزن في مركز بيانات شركة Youtube. لكن كيف تستطيع الوصول لذلك المقطع؟ 


![](https://paper-attachments.dropbox.com/s_4160F6DE7C6BAA2EB66EAEB7A845FBF4C0469F3877CA1B209DF191E1F3F78A5D_1627924002046_image.png)


أي جهاز موصول بشبكة الانترنت يكون معرّف من خلال مجموعة من الأرقام تسمى IP address. تلك العناوين يتم توفيرها من خلال ISP (Internet Service Provider) والتي تقوم بتوفير عنوان مختلف لكل جهاز في شبكة الانترنت. كذلك Server الذي يحتوي على المقطع الذي تريد مشاهدته يكون له عنوان IP خاص به.

![](https://paper-attachments.dropbox.com/s_4160F6DE7C6BAA2EB66EAEB7A845FBF4C0469F3877CA1B209DF191E1F3F78A5D_1627924288139_image.png)


فمن خلال عناوين IP يكون هناك مُرسل Sender ومُستقبل Receiver. 


![](https://paper-attachments.dropbox.com/s_4160F6DE7C6BAA2EB66EAEB7A845FBF4C0469F3877CA1B209DF191E1F3F78A5D_1627924532377_image.png)


وهذا يعني أن موقع Youtube يملك عنوان IP خاص به، لكن للبحث عنه والوصل إليه لا يشترط أن نقوم بحفظ عنوان IP. يمكننا استخدام الرابط `youtube.com` وذلك بمساعدة DNS الذي يقوم بربط كل عنوان IP باسم يسهل حفظه والبحث عنه باستمرار.


![](https://paper-attachments.dropbox.com/s_4160F6DE7C6BAA2EB66EAEB7A845FBF4C0469F3877CA1B209DF191E1F3F78A5D_1627925633246_image.png)

مكونات URL
![](https://paper-attachments.dropbox.com/s_1D6B086A45BCF6338C718F8B8F973D33B9FC54F52764DC46881B977111A9EBB6_1621763678775_Screen+Shot+2021-05-23+at+12.54.26+PM.png)

مفهوم World Wide Web

قبل البدء في تطوير مواقع الويب، نحتاج أولاً إلى معرفة مفهوم الويب بشكل عام. الويب هو عبارة عن نظام من صفحات الويب التي نستطيع الوصول إليها من خلال الإنترنت. مما يعني أن الويب ليس الإنترنت، بل هو واحد من التطبيقات التي تم إنشاؤها على الإنترنت. هناك بعض الأجزاء في World Wide Web نحتاج إلى فهمها ومعرفة الغرض من وجودها لكثرة استخدام مصطلحاتها أثناء تطوير تطبيقات الويب وهي Client, Server, Request, Response.

![](https://paper-attachments.dropbox.com/s_803AD9971490A5B412A11F053A6B7B478D6C3D309C1FBA548D35327DE9020899_1627919570518_image.png)


عندما يتصفح المستخدم الإنترنت من خلال PC, Laptop, Smart Phone, iPad في هذه الحالة يعتبرمستخدم (Client)، بحيث أنه عندما يبحث عن موقع معين من خلال وضع رابط هذا الموقع في المتصفح فهو في هذه الحالة يقوم بإرسال طلب (Request) أي طلب لهذا الموقع، في هذه الأثناء يقوم الخادم (Server) باستقبال طلب المستخدم للموقع ثم يقوم بعرض هذا الموقع للمستخدم كـرد (Response) لطلب المستخدم.



![](https://paper-attachments.dropbox.com/s_803AD9971490A5B412A11F053A6B7B478D6C3D309C1FBA548D35327DE9020899_1627919583193_image.png)

مثال: 

عندما تقوم بفتح المتصفح (safari أو google chrome مثلاً) وتقوم بالبحث عن منصة طويق التعليمية من خلال الرابط `www.tuwaiq.codes` في هذه الحالة أنت Client، ويقوم بعدها DNS باستقبال طلبك لتحويل ذلك الرابط إلى IP address الخاص بمنصة طويق التعليمة، حتى يرسل طلبك إلى Server منصة طويق التعليمة، بعد ذلك يقوم Server منصة طويق التعليمية بالرد على طلبك من خلال عرض الموقع لك.


![](https://paper-attachments.dropbox.com/s_803AD9971490A5B412A11F053A6B7B478D6C3D309C1FBA548D35327DE9020899_1627920531893_image.png)



> ماهو DNS ؟ هو اختصار لمصطلح Domain Name System يستخدم لربط اسم الموقع أو رابط الموقع بعنوان IP address  لذلك الموقع، لأنه من الصعب أن نقوم بحفظ IP address لكل المواقع التي نريد زيارتها، فيقوم DNS بالمساعدة بحيث يربط اسم كل موقع بالعنوان الحقيقي للخادم Server الخاص به. فتبحث أنت باستخدام اسم الموقع مثل `google.com` ويقوم DNS بإيجاد العنوان المقابل `216.58.212.110` وإرسال Request للخادم Server الخاص بذلك الموقع.


![العناوين ليست دقيقة، مجرد مثال.](https://paper-attachments.dropbox.com/s_803AD9971490A5B412A11F053A6B7B478D6C3D309C1FBA548D35327DE9020899_1627920454416_image.png)

ماهي Web Frameworks؟

هي مجموعة من packages أو modules التي تسمح للمطورين بكتابة تطبيقات وخدمات الويب من دون الحاجة للتعامل مع low-level details مثل protocols أو sockets أو إدارة process/thread.

يوجد لدينا Web Frameworks مشهورة مثل: ReactJS, Angular, Vue, Flask, Django, FastApi ويمكن تصنيف هذه Frameworks إلى ثلاثة أنواع كالتالي:

- أولا: Front-end Frameworks وهي تعبر عن كل مايراه المستخدم أو الأجزاء التي يتعامل معها المستخدم أثناء تصفح واجهات الموقع مثل الألوان والخطوط و dropdown menus وبشكل عام مكونات  HTML و CSS و JavaScript. 
- ثانيا: Back-end Frameworks وهي مايُمكن Front-end Frameworks من العمل ويقوم بحفظ البيانات الخاصة بالموقع وتشمل أيضا server و application.
- ثالثا: Full-stack Frameworks وهي تشمل النوعين السابقين، حيث يعمل Full-stack Developer على Client-side و Server-side .

 

![](https://paper-attachments.dropbox.com/s_1D6B086A45BCF6338C718F8B8F973D33B9FC54F52764DC46881B977111A9EBB6_1621763570863_Screen+Shot+2021-05-23+at+12.52.42+PM.png)



ماهو FastApi Framework؟

هو إطار عمل حديث يُستخدم لبناء web APIs يتميز بسرعته وأداؤه العالي ويتوافق مع إصدار Python 3.6+.


مميزاته:
- أداؤه العالي وذلك بسبب استخدامه Starlette و Pydantic.
- سرعة عملية التطوير باستخدام FastApi حيث تكون أسرع 200% إلى 300% .
- قلة الأخطاء حيث يساعد بتقليل الأخطاء البشرية بنسبة 40%.
- سهل التعلم والاستخدام.
- تقليل الأكواد البرمجية.
- يتميز بوجود automatic interactive documentation.
