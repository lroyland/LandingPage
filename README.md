# LandingPage
Form for Submission of Lead Info, notification of submissions, and administrative backend for users/data.

## Installation

### Clone it and cd into it
`git clone https://github.com/lroyland/LandingPage.git`
###
`cd ./LandingPage`

### Create python3 Virtual Environment & Activate
`python3 -m venv .env`
###
`source ./env/bin/activate`
###
Note: (.env) should show up before your terminal prompt

### Install all of the required packages with pip3
`pip install -r requirements.txt`

### See if it gets up and running
`python manage.py runserver`

### Setup migrations
`python manage.py makemigrations Form`

### Migrate
`python manage.py migrate`
###

### Setup admin
`python manage.py createsuperuser`
###
At this point, `/admin` should function as well
