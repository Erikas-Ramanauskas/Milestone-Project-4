import os

os.environ[
    'SECRET_KEY'] = "Your Secret Key here"
os.environ['DEVELOPMENT'] = "True"
# os.environ['DATABASE_URL'] = "Postgress URL here"
os.environ['AWS_ACCESS_KEY_ID'] = "Your Secret Key here"
os.environ['AWS_SECRET_ACCESS_KEY'] = "Your Secret Key here"
os.environ['STRIPE_PUBLIC_KEY'] = "Your Secret Key here"
os.environ['STRIPE_SECRET_KEY'] = "Your Secret Key here"
os.environ['STRIPE_WH_SE'] = "Your Secret Key here"

os.environ['DEBUG'] = "True"
