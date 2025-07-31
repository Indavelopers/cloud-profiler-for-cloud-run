import googlecloudprofiler
import os
import time

from flask import Flask

# It is recommended to start the profiler as early as possible in your
# application's startup sequence.
try:
    googlecloudprofiler.start(
        service='cloud-run-profiler-demo',
        service_version='1.0.0',
        # verbose is the logging level. 0-error, 1-warning, 2-info, 3-debug
        verbose=3)
except (ValueError, NotImplementedError) as exc:
    print(f'Error: Could not start the profiler: {exc}')

app = Flask(__name__)

@app.route('/')
def hello_world():
    start_time = time.time()
    # This loop is added to generate some CPU load,
    # making the profiler output more interesting.
    total = 0
    for i in range(10 * 10):
        total += i
    elapsed_time = time.time() - start_time
    return f'Hello, World! Sum: {total}, Time: {elapsed_time:.4f} s'

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
