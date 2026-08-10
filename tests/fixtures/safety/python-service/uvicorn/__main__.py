"""Serve a dependency-free health endpoint from the copied runtime environment."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        del format, args


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), HealthHandler).serve_forever()
