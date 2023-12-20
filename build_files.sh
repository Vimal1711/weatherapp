echo "BUILD START"
python3.9 -m pip install -r requirements.txt  # Corrected filename to 'requirements.txt'
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
