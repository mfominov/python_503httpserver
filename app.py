import string,cgi,time, datetime
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      self.send_response(503) # let bots know whats up
      self.send_header('Content-type','application/xml')
      self.end_headers()
      self.wfile.write('<!DOCTYPE html>\n<meta charset=utf-8 />\n<title>Notification page</title>\n')
      self.wfile.write('<style>body {max-width:400px; background:#fff8ea;}</style>\n')
      self.wfile.write('\n<p>\nFeels bad, man</p>\n\n')
      self.wfile.write('\n<img src="https://imgur.com/gallery/aSVjtu7"/>\n\n')
      self.wfile.write('<!-- '+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+' // '+self.path+'-->\n')
      return
    except IOError:
      self.send_error(500,'Internal error')

class TimeoutingHTTPServer(HTTPServer):
  def finish_request(self, request, client_address):
    request.settimeout(5) # Really short timeout as there is only 1 thread
    HTTPServer.finish_request(self, request, client_address)

def main():
  try:
    server = TimeoutingHTTPServer(('0.0.0.0',8080), MyHandler)
    print 'Listening...'
    server.serve_forever()
  except KeyboardInterrupt:
    print 'quit...'
    server.socket.close()

if __name__ == '__main__':
  main()
