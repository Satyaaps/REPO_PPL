from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def load_home(self):
        self.client.get("/")

    @task(2)
    def load_process(self):
        self.client.get("/process")
