from fasthtml.common import *

app = FastHTML()

@app.route("/")
def home(): return Div(H1("Hello World!"), P("Deployed with CapRover API"))

serve()
