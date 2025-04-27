from locust import HttpUser, task, between
import random


class CommentApiUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post("/api/v1/token/", data={"username": "555", "password": "555"})
        if response.status_code == 200:
            self.token = response.json().get("access")
            self.client.headers.update({"Authorization": f"Bearer {self.token}"})
        else:
            print(f"Login failed: {response.status_code} - {response.text}")
            self.token = None

    @task
    def create_comment(self):
        if not self.token:
            return
        comment_data = {
            "text": f"Test comment {random.randint(1, 1000000)}",
            "parent_comment": None
        }
        response = self.client.post("/api/v1/comments/", json=comment_data)
        if response.status_code != 201:
            print(f"Failed to create comment: {response.status_code} - {response.text}")

    @task(1)
    def get_comments(self):
        if not self.token:
            return
        response = self.client.get("/api/v1/comments/")
        if response.status_code != 200:
            print(f"Failed to get comments: {response.status_code} - {response.text}")
