
class UserResponse():
    def __init__(self):
        self.majors = []
        self.price_range = None
        self.activity_cats = []
        self.city = None
        self.state = None
        self.in_state = False

    def to_dict(self):
        return {
            'majors': self.majors,
            'price_range': self.price_range,
            'activity_cats' : self.activity_cats,
            'city': self.city,
            'state': self.state,
            'in_state': self.in_state,
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.majors = data.get('majors', [])
        instance.price_range = data.get('price_range')
        instance.activity_cats = data.get('activity_cats', [])
        instance.city = data.get('city')
        instance.state = data.get('state')
        instance.in_state = data.get('in_state', True)
        return instance