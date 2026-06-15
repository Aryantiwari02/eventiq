echo "BUILD START"
pip install --break-system-packages -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"
