import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LogFile
from .serializers import LogFileSerializer
from .log_parser import parse_log
from .error_detector import analyze_errors


@api_view(['POST'])
def upload_log(request):

    serializer = LogFileSerializer(data=request.data)

    if serializer.is_valid():
        log_file = serializer.save()
        return Response({
            "message": "Log uploaded successfully",
            "log_id": log_file.id
        })

    return Response(serializer.errors)


@api_view(['GET'])
def log_summary(request, log_id):

    try:
        log = LogFile.objects.get(id=log_id)
    except LogFile.DoesNotExist:
        return Response({"error": "Log not found"})

    file_path = log.file.path

    parsed_logs = parse_log(file_path)

    error_analysis = analyze_errors(parsed_logs["errors"])

    return Response({
        "total_errors": error_analysis["total_errors"],
        "most_common_error": error_analysis["most_common_error"],
        "error_count": error_analysis["count"],
        "warnings": len(parsed_logs["warnings"]),
        "info_logs": len(parsed_logs["info"])
    })