from rest_framework.response import Response
from Product.models import Comments
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Product.serializers import CommentsModelSerializer


class CommentsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_id):
        comments = Comments.objects.get(id=product_id)
        serializer = CommentsModelSerializer(comments)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentsCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CommentsModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentsDetailView(APIView):

    def get_comments_object(self, comments_id):
        try:
            comments = Comments.objects.get(id=comments_id)
        except Comments.DoesNotExist:
            return Response({"message": "Comment does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return comments

    def delete(self, request, comments_id):
        self.get_comments_object(comments_id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



