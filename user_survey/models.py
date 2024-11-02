
class UserResponse():
    def __init__(self):
        self.majors = []
        self.price_range = None
        self.sports = False
        self.arts = False
        self.professional = False
        self.city = None
        self.state = None
        self.in_state = True

    def to_dict(self):
        return {
            'majors': self.majors,
            'price_range': self.price_range,
            'sports': self.sports,
            'arts': self.arts,
            'professional': self.professional,
            'city': self.city,
            'state': self.state,
            'in_state': self.in_state,
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.majors = data.get('majors', [])
        instance.price_range = data.get('price_range')
        instance.sports = data.get('sports', False)
        instance.arts = data.get('arts', False)
        instance.professional = data.get('professional', False)
        instance.city = data.get('city')
        instance.state = data.get('state')
        instance.in_state = data.get('in_state', True)
        return instance