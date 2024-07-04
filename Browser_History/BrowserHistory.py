class BrowserHistory:
    def __init__(self, homepage: str):
        self.forw = []
        self.backward = [homepage]

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.forw = []  # Clear the forward stack when visiting a new URL

    def back(self, steps: int) -> str:
        while steps and len(self.backward) > 1:
            self.forw.append(self.backward.pop())
            steps -= 1
        return self.backward[-1]

    def forward(self, steps: int) -> str:
        while steps and self.forw:
            self.backward.append(self.forw.pop())
            steps -= 1
        return self.backward[-1]
