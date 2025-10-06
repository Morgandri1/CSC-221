from quart import Quart, send_file, jsonify, request, abort
from quart_cors import cors
from werkzeug.exceptions import HTTPException, InternalServerError
import os
from solders.pubkey import Pubkey

app = Quart("CSC")
app = cors(app, allow_origin="*", allow_methods=["GET", "POST"])
app.config['UPLOAD_FOLDER'] = "/s3"
APP_SECRET = os.environ.get("APP_SECRET")

def generate_uuid(filename: str) -> str:
    # generates an ed25519 compliant pubkey which we'll use as our file's uuid
    uuid = Pubkey.new_unique()
    filetype = filename.split(".")[-1] # get the last slice of the split filename to get suffix
    return str(uuid) + "." + filetype

@app.before_request
async def authenticate_platform():
    if request.method == "OPTIONS" or request.path.startswith("/get"):
        return
    headers = request.headers
    secret = headers.get("Authorization")
    if not secret or not APP_SECRET or secret != APP_SECRET:
        abort(401, "Unauthorized")
    else:
        return
        
@app.route("/get/<path:path>", methods=["GET"])
async def cdn(path: str):
    return await send_file("/s3/"+path, )
    
@app.route("/upload", methods=["POST"])
async def push():
    try:
        file = await request.files
        file = file["file"]
        name = generate_uuid(file.filename)
        await file.save(f"/s3/{name}")
        return jsonify({"status": 0, "filename": name})
    except Exception as e:
        return jsonify({"status": 1, "error": str(e)})        

app.run("0.0.0.0", port=80)