import jwt

# Your encoded JWT
encoded_jwt = "IQoJb3JpZ2luX2VjEIz//////////wEaCWV1LXdlc3QtMSJGMEQCIG9/3+aTvXLS8maTrIz79jD77ynJZbnpoN5HYv/76rywAiB+TPYYNnkUcMIsuLu+NtpJvGSgVY7cZB4C8GY4Tf0qQCrGBAhFEAMaDDczOTkzMDQyODQ0MSIM9LW5IsGx9cbVK+CeKqMEZaVe3nnMpLmk6RixlWVEJKs1AeZu1YnG9GIvhE6mmGrTc5cDUJhAD1AkWd0at7mjPY7ZyRyFEehWVPsTQ1+6pqkzaQYGQG1sYyuWxW4Tqva0zSqBRyC5CYrCuMrm1YXTZT7BaamBXcJFjuPQhzz+i8+wdRd5fYZbesXf7JpuqKVxd/nG7xnPKpWEn3zMCzBtviM1PKDjU2NnIpxEq561vFzQhzoOrR5KNQTXRfiYRTHPzpvmO0HxSSepzg1FoVtqMapy//K81obslKHbUn/UGSf4XVN3Ft3rCqaLpZG/ka9CL+6ejMHJsmiCmN3tC9NWcDGjdXaOIY3AJxnseXj28c3fHR6MWf63PO2qwDAmpe/G3RzqT5MOf+kAYtj4Q2zYg4XblAs2SJn8zG0119ah5OoPorwweJGyAHsc+ZHwf2GJ5Ad0bNl2og7hVgq7LO84iPxbUZM/RQ9yf3cbCnemSfBH+jS0+eycH3hOQHCF5bSoNl9VsNvDMgcUcOtPxKCgu3bZECiS5K6ReqyjdMc87NMaYe7k6YZHw83dI9SXZeNfWaUhmPSXAuSnV/vgTZ7XSMKKwcvom213oQ69Q+iUHJqHJQL6Q8asx2wkCgfyKvDK4RFXY9dib0653gxrNZ0xw73nzwXZbWfJ8Vxbj85dPZOdM5z/NRVsg4qmP4Lv6Dn49UJgWYL6EeHcFImf3/GDUZGdxmYCWQ3MSfmCPmMPtkPGpTDRlYW0BjqUAmeDNhL8bmjJn7GKjwNb6CpDAaP+sgMIJtWDDMwNdJxFeTEF7mEUVuonRnzgmMLaiu+hNUGpSf4cUWeoX0j9x5bVQa0ct0uOZp+gGuYvDysxJJqaI1XlLX0j33Ow/VyDXr/EAwDJiWrWlPauvifxNc5bLx7V1EY6EAl0fADD93n9KoHgaCyP0Se+lMixYh1k57ZTxdmnpN+eMGa46U1rFUK1Opw0MMwrXV699VUNG/Uaoe+zZ3oEHBqTjgTSQc4v/+l7T+9VdEd/zGBduGo46jdueJ7mK/SpnKn9/tVk7lSSR6CTi0qGSxxVbAVnIX9CyrmZfsBPBVyQMcLNc7y+ocdW7BJpERuAe2T4eQC+4puK/x0vwA=="

# Decode the JWT
try:
    decoded_jwt = jwt.decode(encoded_jwt, options={"verify_signature": False})
    print(decoded_jwt)
except Exception as e:
    print(f"Error decoding JWT: {e}")

