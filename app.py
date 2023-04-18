import os
import pydevd_pycharm

from flask import Flask, render_template

import ldclient
from ldclient import Context
from ldclient.config import Config

app = Flask(__name__)

sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")
feature_flag_key = "use-new-emojis"

@app.route('/')
def hello_world():
    context = Context.builder('okteto').name('Cindy').build()
    flag_value = ldclient.get().variation(feature_flag_key, context, False)

    if flag_value:
      msg = 'Hello New World! 🌎'
      return render_template("index-dark.html", msg=msg)

    else: 
      msg = 'Hello World! 🌐'
      return render_template("index-light.html", msg=msg)


def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=9000, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  ldclient.set_config(Config(sdk_key))
  if ldclient.get().is_initialized():
    print("LaunchDarkly SDK successfully initialized!")
  else:
    print("LaunchDarkly SDK failed to initialize")
    exit()

  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)
