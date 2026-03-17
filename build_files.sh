echo "🚀 build started"
pip install -r requirements.txt
echo "📦 collect static..."
python manage.py collectstatic --noinput
echo "📁 show staticfiles"
ls staticfiles/css
echo "✅ done"