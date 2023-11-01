export APP='settings.cfg'
export FLASK_APP='project'
echo 'from project import db'
echo 'db.create_all()'
flask shell
