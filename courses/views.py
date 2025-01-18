from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from .utils.utils import custom_response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# class IsAdminUserPermission:
#     """
#     Custom permission to allow only admin users.
#     """
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff
    

class CourseListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # print("Request data:", request)  
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = custom_response(
            status="success",
            message="Courses fetched successfully",
            data=serializer.data,
        )
        return Response(response, status=status.HTTP_200_OK)

    # Create a new course

    # permission_classes = [IsAuthenticated, IsAdminUserPermission]
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



class CourseDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    # Get a single course
    def get(self, request, pk):
        print("Request data:", pk)  
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            response = custom_response(
                status="success",
                message="Course fetched successfully",
                data=serializer.data,
            )
            return Response(response, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            response = custom_response(
                status="error",
                message="Course not found",
            )
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    # Update a course
    # find ruby and get pyhton me data find karne ke liye karte hai ye   o rm method hai
    

    # permission_classes = [IsAuthenticated, IsAdminUserPermission]
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = custom_response(
                    status="success",
                    message="Course updated successfully",
                    data=serializer.data,
                )
                return Response(response, status=status.HTTP_200_OK)
            response = custom_response(
                status="error",
                message="Failed to update course",
                errors=serializer.errors,
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            response = custom_response(
                status="error",
                message="Course not found",
            )
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    # Delete a course


    # permission_classes = [IsAuthenticated, IsAdminUserPermission]
    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            response = custom_response(
                status="success",
                message="Course deleted successfully",
            )
            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            response = custom_response(
                status="error",
                message="Course not found",
            )
            return Response(response, status=status.HTTP_404_NOT_FOUND)
