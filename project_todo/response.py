from django.http import JsonResponse

class Response:

    def base(self, values=None, message="", error=False, status=200):
        if values is None:
            values = []

        return JsonResponse({
            'error': error,
            'message': message,
            'data': values,
        }, status=status)
    
    @staticmethod
    def success(values=None, message=""):
        return Response().base(values=values, message=message, error=False, status=200)

    @staticmethod
    def unauthorized(values=None, message="Unauthroized access"):
        return Response().base(values=values, message=message, error=True, status=401)
        
    @staticmethod
    def notFound(values=None, message="Not Found"):
        return Response().base(values=values, message=message, error=True, status=404)

    @staticmethod
    def badRequest(values=None, message="Bad Request"):
        return Response().base(values=values, message=message, error=True, status=400)