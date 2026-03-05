# 파이썬 기본 내장 웹서버 라이브러리 가져오기
from http.server import HTTPServer, BaseHTTPRequestHandler

# 요청이 오면 어떻게 응답할지 정의
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):                          # GET 요청이 오면
        self.send_response(200)                # 200 OK 응답
        self.end_headers()                     
        self.wfile.write(b"Hello! Docker is running!")  # 이 텍스트 보내기

# 8000번 포트로 서버 실행
HTTPServer(("", 8000), Handler).serve_forever()