from flask import Flask, render_template, make_response, jsonify, request, Response
import json
import sys
sys.path.append("C:\SOPORTEV\GIT\practico_06")
sys.path.append("C:\SOPORTEV\GIT\practico_05")
from capa_negocio import NegocioSocio
from ejercicio_01 import Socio

app = Flask(__name__)
negocio = NegocioSocio()


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/alta/socio', methods=['GET','POST'])
def altaSocio():
    if request.method == 'GET':
        return jsonify("Dont use GET on this")
    else:
        #INSERTAR FUNCION ALTA SOCIO
        return jsonify("Data OK")

@app.route('modificacion/socio', methods=['PUT'])
def modificacionSocio():
    if request.method != 'PUT':
        return jsonify("Use PUT on this")
    else:
        #INSERTAR FUNCION MODIFICACION SOCIO
        return jsonify("Data OK")

@app.route('baja/socio', methods=['DELETE'])
def bajaSocio():
        if request.method != 'DELETE':
        return jsonify("Use DELETE on this")
    else:
        #INSERTAR BAJA SOCIO
        return jsonify("Data OK")


@app.route('/View')
def TreeView():
    return render_template('view.html')



    