from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from .utils.utils import custom_response

class CourseListView(APIView):
    # Get all courses
    def get(self, request):
        print("Request data:", request)  
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = custom_response(
            status="success",
            message="Courses fetched successfully",
            data=serializer.data,
        )
        return Response(response, status=status.HTTP_200_OK)

    # Create a new course
    def post(self, request):
        print("Request data:", request.data)  
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = custom_response(
                status="success",
                message="Course created successfully",
                data=serializer.data,
            )
            return Response(response, status=status.HTTP_201_CREATED)
        response = custom_response(
            status="error",
            message="Failed to create course",
            errors=serializer.errors,
        )
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
