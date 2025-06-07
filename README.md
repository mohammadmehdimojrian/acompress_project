# 📦 پروژه فشرده‌سازی داده‌ها (acompress_project)

این پروژه شامل پیاده‌سازی الگوریتم‌های فشرده‌سازی داده‌ها به زبان پایتون است. هدف اصلی، فراهم کردن ابزارهایی ساده و مؤثر برای فشرده‌سازی و بازسازی داده‌ها با استفاده از الگوریتم‌های مختلف می‌باشد.

## ✨ ویژگی‌ها

- پیاده‌سازی الگوریتم فشرده‌سازی هافمن (Huffman)
- پیاده‌سازی الگوریتم فشرده‌سازی طول اجرا (Run-Length Encoding - RLE)
- رابط کاربری ساده برای استفاده از الگوریتم‌ها
- ساختار پروژه منظم و قابل توسعه

## 🗂️ ساختار پروژه

```
acompress_project/
├── huffman.py           # پیاده‌سازی الگوریتم هافمن
├── rle.py               # پیاده‌سازی الگوریتم RLE
├── manage.py            # فایل اصلی برای اجرای برنامه
├── requirement.txt      # لیست وابستگی‌های پروژه
├── template/            # قالب‌های رابط کاربری (در صورت وجود)
├── .gitignore           # فایل‌های نادیده گرفته شده توسط Git
└── .gitattributes       # تنظیمات ویژگی‌های Git
```

## 🚀 شروع به کار

### پیش‌نیازها

- Python 3.x

### نصب وابستگی‌ها

```bash
pip install -r requirement.txt
```

### اجرای برنامه

```bash
python manage.py runserver
```

## 🧪 استفاده از الگوریتم‌ها

### الگوریتم هافمن

```python
from huffman import HuffmanCoding

h = HuffmanCoding()
compressed_data = h.compress("متن مورد نظر برای فشرده‌سازی")
original_data = h.decompress(compressed_data)
```

### الگوریتم RLE

```python
from rle import RLE

r = RLE()
compressed_data = r.compress("متن مورد نظر برای فشرده‌سازی")
original_data = r.decompress(compressed_data)
```

## 🤝 مشارکت

مشارکت در توسعه این پروژه خوش‌آمد گفته می‌شود. برای مشارکت:

1. این مخزن را Fork کنید.
2. تغییرات خود را اعمال کنید.
3. یک Pull Request ارسال کنید.

