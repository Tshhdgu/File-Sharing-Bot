from flask import Flask
app = Falsk(__name__)

@app.router('/')
def hello_world():
  return 'GreyMatters'

if __name__"" "__main__":
  app.run()
