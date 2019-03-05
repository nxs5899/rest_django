from flask import jsonify, Blueprint # proxy for flask
from flask_restful import (Resource, Api, reqparse, inputs,
                            fields, abort, url_for,
                           marshal_with, marshal)
import models

review_fields = {
    'id': fields.Integer,
    'for_course': fields.String,
    'rating': fields.Integer,
    'comment': fields.String(default=''),
    'created_at': fields.DateTime
}

def review_or_404(review_id):
    try:
        review = models.Review.get(models.Review.id==review_id)
    except models.Review.DoesNotExist:
        abort(404)
    else:
        return review

def add_course(review):
    review.for_course = url_for(
        'resources.courses.course', id=review.course.id)
    return review

class ReviewList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course', required=True,
            type=inputs.positive,
            help='no course provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'rating', required=True,
            help='no rating provided',
            location=['form', 'json'],# we are telling reqparse where to look for data
            type=inputs.int_range(1,5)
        )

        self.reqparse.add_argument(
            'comment',
            help='no rating provided',
            nullable=True,
            location=['form', 'json'],  # we are telling reqparse where to look for data
            default=''
        )

        super().__init__()

    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

    @marshal_with(review_fields)
    def post(self):
        args = self.reqparse.parse_args()
        review = models.Review.create(**args)
        return add_course(review)


class Review(Resource):

    @marshal_with(review_fields)
    def get(self, id):
        return add_course(review_or_404(id))

    def put(self):
        return jsonify({'course': 1, 'rating': 5})
    def delete(self):
        return jsonify({'course': 1, 'rating': 5})

reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(ReviewList, '/api/v1/reviews',
                 endpoint = 'reviews')
api.add_resource(Review, '/api/v1/reviews/<int:id>',
                 endpoint = 'review')
