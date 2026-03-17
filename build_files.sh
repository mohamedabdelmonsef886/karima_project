echo "🚀 بدء البناء على Vercel"
pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "✅ انتهى البناء"