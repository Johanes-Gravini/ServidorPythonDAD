from flask import Flask, request, jsonify

app = flask(__name__)


usuario=[]

if __name__ == "__main__":
    app.run(debug=true)
    
    
    
@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    nuevo_usuario = request.get_json()
    nuevo_usuario["id"] = len(usuario) + 1
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201



@app.route("/usuario", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuario": usuarios})


@app.route("/usuarios/<int:id>", methods={"GET"})
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u["id"]== id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    
    
    
@app.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        datos = request.get_json()
        usuario.update(datos)
        return jsonify({"mensaje": "Usuario actualizado exitosamente", "usuario": usuario})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    
    
    
    
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({"mensaje": "Usuario eliminado exitosamente"})
    else:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404