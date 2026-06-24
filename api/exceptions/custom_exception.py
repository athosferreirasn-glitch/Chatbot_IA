class BusinessException(Exception):
    status_code=400
    detail="Erro de negócio"

class ErrorAPIAi(BusinessException):
    status_code=503
    detail="Não foi possível conectar ao servidor"

class ResponseError(BusinessException):
    status_code=500
    detail="Erro na resposta da API"

class CoversationIdIvalidError(BusinessException):
    status_code=400
    detail="Id da conversa inválido"