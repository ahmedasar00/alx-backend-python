from rest_framewor import pagination
from rest_framework.response import Response


class CustomPaggination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.page.number,
                "pages": self.page.paginator.num_pages,
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "results": data,
            }
        )
