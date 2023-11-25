

from flask import Flask, request, jsonify

app=Flask(__name__)


@app.route('/Multip',methods=['POST'])
def getMultip():
    nombreUser = request.get_json()
    PriNum=nombreUser["priNum"]
    SegNum=nombreUser["segNum"]
    prod=PriNum*SegNum
    result={"resul":prod}

    return jsonify(result)
@app.route('/suma',methods=['POST'])
def getSuma():
    nombreUser = request.get_json()
    PriNum=nombreUser["priNum"]
    SegNum=nombreUser["segNum"]
    prod=PriNum+SegNum
    result={"resul":prod}
    return jsonify(result)

@app.route('/resta',methods=['POST'])
def getResta():
    nombreUser = request.get_json()
    PriNum=nombreUser["priNum"]
    SegNum=nombreUser["segNum"]
    prod=PriNum-SegNum
    result={"resul":prod}

    return jsonify(result)

@app.route('/divi',methods=['POST'])
def getDivi():
    
    #result=null
    try:
        nombreUser = request.get_json()
        PriNum=nombreUser["priNum"]
        SegNum=nombreUser["segNum"]
        if SegNum==0:
            return "no es posible dividor por 0, ingrese un valor diferente"
        else:
            prod=PriNum/SegNum
            result={"resul":prod}
            return jsonify(result)
    except:
        print("verifique los datos ingrasados")
   # return jsonify(result)
  # return ""

@app.route('/raiz',methods=['POST'])
def getRaiz():
    result=0.0
    try:
        nombreUser = request.get_json()
        PriNum=nombreUser["priNum"]
        SegNum=nombreUser["segNum"]
        if PriNum==0:
            return "no es posible hacer esta operacion con radical 0, ingrese un valor diferente"
        else:
            PriNum= 1/PriNum
            prod=SegNum**PriNum
            result={"resul":prod}
            return jsonify(result)
    except:
        print("verifique los datos ingrasados")
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=82)