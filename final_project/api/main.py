from quart import Quart, send_file, jsonify, request, abort
from quart_cors import cors
import os
from solders.pubkey import Pubkey

app = Quart("CSC")
app = cors(app, allow_origin="*", allow_methods=["GET", "POST"])
app.config['UPLOAD_FOLDER'] = "/s3"
APP_SECRET = os.environ.get("APP_SECRET")

def generate_uuid(filename: str) -> str:
    """generates an ed25519 compliant pubkey as a UUID and adds the appropriate file type
        - args: original filename
        - returns: new filename with uuid and original file's suffix"""
    uuid = Pubkey.new_unique()
    # get the last slice of the split filename to get suffix
    filetype = filename.split(".")[-1]
    return str(uuid) + "." + filetype

@app.before_request
async def authenticate_platform():
    """Authenticates and validates request using 
    app secret JWT to ensure no outside requests"""
    if request.method == "OPTIONS" or request.path.startswith("/get"):
        return # allow OPTIONS requests and GET requests without authorization
    headers = request.headers
    secret = headers.get("Authorization") # get app secret header 
    if not secret or not APP_SECRET or secret != APP_SECRET:
        abort(401, "Unauthorized")
    elif request.headers.get("Content-Type") != "multipart/form-data":
        abort(400, "Invalid request content")
    else:
        return
        
@app.route("/get/<path:path>", methods=["GET"])
async def get(path: str):
    # send file helper will load file payload and construct response 
    return await send_file("/s3/"+path)
    
@app.route("/upload", methods=["POST"])
async def upload():
    """Try to load file from Multipart form data"""
    try:
        file = (await request.files).get("file")
        if file is None:
            abort(400, "No file provided")
        name = generate_uuid(file.filename)
        await file.save(f"/s3/{name}") # save to s3 folder with uuid
        return jsonify({"status": 0, "filename": name})
    except Exception as e:
        return jsonify({"status": 1, "error": str(e)})        

app.run("0.0.0.0", port=80) # run on default http port - forwarded to https via host 