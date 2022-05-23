from flask import Flask, request

import backend.service
import config
import tool

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

sqlClient = tool.sql.sqlClient(config.sqlIp,
                               config.sqlPort,
                               config.sqlDatabase,
                               config.sqlAccount,
                               config.sqlPassword)

minioClient = tool.mio.minioClient(config.minioIp,
                                   config.minioPort,
                                   config.minioAccount,
                                   config.minioPassword,
                                   config.minioBucket)

sqlClient.setConnection()
minioClient.setConnection()


@app.route('/user/login', methods=['POST', 'GET'])
def userLogin():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.login(sqlClient, data)
    return res


@app.route('/user/register', methods=['POST', 'GET'])
def userRegister():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.register(sqlClient, data)
    return res


@app.route('/user/forget', methods=['POST', 'GET'])
def userForget():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.forget(sqlClient, data)
    return res


@app.route('/user/getById', methods=['POST', 'GET'])
def userGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.getElemById(sqlClient, data)
    return res


@app.route('/user/getByAccount', methods=['POST', 'GET'])
def userGetByAccount():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.getElemByAccount(sqlClient, data)
    return res


@app.route('/order/getUserOrderById', methods=['POST', 'GET'])
def userGetUserOrderById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.orderService.getUserOrderById(sqlClient, data)
    return res


@app.route('/flower/getById', methods=['POST', 'GET'])
def flowerGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.getElemById(sqlClient, data)
    return res


def run():
    app.run(host=config.httpIp, port=config.httpPort, debug=False)


if __name__ == "__main__":
    run()
