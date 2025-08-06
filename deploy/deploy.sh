#!/bin/bash
set -e

git pull
pip install -r requirements.txt
alembic upgrade head
systemctl restart dash.service
