class Review:
    all_reviews = []#list to store reviews

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        '''
        Adds revies to list
        '''
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        '''
        Clear reviews from list
        '''
        Review.all_reviews.clear()

    

        