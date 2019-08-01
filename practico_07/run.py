from src import app
import os



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
    app.run(debug=True)