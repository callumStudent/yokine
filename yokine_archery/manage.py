import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from yokine_archery import app
from flask.ext.script import Manager, Server
#from flask.ext.migrate import MigrateCommand

manager = Manager(app)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = '5000'
    )
)

if __name__ == "__main__":
    manager.run()
