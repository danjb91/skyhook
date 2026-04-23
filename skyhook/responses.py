from dataclasses import dataclass


@dataclass(frozen=True)
class HtmlResponse:
    """
    Sentinel class for handler functions that return HTML content.

    When a handler returns an HtmlResponse, the server will emit the body
    verbatim as HTML instead of encoding it as JSON.
    """
    body: str
    status: int = 200
    content_type: str = "text/html; charset=utf-8"
