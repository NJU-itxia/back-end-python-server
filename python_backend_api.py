# Flask 1.0.2
# Flask_restful 0.3.6-2
# Python 3.7.0

from flask import Flask, request
from flask_restful import Resource,Api
import re
import demo_sms_send

app = Flask(__name__)
api = Api(app)

#使JSON中文不乱码
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

#储存数据的字典
sms = {}

class SMS_API(Resource):
    # def get(self, num):
    #     return {num: sms[num]}
    
    def post(self, num):
        
        Response = demo_sms_send.send_sms(business_id='none', phone_numbers=num, sign_name='none', template_code='none', template_param='none')
        return Response

        # 储存短信数据-POST
        # sms.setdefault(num, []).append(request.form['data'])

        # 返回POST后的JSON列表
        # return {num: sms[num]}

        # 判断手机号码是否正确
        # if len(list(num)) == 11 and list(num)[0] == '1':
        #     return {"success" : "true"}
        # else:
        #     return {"success": "false"}


api.add_resource(SMS_API, '/service/sms/<string:num>')

if __name__ == '__main__':
    app.run(debug=True)
