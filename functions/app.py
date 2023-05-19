import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def aUser(name, role):
    return {
        "id": name + "Id",
        "bearer": "bearer " + name,
        "role": role
    }

def aUserResponse(statusCode, user):
    return {
        "statusCode": statusCode,
        "body": json.dumps({
            "id": user["id"],
            "role": user["role"]
        })
    }

lita = aUser("lita", "student")
bema = aUser("bema", "teacher")
bozy = aUser("bozy", "teacher")
lou = aUser("lou", "manager")

apiKey = "iza-api-key"

forbiddenResponse = {
    "statusCode": 403,
    "body": "forbidden"
}

notFoundResponse = {
    "statusCode": 404,
    "body": "not found"
}

def whoami_handler(event, context):
    headers = event["headers"]
    bearer = headers["authorization"]
    if bearer == lita["bearer"]:
        return aUserResponse(200, lita)
    if bearer == bema["bearer"]:
        return aUserResponse(200, bema)
    if bearer == bozy["bearer"]:
        return aUserResponse(200, bozy)
    if bearer == lou["bearer"]:
        return aUserResponse(200, lou)
    return forbiddenResponse

def whois_handler(event, context):
    logger.info(event)
    headers = event["headers"]
    if(apiKey != headers["x-api-key"]):
        return forbiddenResponse

    httpContext = event["requestContext"]["http"]
    path = httpContext["path"]
    if lita["id"] in path:
        return aUserResponse(200, lita)
    if bema["id"] in path:
        return aUserResponse(200, bema)
    if bozy["id"] in path:
        return aUserResponse(200, bozy)
    if lou["id"] in path:
        return aUserResponse(200, lou)
    return notFoundResponse
