# Flask 1.0.2
# Flask_restful 0.3.6-2
# Python 3.7.0

from flask import Flask, request
from flask_restful import Resource,Api
import re
from dysms_python import demo_sms_send
import config


app = Flask(__name__)
api = Api(app)

#使JSON中文不乱码
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))


class SMS_API(Resource):
    # def get(self, num):
    #     return {num: sms[num]}
    
    def post(self, num):
        name = request.form['name']
        Response = demo_sms_send.send_sms(business_id=config.SMS_ID, phone_numbers=num, sign_name=config.SMS_SIGN, template_code=config.SMS_CODE, template_param={"name": name})
        Response = Response.decode(encoding='UTF-8',errors='strict')

        return Response


api.add_resource(SMS_API, '/service/sms/<string:num>')

if __name__ == '__main__':
    app.run(debug=True)
