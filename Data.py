from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
هلو {}

أهلا بك في {}

يمكنني تحميل الوسائط إلى telegra.ph وإعادة الرابط إليك بسهولة. حاول إرسال وسائط متعددة ، ولن يوقفني ذلك بعد.
يمكنني أيضًا أن أستخدم في مجموعات !!

لمشاهدة "أنواع الوسائط المدعومة" ، انقر فوق الزر ذي الصلة أدناه.
استخدم الأزرار الأخرى لمعرفة المزيد عني وعن استخداماتي.
By : @YY8GG 📂
    """

    # Help Message
    HELP = """
**اقرأ أدناه لتعرف كيف تستعملني.**

راجع "أنواع الوسائط المدعومة" بالنقر فوق الزر ذي الصلة أدناه.


**كيف تستعملني هنا؟**
فقط أرسل وسائل الإعلام واترك الراحة على عاتقي.

**كيفية الاستخدام في المجموعة?**
أضف لي المجموعة. ثم قم بالرد على إحدى الوسائط باستخدام "/telegraph" للحصول على رابط telegra.ph. يمكنك أيضًا بدلاً من ذلك استخدام "/t" أو "/tg" كأوامر و "!" كبادئة لفعل الشيء نفسه. هذا هو،

[إذا أضفت مجموعتك ، فلن يحتاج مستخدمو مجموعتك إلى الانضمام إلى قناتنا.]

ملاحظة: إذا لم يستجب الروبوت بالطريقة المتوقعة ، فاجعل مسؤول الروبوت حتى يحصل الروبوت على التحديثات بالتأكيد. برقية غريبة.

المزيد من الميزات قيد التطوير. تتبع من خلال الانضمام : @YY8GG
    """

    # About Message
    ABOUT = """
**About This Bot** 

السورس : @YY8GG

المطور : @KU_KX

كروب الدعم : @MUSICSOURCEDRAGON
    """

    SUPPORTED_MEDIA_TYPES = """
✨ **أرسل لي** ✨

1) صورة
2) ملصق
3) صورة متحركة
4) فيديو
5) ملاحظة فيديو
6) مستند (فيديو / صورة / صورة متحركة)
7) ملاحظة : أن لا يبلغ حجم المستند 5 ميغا
   
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("حالة البوت والمزيد من الروبوتات", url="https://t.me/YY8GGX")],
        [InlineKeyboardButton("أنواع الوسائط المدعومة", callback_data="supported_media_types")],
        [InlineKeyboardButton("أغلاق", callback_data="close")],
        [InlineKeyboardButton(text="رجوع", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("حالة البوت والمزيد من الروبوتات", url="https://t.me/YY8GGX")
        ],
        [InlineKeyboardButton("أنواع الوسائط المدعومة", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("كيف يستخدم", callback_data="help"),
            InlineKeyboardButton("حول", callback_data="about")
        ],
        [InlineKeyboardButton("أغلاق", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("حالة البوت والمزيد من الروبوتات", url="https://t.me/YY8GGX")],
        [InlineKeyboardButton("أغلاق", callback_data="close")],
        [InlineKeyboardButton(text="رجوع", callback_data="home")]
    ]
