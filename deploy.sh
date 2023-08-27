apt-get install -y python3-dev python3-pip
pip3 install poetry
poetry install
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver