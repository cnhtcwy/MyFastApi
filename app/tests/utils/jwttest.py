from datetime import datetime, timedelta
import time
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

# 加密密钥 这个很重要千万不能泄露了
SECRET_KEY = "kkkkk"

# 设置过期时间 现在时间 + 有效时间    示例5分钟
expire = datetime.utcnow() + timedelta(seconds=1)
# expire = datetime.utcnow() + timedelta(minutes=1)

# exp 是固定写法必须得传  sub和uid是自己存的值
to_encode = {"exp": expire, "sub": str(123), "uid": "12345", "password": "111"}

# 生成token
encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM2MTc1MDYsInN1YiI6IjEyMyIsInVpZCI6IjEyMzQ1In0.6ViGpBJNi4aov59O-OSqBwOQNWapkDSrrjZwOXHZebc
print(encoded_jwt)
time.sleep(2)
# payload = jwt.decode(encoded_jwt,SECRET_KEY,algorithms="HS256")
try:
    payload = jwt.decode(
                encoded_jwt,
                SECRET_KEY, algorithms="HS256"
            )
    print(payload)
# 当然两个异常捕获也可以写在一起，不区分
except ExpiredSignatureError as e:
    print("token过期")
except JWTError as e:
    print("token验证失败")
# print(payload)
# print(payload.get("uid"))