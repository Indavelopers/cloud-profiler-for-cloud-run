import googlecloudprofiler
import logging
import os
import time

from flask import Flask


# Start the profiler
# It is recommended to start the profiler as early as possible in your
# application's startup sequence.
try:
    googlecloudprofiler.start(
        service='cloud-run-profiler-demo',
        service_version='cloud-run-v4',
        # verbose is the logging level. 0-error, 1-warning, 2-info, 3-debug
        verbose=3)
except (ValueError, NotImplementedError) as exc:
    print(f'Error: Could not start the profiler: {exc}')


app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)


def load_operation1(load = 100000):
    total = 0
    for i in range(load):
        total += i
    return total

def load_operation2(load = 200000):
    total = 0
    for i in range(load):
        total += i
    return total

def load_operation3(load = 300000):
    total = 0
    for i in range(load):
        total += i
    return total


def generate_load1():
    # This loop is added to generate some CPU load,
    # making the profiler output more interesting.
    start_time = time.time()
    
    total1 = load_operation1()
    total2 = load_operation2()
    total3 = load_operation3()

    total = total1 + total2 + total3
    elapsed_time = time.time() - start_time

    app.logger.info(f'Generate load 1. Sum: {total}, Time: {elapsed_time:.4f} s')

    return total, elapsed_time

def generate_load2():
    # This loop is added to generate some CPU load,
    # making the profiler output more interesting.
    start_time = time.time()
    
    total1 = load_operation1()
    total2 = load_operation2()
    total3 = load_operation3()

    total = total1 + total2 + total3
    elapsed_time = time.time() - start_time

    app.logger.info(f'Generate load 2. Sum: {total}, Time: {elapsed_time:.4f} s')

    return total, elapsed_time


@app.route('/')
def hello_world():
    total1, elapsed_time1 = generate_load1()
    total2, elapsed_time2 = generate_load2()

    total = total1 + total2
    elapsed_time = elapsed_time1 + elapsed_time2

    app.logger.info(f'Hello, World! Sum: {total}, Time: {elapsed_time:.4f} s')

    return f'Hello, World! Sum: {total}, Time: {elapsed_time:.4f} s'

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Cloud Run.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
