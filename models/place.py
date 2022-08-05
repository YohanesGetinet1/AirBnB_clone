#!/usr/bin/python3
"""Defining Place model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Defining Place class"""

	city_id = ""
	user_id = ""
	descripition = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []



	def __init__(self, *args, **kwargs):
	"""initializing Place class"""


	super().__init__(*args, **kwargs)
