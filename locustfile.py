from locust import HttpUser, task, between

class WebappUser(HttpUser):
    # Wait between 1 and 5 seconds between tasks
    wait_time = between(1, 5)
    host = "https://SERVICE-NAME-PROJECT-NUMBER.europe-west4.run.app/"

    @task
    def hello_world(self):
        self.client.get("/")