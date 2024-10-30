from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

# route to set cookie
@app.route('/setcookie', methods=['POST'])
def set_cookie():
    # get name from request
    name = request.json.get('name')

    resp = make_response(jsonify({"message": "cookie has been set"}))
    resp.set_cookie('name', name, max_age=60*60*24) # cookie last 1 day
    return resp

# route to read the cookie
@app.route('/getcookie', methods=['GET'])
def get_cookie():
    name = request.cookies.get('name')
    if name:
        return jsonify({"name": name})
    else:
        return jsonify({"message": "no name cookie found"}), 404

# route to delete the cookie
@app.route('/deletecookie', methods=['GET'])
def delete_cookie():
    resp = make_response(jsonify({"message": "cookie has been deleted"}))
    resp.set_cookie('userID', '', expires=0) # set expiration to delete the cookie
    return resp


if __name__ == '__main__':
    app.run(debug=True)