from schemas import ReviewSchema

review_data = []

def submitReview(user_id, driver_id, rating, review):
    new_review = {
        "user_id": user_id,
        "driver_id": driver_id,
        "rating": rating,
        "review": review
    }

    # Validate the review data against the schema
    errors = ReviewSchema().validate(new_review)
    if errors:
        return {"status": "error", "errors": errors}

    # Add the review to the review_data list
    review_data.append(new_review)

    return {"status": "success", "message": "review_success"}


def getReviews(user_id=None, driver_id=None):
    if user_id:
        return [review for review in review_data if review["user_id"] == user_id]
    elif driver_id:
        return [review for review in review_data if review["driver_id"] == driver_id]
    else:
        return review_data
