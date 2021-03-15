def lambda_handler(event, context):
    print(event)
    headers = {
      "Access-Control-Allow-Origin": "*"
    }
    body = '{"Status": "200 Groovy"}'
    return {"headers": headers, "statusCode": 200, "body": body}