#!/bin/sh
# export FN_AUTH_REDIRECT_URI=http://localhost:8059/google/auth
# export FN_BASE_URI=http://localhost:8059
# export FN_CLIENT_ID=759666219031-62n3t19980gctqmlso31epcfp444h47b.apps.googleusercontent.com
# export FN_CLIENT_SECRET=SkNrPzIXJCVyrT7xeseRBupT

# export FLASK_APP=app.py
# export FLASK_DEBUG=1
# export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET

lsof -ti tcp:8059 | xargs kill -9

cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
# nohup python3.8 run.py &
flask run --port=8059 --host='0.0.0.0'
# nohup flask run --port=8059 --host='0.0.0.0' &
