from typing import Any, Optional

from django.core.handlers.wsgi import WSGIHandler, WSGIRequest

class StaticFilesHandler(WSGIHandler):
    handles_files: bool = ...
    application: WSGIHandler = ...
    base_url: Any = ...
    def __init__(self, application: WSGIHandler) -> None: ...
    def load_middleware(self) -> None: ...
    def get_base_url(self) -> str: ...
    def file_path(self, url: str) -> str: ...
    def serve(self, request: WSGIRequest) -> Any: ...
    def get_response(self, request: WSGIRequest) -> Any: ...
    def __call__(self, environ: Any, start_response: Any): ...
