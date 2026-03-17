#!/bin/bash
echo "🚀 بدء البناء على Vercel"
python3.9 -m pip install --no-cache-dir -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo "✅ انتهى البناء"
