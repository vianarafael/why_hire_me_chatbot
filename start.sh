#!/usr/bin/env bash
set -e

# 1. Build your vector DB
echo "▶️ Building index..."
python3 scripts/build_index.py

# 2. (Optional) Copy your React build into Flask’s static folder
#    Assuming your React build output is in frontend-react/build/
#    and your Flask app serves from ./static/
#rm -rf static
#cp -R frontend-react/build static

# 3. Launch Gunicorn
echo "▶️ Starting Flask..."
exec gunicorn flask_app:app --preload --log-file -
