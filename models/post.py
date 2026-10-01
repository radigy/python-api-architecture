from dataclasses import dataclass

@dataclass
class Post:
    user_id: int
    title: str
    body: str

    def to_payload(self):
        return {
            "userId": self.user_id,
            "title": self.title,
            "body": self.body
        }
